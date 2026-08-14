---
name: evidence-matrix-orchestration
description: "Use when charting an evidence matrix or auditing links."
version: 1.0.0
author: Nous Research
license: Proprietary. LICENSE.txt has complete terms
platforms: [linux]
metadata:
  hermes:
    tags: [orchestration, evidence-matrix, delegate_task, subagents, monstare, research]
    category: autonomous-ai-agents
    related_skills: [in-session-capability-verification, xlsx, grounded-citations]
---

# Evidence-Matrix Orchestration (Monstare harness)

Disciplined, role-QC'd charting of an evidence matrix using `delegate_task` subagents, with
source verification BEFORE reading and additive in-place patching. Proven on the Monstare
project (3 batches, 26 rows charted, 2026-08-13). The Monstare handoff spec (v3 §5) is the
design; this skill is the operational knowledge from executing it.

## When to Use
- Running a charting batch on the Monstare evidence matrix (canonical xlsx, see references/monstare-harness-state.md).
- Auditing all matrix source links (liveness + note-takability) and keeping a bad-links list.
- Hunting replacements for dead/bot-hostile source links and patching them into the matrix.
- Any "orchestrator + role subagents QC a spreadsheet of evidence" task.

## User's working law (Silvey, non-negotiable)
1. **ONE canonical evidence matrix**, patched additively in place every pass, with a Source Patch Log entry.
2. **NEVER create a new knowledge base / derived workbook / rebuilt table after a pass.** Findings memos are pass artifacts; the matrix is the single database.
3. **Nail/verify source links BEFORE reading/charting.** Citation is not evidence; a link must be live AND note-takable before its row is charted.
4. Save progress to disk under /opt/data with explicit file names.

## Orchestration pattern (proven, 2 batches)
Pip = the main session (orchestrator). Roles are leaf subagents spawned via `delegate_task`
(max 3 concurrent — run in waves). Subagents read files locally, so spawn prompts stay small:
pass file paths, not content. Each role prompt carries: mandate, rows/claims, files to read,
EXACT return fields, token budget. Each subagent saves its report to
`/opt/data/Monstare_role_reports/<Role>_report.md` AND returns it in the final message.

1. Read handoff + matrix rows (dump rows to JSON for the subagents).
2. **Source pass**: verify every row's URLs (two-pass audit, below); hunt replacements BEFORE charting.
3. **Pip reading**: extract targeted passages (abstracts/intro/conclusion windows) to files; print compact heads. Chart all rows into a drafts file.
4. **Wave 1 (source-facing, 3 parallel)**: Evidence Librarian + Methodologist + Phenomenologist (spawn when the batch has Area 5/8/9 rows OR an archetypal phenomenological row in any area — batch 3: CORE-16 Csikszentmihalyi Flow required the role even though the row is Area "core"). All other roles on standby.
5. **Reconcile**: apply Methodologist/Purist corrections into a final charting JSON. VERIFY subagent claims against files yourself — self-reports are not facts.
6. **Wave 2**: Cosmotechnic-Purist (spawn if any row Cosmo Rel. = high), Ethics & Cosmotechnic Auditor (spawn if Fail Modes/protected-floor stakes present), Data & Instrumentation Steward (always, audits the proposed edit list). Locus runs batch-level check last (or in the same wave).
7. **Patch** the matrix additively (see patching section), read back cells, append patch-log entry.
8. **Memo**: findings/fault-lines + next-batch agenda + token spend. No separate handoff package per pass.

Role spawn rules (v3 §5.2): ≤4-row single-area batch → collapse to Pip + Locus. 5–8 rows →
Pip + Locus + Librarian + Methodologist, add roles per concern. Budget caps: Locus 8k, Librarian
12k, Methodologist 10k, Purist 10k, Phenomenologist 8k, Ethics 8k, Data Steward 4k tokens.

## Source verification: two-pass audit
**Pass 1 — curl audit** (scriptable, see /opt/data/scripts/monstare_link_audit.py):
status code, content-type, `%PDF` magic sniff, redirect target, size. For PDFs probe the text
layer with BOTH pypdf AND pymupdf: first 4 pages AND a middle-page window (front matter is often
scanned while the body has text). HTML: strip tags, count text chars, grep paywall/login markers.
Classify: READY / OCR-only / landing-only / scanned / stub / dead / blocked.

**Pass 2 — browser-stack retries** for curl-blocked URLs (403/429): firecrawl `web_extract`
renders JS and OCRs scanned PDFs. Key insight: **bot-blocked ≠ unreadable** — philpapers PDFs,
PMC full-text pages (JS shell to curl), academia.edu, ResearchGate, DOAJ pages all read fine via
browser-stack. True scans (no text layer anywhere) still read via firecrawl OCR.

Known access classes and their handling:
- Open PDF with text layer → best; cache locally.
- OCR-only (broken ToUnicode or scanned) → readable via firecrawl; record "read via OCR" caveat.
- Archive.org lending items → NO direct download (401); legal path only, or find companion source.
- In-copyright books with no open full text → author-homepage preface/adapted chapters are acceptable PARTIAL coverage, labeled with what they cover (e.g. A1-08 Feenberg *Questioning Technology*: preface + "Crossroads" chapter = Part III only); full hunt recipe: `external-source-verification` references/open-fulltext-hunting.md.
- Course-mirror PDFs → verify text, add "course-hosted copy" caveat.
- Landing-only (paywalled) → chart at abstract level, record the limitation.
- Bot-hostile (ACM DL, ResearchGate, academia) → needs manual/institutional retrieval.

## Replacement workflow
Before writing ANY replacement URL to the matrix: HTTP 200 + text layer verified (or browser-stack
read confirmed). Record in Discovery Notes: "REPLACEMENT <date>: <old> dead (<reason>); new link
verified". Legal paths preferred (archive.org lending, ERIC, monoskop, publisher landing, author
site); flag rights caveats (e.g., scanned archive copies, mirror copies).

## Additive matrix patching (openpyxl)
- Load workbook WITHOUT `data_only` (preserves formulas). Save in place; never rebuild.
- Only fill blank cells, append notes, update statuses, improve links. Seeded-cell upgrades
  (Key Finding/Design Implication/Causal Status) are sanctioned by the charting plan but must be
  logged truthfully: distinguish "additive fills" from "instructed seeded-cell upgrades" and
  "Verif. flips" in the Source Patch Log entry (repair-not-removal convention).
- After save: read back cell VALUES with `data_only=True`; count Dashboard formulas by loading
  WITHOUT `data_only` (a data_only load returns cached values and reports 0 formulas — a false
  negative that masks formula loss; batch-3 Data Steward caught this in the patch script).
  Confirm the patch-log row appended.
- BEFORE patching, verify whether target cells are blank vs seeded: a batch whose charting cells
  all hold seed text is 100% "instructed seeded-cell upgrades" (0 pure fills), and the patch-log
  entry must state that truthfully (batch-3: Data Steward verified 0 of 90 cells blank pre-patch).
- No LibreOffice in this container → formula cached values are lost on openpyxl save; disclose
  that Excel recalculates on open (formulas are preserved as strings).

## Pitfalls
- **Terminal guard trips on inline `python3 -c "..."` / heredocs** (esp. multi-line with
  pymupdf): error "embedded null character in path". ALWAYS write a script file and run it.
- pymupdf can return EMPTY text on some PDFs where pypdf extracts fine (font-encoding quirks) —
  verify with both extractors before declaring a PDF scanned.
- A PDF can have a "text layer" that is garbage (broken ToUnicode → control characters). Firecrawl
  OCR reads these cleanly; never trust a garble-free char count as readable text.
- pypdf "Ignoring wrong pointing object" warnings = malformed xref; try pymupdf before flagging.
- Wayback `id_` URLs return 302 (not the file) when no snapshot exists; archive.org direct
  download of lending items returns 401.
- Semantic Scholar API rate-limits (429) — retry with backoff.
- Subagents misread files: batch-1 Data Steward reported JSON key `cimpl` was null on all rows;
  direct check showed it populated. Always verify subagent data claims against the file before
  acting on them.
- PMC/Frontiers pages: curl sees a JS shell (~140 chars); browser-stack gets full text.
- A live, readable URL can be the WRONG article: stub/bot-challenged verdicts mean the content was never read — content-verify identity (eutils/CrossRef title match, see `external-source-verification` §6.5) before charting (batch 3: CORE-19's seeded PMC URL was a different study AND the landing DOI a third article; both replaced).
- PMC direct "Download PDF" endpoints can be challenge-walled for curl (return a 1-page stub, e.g. nihms PDF links); the firecrawl full-text cache of the article page is the reliable reading base (CORE-13).
- Audit CSV verdicts are keyed to the URLs that were audited, not the matrix's current URLs — match by URL equality before acting (CORE-20: "BAD_DEAD" belonged to a superseded URL; current URL live).
- Abstract-level causal-status convention: primary empirical source charted at catalog level → "causal (lab-bounded, animal; catalog-attributed — unverified against text, Tier-P)"; methods papers → "conceptual (methods)" with scoped design-licenses notes. See references/monstare-batch3-pass.md.

## Verification after each pass
- Read back the patched cells (KFT/CS/Verif.) from the xlsx.
- Confirm Source Patch Log entry appended with truthful wording.
- Confirm sheet count and Dashboard formula count unchanged.

## Synthesis memos as deliverables

After charting a spine (area or sub-batch), produce a **synthesis memo** that traces the cross-row tissue — the living organism of ideas in relation, not just a list of theses. Anatomy: organs (which authors serve which function), interconnecting nexuses (fault lines that are also connections), cross-cutting themes (through-lines that run across the whole spine), remaining specializations needed. The synthesis is where recallability becomes explicit: "when this author is needed, what whole body of thought does it call up?"

## Epithet register (living document)

The Epithet Register (`/opt/data/Monstare_epithet_register.md`) preserves each author's voice — not just their claims, but their tonal signature and the felt sense of what they are pointing at. Downstream artifacts (Design Veto Catalogue, Cosmotechnic Audit Card, pilot rules) draw from this register so rules grounded in an author *sound* like that author.

Per author: **Epithet** (1-3 word signature), **Quotations** (range from subtle to robust — tonal register is exemplified, never described), **Reverie** (evocative vignette, 100-200 words, conveying the full spectrum of feelings and thoughts on the concept).

Grow the register with each batch. The epithet is the seed; the quotations are the body; the reverie is the felt sense.

## Batch 4-5 lessons (2026-08-14)

- Image-only sources (A1-14 Mitcham, A1-16 Mumford) were charted supplemented by secondary synthesis (Philpapers abstract, independent summaries, publisher pages). Flag as "image-only" or "abstract-level" in Discovery Notes and record verification debt.
  ⚠️ CORRECTION (2026-08-14, gap-closing pass): this section originally listed A1-07 Stiegler and A1-11 Winner as image-only TOO, but that was WRONG — both have genuine text layers (re-probe, below). Only A1-14 + A1-16 are truly scanned (0 chars). Do NOT trust a "image-only" flag as a permanent truth; re-probe cached PDFs before asking the user to hunt full-text copies.
- 18-row batches are the max case — split into sub-batches (4a/4b) to stay within token envelope per sub-batch.
- 52-row sessions produce ~400-480k spend — far over envelope. Record honestly and justify by scope.
- The Phenomenologist role is essential for Area 5/8/9 rows — capture-order checks and phenomenological fidelity are real, propagating corrections.
- Same-author consistency checks (A1-02/A1-01/HUI-2024; A1-10/A1-19 Verbeek; A1-05/A1-06 Simondon) are a canonical QC move.

## Batch 8 lesson (2026-08-14) — final charting batch (Areas 9 & 10)
- Epithet register classifier bug: `assemble_register.py` used naive substring matching (`"pending" in body`), so the word "de**pending**" false-flagged full-text entries as "deferred" in the tracking table. Fix: match on word boundaries (`\bword\b`). Audit any status-classifier for substring false positives before trusting tracking-table status.
- Archive.org lending rows (Deep Work, GTD, Shweder, Nisbett) chart at ABSTRACT-LEVEL from publisher landing pages (Hachette, HUP, official site); Open Library may be bot-blocked (human-verification wall) — use the archive.org landing as canonical readable.
- Batch 8 = final charting pass; matrix COMPLETE at 128/129 (only CORE-07 Lepper remains "Located (not charted)").

## Gap-closing pass lesson (2026-08-14) — close the last not-charted row + clear verification debt
- **PROBE-BEFORE-HUNT (image-only flag is not truth):** before asking the user to source a full-text copy of any row flagged "image-only"/"abstract-level," re-probe the locally-cached PDFs with pymupdf for a genuine text layer. This pass found A1-07 (monoskop Stiegler, 745K chars) and A1-11 (ratical Winner, 479K chars) are actually readable full text and upgraded both from image-only → TEXT-VERIFIED, clearing real verification debt. Only A1-14 Mitcham (204p) and A1-16 Mumford (530p) are truly scanned (0 chars). Probe = total chars across pages + sample a mid-body page (p10-15+), not just front matter; an "image-only" verdict can be a stale or front-matter-only reading. Add a `scripts/probe_pdf_textlayer.py` helper call before hunting copies.
- **Last not-charted row close-out (CORE-07):** the final "Located (not charted)" row was charted from the ERIC ED084210 final-report full text (32p, text-layer verified) — filling ES/Limitations/Disconfirming cells + flipping Verif. + appending patch-log row. This closed the matrix to **129/129**. When one row blocks "complete," a full-text-verified chart of it is the highest-value single action.
- **openpyxl not in system python in this container** — use `uv run --with openpyxl python <script>.py` (and `--with pymupdf` / `--with pypdf`) rather than assuming a venv; uv wheels are already cached.

## Support files
- `scripts/probe_pdf_textlayer.py` — probe cached PDFs for a genuine text layer before trusting an "image-only" flag or hunting a full-text copy (run: `uv run --with pymupdf python <path>`).
- `references/monstare-harness-state.md` — file map, harness state, batch outcomes, adjudications.
- `references/monstare-batch3-pass.md` — batch-3 session detail: wrong-article catches, abstract-level decisions, causal-status/evidence-type adjudications, CORE-16 Phenomenologist re-chart (felt-invariants checklist), pilot flags.
- `references/monstare-batch4-5-summary.md` — batches 4-5 summary: 70 rows charted, source quality distribution, key cross-area findings.
- `references/monstare-github-workflow-pitfalls.md` — GitHub auth, credential storage, token redaction, .gitignore gotchas.
