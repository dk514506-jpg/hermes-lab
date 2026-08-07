---
name: large-corpus-ingestion
description: Ingest corpora via manifest, selective reads, subagents.
---

# Large Corpus Ingestion

Ingest big document corpora (hundreds of files, multi-book PDFs, ~1M tokens
of raw text) without blowing the context window. Validated 2026-07-30 on a
115-file Valens Anthologies corpus + 212-page book (~940K tokens) distilled
into an Obsidian wiki.

## When to use

- User hands over a corpus folder ("ingest this", "review these artifacts",
  "teach yourself this material") with many files
- A large book/PDF plus extracted notes or per-chapter artifacts
- Building a knowledge base / wiki from primary sources
- Any task where reading everything into context is infeasible

## Governing principle

**Tokens are only spent when text enters the context window. Files on disk
cost nothing.** Never paste corpus content into chat; never read a whole
corpus into context. Keep everything on disk and read selectively.

## The three-tier ladder

### Tier 0 — Delivery (0 tokens)
Files stay on disk in one directory tree. Mixed formats fine (PDF, txt,
docx, md). User just drops them and gives you the path.

### Tier 1 — Extraction + manifest (~0 model tokens)
Run a script that:
1. `pdftotext -layout` every PDF (read_file cannot extract local PDFs —
   use terminal + pdftotext)
2. Reads txt/md directly; docx via python-docx
3. Emits `manifest.json`: per file {path, section/book, name, word count,
   est_tokens = words × 1.3}, plus per-directory totals
4. Also prints the artifact-type histogram (filename patterns like
   "orientation", "register", "worked_example") to spot distilled layers

The manifest IS the map of the corpus. Reading it costs a few hundred
tokens and is the single highest-value spend. Use
`scripts/build_manifest.py` — adjust the root path and run.

Also: `find . -type f | wc -l` and file-type counts via
`find . -type f | sed 's/.*\.//' | sort | uniq -c` to size the job before
reading anything.

### Tier 2 — Selective reading (controlled spend)
- Read the manifest first.
- Read the **distilled layers first**: orientation/root-technical-grammar
  files, method-family/dependency maps, cross-reference indexes — these are
  the highest signal-to-token ratio.
- Then worked examples, then registers/indexes, then quarantine appendices.
- Paginate: `read_file` with offset/limit = ~2-4K tokens per read.
- For a large book: read TOC/front matter first (~2K tokens) to learn
  structure, then `search_files` for specific sections on demand. NEVER
  read a 200+ page book end-to-end in one context (~100K tokens — window
  blowout + attention degradation).

### Tier 3 — Parallel subagent distillation (context isolation)
When the corpus has clear partitions (book folders, topic directories),
dispatch `delegate_task` with up to 3 parallel subagents, one per partition:

- Goal: "Read every file in folder X (pagination for large ones), return a
  structured distillation"
- Context must include: exact paths, which files are highest-signal, and
  the EXACT output format (per-section: core technical grammar, key methods,
  worked-example patterns; then cross-section relations, emergent
  principles)
- Target 600-900 words per subagent — detailed reads happen in their
  contexts, only distillations enter yours
- Watch progress via the live_transcripts paths; don't poll
- **Retrieve deliverables from the summary files, not the transcripts.**
  Full subagent outputs land in
  `~/.hermes/cache/delegation/subagent-summary-<n>-<timestamp>.txt`; the
  live transcripts truncate long messages with `(+N chars)` markers and are
  progress logs, not the deliverable. Copy the summary files into the
  campaign's notes dir before assembling.

Subagents reading ~30-40 files each takes ~2.5 min. Your context only pays
for the three distillations (~2-3K tokens total).

## Multi-phase research campaigns (beyond ingestion)

The Tier-3 council pattern scales past corpus ingestion into full research
programs: literature review → synthesis → skill build → integration, with a
critique round and revision round between phases. Validated 2026-08-06 on the
Motivational Ecology campaign (Phases 1-4, ~140 files, 4 council dispatches).

- **Each phase = one council dispatch** (3 parallel subagents, fixed deliverable
  format in context), then the parent assembles artifacts from the summary
  files. Phase outputs are governed documents, not chat replies.
- **Evidence discipline travels with every subagent brief:** VERIFIED = fetched
  the source, RECONSTRUCTED = agent-applicability inference (labeled), UNVERIFIED
  = search-only; retracted/withdrawn works are register-only, never cited.
  Declare window conventions explicitly ("post-2024 = 2025+").
- **Critique round (user-requested pattern):** after build phases, dispatch 3
  critics (epistemology/evidence, architecture/design, ecology/governance),
  each returning: kernel (what's strong) / limitations (file:section) / missing /
  concrete numbered revisions / one-sentence verdict. Then do a revision round
  and re-verify. The user calls this "sublate the worse, reinvigorate the best."
- **Durable verification is the release gate.** Inline heredoc checks get
  re-flagged as "unverified" because there is no named entry point to re-run.
  Write `verify_<phase>.py` test files (assertions on the changed paths) plus a
  single `verify_all.py` runner that compiles + parses + executes every
  verifier in one process, one exit code. Run once; exit 0 is the proof.
- **Delayed delegation deliveries are duplicates.** Consolidated results
  re-enter as messages long after the work is consumed. Byte-compare the
  delivery against the summary files already copied into council_notes/
  (`wc -c` both) before re-integrating — they will match; note it and move on.
- **Register the campaign in its own ecology:** handoff_notes.md per phase,
  journal entry in the wiki vault, Open Questions Register QIDs, Project Atlas
  entry, and self-application tracking (what the user does unassisted per
  phase — councils that do all the reading risk deskilling the user they serve).

Full recipe (phase output shapes, dispatch briefs, critique format, API quirks):
`references/multi-phase-research-campaign.md`.

## After distillation — build the wiki

- Create the wiki vault structure FIRST (summaries/, concepts/, syntheses/,
  entities/, journal/, index.md, log.md) while subagents work — use the
  book TOC to write skeleton summary pages (structure + section list,
  `confidence: low`, status PENDING) before distillations arrive.
- Write concept pages from cross-referenced workbook/source knowledge you
  already have in context — don't wait for subagents for concepts you can
  ground immediately.
- Populate summaries and syntheses from the distillations when they land.
- **Verify wiki link integrity before declaring done** — a 10-line check
  that every `[[wiki-link]]` resolves to a real page (regex for `\[\[`,
  map to page stems, report orphans). This session's 21-page wiki had 2
  broken links that this check caught immediately (one concept page merged
  into another but the old links remained). Full-link resolution + no
  orphans is the "wiki is done" gate.
- Obsidian vault = a plain directory of markdown files; install the desktop
  app via AppImage: copy to `~/Applications/`, `chmod +x`, write a
  `~/.local/share/applications/*.desktop` entry (Exec must include
  `--no-sandbox`). No system surgery needed.

## Cost reality check

| Approach | Token cost |
|---|---|
| Pasting corpus into chat | 300-800K (infeasible) |
| Reading book end-to-end in context | ~100K (window blowout) |
| Manifest + selective reads | ~15-30K total |
| Manifest + full distillation to wiki | ~50-80K once, then 2-5K per future query |

The wiki is the durable store. Re-reading raw sources every session is the
anti-pattern this ladder exists to prevent. Distill once, query cheap
forever.

## Pitfalls

- **Inline verification gets re-flagged.** Running heredoc `python3 - <<EOF`
  checks "works" but the system re-asks for verification because there's no
  named test entry point to re-run. Consolidate assertions into a persistent
  `verify_<phase>.py` (one file per phase/revision round) and a `verify_all.py`
  single-entry runner; run that once and report its exit code.
- **Council deliverables live in summary files, not transcripts.** Subagent
  outputs land in `~/.hermes/cache/delegation/subagent-summary-*.txt`;
  live transcripts truncate long messages with `(+N chars)` markers. Always
  copy the summary files into the campaign notes dir before assembling.
- **Late delegation deliveries are usually duplicates.** When a consolidated
  batch message arrives after you've already consumed the work, byte-compare
  (`wc -c`) against the summary files on disk before re-integrating.
- **pdftotext may not be installed** — check `which pdftotext`; if missing,
  install poppler-utils. Not a blocker, just a prerequisite.
- **Large PDFs extracted to text can be ~185K words** — never feed the
  whole thing to context; it's for search_files and section reads only.
- **Duplicate artifacts across partitions** (same content in multiple book
  folders) — the manifest + filename patterns expose this; flag it, don't
  re-distill.
- **OCR-quality sources**: if artifacts carry evidence/verification status
  vocabulary (Stabilized, Structured OCR, Numeric candidate, Quarantined),
  preserve those statuses in the wiki pages — don't flatten them to
  "confidence: high" just because the text is readable.
- **Don't create pages for passing mentions** — follow wiki page thresholds
  (concept appears in 2+ sources or is central to one).
- **Merging concept pages breaks links** — when two concepts share one page
  (e.g. relation-state + condition-state), every old `[[condition-state]]`
  link breaks. Either create a stub redirect page or sweep all pages for
  stale links after the merge. The link-integrity check catches this.

## Related

- Bundled `llm-wiki` skill — the maintenance pattern for the wiki itself
  (orientation, lint, update policy). This skill covers the ingestion side
  that llm-wiki's bulk-ingest section only gestures at.
- `obsidian` skill — vault file operations once the wiki exists.
- Support: `scripts/build_manifest.py` — corpus manifest generator.
