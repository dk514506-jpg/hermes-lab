# Compilation & Merge Discipline (Monstare Batch 5+)

After charting 70 rows across batches 4-5, the user flagged that the agent had been creating new charting draft files for each batch instead of editing the evidence matrix directly. This produced ~30 scattered files when the project should have had ~7 canonical documents. The user explicitly corrected this: "you have been creating new charts every time instead of editing the evidence matrix like I asked."

## The Problem

The agent's pattern was:
1. Read sources
2. Write charting drafts to a new file (`Monstare_batch4a_charting_drafts.md`, `Monstare_batch5a_charting_drafts.md`, etc.)
3. Patch the matrix from the drafts
4. Write findings memos
5. Write synthesis memos

This produced a proliferation of intermediate files that served no long-term purpose — the matrix was the operational database, and the memos were the continuity frames. The charting drafts were redundant with the matrix.

## The Canonical Document Set

The project should maintain exactly these canonical documents:

| # | Document | Purpose | Source material |
|---|---|---|---|
| 1 | **Evidence Matrix** (xlsx) | Operational database — the single source of truth | No change needed |
| 2 | **Master Findings Memo** (md) | All fault lines, weight reclassifications, pilot implications across all batches | Batch 1/2/3/4a/4b/5 findings memos |
| 3 | **Master Synthesis Memo** (md) | Cross-batch tissue, through-lines, incommensurabilities, unresolved tensions | 4ab synthesis, 5 synthesis, premature coherence audit |
| 4 | **Master Handoff Prompt** (md) | Single continuity frame for future sessions | Batch 3 handoff, batch 4 handoff, context window package |
| 5 | **Epithet Register** (md) | Voice preservation — grows with each batch | Current register + new entries |
| 6 | **Premature Coherence Protocol** (md) | Corrective measures — living document | Current protocol |
| 7 | **Source Audit** (csv + md) | Per-URL status — living document | Current audit files |

Plus: role prompts (7 files, refined per batch) and the Premature Coherence Protocol.

## Merge Strategy

### Master Findings Memo
- Front matter: scope, token spend summary, source quality distribution
- Body: One section per batch (## Batch 1, ## Batch 2, etc.), each containing ONLY: what became stronger, fault lines, weight reclassifications, binding pilot implications
- Strip out: apparatus burden (redundant), next-session agenda (obsolete), token spend details (move to front matter), open items (resolve or drop)
- Back matter: cumulative binding pilot implications (deduplicated), cumulative verification debts

### Master Synthesis Memo
- Front matter: scope, stable figure summary
- Body: Cross-cutting nexuses (one per major tension), through-lines (pharmacological, genesis, politics-ethics), incommensurability table, unresolved tensions table
- Strip out: per-row design implications (belong in matrix), per-batch token spend (obsolete)
- Back matter: next specialization agenda

### Master Handoff Prompt
- Front matter: project purpose, current state, file directory map
- Body: Step 0 (read order), Step 1 (harness verification), Step 2 (budget), Step 3 (scope)
- Strip out: obsolete batch-specific details, completed tasks
- This replaces the batch-specific handoff prompts

## What Gets Deleted After Merge

- `Monstare_batch_1/2/3/4a/4b/5_findings_faultlines_memo.md` → absorbed into Master Findings Memo
- `Monstare_batch4a/4b_charting_drafts.md` → absorbed into matrix (already patched)
- `Monstare_batch5a/5b/5c/5d/5e_charting_drafts.md` → absorbed into matrix (already patched)
- `Monstare_batch4ab_synthesis_memo.md` → absorbed into Master Synthesis Memo
- `Monstare_batch5_synthesis_memo.md` → absorbed into Master Synthesis Memo
- `Monstare_Handoff_Prompt_Batch3.txt` → absorbed into Master Handoff Prompt
- `Monstare_Handoff_Prompt_Batch4.txt` → absorbed into Master Handoff Prompt
- `Monstare_batch4_rows_dump.json`, `Monstare_batch5_rows_dump.json` → obsolete (matrix is patched)
- `Monstare_batch4b_extracted_texts.json` → obsolete
- `Monstare_batch4_source_hunt_results.md` → obsolete
- `Monstare_batch_3_*.md` (caveat notes, evtype updates, url updates, access updates, wave2 prompts, locus tags, charting drafts) → obsolete
- `Monstare_secondpass_retry.json` → obsolete
- `Monstare_bad_source_links_2026-08-13.md` → absorbed into Source Audit

## Key Lesson

**Edit the matrix directly. Do not create per-batch charting draft files.** The matrix is the operational database; memos are continuity frames. Everything else is intermediate debris that should be deleted after compilation.

The user's instruction was explicit: "treat the Evidence Matrix as the operational database" and "you have been creating new charts every time instead of editing the evidence matrix like I asked." This is a first-class workflow correction.
