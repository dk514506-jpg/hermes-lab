#!/usr/bin/env python3
"""Journal-API seed probe for literature-review campaigns.

Probes OpenAlex, PubMed, arXiv, and Semantic Scholar (all free/keyless) with
the QUERIES below and writes a seed registry (JSONL + readable MD) that
council members extend rather than re-derive. Validated 2026-08-06 on the
Motivational-Ecology campaign.

Usage:
    python3 journal_api_probe.py <output_dir> [--per N]

Edit QUERIES per campaign. Declare the window convention in the registry
header before dispatching the council.

Pitfalls encoded (each cost real debugging time):
  * Never pre-encode %22 into the OpenAlex filter before urllib.parse.quote()
    — quote() turns % into %2522 and every query silently returns count=0.
    Use literal '"' in the filter string and let quote(filter_str, safe=':,-')
    do the encoding.
  * OpenAlex multi-concept queries need explicit OR/AND between quoted
    phrases; a bare multi-word string is treated as one exact phrase.
  * primary_location can exist with source=None — guard every .get().
  * 429 under burst: exponential backoff honoring Retry-After; one API's
    rate limit must not abort the other APIs.
"""
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = {"User-Agent": "research-campaign-probe/0.1 (mailto:research@example.com)"}
WINDOW = "2024-01-01"  # inclusive lower bound; adjust per campaign

# name -> (api, query expression). OpenAlex accepts quoted phrases joined by
# OR/AND; PubMed takes its [Title/Abstract] syntax; arXiv takes plain words.
QUERIES = [
    # ("area_key", "openalex", '"motivational interviewing"'),
    # ("area_key", "pubmed", "motivational interviewing"),
    # ("area_key", "arxiv", "proactive agents"),
    # ("area_key", "s2", "empowerment human agency"),
]


def get(url, timeout=25, retries=3):
    last = None
    for i in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429:
                wait = 2 * (2 ** i)
                if e.headers.get("Retry-After"):
                    wait = max(wait, int(e.headers["Retry-After"]))
                time.sleep(wait)
                continue
            raise
        except Exception as e:
            last = e
            time.sleep(1)
    raise last


def openalex(query, per=6):
    expr = query if (" OR " in query or " AND " in query) else f'"{query}"'
    f = f'from_publication_date:{WINDOW},title_and_abstract.search:{expr}'
    url = ("https://api.openalex.org/works?filter=" + urllib.parse.quote(f, safe=":,-") +
           f"&sort=cited_by_count:desc&per-page={per}")
    data = json.loads(get(url))
    meta_count = data.get("meta", {}).get("count", 0)
    out = []
    for w in data.get("results", []):
        pl = w.get("primary_location") or {}
        src = pl.get("source") or {}
        out.append({
            "title": w.get("title") or w.get("display_name"),
            "year": w.get("publication_year"),
            "authors": [a.get("author", {}).get("display_name") for a in w.get("authorships", []) if a.get("author")][:6],
            "venue": src.get("display_name"),
            "cited": w.get("cited_by_count"),
            "doi": w.get("doi"),
            "openalex_id": w.get("id"),
            "url": pl.get("landing_page_url"),
        })
    return meta_count, out


def pubmed(query, per=6):
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    q = urllib.parse.quote(f'({query}[Title/Abstract]) AND 2024:2026[dp]')
    ids = json.loads(get(f"{base}/esearch.fcgi?db=pubmed&retmode=json&retmax={per}&term={q}"))
    plist = ids["esearchresult"].get("idlist", [])
    out = []
    if plist:
        s = get(f"{base}/esummary.fcgi?db=pubmed&retmode=json&id={','.join(plist)}")
        for pid, rec in json.loads(s)["result"].items():
            if pid == "uids":
                continue
            out.append({
                "title": rec.get("title"),
                "year": rec.get("pubdate", "")[:4],
                "authors": [a["name"] for a in rec.get("authors", [])][:6],
                "venue": rec.get("fulljournalname"),
                "pmid": pid,
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pid}/",
            })
        time.sleep(0.5)
    return out


def arxiv(query, per=6):
    q = urllib.parse.quote(f'all:"{query}"')
    url = (f"https://export.arxiv.org/api/query?search_query={q}"
           f"&max_results={per}&sortBy=submittedDate&sortOrder=descending")
    root = ET.fromstring(get(url))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for e in root.findall("a:entry", ns):
        aid = e.find("a:id", ns).text.strip().split("/abs/")[-1]
        out.append({
            "title": (e.find("a:title", ns).text or "").strip().replace("\n", " "),
            "year": (e.find("a:published", ns).text or "")[:10],
            "authors": [a.find("a:name", ns).text for a in e.findall("a:author", ns)][:6],
            "venue": "arXiv",
            "arxiv_id": aid,
            "url": f"https://arxiv.org/abs/{aid}",
        })
    time.sleep(3)
    return out


def s2(query, per=6):
    url = ("https://api.semanticscholar.org/graph/v1/paper/search?query=" +
           urllib.parse.quote(query) + f"&year=2024-&limit={per}&fields=title,year,authors,venue,citationCount,externalIds,openAccessPdf")
    try:
        data = json.loads(get(url))
    except Exception:
        return []  # rate-limited → empty, not fatal
    out = []
    for p in data.get("data", []):
        out.append({
            "title": p.get("title"),
            "year": p.get("year"),
            "authors": [a["name"] for a in p.get("authors", [])][:6],
            "venue": p.get("venue"),
            "cited": p.get("citationCount"),
            "url": (p.get("openAccessPdf") or {}).get("url"),
        })
    time.sleep(1.2)
    return out


def main():
    if len(sys.argv) < 2 or not QUERIES:
        print(__doc__)
        sys.exit(1 if not QUERIES else 0)
    out_dir = sys.argv[1].rstrip("/")
    per = 6
    if "--per" in sys.argv:
        per = int(sys.argv[sys.argv.index("--per") + 1])
    out_jsonl = f"{out_dir}/api_seed.jsonl"
    out_md = f"{out_dir}/api_seed.md"

    rows = []
    with open(out_jsonl, "w") as jf:
        for key, api, q in QUERIES:
            try:
                meta_n = None
                if api == "openalex":
                    meta_n, res = openalex(q, per)
                elif api == "pubmed":
                    res = pubmed(q, per)
                elif api == "arxiv":
                    res = arxiv(q, per)
                else:
                    res = s2(q, per)
                for r in res:
                    r["_api"] = api
                    r["_query"] = key
                    jf.write(json.dumps(r) + "\n")
                rows.append((key, api, q, res))
                tag = f" (total matches: {meta_n})" if meta_n is not None else ""
                print(f"[{api}] {key}: {len(res)} hits{tag}")
            except Exception as e:
                print(f"[{api}] {key}: ERROR {e}")

    with open(out_md, "w") as md:
        md.write(f"# API Seed Registry\n\nWindow: {WINDOW}.. (declare convention)\n"
                 f"APIs: OpenAlex, PubMed, arXiv, Semantic Scholar\n\n")
        for key, api, q, res in rows:
            md.write(f"\n## {key} ({api}) — \"{q}\"\n\n")
            for r in res:
                md.write(f"- ({r.get('year')}) {r.get('title')} — {', '.join((r.get('authors') or [])[:3])}\n")
                md.write(f"  venue: {r.get('venue')} | cited: {r.get('cited', 'n/a')} | {r.get('url', r.get('doi', r.get('pmid')))} | {r.get('arxiv_id', '')}\n")

    print(f"\nWrote {out_jsonl} and {out_md}")


if __name__ == "__main__":
    main()
