#!/usr/bin/env python3
"""Mass source-corpus link audit: liveness + readability probe for every URL.

Validated 2026-08-13 on a 129-row / 257-URL evidence matrix (~10-25 min, 6 workers).

USAGE:
    uv run --with pypdf python3 matrix_url_audit.py rows.json [out_prefix]

    rows.json    list of dicts, each with at least:
                 {"ID": "...", "Citation": "...",
                  "Readable Source URL": "https://...", "Source Landing URL": "https://...",
                  "Access Type": "...", "Source Discovery Status": "..."}
                 (missing keys are tolerated; empty readable URL => row classified NO_URL)
    out_prefix   output files: <prefix>.csv, <prefix>_bad.md, <prefix>_report.md
                 (default: rows.json path minus .json)

OUTPUTS
    <prefix>.csv        one row per URL (row_id, kind, http code, final URL, content-type,
                        size, text chars, verdict, notes)
    <prefix>_bad.md     dedicated bad-links list: BROKEN/NO_URL rows + CAVEAT rows
    <prefix>_report.md  full report incl. per-URL verdict distribution

VERDICTS (per URL)
    OK_READABLE   PDF with real text layer (note-takable)
    OK_HTML       HTML page with substantial text
    OK_LANDING    HTML page but paywall/login markers present (abstract-only likely)
    BAD_SCANNED   PDF with NO text layer (image-only; needs OCR)
    BAD_STUB      HTML with <800 chars text (JS-walled/empty)
    BAD_DEAD      HTTP 4xx/5xx (except 403/429 -> BAD_BLOCKED)
    BAD_TIMEOUT / BAD_UNREACHABLE / BAD_UNREADABLE (parse failure)
    UNKNOWN       non-PDF/HTML binary

ROW CLASSIFICATION
    READY (readable URL ok) / CAVEAT (scanned, stub, landing-only) / BROKEN / NO_URL

NOTES
    - Browser UA + redirects + 50s timeout + one retry on connection failure.
    - PDFs <= 20MB are cached next to the outputs (renamed .pdf) for the reading phase;
      larger ones are deleted after probing.
    - Google Scholar / search-query URLs should NOT be included in rows.json (not bot-testable).
"""
import json, os, re, subprocess, html as ihtml, time, csv, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

PAYWALL_MARKERS = ["log in", "login", "sign in", "signin", "purchase", "subscribe",
                   "paywall", "access denied", "captcha", "cloudflare", "not logged in",
                   "institutional access", "checkout", "request access", "read now",
                   "get access", "add to cart", "403 forbidden", "to continue, enable javascript"]


def strip_html(s):
    s = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = ihtml.unescape(s)
    return re.sub(r"\s+", " ", s)


def do_curl(url, tmp):
    cmd = ["curl", "-sL", "--max-time", "50", "-A", UA, "--compressed",
           "-o", tmp, "-w", "%{http_code}\t%{content_type}\t%{size_download}\t%{url_effective}",
           url]
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return None


def check_url(url, cache_dir):
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", url)[:150]
    tmp = os.path.join(cache_dir, f"{slug}.dl")
    base = dict(url=url, http_code=0, content_type="", size=0, final_url="",
                verdict="BAD_UNREACHABLE", text_chars=0, notes="")
    p = do_curl(url, tmp)
    if p is None:
        return {**base, "verdict": "BAD_TIMEOUT", "notes": "curl timed out (60s)"}
    parts = p.stdout.strip().split("\t")
    r = {**base, "http_code": parts[0] if parts else "000",
         "content_type": parts[1] if len(parts) > 1 else "",
         "final_url": parts[3] if len(parts) > 3 else ""}
    try:
        r["size"] = int(parts[2]) if len(parts) > 2 else 0
    except ValueError:
        r["size"] = 0
    if r["http_code"] == "000":  # one retry
        time.sleep(2)
        p = do_curl(url, tmp)
        if p is None:
            return {**r, "verdict": "BAD_TIMEOUT", "notes": "curl timed out twice"}
        parts = p.stdout.strip().split("\t")
        r["http_code"] = parts[0] if parts else "000"
        r["content_type"] = parts[1] if len(parts) > 1 else ""
        r["final_url"] = parts[3] if len(parts) > 3 else ""
        try:
            r["size"] = int(parts[2]) if len(parts) > 2 else 0
        except ValueError:
            r["size"] = 0
        if r["http_code"] == "000":
            return {**r, "verdict": "BAD_UNREACHABLE",
                    "notes": (p.stderr or "").strip()[:140] or "connection error"}
    if r["http_code"].startswith(("4", "5")):
        try:
            os.remove(tmp)
        except OSError:
            pass
        verdict = "BAD_BLOCKED" if r["http_code"] in ("403", "429") else "BAD_DEAD"
        return {**r, "verdict": verdict, "notes": f"HTTP {r['http_code']}"}
    blob = b""
    try:
        with open(tmp, "rb") as f:
            blob = f.read(4096)
    except OSError:
        blob = b""
    is_pdf = ("pdf" in r["content_type"].lower()) or blob.startswith(b"%PDF")
    if is_pdf:
        try:
            from pypdf import PdfReader
            reader = PdfReader(tmp)
            n = min(len(reader.pages), 4)
            txt = "".join((reader.pages[i].extract_text() or "") for i in range(n))
            text_chars = len(re.sub(r"\s+", "", txt or ""))
            npages = len(reader.pages)
            if text_chars >= 300:
                r.update(verdict="OK_READABLE",
                         notes=f"PDF {npages}p, text layer OK ({text_chars} chars in first {n}p)",
                         text_chars=text_chars)
            else:
                r.update(verdict="BAD_SCANNED",
                         notes=f"PDF {npages}p, NO text layer (scanned/image-only, needs OCR)",
                         text_chars=text_chars)
        except Exception as e:
            r.update(verdict="BAD_UNREADABLE",
                     notes=f"PDF parse failed: {type(e).__name__}: {str(e)[:120]}")
        if r["size"] <= 20 * 1024 * 1024:
            try:
                os.rename(tmp, tmp.replace(".dl", ".pdf"))
            except OSError:
                pass
        else:
            try:
                os.remove(tmp)
            except OSError:
                pass
    elif "html" in r["content_type"].lower() or blob[:1] in (b"<", b"\xef\xbb\xbf<") or blob.startswith(b"<!DOCTYPE"):
        try:
            with open(tmp, "r", encoding="utf-8", errors="replace") as f:
                raw = f.read()
        except OSError:
            raw = ""
        text = strip_html(raw)
        text_chars = len(re.sub(r"\s+", "", text))
        low = text.lower()
        found = [m for m in PAYWALL_MARKERS if m in low]
        if text_chars >= 800:
            r.update(verdict="OK_HTML" if not found else "OK_LANDING",
                     notes=f"HTML {text_chars} chars" + (f"; markers: {found[:6]}" if found else ""),
                     text_chars=text_chars)
        else:
            r.update(verdict="BAD_STUB",
                     notes=f"HTML stub, only {text_chars} chars; markers: {found[:6]}",
                     text_chars=text_chars)
        try:
            with open(tmp.replace(".dl", ".txt"), "w", encoding="utf-8") as f:
                f.write(text[:60000])
        except OSError:
            pass
        try:
            os.remove(tmp)
        except OSError:
            pass
    else:
        try:
            os.remove(tmp)
        except OSError:
            pass
        r.update(verdict="UNKNOWN", notes=f"content-type {r['content_type'] or 'none'}")
    return r


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    rows_path = sys.argv[1]
    out_prefix = sys.argv[2] if len(sys.argv) > 2 else re.sub(r"\.json$", "", rows_path)
    rows = json.load(open(rows_path))
    cache_dir = os.path.dirname(os.path.abspath(out_prefix)) or "."
    os.makedirs(cache_dir, exist_ok=True)

    url_map = {}
    for o in rows:
        rid = str(o.get("ID", "")).strip()
        for kind, key in (("readable", "Readable Source URL"), ("landing", "Source Landing URL")):
            u = (o.get(key) or "").strip()
            if u:
                url_map.setdefault(u, []).append((rid, kind))
    urls = list(url_map.keys())
    print(f"CHECKING {len(urls)} UNIQUE URLS", flush=True)

    results = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(check_url, u, cache_dir): u for u in urls}
        done = 0
        for fut in as_completed(futs):
            done += 1
            try:
                res = fut.result()
            except Exception as e:
                res = dict(url=futs[fut], http_code=0, content_type="", size=0, final_url="",
                           verdict="BAD_UNREACHABLE", text_chars=0, notes=f"worker error: {e}")
            results[res["url"]] = res
            if done % 25 == 0 or done == len(urls):
                print(f"  {done}/{len(urls)} done", flush=True)

    def vclass(v):
        return {"OK_READABLE": "ok", "OK_HTML": "ok", "OK_LANDING": "warn",
                "BAD_SCANNED": "warn", "BAD_STUB": "warn", "UNKNOWN": "warn",
                "BAD_DEAD": "bad", "BAD_BLOCKED": "bad", "BAD_TIMEOUT": "bad",
                "BAD_UNREACHABLE": "bad", "BAD_UNREADABLE": "bad"}.get(v, "warn")

    rows_out = []
    for o in rows:
        rid = str(o.get("ID", "")).strip()
        cit = str(o.get("Citation") or "").strip()
        acc = str(o.get("Access Type") or "").strip()
        st = str(o.get("Source Discovery Status") or "").strip()
        rurl = (o.get("Readable Source URL") or "").strip()
        lurl = (o.get("Source Landing URL") or "").strip()
        rres = results.get(rurl) if rurl else None
        lres = results.get(lurl) if lurl else None
        if not rurl:
            row_status = "NO_URL"
        elif vclass(rres["verdict"]) == "bad" if rres else True:
            row_status = "BROKEN"
        elif vclass(rres["verdict"]) == "warn" if rres else False:
            row_status = "CAVEAT"
        else:
            row_status = "READY"
        rows_out.append(dict(ID=rid, Citation=cit, AccessType=acc, DiscoveryStatus=st,
                             RowStatus=row_status, ReadableURL=rurl, ReadableResult=rres,
                             LandingURL=lurl, LandingResult=lres))

    with open(f"{out_prefix}.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["RowID", "Citation", "URL_Kind", "URL", "HTTP_Code", "Final_URL",
                    "Content_Type", "Size_Bytes", "Text_Chars", "Verdict", "Notes"])
        for r in rows_out:
            for kind, res, u in (("readable", r["ReadableResult"], r["ReadableURL"]),
                                 ("landing", r["LandingResult"], r["LandingURL"])):
                if u:
                    w.writerow([r["ID"], r["Citation"], kind, u,
                                res.get("http_code") if res else "",
                                res.get("final_url") if res else "",
                                res.get("content_type") if res else "",
                                res.get("size") if res else "",
                                res.get("text_chars") if res else "",
                                res.get("verdict") if res else "NOT_CHECKED",
                                res.get("notes") if res else ""])
    print(f"CSV: {out_prefix}.csv", flush=True)

    def res_brief(res):
        if not res:
            return "NOT_CHECKED"
        v = res["verdict"]
        if v in ("OK_READABLE", "OK_HTML"):
            return f"OK ({res['notes']})"
        if v == "OK_LANDING":
            return f"LANDING-ONLY ({res['notes']})"
        return f"{v}: {res['notes']}"

    bad = [r for r in rows_out if r["RowStatus"] in ("BROKEN", "NO_URL")]
    caveat = [r for r in rows_out if r["RowStatus"] == "CAVEAT"]
    ready = [r for r in rows_out if r["RowStatus"] == "READY"]

    md = [f"# SOURCE-LINK AUDIT — BAD / BROKEN LINKS",
          "",
          f"- Rows BROKEN or NO_URL: {len(bad)}",
          f"- Rows with CAVEAT (readable but scanned/landing-only/stub): {len(caveat)}",
          f"- Rows READY (readable URL verified note-takable): {len(ready)}",
          "",
          f"Full per-URL detail: `{os.path.basename(out_prefix)}.csv`.", ""]
    if bad:
        md += ["## BROKEN / NO-URL ROWS", "", "| RowID | Citation | Status | Readable URL result | Landing URL result |",
               "|---|---|---|---|---|"]
        for r in bad:
            md.append(f"| {r['ID']} | {r['Citation']} | {r['RowStatus']} | "
                      f"{res_brief(r['ReadableResult'])} | {res_brief(r['LandingResult'])} |")
        md.append("")
    if caveat:
        md += ["## CAVEAT ROWS", "", "| RowID | Citation | Readable URL result |", "|---|---|---|"]
        for r in caveat:
            md.append(f"| {r['ID']} | {r['Citation']} | {res_brief(r['ReadableResult'])} |")
        md.append("")
    with open(f"{out_prefix}_bad.md", "w") as f:
        f.write("\n".join(md))
    print(f"BAD LIST: {out_prefix}_bad.md", flush=True)

    report = [f"# SOURCE-LINK AUDIT REPORT", f"- Rows audited: {len(rows_out)}",
              f"- Unique URLs checked: {len(urls)}",
              f"- READY: {len(ready)} | CAVEAT: {len(caveat)} | BROKEN/NO_URL: {len(bad)}",
              "", "## Verdict distribution (per URL)", ""]
    vc = Counter(res["verdict"] for res in results.values())
    report += [f"- {v}: {c}" for v, c in vc.most_common()]
    report += ["", "## BROKEN / CAVEAT ROWS", ""]
    for r in bad + caveat:
        report += [f"### {r['ID']} — {r['Citation']}  ({r['RowStatus']})",
                   f"- Readable: {res_brief(r['ReadableResult'])}",
                   f"- Landing:  {res_brief(r['LandingResult'])}",
                   f"- Access Type: {r['AccessType']}",
                   f"- Discovery Status: {r['DiscoveryStatus']}", ""]
    report += ["## READY ROWS", ""]
    report += [f"- {r['ID']}: {r['Citation']} — {res_brief(r['ReadableResult'])}" for r in ready]
    with open(f"{out_prefix}_report.md", "w") as f:
        f.write("\n".join(report))
    print(f"REPORT: {out_prefix}_report.md", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
