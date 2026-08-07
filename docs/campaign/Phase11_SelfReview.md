# Phase 11 Self-Review — findings (pre-external-verdict)

Date: 2026-08-07
Status: SELF-REVIEW FINDINGS — Pip's own critical pass over the Phase 11
build, recorded BEFORE the external judge/Locus verdicts arrive.

## Findings

1. **[FIXED] Q7 gate slip-through probes — CLEAN.** Three partial-trigger
   paths probed: reward-without-request, request-without-disclosure,
   disclosure-without-request — ALL DENY correctly (DENIED_never_auto_selected).
   No slip-through path found in select_bct.

2. **[FIXED] Stepwise PROMOTION_EDGES over-broad (real fidelity bug).**
   Initial PROMOTION_EDGES = {S3->S4, S4->S5} wrongly required a
   pre-declared selector at S3->S4 — but the FAOS config's rule is
   "Promotion (S3/S4→S5) requires a selector," and under stepwise
   enforcement the ONLY reachable promotion edge is S4->S5 (S3->S4 is
   qualification completion; S3->S5 is a prohibited skip). Corrected to
   {S4->S5}; self-test + verifier + witness updated to pin the corrected
   edge. This is exactly the class of over-enforcement the judge would
   have caught.

3. **[FIXED] Halt-state exit was unenforced (Phase 10 W5 residue).** The
   Phase 10 note said halt = "membership queries only, never 'must not
   proceed past.'" Phase 11 D4 is the enforcement upgrade, so
   StepwiseLineage.advance_item now BLOCKS any forward transition from a
   halt state (S6/S7/S8 are terminal, Book IX). Self-test + verifier pin
   S6->S7 blocked.

4. **[NOTED] HEB enum drift (rising|flat|falling vs steady).** The Phase 10
   GateContext used "steady"; HEB's canonical state_schema enum is
   rising|flat|falling. SkillLoadTrend emits the HEB canonical enum
   ("flat"). The Phase 10 GateContext accepts any string (it only checks
   != "falling"), so no runtime break — but the drift is recorded for the
   reviewers; a future unification should align GateContext's default to
   "flat" (recorded, not fixed here — touching Phase 10 code is out of
   Phase 11 scope; verifier keeps both in sync via the W2 check).

## Verification after fixes

- phase11_intervention.py self-test: PASS (incl. corrected promotion edge
  + halt-exit block)
- verify_phase11.py: PASS (exit 0; stepwise pins updated)
- witness_run_phase11.py: PASS (exit 0; intervention pipeline end-to-end)
- verify_all.py full gate: PASS (12 verifiers) — re-run pending external
  verdict round.

## Expected external input

- judge_deepseek_phase11.txt (adversarial; hunting hidden flaws)
- locus_validation_phase11.txt (7-check discipline)

Both subagents dispatched; findings will be merged sublatively with these.
