# Edit-in-Place Discipline & Compilation Protocol

## Silvey's correction (batch 4, 2026-08-14)

After batch 4, the user explicitly corrected: "you have been creating new charts every time instead of editing the evidence matrix like I asked." This is a first-class workflow rule that belongs in every evidence-matrix charting skill.

## The rule

**The matrix xlsx is the operational database — patch it additively each pass.**

- Do NOT create new `.md` files for every batch's charting drafts when the matrix already holds the charted data
- Findings memos are pass artifacts for continuity, not replacements for the matrix
- If a pass produces new insights, patch the matrix cells — don't spawn a new document

## The pitfall

Spawning `batch_N_charting_drafts.md`, `batch_N_rows_dump.json`, `batch_N_synthesis_memo.md` for every batch creates a scattered archive that explodes the project. The user had to explicitly ask for compilation into singular canonical documents after batch 5.

## Compilation protocol

Periodically (every 3-5 batches), merge scattered batch files into singular canonical documents:

| Canonical document | Absorbs |
|---|---|
| Master Findings Memo | All `batch_N_findings_faultlines_memo.md` |
| Master Synthesis Memo | All `batch_N_synthesis_memo.md` + cross-batch audits |
| Master Handoff Prompt | All `batch_N_handoff_prompt.txt` + context window package |
| Epithet Register | Grows with each batch, stays singular |

**Merge strategy**: Front matter (scope, token spend, source quality), body (one section per batch with fault lines + weight reclassifications + binding implications), back matter (cumulative binding rules, verification debts). Strip apparatus-burden and next-session agendas (obsolete after merge).

**Delete after merge**: Batch-specific charting drafts, row dumps, update files, retry files. Retain source files, role prompts, evidence matrix, and the canonical documents.

## Git init discipline

ALWAYS initialize git at project start:
```bash
cd /opt/data && git init
```

Do not assume `.git` exists. Create `.gitignore` BEFORE first `git add` to avoid committing secrets. Verify each ignore pattern with `git check-ignore -v <pattern>` before relying on it.

## Token envelope discipline

The user reframed the 100k token envelope: it is a **landmark that disciplines cognition, not a fence that terminates work**. It means:

- Don't waste tokens — batch parallel calls, read efficiently, collapse roles when v3 §5.2 says so
- But don't stop artificially — if a source needs reading to be charted, read it; if QC catches a fault line, fix it
- If the envelope runs past 100k, keep going and record honestly rather than delivering an uncharted row as a token-saving measure

Batch 3 overran to 105-125k and the user authorized it — that's the precedent. The envelope is a regulator of pace and efficiency, not a substitute for rigor.
