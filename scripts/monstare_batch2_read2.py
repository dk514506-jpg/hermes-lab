#!/usr/bin/env python3
"""Re-extract CORE-09 text + A9-05 full abstract from cached html."""
import pymupdf, re

doc = pymupdf.open("/opt/data/Monstare_batch1_sources/CORE-09_cand.pdf")
txt = ""
for i in range(min(10, len(doc))):
    t = doc[i].get_text() or ""
    txt += t
    if len(re.sub(r"\s+", "", txt)) > 3000:
        break
print("=== CORE-09 Carver & Scheier (first pages w/ text) ===")
print(re.sub(r"[ \t]+", " ", re.sub(r"\s+", " ", txt))[:2200])
doc.close()

raw = open("/opt/data/Monstare_batch1_sources/A9-05_front.html", encoding="utf-8", errors="replace").read()
txt = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
txt = re.sub(r"(?s)<[^>]+>", " ", txt)
txt = re.sub(r"\s+", " ", txt)
idx = txt.find("Information overload is a problem")
print("\n=== A9-05 Arnold et al. abstract (full) ===")
print(txt[idx:idx + 1600] if idx >= 0 else "abstract not found")
