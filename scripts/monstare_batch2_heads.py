#!/usr/bin/env python3
"""Batch-2 reading heads: local PDFs + Frontiers abstract."""
import pymupdf, re, os

def head(path, label, pages=5, n=1500):
    doc = pymupdf.open(path)
    txt = "".join((doc[i].get_text() or "") for i in range(min(pages, len(doc))))
    txt = re.sub(r"[ \t]+", " ", txt)
    print(f"### {label}: {len(doc)}p")
    print(" ", re.sub(r"\s+", " ", txt)[:n])
    print()
    doc.close()

head("/opt/data/Monstare_batch1_sources/CORE-09_cand.pdf", "CORE-09 Carver&Scheier (weebly)")
head("/opt/data/Monstare_batch1_sources/CORE-10_cand.pdf", "CORE-10 Locke&Latham (ubalt)")
head("/opt/data/Monstare_source_audit_cache/https_ics.uci.edu_gmark_chi08-mark.pdf.pdf", "A9-01 Mark et al CHI2008")
head("/opt/data/Monstare_source_audit_cache/https_ics.uci.edu_gmark_CHI2004.pdf.pdf", "A9-02 Gonzalez&Mark CHI2004")

# A9-05 Frontiers abstract from cached html
raw = open("/opt/data/Monstare_batch1_sources/A9-05_front.html", encoding="utf-8", errors="replace").read()
m = re.search(r"(?is)<section[^>]*class=\"[^\"]*abstract[^\"]*\"[^>]*>(.*?)</section>", raw)
if not m:
    m = re.search(r"(?is)<div[^>]*class=\"[^\"]*abstract[^\"]*\"[^>]*>(.*?)</div>", raw)
if m:
    txt = re.sub(r"(?s)<[^>]+>", " ", m.group(1))
    txt = re.sub(r"\s+", " ", txt).strip()
    print("### A9-05 Frontiers abstract")
    print(" ", txt[:1500])
else:
    # fallback: dump text around 'Abstract'
    txt = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    txt = re.sub(r"(?s)<[^>]+>", " ", txt)
    txt = re.sub(r"\s+", " ", txt)
    idx = txt.find("Abstract")
    print("### A9-05 Frontiers (fallback around 'Abstract')")
    print(" ", txt[idx:idx + 1500] if idx >= 0 else txt[:800])
