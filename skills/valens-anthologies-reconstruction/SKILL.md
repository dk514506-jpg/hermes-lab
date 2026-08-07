---
name: valens-anthologies-reconstruction
description: Use when reading/distilling the Valens Anthologies corpus.
version: 1.0
author: greenknight
tags: [valens, anthologies, astrology, corpus, reconstruction, home-lab, quarantine, distillation]
platforms: [linux]
---

# Valens Anthologies Reconstruction

The Valens Anthologies project reconstructs Vettius Valens' *Anthologies*
(Mark T. Riley translation, supplied as per-book PDFs) into a governed
artifact corpus under:

```
~/.hermes/hermes-agent/docs/Valens Anthologies/Anthologies Artifacts/
  Book N Artifacts/<valens_book_N_*.txt>
```

Each book folder holds 9–15 artifacts following a fixed production order.
Every artifact is a reconstruction document with a strict result-state
discipline (PARTIAL / VERIFIED / BLOCKED / QUARANTINED) and an explicit
final result line.

## When to Use

- Reading/distilling the artifact corpus for a book or book-range. FULL
  corpus read completed 2026-07-30: all 115 artifacts across Books 1–10
  plus the 185K-word book text, distilled into the wiki at
  `~/Documents/digital_brain/valens_wiki/` (21 pages: 10 book summaries,
  7 concept pages, 2 syntheses — `syntheses/valens-operating-logics.md`
  and `syntheses/home-lab-applications.md` are the distilled entry points
  for recovered operating logics).
- Building the next artifact in the sequence for a book.
- Any task that references "the Valens corpus", "Book V/VI/VII artifacts",
  the home-lab "Lots layer", or the planetary-persona source-grounded work.
- **The method generalizes.** The reconstruction discipline (witness
  conflicts preserved, printed-vs-reconstructed separated, quarantine law,
  corpus-scale reading) transfers to non-Valens research campaigns.
  Validated 2026-08-06 on the Motivational-Ecology campaign
  (`~/.hermes/hermes-agent/docs/Ecology/Foundation/`): same evidence
  discipline + council distillation + governed artifacts. For the
  generalized playbook see the `recent-evidence-distillation` skill
  (parent-side campaign orchestration + council critique rounds) and the
  `large-corpus-ingestion` skill (subagent distillation ladder).

## The Standard Artifact Sequence (per book)

1. Two-Pass Reading Ledger
2. Orientation and Root Technical Grammar   ← highest signal
3. Method-Family and Dependency Map         ← highest signal
4. Calculation / Period-Unit / Table Dependency Appendix
5. Worked Example Reconstruction Ledger
6. Topical registers (operative month/day, aphetic points, degree
   contact, distribution registers, etc.)
7. Authority / Epistemology / Method-Criticism Register
8. Quarantine Appendix and Dangerous-Material Update
9. Source Procedure Index
10. Run Cards
11. Machine-Readable Data Pack
12. Cross-Book Interface Map

Ordering law: ORIENT THE LANGUAGE → SEPARATE METHODS → RECONSTRUCT
CALCULATIONS → TEST EXAMPLES → STABILIZE REGISTERS → INDEX PROCEDURES →
QUARANTINE → OPERATIONALIZE → MAP CROSS-BOOK EFFECTS.

## Corpus-Scale Reading Protocol (context-budgeted)

When asked to "read every file" in a folder range but the corpus exceeds
context (Books 5–7 ≈ 1.95 MB / ~44K lines across 38 files):

1. **Enumerate + size-budget first** — `search_files(target='files')` to
   list all files, then `wc -l` and `du -b` per folder to know the volume
   before reading anything.
2. **Skeleton-extract every file cheaply** — run
   `scripts/heading_skeleton.py` over each folder (one execute_code run
   per BOOK, not per file — stdout caps ~50KB and batches of 7–9 files
   fill it). The skeleton maps every file's section structure for a few
   KB of context. Batch 2–3 book folders as parallel execute_code calls.
3. **Full-read in signal order** — orientation/grammar and
   method-family/dependency maps first (highest signal), then worked
   examples, then registers, then quarantine/index/run-card/machine-pack
   (skeleton + targeted body reads suffice for the low-signal tail).
4. **Fall back to direct `read_file` when execute_code's read_file
   wrapper throws** (transient `KeyError: 'content'` seen once) — re-run
   the same reads with the native tool; it is a retry/fallback pattern,
   not evidence the wrapper is broken.
5. **Deliverable discipline** — the parent task usually specifies an
   exact output format (e.g. 600–900 word structured distillation with
   per-book sections: core grammar, methods/dependencies, worked-example
   patterns, home-lab relevance, cross-book relations, emergent
   principles). Reuse `references/books5-7-technical-distillation.md` as
   the knowledge base; the wiki (`~/Documents/digital_brain/valens_wiki/`)
   is now the durable store for the full-corpus distillations.
6. **Larger partition reads** — when a book-range exceeds even skeleton
   budget, split the corpus across parallel subagents via delegate_task
   (one per book-group, exact output format in context, 600-900 words
   back) — see the `large-corpus-ingestion` skill for the full ladder.

## Verification Discipline (the corpus's own rules)

These recur in every artifact and must be honored in any reconstruction:

- **Two sign-distance conventions coexist in Book V**: INCLUSIVE
  (origin counted as 1, remainder 0 → 12) governs interval/matrix/day
  families; EXCLUSIVE (0–11) is attested once (degree-angle passage).
  Declare the convention per method — never assume one globally.
- **Printed vs reconstructed values stay separate.** A reconstruction
  that makes an example coherent is not promoted to MAIN_TEXT_EXPLICIT.
- **Ordinal ≠ completed count** (Book VI: 148 completed 129-day cycles
  vs the 149th current cycle; 270 days vs "tenth month").
- **Unit typing is constitutive** — the same integer (25, 129) acts as
  years/months/days/weights by scale; NUMBER_VALUE and UNIT are separate
  fields.
- **Direction matters, not just magnitude** — transmitter → receiver is
  non-symmetric; a reversed pairing can coincidentally satisfy a test.
- **Witness conflicts are preserved, not harmonized** (operative-month
  luminary order in B5; Jupiter 9-vs-10 in Critodemus' table; Saturn's
  missing mean period in B7; 123/124-day calendar split).
- **Combinatorial retrospection is the standing epistemic defect** —
  multiple arithmetic routes to one target interval are NOT independent
  confirmations; grade INDEPENDENCE_STATUS per route.
- **Quarantine law**: Q0 structural research … Q6 mortality hard-block …
  Q8 living-person application prohibited … Q9 effect-based rectification
  blocked. VERIFIED_STRUCTURE ≠ PERMITTED_APPLICATION. Outcome
  catalogues are archive-only; safe abstraction preserves relations.

## Pitfalls

- Reading 2MB of corpus into context verbatim will overflow — always
  budget first; skeleton extraction is the cheapest full-corpus map.
- execute_code output truncation: keep per-run output under ~50KB; when a
  skeleton run truncates, re-run with narrower file batches.
- Do not create a universal "master beginning" or master apheta — the
  corpus explicitly rejects single-algorithm readings; beginnings are
  method-typed.
- The home-lab persona pipeline (Situated Mode Compiler, Lots layer,
  neutralization/contrast) is the operational consumer of this corpus —
  distillations should include a home-lab relevance section.

## Support Files

- `scripts/heading_skeleton.py` — heading-skeleton extractor for corpus
  structure mapping.
- `references/books5-7-technical-distillation.md` — condensed technical
  knowledge bank for Books 5–7 (the parent-task deliverable format).
