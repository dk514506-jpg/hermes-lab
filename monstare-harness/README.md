# Monstare Agentic Harness

The agentic orchestration for **Monstare** — a Tier-P cosmotechnic research instrument
whose purpose is productivity-supporting cosmotechnic cultivation (NOT output maximization).
This directory is the published copy of the harness; the live workspace is `/opt/data`
(canonical matrix, batch artifacts, source caches). The evidence matrix is the single
database; this harness is the discipline that charts it.

**Working law (non-negotiable):**
1. ONE canonical evidence matrix, patched additively in place every pass, with a Source Patch Log entry.
2. NEVER create a new knowledge base / derived workbook after a pass. Findings memos are pass artifacts.
3. Nail/verify source links (liveness + note-takability) BEFORE reading/charting. Citation is not evidence.
4. Save progress to disk with explicit file names; memos + matrix carry continuity (no handoff packages per pass).

## Roles (leaf subagents spawned by Pip via `delegate_task`, max 3 concurrent)

| Role | Mandate | Budget |
|---|---|---|
| Locus | Frame-keeper / QC steward — batch-level interface + discipline check, last | 8k |
| Evidence Librarian | Source identity + access-path gate BEFORE claims are extracted | 12k |
| Methodologist | Causal status, evidence type, effect-size proportionality, SCED/pilot logic | 10k |
| Cosmotechnic-Purist | Anti-veneer guard: no false cosmotechnics, no scalar drift, citation hygiene on Hui | 10k |
| Phenomenologist | Lived-experience fidelity, capture-order (phenomenology-before-calibration) | 8k |
| Ethics & Cosmotechnic Auditor | Protected floors S1 Telic / S7 Moral / S10 Reversibility; cross-stake collisions | 8k |
| Data & Instrumentation Steward | Additive-patch gate: every proposed edit classified before the matrix is written | 4k |

Full prompts: `role_prompts/` (refined through 3 charting batches, 2026-08-13).

## Orchestration pattern (proven, 3 batches / 26 rows)

1. **Source pass**: audit every row's URLs (curl + browser-stack retry; pypdf+pymupdf text-layer
   verification; OCR-only vs scanned vs landing-only vs dead classification). Hunt verified
   replacements BEFORE charting. Keep a bad-links list.
2. **Pip reading + drafts**: extract targeted passages (abstracts/intro/conclusion windows) to
   files; chart all rows into a drafts file.
3. **Wave 1** (3 parallel): Evidence Librarian + Methodologist (+ Phenomenologist where Area 5/8/9
   or an archetypal phenomenological row is present).
4. **Reconcile**: apply corrections into a final charting JSON. VERIFY subagent claims against
   files yourself — self-reports are not facts.
5. **Wave 2**: Cosmotechnic-Purist (any Cosmo Rel. = high or cosmotechnic claim), Ethics Auditor
   (Fail Modes / protected-floor stakes), Data Steward (always, before the write). Locus last.
6. **Patch** the canonical matrix additively (openpyxl WITHOUT `data_only` — formulas preserved;
   Excel recalculates on open; LibreOffice unavailable). Read back; append one truthful patch-log
   entry (distinguish pure fills from instructed seeded-cell upgrades; 0 rows removed).
7. **Memo**: findings / fault-lines / pilot rules / weight changes / next-session agenda / actual
   spend. Save role-prompt refinements back.

Collapse economy (v3 §5.2): ≤4-row single-area conceptual batch → Pip + Locus only; 5–8 rows →
Pip + Locus + Librarian + Methodologist; full 7-role only when the batch justifies it. Burden is a stake.

## Key disciplines

- Citation is not evidence. Tier-P stays visible (plausible, not proven). H2 is a vector, never a scalar.
- Causal status matches what the source IS: narrative reviews → correlational; methods papers →
  conceptual (methods); only executed designs license causal claims (scoped: proximal-only MRT,
  confirming-phase-only MOST, per-case-with-baseline SCED).
- No external effect-size imports. `not_quantifiable` is the honest default for reviews/theory/philosophy.
- The tool never possesses a reinforcement layer (cybernetics guard: the person is not the plant);
  consequences are mirror, not leash. Flow conditions are structural 0/1, never calibrated scalars.
- Protected floors S1/S7/S10 are never traded; a breach is escalated, not patched over.

## Skills (in this repo, also live under /opt/data/skills/)

- `skills/evidence-matrix-orchestration/` — orchestration pattern, source-verification two-pass
  audit, replacement workflow, additive patching, pitfalls, harness state.
- `skills/evidence-matrix-charting-qc/` — Methodologist role: report format, per-row checklist,
  verification techniques, worked batch-1 case.
- Companion (general, not Monstare-specific): `external-source-verification` skill in the Hermes
  skill library (mass source-corpus audit, second-pass disambiguation, replacement hunting).

## Scripts (`scripts/`)

- `monstare_link_audit.py` — mass URL audit (status, content-type, PDF text-layer probe, classification).
- `monstare_consolidate.py` — workbook consolidation utilities.
- `monstare_patch_matrix.py` / `monstare_patch_charting.py` / `monstare_patch_charting_b3.py` —
  additive in-place patchers (formula-preserving, patch-log append, readback). b3 is the current template.
- `monstare_extract_reading.py` — targeted passage extraction (abstract/intro/conclusion windows).
- `monstare_batch2_rows.py` — rows-dump template (matrix → JSON for subagents).
- `sync_monstare_harness.sh` — one-way sync of the harness from the live workspace into this
  repo (role prompts + curated scripts + the two skills), commits, optionally `--push`.
  Run from anywhere: `monstare-harness/scripts/sync_monstare_harness.sh [--push]`.

Run scripts with `uv run --with openpyxl python3 <script>.py` (or pypdf/pymupdf as needed).
Never use inline `python3 -c` / heredocs for multi-line extraction — the terminal guard rejects them;
write a script file.

## Canonical workspace map (live, under /opt/data)

- Matrix: `Monstare_Evidence_Matrix_Source_Links_v3_Staleness_Patched_artifact.xlsx`
- Role prompts (canonical, refined): `Monstare_role_prompts/`
- Role reports: `Monstare_role_reports/` (B1_*/B2_*/B3_* per batch)
- Batch artifacts: `Monstare_batch_{1,2,3}_charting_drafts.md`, `..._charting_final.json`,
  `..._rows.json`, `..._findings_faultlines_memo.md`
- Source extracts: `Monstare_batch{1,2,3}_sources/`, `Monstare_source_audit_cache/`, `cache/web/`
- Audit artifacts: `Monstare_source_link_audit_2026-08-13.csv/.md`, `Monstare_bad_source_links_2026-08-13.md`

State as of 2026-08-13: 3 batches complete, 26 rows charted (CORE block 26/26), full role QC every pass.
Next: batch 4 — A1 philosophy-of-technology spine (institutional-access pass first) or A5/A8 rows.
