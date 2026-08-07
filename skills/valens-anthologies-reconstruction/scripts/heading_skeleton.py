#!/usr/bin/env python3
"""Print heading skeletons for every .txt file under the given directories.

Corpus-scale reading aid: when a task says "read every file in these
folders" but the corpus is too large to load verbatim (~MBs / tens of
thousands of lines), run this first to get a structure map of every file
for a few KB of context. Then full-read the highest-signal files and
skeleton-plus-targeted-body the rest.

Usage:
    python heading_skeleton.py <dir-or-file> [<dir-or-file> ...]

Notes:
- One execute_code run per BOOK folder when stdout is capped (~50KB):
  batching too many files truncates the middle of the output.
- Heading-like lines: all-caps titles, numbered sections, '##'/'===='
  markers, and long uppercase runs. Adjust the regex if a corpus uses
  different conventions.
- Lines are truncated to 110 chars to keep the skeleton compact.
"""
import re
import sys
from pathlib import Path


def heading_like(text: str) -> bool:
    t = text.strip()
    if not t:
        return False
    if len(t) >= 110:
        return False
    if t.isupper():
        return True
    if re.match(r"^\d+\.\d*\s+[A-Z]", t):
        return True
    if t.startswith("#") or t.startswith("="):
        return True
    if re.match(r"^[A-Z][A-Z\s]{15,}$", t):
        return True
    return False


def skeleton(path: Path) -> list[str]:
    out = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return [f"ERROR reading {path}: {e}"]
    total = text.count("\n") + 1
    out.append(f"########## {path} ({total} lines) ##########")
    for line in text.splitlines():
        if heading_like(line):
            out.append(line.strip()[:110])
    return out


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1
    targets = []
    for arg in argv:
        p = Path(arg)
        if p.is_dir():
            targets.extend(sorted(p.glob("*.txt")))
        elif p.is_file():
            targets.append(p)
        else:
            print(f"skipping (not found): {arg}", file=sys.stderr)
    for t in targets:
        print("\n".join(skeleton(t)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
