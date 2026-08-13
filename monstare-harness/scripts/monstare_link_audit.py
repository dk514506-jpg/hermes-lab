#!/usr/bin/env python3
"""Monstare source-link audit: status + readability probe for every matrix URL.

For each unique URL (Readable Source URL + Source Landing URL across all rows):
  - GET with curl (browser UA, follow redirects, 50s timeout, one retry)
  - classify: dead/blocked/timeout vs live
  - probe readability: PDF -> pypdf text layer (first 4 pages); HTML -> stripped text
    chars + paywall/login markers
Outputs:
  - Monstare_source_link_audit_2026-08-13.csv   (per-URL rows)
  - Monstare_bad_source_links_2026-08-13.md     (dedicated bad-links list)
  - Monstare_source_link_audit_2026-08-13.md    (full report)
"""
import json, os, re, subprocess, html as ihtml, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
from collections import Counter

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
ROWS = json.load(open("/opt/data/Monstare_all_rows_urls.json"))
CACHE = "/opt/data/Monstare_source_audit_cache"
os.makedirs(CACHE, exist_ok=True)
DATE = "2026-08-13"

url_map = {}
for o in ROWS:
    rid = str(o["ID"]).strip()
    for kind, key in (("readable", "Readable Source URL"), ("landing", "Source Landing URL")):
        u = (o.get(key) or "").strip()
        if u:
            url_map.setdefault(u, []).append((rid, kind))
URLS = list(url_map.keys())
print(f"CHECKING {len(URLS)} UNIQUE URLS", flush=True)

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
    curl_cmd = ["curl", "-sL", "--max-time", "50", "-A", UA, "--compressed",
                "-o", tmp, "-w", "%{http_code}\t%{content_type}\t%{size_download}\t%{url_effective}",
                url]
    try:
        p = subprocess.run(curl_cmd, capture_output=True, text=True, timeout=60)
        return p
    except subprocess.TimeoutExpired:
        return None

def check_url(url):
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", url)[:150]
    tmp = os.path.join(CACHE, f"{slug}.dl")
    base = dict(url=url, http_code=0, content_type="", size=0, final_url="",
                verdict="BAD_UNREACHABLE", text_chars=0, notes="")
    p = do_curl(url, tmp)
    if p is None:
        return {**base, "verdict": "BAD_TIMEOUT", "notes": "curl timed out (60s)"}
    parts = p.stdout.strip().split("\t")
    code = parts[0] if parts else "000"
    ctype = parts[1] if len(parts) > 1 else ""
    size = parts[2] if len(parts) > 2 else "0"
    final = parts[3] if len(parts) > 3 else ""
    try:
        size = int(size)
    except ValueError:
        size = 0
    r = {**base, "http_code": code, "content_type": ctype, "size": size, "final_url": final}
    if code == "000":
        # one retry
        time.sleep(2)
        p = do_curl(url, tmp)
        if p is None:
            return {**r, "verdict": "BAD_TIMEOUT", "notes": "curl timed out twice"}
        parts = p.stdout.strip().split("\t")
        code = parts[0] if parts else "000"
        r["http_code"] = code
        r["content_type"] = parts[1] if len(parts) > 1 else ""
        try:
            r["size"] = int(parts[2]) if len(parts) > 2 else 0
        except ValueError:
            r["size"] = 0
        r["final_url"] = parts[3] if len(parts) > 3 else ""
        if code == "000":
            return {**r, "verdict": "BAD_UNREACHABLE",
                    "notes": (p.stderr or "").strip()[:140] or "connection error"}
    if code.startswith(("4", "5")):
        try: os.remove(tmp)
        except OSError: pass
        verdict = "BAD_BLOCKED" if code in ("403", "429") else "BAD_DEAD"
        return {**r, "verdict": verdict, "notes": f"HTTP {code}"}
    # 2xx/3xx-final: probe
    blob = b""
    try:
        with open(tmp, "rb") as f:
            blob = f.read(4096)
    except OSError:
        blob = b""
    is_pdf = ("pdf" in ctype.lower()) or blob.startswith(b"%PDF")
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
        if r["size"] > 20 * 1024 * 1024:
            try: os.remove(tmp)
            except OSError: pass
        else:
            final_path = tmp.replace(".dl", ".pdf")
            try: os.rename(tmp, final_path)
            except OSError: pass
    elif "html" in ctype.lower() or blob[:1] in (b"<", b"\xef\xbb\xbf<") or blob.startswith(b"<!DOCTYPE"):
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
        txt_path = tmp.replace(".dl", ".txt")
        try:
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text[:60000])
        except OSError:
            pass
        try: os.remove(tmp)
        except OSError: pass
    else:
        try: os.remove(tmp)
        except OSError: pass
        r.update(verdict="UNKNOWN", notes=f"content-type {ctype or 'none'}")
    return r

results = {}
with ThreadPoolExecutor(max_workers=6) as ex:
    futs = {ex.submit(check_url, u): u for u in URLS}
    done = 0
    for fut in as_completed(futs):
        done += 1
        try:
            res = fut.result()
        except Exception as e:
            res = dict(url=futs[fut], http_code=0, content_type="", size=0, final_url="",
                       verdict="BAD_UNREACHABLE", text_chars=0, notes=f"worker error: {e}")
        results[res["url"]] = res
        if done % 25 == 0 or done == len(URLS):
            print(f"  {done}/{len(URLS)} done", flush=True)

# ----- aggregate per row -----
def verdict_class(v):
    return {"OK_READABLE": "ok", "OK_HTML": "ok", "OK_LANDING": "warn",
            "BAD_SCANNED": "warn", "BAD_STUB": "warn", "UNKNOWN": "warn",
            "BAD_DEAD": "bad", "BAD_BLOCKED": "bad", "BAD_TIMEOUT": "bad",
            "BAD_UNREACHABLE": "bad", "BAD_UNREADABLE": "bad"}.get(v, "warn")

rows_out = []
for o in ROWS:
    rid = str(o["ID"]).strip()
    cit = str(o.get("Citation") or "").strip()
    acc = str(o.get("Access Type") or "").strip()
    st = str(o.get("Source Discovery Status") or "").strip()
    rurl = (o.get("Readable Source URL") or "").strip()
    lurl = (o.get("Source Landing URL") or "").strip()
    rres = results.get(rurl) if rurl else None
    lres = results.get(lurl) if lurl else None
    if not rurl:
        row_status = "NO_URL"
    else:
        rv = verdict_class(rres["verdict"]) if rres else "bad"
        if rv == "bad":
            row_status = "BROKEN"
        elif rv == "warn":
            row_status = "CAVEAT"
        else:
            row_status = "READY"
    rows_out.append(dict(ID=rid, Citation=cit, AccessType=acc, DiscoveryStatus=st,
                         RowStatus=row_status, ReadableURL=rurl, ReadableResult=rres,
                         LandingURL=lurl, LandingResult=lres))

# ----- CSV -----
import csv
csv_path = f"/opt/data/Monstare_source_link_audit_{DATE}.csv"
with open(csv_path, "w", newline="") as f:
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
print(f"CSV: {csv_path}", flush=True)

# ----- bad-links list (markdown) -----
bad_rows = [r for r in rows_out if r["RowStatus"] in ("BROKEN", "NO_URL")]
caveat_rows = [r for r in rows_out if r["RowStatus"] == "CAVEAT"]
ready_rows = [r for r in rows_out if r["RowStatus"] == "READY"]

def res_brief(res):
    if not res:
        return "NOT_CHECKED"
    v = res["verdict"]
    if v in ("OK_READABLE", "OK_HTML"):
        return f"OK ({res['notes']})"
    if v == "OK_LANDING":
        return f"LANDING-ONLY ({res['notes']})"
    return f"{v}: {res['notes']}"

md_bad = [f"# MONSTARE — BAD / BROKEN SOURCE LINKS ({DATE})",
          "",
          "Row-by-row verification of Readable Source URLs and Source Landing URLs in",
          "`Monstare_Evidence_Matrix_Source_Links_v3_Staleness_Patched_artifact.xlsx`.",
          "A row is BROKEN if its Readable Source URL is dead, blocked, unreadable, or missing.",
          "",
          f"- Rows BROKEN or NO_URL: **{len(bad_rows)}**",
          f"- Rows with CAVEAT (readable but scanned/landing-only/stub): **{len(caveat_rows)}**",
          f"- Rows READY (readable URL verified note-takable): **{len(ready_rows)}**",
          "",
          "Full per-URL detail: `Monstare_source_link_audit_2026-08-13.csv`.",
          ""]
if bad_rows:
    md_bad.append("## BROKEN / NO-URL ROWS")
    md_bad.append("")
    md_bad.append("| RowID | Citation | Status | Readable URL result | Landing URL result |")
    md_bad.append("|---|---|---|---|---|")
    for r in bad_rows:
        md_bad.append(f"| {r['ID']} | {r['Citation']} | {r['RowStatus']} | "
                      f"{res_brief(r['ReadableResult'])} | {res_brief(r['LandingResult'])} |")
    md_bad.append("")
else:
    md_bad.append("## BROKEN ROWS: none")
    md_bad.append("")
if caveat_rows:
    md_bad.append("## CAVEAT ROWS (readable, but not clean full-text)")
    md_bad.append("")
    md_bad.append("| RowID | Citation | Readable URL result |")
    md_bad.append("|---|---|---|")
    for r in caveat_rows:
        md_bad.append(f"| {r['ID']} | {r['Citation']} | {res_brief(r['ReadableResult'])} |")
    md_bad.append("")
bad_path = f"/opt/data/Monstare_bad_source_links_{DATE}.md"
with open(bad_path, "w") as f:
    f.write("\n".join(md_bad))
print(f"BAD LIST: {bad_path}", flush=True)

# ----- full report (markdown) -----
md = ["# MONSTARE SOURCE-LINK AUDIT REPORT",
      f"Date: {DATE}",
      "",
      f"- Rows audited: {len(rows_out)} (129 matrix rows)",
      f"- Unique URLs checked: {len(URLS)} (readable + landing columns)",
      f"- READY: {len(ready_rows)} | CAVEAT: {len(caveat_rows)} | BROKEN/NO_URL: {len(bad_rows)}",
      "",
      "## Verdict distribution (per URL)",
      ""]
vc = Counter()
for res in results.values():
    vc[res["verdict"]] += 1
md += [f"- {v}: {c}" for v, c in vc.most_common()]
md += ["", "## BROKEN / CAVEAT ROWS", ""]
md += [f"### {r['ID']} — {r['Citation']}  ({r['RowStatus']})",
       f"- Readable: {res_brief(r['ReadableResult'])}",
       f"- Landing:  {res_brief(r['LandingResult'])}",
       f"- Access Type: {r['AccessType']}",
       f"- Discovery Status: {r['DiscoveryStatus']}",
       ""]
md += ["## READY ROWS", ""]
md += [f"- {r['ID']}: {r['Citation']} — {res_brief(r['ReadableResult'])}" for r in ready_rows]
report_path = f"/opt/data/Monstare_source_link_audit_{DATE}.md"
with open(report_path, "w") as f:
    f.write("\n".join(md))
print(f"REPORT: {report_path}", flush=True)
print("DONE", flush=True)
