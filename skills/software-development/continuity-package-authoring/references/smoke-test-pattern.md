# Smoke Test Pattern for Continuity Packages

A smoke test is a 1-row (or smallest-possible) execution with the collapsed configuration that confirms the harness produces usable structured output before the next window commits to a full batch.

## Why it matters

A continuity package that sends the next window straight into a full 8-12 row batch with a newly built harness is risky. If the harness is broken — role prompts return off-topic output, the return-field contracts are wrong, the spawn mechanism doesn't work as expected — the next window burns budget on a broken pipeline and produces low-quality charted rows. A 1-row smoke test is cheap insurance.

## Row selection criteria

The smoke test row should be:

1. **From the same batch as the full execution.** If the full batch is the motivational/cosmotechnic spine, the smoke test row should be from that spine (e.g. CORE-01).
2. **Load-bearing enough to be representative.** A Priority C row is too easy — it won't exercise the real charting path. A Priority A row is right.
3. **Has a readable source (not restricted/gated).** You want to exercise the real charting path, not an access-gate bypass.
4. **Small enough to be cheap.** A 30-page PDF is fine; a multi-hundred-page monograph is not.
5. **Not the most complex row in the batch.** If the batch has a row that is known to be difficult (ambiguous label, multi-part source, heavy caveats), don't use it for the smoke test. Use a clean representative row.

## Configuration

Run the smoke test with the **collapsed configuration** — Pip + Locus only. Do not spawn the full harness for the smoke test. The point is to confirm the charting pipeline works, not to exercise all seven roles.

If the full batch qualifies for a collapsed configuration under the package's decision table, use that same collapsed configuration for the smoke test.

If the full batch requires the full harness, the smoke test still uses the collapsed configuration — you're testing whether Pip can read and chart a row and whether Locus can check it, not whether all seven roles spawn correctly. The full harness is tested in the first real batch.

## Pass/fail criteria

**Pass** — all of:
- Pip produced a charting draft for the row with all four evidential columns filled (Key Finding/Thesis, Effect Size/Strength, Limitations, Disconfirming Implication).
- Locus returned a structured report that engages with the charting (not a default "all clear" with no substance).
- The matrix update is an additive patch (no rows deleted, no URLs removed, no formulas removed).
- The total smoke-test spend is within 10% of the estimated cost for one row.

**Fail** — any of:
- Pip's charting draft is missing evidential columns or is seeded text paraphrased rather than source-extracted.
- Locus's report is off-topic, truncated, or a hollow "all clear."
- The matrix update violates the patch law.
- The smoke-test spend exceeds the estimate by more than 10% (budget discipline problem).
- The source access path doesn't work as expected (404, gated when the package said open, etc.).

## When smoke test fails

- Diagnose before retrying. Is it the role prompt, the source access, the return contract, or the budget?
- Fix the specific problem. Do not retry the same smoke test without a change.
- If the smoke test fails twice, escalate to the user rather than proceeding to the full batch.

## What to record

In the handoff note, record:
- Smoke test row ID and citation.
- Configuration used (collapsed Pip + Locus).
- Pass or fail.
- If pass: a one-line note that the harness produces usable structured output and the full batch is cleared to proceed.
- If fail: the diagnosis and what was fixed.
- Smoke test spend.
