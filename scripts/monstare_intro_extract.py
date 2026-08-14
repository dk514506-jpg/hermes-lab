#!/usr/bin/env python3
"""Targeted extraction: A1-01 introduction core + HUI-2024 introduction."""
import pymupdf, re

# A1-01: pages 25-50 (Introduction sections 1-2: Prometheus + cosmotechnics definition)
doc = pymupdf.open("/opt/data/Monstare_batch1_sources/A1-01_raw.pdf")
txt = "".join((doc[i].get_text() or "") for i in range(24, 50))
txt = re.sub(r"[ \t]+", " ", txt)
print("=== A1-01 Introduction (pp.25-50) ===")
print(txt[:5200])
print()
doc.close()

# HUI-2024: pages 8-34 (Introduction: For a Planetary Thinking)
doc = pymupdf.open("/opt/data/machine and sovereignty yuk hui.pdf")
txt = "".join((doc[i].get_text() or "") for i in range(7, 34))
txt = re.sub(r"[ \t]+", " ", txt)
print("=== HUI-2024 Introduction (pp.8-34) ===")
print(txt[:5200])
doc.close()
