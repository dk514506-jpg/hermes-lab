#!/usr/bin/env python3
"""Extract HUI-2024 Introduction + A1-01 cosmotechnics section."""
import pymupdf, re

doc = pymupdf.open('/opt/data/machine and sovereignty yuk hui.pdf')
txt = "".join((doc[i].get_text() or "") for i in range(7, 34))
txt = re.sub(r"[ \t]+", " ", txt)
print("=== HUI-2024 Introduction (pp.8-34) ===")
print(txt[:6000])
doc.close()

doc = pymupdf.open('/opt/data/Monstare_batch1_sources/A1-01_raw.pdf')
txt = "".join((doc[i].get_text() or "") for i in range(29, 40))
txt = re.sub(r"[ \t]+", " ", txt)
print("\n=== A1-01 sect2 cosmotechnics (pp.30-40) ===")
print(txt[:5000])
doc.close()
