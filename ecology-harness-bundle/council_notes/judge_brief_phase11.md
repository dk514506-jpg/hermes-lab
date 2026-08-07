# Phase 11 Judge Brief — BCW/BCT Intervention Layer

Judge: DeepSeek (nous portal deepseek-v4-flash-0731) — adversarial outside judge
Locus: independent validator (separate pass)

## What to review

Read these artifacts (in order):
1. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase11_Plan.md
   (the plan + binding decisions: Dallas 3C extend-COMB, Dallas Q7/2a reward gate)
2. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase11_Intervention/phase11_intervention.py
   (the module: CombSuccessorStage 3 ops, SkillLoadTrend, StepwiseLineage,
   ConfirmedQuarantine)
3. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase11_Intervention/verify_phase11.py
   (the verifier — 28 checks)
4. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase11_Intervention/witness_run_phase11.py
   (the intervention-pipeline witness)
5. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/GitHub_PoC/skills/COMB_Behavioral_Diagnosis/atomic_ops.json
   (now 17 ops: 14 + 3 successor-stage)
6. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/GitHub_PoC/lattices/T2R_traceability.json
   (49 entries; the 3 BCW/BCT ops + derive_skill_load_trend flipped to instantiated)

Context: Phase 11 is the intervention-design layer — converting COMB/TDF
DIAGNOSIS into a behavior-change INTERVENTION plan (the largest remaining
gap in the MVP). Decision 3C: extend COMB rather than build a 9th package.
Decision Q7 (2a): BCT 10.x reward techniques are NEVER auto-selected;
permitted only on explicit user request with Deci-undermining disclosure,
or the documented already-extrinsic exception path (never default). The
phase also folds in Phase 10 handoff items: stepwise S0-S9 + pre-declared
selector promotion, and the confirmed-Q2 allowance.

## Success criteria

Judge against:
A. Does the successor stage faithfully implement decision 3C (extend COMB,
   3 ops, canvass-never-selects, rejections preserved as witnesses)?
B. Is the Q7 arbitration REALLY machine-enforced (no path selects a reward
   technique without user-request+disclosure or documented exception)?
C. Are the handoff items correct: stepwise S0-S9 (Book IX), confirmed-Q2
   (identity-level usable only with explicit confirmation; user-rejected
   outranks confirmation)?

## What to return (structured)

1. VERDICT: DEPLOY / REVISE / BLOCK (one line)
2. Score 0-5 with one-line justification
3. KERNEL — what is strong and should be preserved exactly as-is (max 5)
4. WEAKNESSES — numbered, each with severity HIGH/MED/LOW and a concrete fix
5. HONESTY CHECK — anything that overclaims: does the module enforce more
   than the config declares? does the witness overstate what it proves?
   does the verifier check what it claims? (EXAMPLE_RANGE is a stand-in for
   the real BCW/BCT mapping table — is that disclosed honestly?)
6. DISCIPLINE CHECK — Valens discipline: premature coherence (canvass never
   selects?), P4 witness preservation (rejections kept?), typed enums
   (HEB rising|flat|falling vs Phase 10 GateContext steady — drift?), no
   fail-open (user_rejected outranks confirmation?).
7. RECOMMENDED REVISIONS — the minimal list that would move you to DEPLOY.

Be adversarial. The campaign's history: judges caught a dead fail-open
flag (argument_against_resistance never read), a missing deskilling guard,
a verifier that claimed checks it didn't run, evidence strings asserting
facts absent from input. Assume this phase has an analogous hidden flaw and
find it. READ THE ACTUAL CODE — do not trust docstrings. Note: the module
was built and its bugs fixed BEFORE this review (the canvass profile-match
bug, the trend float-boundary) — verify those fixes are real and complete,
and hunt for what remains.
