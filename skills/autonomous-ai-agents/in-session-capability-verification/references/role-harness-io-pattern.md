# Role-Harness I/O Pattern (delegate_task orchestration with file-based I/O)

Verified working 2026-08-13 on the Monstare batch-1 charting pass: a parent (Pip) session
spawned role subagents (Evidence Librarian, Methodologist, Cosmotechnic-Purist in wave 1;
Ethics Auditor, Data Steward, Locus in wave 2) that all returned usable structured reports.
The pattern keeps parent context lean and child prompts self-contained.

## Why file-based I/O

Leaf subagents know nothing of the parent conversation. Passing long drafts inline bloats the
spawn prompt and eats the child's budget. Instead, the parent writes artifacts to disk and the
spawn prompt carries only paths + the role's mandate + return contract. The child reads what it
needs, writes its report to disk, and returns the report text (or a compact pointer) as its
final message.

## The pattern

1. **Parent writes shared artifacts first** (before spawning):
   - `rows.json` — the structured input rows (IDs, citations, URLs, seeded fields).
   - `drafts.md` — the parent's working draft (the thing being QC'd).
   - `final.json` — post-reconciliation values (written AFTER the waves return).
   - Source extracts / full-text caches in a `sources/` dir the children can read.
2. **Spawn in waves of ≤3** — `delegate_task` batch mode caps concurrent children (3 for this
   user). Put 3 role tasks in ONE `tasks` array call per wave; a second wave waits for the
   first to finish. Wave 1 = content roles; wave 2 = audit/floor roles + batch-level check.
3. **Each spawn prompt carries**: (a) role mandate, (b) exact file paths to read, (c) the rows
   or claims it is responsible for, (d) the return format — numbered fields, exact — and
   (e) a stated token budget (the child self-manages; the budget line keeps it disciplined).
   Tell it to save its report to a `reports/` dir AND return the full report text.
4. **Children write reports to disk** (`/opt/data/Monstare_role_reports/<Role>_report.md`).
   The parent can then re-read any report fully without paying for it twice in context.
5. **Reconcile in the parent**: read the saved reports, apply accepted corrections to
   `final.json` (parent owns synthesis — children flag and recommend, they do not rewrite).
   Contradictory child findings are resolved by the parent with a recorded reason.
6. **Then write the canonical artifact** (matrix patch, memo) from `final.json` — one
   additive pass, never a rebuild.

## Rules that make it work

- **Children must not rewrite the drafts** — their prompts say "flag and recommend, do not
  rewrite". The parent merges. Otherwise parallel children clobber each other.
- **Give children the environment facts they need** — e.g. "this PDF is OCR-only", "this
  archive item is lending-only", "this URL 403s curl but the browser stack reads it". A child
  that re-discovers these burns budget and may reach the wrong conclusion.
- **Return contracts are numbered and exact** — the child returns ONLY the numbered fields;
  no preamble. This makes reports comparable across roles and machine-mergeable.
- **Structured reports are self-reports** — a child claiming "verified" may be wrong (e.g. a
  child's char-count "TEXT_OK" on a PDF with a broken ToUnicode map). The parent spot-checks
  load-bearing child claims (see external-source-verification for the garbled-layer trap).
- **State budgets per role in the prompt** (e.g. 12k/10k/10k for wave 1, 8k/4k/8k for wave 2)
  and an overall session envelope; record actual spend after the pass.
- **Live transcripts**: each dispatched child streams to
  `/opt/data/cache/delegation/live/<deleg_id>/task-N.log` — usable for auditing what a child
  actually did without re-running it.

## Failure handling

- If a child returns unusable output (off-topic, truncated, hallucinated): mark the row
  "QC failed — re-chart required", do NOT patch over it, log it. Re-dispatch that one role
  with a tighter prompt rather than accepting the garbage.
- If one wave's children disagree irreconcilably, spawn a tie-breaker (a fresh role with both
  reports in its prompt) or escalate to the user — never average the disagreement silently.
