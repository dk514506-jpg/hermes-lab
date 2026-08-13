#!/usr/bin/env python3
"""Extract targeted reading passages for batch-1 charting (Pip pass).
Saves full head/tail windows to Monstare_batch1_sources/ and prints compact windows."""
import pymupdf, re, os

OUT = "/opt/data/Monstare_batch1_sources"

def dump(label, path, head_pages=12, tail_pages=8, max_print=1600):
    doc = pymupdf.open(path)
    n = len(doc)
    head = "".join((doc[i].get_text() or "") for i in range(min(head_pages, n)))
    tail = "".join((doc[i].get_text() or "") for i in range(max(0, n - tail_pages), n))
    full = head + "\n[---MIDDLE OMITTED---]\n" + tail
    outpath = os.path.join(OUT, f"{label}_reading.txt")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(f"SOURCE: {label} | pages {n}\n\n{full}")
    h = re.sub(r"\s+", " ", head)
    t = re.sub(r"\s+", " ", tail)
    print(f"### {label}: {n}p -> {outpath}")
    print(f"  HEAD({min(head_pages,n)}p): {h[:max_print]}")
    print(f"  TAIL({min(tail_pages,n)}p): {t[:max_print]}")
    print()
    doc.close()

dump("CORE-06", "/opt/data/Monstare_batch1_sources/CORE-06_raw.pdf", head_pages=10, tail_pages=6)
dump("A1-01", "/opt/data/Monstare_batch1_sources/A1-01_raw.pdf", head_pages=14, tail_pages=10)
dump("HUI-2024", "/opt/data/machine and sovereignty yuk hui.pdf", head_pages=16, tail_pages=10)
