#!/usr/bin/env python3
"""Build a corpus manifest for token-efficient ingestion.

Usage: python3 build_manifest.py <corpus_root> [output_dir]

Scans the corpus root for txt/md/pdf/docx files, extracts PDFs via
pdftotext into <output_dir>/_extracted/, and writes manifest.json with
per-file word counts and token estimates. Prints per-directory totals
and an artifact-type histogram (filename patterns) so the highest-signal
files (orientation/grammar, method maps) are visible before reading.

Validated on the Valens Anthologies corpus (115 files + 212-page book,
~940K tokens) — see large-corpus-ingestion skill.
"""
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path


def word_count(path: Path) -> int:
    if path.suffix.lower() == ".pdf":
        return 0  # extracted separately
    try:
        return len(path.read_text(encoding="utf-8", errors="ignore").split())
    except OSError:
        return 0


def extract_pdfs(corpus: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for pdf in corpus.rglob("*.pdf"):
        target = out_dir / f"{pdf.stem}.txt"
        if target.exists():
            continue
        subprocess.run(
            ["pdftotext", "-layout", str(pdf), str(target)],
            check=False,
            capture_output=True,
        )


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    corpus = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else corpus / "_extracted"
    extract_pdfs(corpus, out_dir)

    manifest = []
    totals = defaultdict(lambda: [0, 0])  # dir -> [files, est_tokens]
    for f in sorted(corpus.rglob("*")):
        if not f.is_file():
            continue
        if f.suffix.lower() not in {".txt", ".md", ".pdf", ".docx"}:
            continue
        if f.suffix.lower() == ".pdf":
            txt = out_dir / f"{f.stem}.txt"
            words = word_count(txt) if txt.exists() else 0
        else:
            words = word_count(f)
        est = int(words * 1.3)
        rel = f.relative_to(corpus)
        manifest.append({
            "path": str(rel),
            "book": f.parent.name,
            "file": f.name,
            "words": words,
            "est_tokens": est,
        })
        totals[f.parent.name][0] += 1
        totals[f.parent.name][1] += est

    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))

    print(f"=== CORPUS: {corpus} ===")
    print(f"{'Directory':<28} {'Files':>5} {'~tokens':>10}")
    for d, (n, t) in sorted(totals.items()):
        print(f"{d:<28} {n:>5} {t:>10,}")
    print(f"{'TOTAL':<28} {len(manifest):>5} {sum(t for _, t in totals.values()):>10,}")

    # Artifact-type histogram from filename patterns
    pats = Counter()
    for m in manifest:
        name = m["file"].lower()
        matched = False
        for key in ["orientation", "grammar", "register", "index", "worked_example",
                    "run_cards", "quarantine", "cross_book", "appendix", "ledger",
                    "method_family", "machine_readable", "map", "memo", "handoff",
                    "addendum", "data_pack", "implementation_plan"]:
            if key in name:
                pats[key] += 1
                matched = True
                break
        if not matched:
            pats["other"] += 1
    print("\n=== ARTIFACT TYPES ===")
    for k, v in pats.most_common():
        print(f"  {k}: {v}")

    print(f"\nManifest written to {out_dir / 'manifest.json'}")
    print("Read the manifest first. Then read distilled layers (orientation/grammar,")
    print("method maps, cross-references) before raw registers. Never read a 200+")
    print("page book end-to-end in context — use TOC + search_files.")


if __name__ == "__main__":
    main()
