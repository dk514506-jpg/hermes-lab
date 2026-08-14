#!/usr/bin/env python3
"""Second-pass disambiguation for source-link audits.

Pass 1 (matrix_url_audit.py) flags PDFs as BAD_SCANNED when pypdf extracts <~300 chars
from the first pages. That verdict is frequently WRONG: pypdf's xref parser fails on
malformed xref tables, and books often have scanned front matter (title pages, plates)
with a real text layer in the body. This script re-extracts with pymupdf (robust xref
handling) and samples the MIDDLE of the document before confirming "no text layer".

Usage:
    uv run --with pymupdf python3 second_pass_disambiguation.py <pdf1> [pdf2 ...]
    uv run --with pymupdf python3 second_pass_disambiguation.py --dir <cache_dir>

Exit: 0 always; prints one line per file:
    <label>: pages=N chars_first4p=X middle(N)=Y -> TEXT_OK | NO_TEXT
"""
import argparse
import os
import re
import sys

try:
    import pymupdf  # preferred import; 'import fitz' also works on older builds
except ImportError:
    import fitz as pymupdf

MIN_CHARS = 300
MID_SAMPLE = 5  # pages sampled around the document middle


def extract_chars(doc, start, count):
    txt = ""
    for i in range(start, min(start + count, len(doc))):
        txt += doc[i].get_text() or ""
    return len(re.sub(r"\s+", "", txt))


def check(path, label=None):
    label = label or os.path.basename(path)
    try:
        doc = pymupdf.open(path)
    except Exception as e:
        print(f"{label}: ERROR {type(e).__name__}: {str(e)[:120]}")
        return
    n = len(doc)
    first = extract_chars(doc, 0, min(4, n))
    if first >= MIN_CHARS:
        print(f"{label}: pages={n} chars_first4p={first} -> TEXT_OK")
        doc.close()
        return
    # first pages empty or scanned front matter: sample the middle
    mid = n // 2
    middle = extract_chars(doc, mid, min(MID_SAMPLE, n - mid))
    verdict = "TEXT_OK" if middle >= MIN_CHARS else "NO_TEXT"
    print(f"{label}: pages={n} chars_first4p={first} middle({mid}-{mid + MID_SAMPLE})={middle} -> {verdict}")
    doc.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="*", help="PDF files to re-check")
    ap.add_argument("--dir", help="Check every *.pdf in a directory")
    ap.add_argument("--label", help="Label prefix for files given as bare paths")
    args = ap.parse_args()

    files = list(args.paths)
    if args.dir:
        files += [os.path.join(args.dir, f) for f in sorted(os.listdir(args.dir)) if f.lower().endswith(".pdf")]
    if not files:
        ap.error("no PDFs given (pass paths or --dir)")

    for f in files:
        check(f, label=args.label)


if __name__ == "__main__":
    main()
