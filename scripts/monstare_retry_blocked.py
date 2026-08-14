#!/usr/bin/env python3
"""Retry curl with alternate UA/referer on remaining blocked readable URLs."""
import os, subprocess, re

UA2 = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
       "(KHTML, like Gecko) Version/17.0 Safari/605.1.15")
TARGETS = [
    ("A3-08", "https://salford-repository.worktribe.com/preview/1493547/The20Walkthrough20Method20-20Final20Pre-print20version1.pdf"),
    ("A4-04", "https://repositorio.udd.cl/bitstream/11447/6275/1/Place%20attachment%20and%20identification%20as%20predictors%20of%20expected%20landscape%20restorativeness.pdf"),
    ("A7-06", "https://www.leiderschapsdomeinen.nl/wp-content/uploads/2016/12/Zimmerman-B.-2002-Becoming-Self-Regulated-Learner.pdf"),
    ("A7-09", "https://research.aalto.fi/files/42021453/Oulasvirta_Combinatorial_optimization_of_Graphical_user_interface.pdf"),
    ("A3-06", "https://www.morganclaypool.com/doi/pdf/10.2200/S00438ED1V01Y201207HCI015"),
]

for rid, url in TARGETS:
    out = f"/opt/data/Monstare_batch1_sources/{rid}_retry.bin"
    try:
        p = subprocess.run(
            ["curl", "-sL", "--max-time", "60", "-A", UA2,
             "-e", "https://www.google.com/", "-o", out,
             "-w", "%{http_code}", url],
            capture_output=True, text=True, timeout=70)
        code = p.stdout.strip() or "000"
    except subprocess.TimeoutExpired:
        code = "TIMEOUT"
    head = b""
    try:
        with open(out, "rb") as f:
            head = f.read(8)
    except OSError:
        pass
    ispdf = head.startswith(b"%PDF")
    size = os.path.getsize(out) if os.path.exists(out) else 0
    print(f"{rid}: http={code} ispdf={ispdf} size={size}")
    if not ispdf and os.path.exists(out):
        os.remove(out)

# CORE-06 replacement PDF text check
import pymupdf
doc = pymupdf.open("/opt/data/Monstare_batch1_sources/CORE-06_raw.pdf")
txt = "".join((doc[i].get_text() or "") for i in range(min(4, len(doc))))
chars = len(re.sub(r"\s+", "", txt))
print(f"CORE-06 bsfrey PDF: {len(doc)} pages, chars first4p = {chars} -> {'TEXT_OK' if chars > 300 else 'NO_TEXT'}")
print("HEAD:", txt[:280].replace("\n", " "))
doc.close()
