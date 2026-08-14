#!/usr/bin/env python3
"""Batch-3 source staging: download + verify CORE-13 (PMC PDF), CORE-16 (Flow mirror), CORE-19 (MRT author PDF); check PMC4372982 identity."""
import os, urllib.request, re

OUT = "/opt/data/Monstare_batch3_sources"
os.makedirs(OUT, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}

JOBS = {
    "CORE-13": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1473025/pdf/nihms-2125.pdf",
    "CORE-16": "https://timothydavidson.com/Library/Books/Csikzetmihalyi-1990-Psychology%20of%20Optimal%20Experience/Csikszentmihalyi-1990-The%20Pyschology%20of%20optimal%20experience.pdf",
    "CORE-19": "https://www.ambujtewari.com/research/klasnja15microrandomized.pdf",
}

def fetch(url, dest):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as r, open(dest, "wb") as f:
        f.write(r.read())
    return os.path.getsize(dest)

for rid, url in JOBS.items():
    dest = f"{OUT}/{rid}.pdf"
    if not os.path.exists(dest):
        try:
            n = fetch(url, dest)
            print(f"{rid}: downloaded {n} bytes")
        except Exception as e:
            print(f"{rid}: DOWNLOAD FAILED {e}")
    else:
        print(f"{rid}: already present")

# verify text layer with pymupdf (first 4 pages + middle sample)
import pymupdf
for rid in JOBS:
    p = f"{OUT}/{rid}.pdf"
    if not os.path.exists(p):
        continue
    try:
        doc = pymupdf.open(p)
        n = doc.page_count
        idx = sorted(set(list(range(min(4, n))) + [n // 2]))
        total = 0
        head = ""
        for i in idx:
            t = doc[i].get_text()
            total += len(t)
            if head == "" and t.strip():
                head = t.strip()[:100].replace("\n", " ")
        print(f"{rid}: pymupdf pages={n} sampled_chars={total} head={head!r}")
    except Exception as e:
        print(f"{rid}: pymupdf error {e}")

# PMC4372982 identity check
try:
    req = urllib.request.Request("https://pmc.ncbi.nlm.nih.gov/articles/PMC4372982/", headers=UA)
    html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "ignore")
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    print("PMC4372982 title:", m.group(1).strip()[:200] if m else "n/a")
    if "Microrandomized" in html or "microrandomized" in html:
        print("PMC4372982 mentions microrandomized: YES")
except Exception as e:
    print("PMC4372982 fetch error:", e)

# What is 10.1016/j.cct.2015.07.003? (the matrix's seeded landing DOI)
try:
    req = urllib.request.Request("https://doi.org/10.1016/j.cct.2015.07.003", headers=UA)
    html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "ignore")
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    print("cct.2015.07.003 title:", m.group(1).strip()[:200] if m else "n/a")
except Exception as e:
    print("cct DOI fetch error:", e)
