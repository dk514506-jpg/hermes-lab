# Phase 10 Self-Review — findings (pre-external-verdict)

Date: 2026-08-07
Status: SELF-REVIEW FINDINGS — Pip's own critical pass over the Phase 10
build, recorded BEFORE the external judge/Locus verdicts arrive, per
campaign discipline (independent thought catches what reviewers miss).

## Findings

1. **[FIXED] ASK fidelity gap (medium-meaning unknown-direction).**
   Source (empowerment_boundary.md): ASK fires for "high branching, OR
   medium meaning with genuinely unknown direction." My first selector
   only handled high branching; medium-meaning-unknown-direction fell to
   DEFER. Fail-closed but unfaithful. Fix: `_want_ask` now fires on
   (high branching + insufficient + one-question-resolves) OR (medium
   meaning + medium branching + insufficient + one-question-resolves).
   Self-test covers both ASK cases. Verified: engine self-test PASS.

2. **[FIXED] Over-broad DEFER evidence clause.** `_want_defer` fired on
   "insufficient evidence + meaning != low" unconditionally — which
   shadowed the ASK probe (the source's "ASK never substitutes for DEFER"
   means ASK applies exactly when the choice is NOT the user's by right
   and one question resolves it). The clause was redundant: ACT requires
   sufficient evidence, so non-resolvable insufficiency falls through to
   the fail-closed DEFER default anyway. Removed the clause; fail-closed
   default covers the residual case. Verified: engine self-test PASS.

3. **[NOTED, not fixed] Q2 identity-level blocked flat.** The engine's
   Ecology tier set treats only Q0/Q1 as operational; Q2 (identity-level)
   is always blocked. The lattice says Q2 is "default quarantine;
   requires explicit user confirmation before use" — so Q2 should be
   usable WITH explicit confirmation (via the DEFER→confirm path). Flat
   blocking is fail-closed and safe for v1, but a future revision should
   add the confirmed-Q2 allowance (explicit user confirmation recorded →
   Q2 permitted). Recorded as a Phase 10/11 boundary note.

## Verification after fixes

- faos_ecology_engine.py self-test: PASS (6 gate cases incl. both ASK)
- verify_integration.py: PASS (exit 0, incl. legacy non-recursive checks)
- witness_run_integration.py: PASS (merged pipeline end-to-end)
- Full gate (verify_all.py): PASS (11 verifiers) — re-run after fixes
  pending external verdict round.

## Expected external input

- judge_deepseek_phase10.txt (adversarial; hunting hidden flaws)
- locus_validation_phase10.txt (7-check discipline)

Both subagents dispatched; findings will be merged sublatively with these.
