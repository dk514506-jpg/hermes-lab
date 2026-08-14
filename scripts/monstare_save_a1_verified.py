#!/usr/bin/env python3
"""Save the verified A1-01 body passages (scan pp.25-50 + p.37 definition) to disk
so the charting record matches what Pip actually read."""
import pymupdf, re

doc = pymupdf.open("/opt/data/Monstare_batch1_sources/A1-01_raw.pdf")
txt = "".join((doc[i].get_text() or "") for i in range(24, 50))
txt = re.sub(r"[ \t]+", " ", txt)
out = "/opt/data/Monstare_batch1_sources/A1-01_intro_verified.txt"
with open(out, "w", encoding="utf-8") as f:
    f.write("A1-01 verified body passages (archive scan): PDF pages 25-50 ~ print pp.18-43.\n")
    f.write("Contains: Heidegger-impasse argument (Introduction), §1 The Becoming of Prometheus, §2 Cosmos Cosmology and Cosmotechnics (incl. cosmotechnics definition and Leroi-Gourhan/Gille critiques).\n\n")
    f.write(txt)
print("wrote", out, len(txt), "chars")

# also the definition page alone
t37 = doc[36].get_text() or ""
with open("/opt/data/Monstare_batch1_sources/A1-01_cosmotechnics_definition.txt", "w") as f:
    f.write("A1-01 cosmotechnics definition passage (archive scan PDF p.37 ~ print pp.19-20):\n\n")
    f.write(t37)
print("wrote A1-01_cosmotechnics_definition.txt", len(t37), "chars")
doc.close()
