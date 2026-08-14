# Cost-Control Checklist for Continuity Packages

This checklist captures the cost-control section that every continuity package for an agentic research project should include. Copy the relevant pieces into the package's cost-control section; do not paste this whole file in.

## Per-session budget envelope

- Set a session token budget before starting. Recommended default: enough for the planned batches plus the QC layers, with a 20% buffer.
- Track spend as you go. After each batch, record actual spend in the handoff note.
- At 80% of session budget: stop spawning new roles. Finish the current batch with Pip + Locus only.
- At 95% of session budget: stop entirely. Write the handoff note with partial progress.
- If the user wants to exceed the default, they must explicitly authorize it and name the new envelope.

## Per-role token budgets

Default shape (fill in actual numbers from model pricing before execution):

| Role | Default budget per batch | Increase when | Decrease when |
|---|---|---|---|
| Locus | (fill) | Batch touches a protected-floor stake or a cosmotechnic claim | Single-area batch ≤ 4 rows |
| Evidence Librarian | (fill) | Row has a restricted/gated/landing-only source | All rows are open PDFs with clear DOIs |
| Methodologist | (fill) | Row is load-bearing (Priority A) and empirical | Priority C rows |
| Cosmotechnic-Purist | (fill) | Row has Cosmo Rel. = high and a Cosmotechnic Implication | Cosmo Rel. = low rows |
| Phenomenologist | (fill) | Batch includes Area 5 / Area 8 / arousal-flow rows | Batch has no phenomenological rows |
| Ethics & Cosmotechnic Auditor | (fill) | Batch touches S1/S7/S10 or a Fail Mode | Batch is all Priority C |
| Data & Instrumentation Steward | (fill) | Any batch that writes matrix edits | N/A — cheap, always worth it |

Rules:
- Do not exceed a role's budget without a deliberate decision recorded in the handoff note.
- If the session model is a lower-tier model, increase per-role budgets slightly to compensate for extra turns.
- Do not use a more expensive model for a collapsed (Pip + Locus only) batch.

## Batch-size discipline

- Max batch size: 8-12 rows. Do not exceed.
- Estimated cost per row = (source access cost) + (Pip read + chart cost) + (role spawn costs for active roles on the batch).
- If a batch's estimated cost exceeds 15% of session budget: split into two smaller batches.
- Priority A rows: full QC layer.
- Priority B rows: Pip + Locus + Methodologist minimum.
- Priority C rows: Pip + Locus only unless a specific concern arises.

## Source-access cost control

- Do not download full PDFs for every row. For most rows, abstract + introduction + conclusion + methods/results (if empirical) is enough.
- Use targeted extraction (web_extract, targeted read), not full PDF pull, unless the row is load-bearing and the source is short (< 30 pages).
- For restricted/gated sources: do not burn budget bypassing the gate. Record the caveat and move on.
- For fast-moving AI/digital/work-trend rows (6-month re-search interval): prefer the most recent available source and record the access date. Do not chase multiple versions in one batch.

## Role-collapse economy

The full harness is the expensive case. The economy comes from collapsing roles when the batch doesn't need them.

Decision table (shape — fill in project-specific thresholds):

| Condition | Action |
|---|---|
| Batch ≤ 4 rows, one area, all readable PDFs | Collapse to Pip + Locus only |
| Batch 5-8 rows, mixed areas or mixed access types | Pip + Locus + Evidence Librarian + Methodologist; add others only if a specific concern arises |
| Batch 9-12 rows, or any batch touching a protected-floor stake | Full harness |
| Token budget below per-batch floor | Defer the batch |

Rule: do not spawn a role "just in case." Spawn a role because the condition in the decision table says to.

After each batch, if a role's output was low-signal (e.g. Cosmotechnic-Purist returned "none" for a non-cosmotechnic batch), record that and consider collapsing that role for the next similar batch.

## Hard stop conditions

Stop the session immediately if any of these occur:

1. A protected-floor breach is detected by the Ethics & Cosmotechnic Auditor and cannot be resolved by revising the matrix implication. Escalate to the user.
2. Session token budget is exhausted (95% reached).
3. Two consecutive batches produce QC failures (rows marked "re-chart required") without a clear fix. Pause and diagnose.
4. Data & Instrumentation Steward flags a proposed edit as forbidden and the user does not authorize it.

## What to record

After each batch, record in the handoff note:
- Batch size (rows charted).
- Roles spawned and their actual spend.
- Total session spend to date.
- Any role collapsed vs. the decision table.
- Any hard stop triggered (and why).
- Any QC failures (rows marked re-chart required).
