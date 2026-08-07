#!/usr/bin/env python3
"""Phase 2 API probe — seed candidate registry for Recent Evidence Review.

APIs (all free, keyless): OpenAlex, PubMed E-utilities, arXiv, Semantic Scholar.
Window convention: primary 2025-01-01..2026-08-06 (post-2024); 2024 flagged separately.
Outputs:
  council_notes/phase2_api_seed.jsonl  — machine-readable seed lines
  council_notes/phase2_api_seed.md     — readable digest
  stdout                                — compact digest for the parent context
"""
import json, time, urllib.error, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from datetime import date

OUT_JSONL = "/home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/council_notes/phase2_api_seed.jsonl"
OUT_MD    = "/home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/council_notes/phase2_api_seed.md"
WINDOW = "2024-01-01"  # inclusive lower bound; 2025+ is the strict post-2024 core

UA = {"User-Agent": "motivational-ecology-research/0.1 (mailto:research@example.com)"}

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
                time.sleep(wait)  # exponential backoff, honor Retry-After
                continue
            raise
        except Exception as e:
            last = e
            time.sleep(1)
    raise last

def openalex(query, per=6):
    # query may be a pre-formatted search expression; wrap bare phrases in quotes
    expr = query if (" OR " in query or " AND " in query) else f'"{query}"'
    f = f'from_publication_date:{WINDOW},title_and_abstract.search:{expr}'
    url = ("https://api.openalex.org/works?filter=" + urllib.parse.quote(f) +
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
        out.append({
            "title": e.find("a:title", ns).text.strip().replace("\n", " "),
            "year": e.find("a:published", ns).text[:10],
            "authors": [a.find("a:name", ns).text for a in e.findall("a:author", ns)][:6],
            "venue": "arXiv",
            "arxiv_id": e.find("a:id", ns).text.strip().split("/abs/")[-1],
            "url": f"https://arxiv.org/abs/{e.find('a:id', ns).text.strip().split('/abs/')[-1]}",
        })
    time.sleep(3)
    return out

def s2(query, per=6):
    url = ("https://api.semanticscholar.org/graph/v1/paper/search?query=" +
           urllib.parse.quote(query) + f"&year=2024-&limit={per}&fields=title,year,authors,venue,citationCount,externalIds,openAccessPdf")
    try:
        data = json.loads(get(url))
    except Exception:
        return []
    out = []
    for p in data.get("data", []):
        out.append({
            "title": p.get("title"),
            "year": p.get("year"),
            "authors": [a["name"] for a in p.get("authors", [])][:6],
            "venue": p.get("venue"),
            "cited": p.get("citationCount"),
            "url": p.get("openAccessPdf", {}).get("url") if p.get("openAccessPdf") else None,
        })
    time.sleep(1.2)
    return out

QUERIES = {
    "openalex": [
        ("MI_settings", '"motivational interviewing"'),
        ("COM-B_TDF_implementation", '"theoretical domains framework" OR "COM-B"'),
        ("SDT_digital", '"self-determination theory"'),
        ("skill_atrophy_AI", '"skill atrophy" OR "deskilling"'),
        ("empowerment_assistive_agents", '"human empowerment" OR "AI assistance"'),
        ("LLM_roleplay_training", '"role-play" OR "conversational training"'),
        ("proactive_personalized_agents", '"proactive" AND "assistant"'),
        ("behavior_latticing", '"user modeling" OR "motivation inference"'),
        ("cybernetics_autopoiesis", '"autopoiesis" OR "technodiversity" OR "second-order cybernetics"'),
    ],
    "pubmed": [
        ("MI_clinical", "motivational interviewing"),
        ("TDF_COMB", "theoretical domains framework OR COM-B"),
        ("SDT_health", "self-determination theory"),
    ],
    "arxiv": [
        ("LLM_roleplay_arxiv", "role-play"),
        ("skill_atrophy_arxiv", "deskilling"),
        ("empowerment_arxiv", "empowerment"),
        ("proactive_agents_arxiv", "proactive agents"),
    ],
    "s2": [
        ("behavior_latticing_s2", "motivation inference user modeling agents"),
        ("empowerment_s2", "AI assistance human empowerment skill atrophy"),
    ],
}

rows = []


def main():
    with open(OUT_JSONL, "w") as jf:
        for api, qs in QUERIES.items():
            for key, q in qs:
                try:
                    meta_n = None
                    if api == "openalex":
                        meta_n, res = openalex(q)
                    elif api == "pubmed":
                        res = pubmed(q)
                    elif api == "arxiv":
                        res = arxiv(q)
                    else:
                        res = s2(q)
                    for r in res:
                        r["_api"] = api
                        r["_query"] = key
                        jf.write(json.dumps(r) + "\n")
                    rows.append((api, key, q, res))
                    tag = f" (total matches: {meta_n})" if meta_n is not None else ""
                    print(f"[{api}] {key}: {len(res)} hits{tag}")
                except Exception as e:
                    print(f"[{api}] {key}: ERROR {e}")

    with open(OUT_MD, "w") as md:
        md.write(f"# Phase 2 API Seed Registry\n\nWindow: {WINDOW}..2026-08-06 (post-2024 core = 2025+)\nAPIs: OpenAlex, PubMed, arXiv, Semantic Scholar\n\n")
        for api, key, q, res in rows:
            md.write(f"\n## {key} ({api}) — \"{q}\"\n\n")
            for r in res:
                md.write(f"- ({r.get('year')}) {r.get('title')} — {', '.join((r.get('authors') or [])[:3])}\n")
                md.write(f"  venue: {r.get('venue')} | cited: {r.get('cited', 'n/a')} | {r.get('url', r.get('doi', r.get('pmid')))} | {r.get('arxiv_id', '')}\n")

    print(f"\nWrote {OUT_JSONL} and {OUT_MD}")


if __name__ == "__main__":
    main()
