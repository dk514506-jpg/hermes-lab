#!/usr/bin/env python3
"""Verify HUI-2024 §32 prosthesis-vs-replacement passage in the local PDF."""
import pymupdf, re

doc = pymupdf.open("/opt/data/machine and sovereignty yuk hui.pdf")
hits = []
for p in range(len(doc)):
    t = doc[p].get_text() or ""
    if "prosthesis" in t.lower() or "prosthetic" in t.lower():
        hits.append((p + 1, t))
print(f"pages mentioning prosthesis/prosthetic: {len(hits)}")
for p, t in hits[:6]:
    t2 = re.sub(r"[ \t]+", " ", t)
    idx = t2.lower().find("prosthes")
    print(f"--- page {p} ---")
    print(t2[max(0, idx - 400):idx + 700])
    print()
doc.close()
