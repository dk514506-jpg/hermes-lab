#!/usr/bin/env python3
"""Probe PDFs for a genuine text layer before deciding they are 'image-only'.

The Monstare matrix has carried stale 'image-only' flags that were WRONG (A1-07 Stiegler
and A1-11 Winner both have real text layers). Run this on any locally-cached PDF that a
row flags as image-only / scanned BEFORE asking the user to hunt a full-text copy.

Usage:
    uv run --with pymupdf python probe_pdf_textlayer.py <pdf> [<pdf> ...]

It prints, per file: page count, total text chars, per-page sample, and a mid-body text
sample (pages ~10-15, skipping front matter). A file with 0 total chars is genuinely
scanned/image-only. A file with meaningful chars AND clean prose on a mid-body page is
full-text readable — upgrade the matrix, don't hunt a copy.
"""
import sys
import pymupdf

def probe(path: str):
    print("=" * 70)
    print("FILE:", path)
    try:
        doc = pymupdf.open(path)
    except Exception as e:
        print("  OPEN FAILED:", e)
        return
    n = doc.page_count
    total = 0
    page_lens = []
    for i in range(n):
        L = len(doc[i].get_text().strip())
        total += L
        page_lens.append(L)
    print(f"  pages: {n}   total_text_chars: {total}")
    # show per-page sample across the whole doc (coarse)
    step = max(1, n // 10)
    sample = [(i, page_lens[i]) for i in range(0, n, step)]
    print("  per-page chars (sampled):", sample)
    if total == 0:
        print("  VERDICT: GENUINELY IMAGE-ONLY / SCANNED (0 chars) — need OCR or a text copy")
        return
    # find a mid-body page with real prose (skip front matter pages 0..2)
    found = None
    for i in range(3, n):
        t = doc[i].get_text().strip()
        if len(t) > 200:
            found = (i, t)
            break
    if found:
        print(f"  mid-body sample p{found[0]} ({len(found[1])} chars):")
        print("   ", found[1][:280].replace("\n", " | "))
        print("  VERDICT: FULL-TEXT READABLE (upgrade matrix, do NOT hunt a copy)")
    else:
        print("  VERDICT: chars present but no clean mid-body prose — inspect further "
              "(may be broken ToUnicode/garble; try firecrawl OCR)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for p in sys.argv[1:]:
        probe(p)
