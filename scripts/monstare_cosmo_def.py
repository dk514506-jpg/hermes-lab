#!/usr/bin/env python3
"""Grep A1-01 for the cosmotechnics definition passage."""
import pymupdf, re

doc = pymupdf.open('/opt/data/Monstare_batch1_sources/A1-01_raw.pdf')
# search pages 15-60 for 'cosmotechnics' occurrences with context
target = None
for p in range(14, 60):
    t = doc[p].get_text() or ""
    if "cosmotechnics" in t.lower() and len(t) > 500:
        target = (p, t)
        break
if target:
    p, t = target
    t = re.sub(r"[ \t]+", " ", t)
    print(f"=== A1-01 page {p+1}: cosmotechnics passage ===")
    print(t[:4000])
else:
    print("no cosmotechnics passage found in pp.15-60")
doc.close()
