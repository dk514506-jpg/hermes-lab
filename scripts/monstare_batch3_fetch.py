#!/usr/bin/env python3
"""Download CORE-03 + CORE-11 PDFs into Monstare_batch3_sources/, verify text layer (pypdf + pymupdf first pages), and pull archive.org metadata for CORE-12."""
import os, subprocess, urllib.request, json, sys

OUT = "/opt/data/Monstare_batch3_sources"
os.makedirs(OUT, exist_ok=True)

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}

PDFS = {
    "CORE-03": "https://selfdeterminationtheory.org/wp-content/uploads/2014/04/2012_VansteenkisteWilliamsResnicow_InterventionDevelopment_IJBNPA.pdf",
    "CORE-11": "https://www.hbs.edu/ris/Publication%20Files/09-083.pdf",
}

def fetch(url, dest):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
        f.write(r.read())
    return os.path.getsize(dest)

for rid, url in PDFS.items():
    dest = f"{OUT}/{rid}.pdf"
    if not os.path.exists(dest):
        try:
            n = fetch(url, dest)
            print(f"{rid}: downloaded {n} bytes -> {dest}")
        except Exception as e:
            print(f"{rid}: DOWNLOAD FAILED {e}")
            continue
    else:
        print(f"{rid}: already present")

# text-layer verification with pypdf, then pymupdf on first pages
try:
    from pypdf import PdfReader
    for rid in PDFS:
        p = f"{OUT}/{rid}.pdf"
        if not os.path.exists(p):
            continue
        try:
            r = PdfReader(p)
            txt = "".join((pg.extract_text() or "") for pg in r.pages[:4])
            print(f"{rid}: pypdf pages={len(r.pages)} first4_chars={len(txt)} head={txt[:80]!r}")
        except Exception as e:
            print(f"{rid}: pypdf error {e}")
except ImportError:
    print("pypdf not available")

try:
    import fitz
    for rid in PDFS:
        p = f"{OUT}/{rid}.pdf"
        if not os.path.exists(p):
            continue
        try:
            doc = fitz.open(p)
            txt = "".join(doc[i].get_text() for i in range(min(4, doc.page_count)))
            print(f"{rid}: pymupdf pages={doc.page_count} first4_chars={len(txt)} head={txt[:80]!r}")
        except Exception as e:
            print(f"{rid}: pymupdf error {e}")
except ImportError:
    print("pymupdf not available")

# archive.org metadata for CORE-12 (abstract-level source)
try:
    req = urllib.request.Request("https://archive.org/metadata/schedulesofreinf0000fers", headers=UA)
    md = json.load(urllib.request.urlopen(req, timeout=40))
    meta = md.get("metadata", {})
    for k in ["title", "creator", "description", "date", "subject", "publisher"]:
        v = meta.get(k)
        if v:
            s = v if isinstance(v, str) else " ".join(str(x) for x in v)
            print(f"CORE-12 archive meta {k}: {s[:400]}")
except Exception as e:
    print(f"CORE-12 metadata error: {e}")
