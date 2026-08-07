# Phase 12 Self-Review — findings (pre-external-verdict)

Date: 2026-08-07
Status: SELF-REVIEW FINDINGS — Pip's own critical pass over the Phase 12
build, recorded BEFORE the external judge/Locus verdicts arrive.

## Findings

1. **[CLEAN] Identity-level confirmation gating is in CODE, not just JSON.**
   Probe: "Walking is just not me. I'm a couch person." → identity level
   detected, 1 reframe candidate, all candidates carry
   confirmation_required=True. The atomic_ops.json guardrail is mirrored
   in executable behavior.

2. **[CLEAN] design_novelty_into_routine never touches meaning.**
   Probe: identity-level meaning in inventory → zero proposals reference
   meaning/reframe. Arrangement-only discipline holds in code.

3. **[CLEAN] CMO hypotheses stay claim-level.**
   form_cmo_hypothesis returns hypothesis_status="hypothesis", mechanism
   anchored, "feeds calibration, never autonomous action" — never a
   verdict. Valens P4/P10 held.

4. **[CLEAN] Agent asks, never supplies meaning.**
   assess_coherence returns 2 coherence_questions and the meaning field
   reads "user-defined (agent asks, never supplies)" — the T2R row 64
   rule is carried in output, not just docstring.

5. **[NOTED] T2R "49/49 instantiated" vs REGISTERED-NOT-BUILT ops.**
   assess_participation / assess_collective_action / assess_monitoring
   are NOT T2R register entries — they are documented as REGISTERED-NOT-
   BUILT in Feedback_Ecology_Map/support_ops.md (2 markers) and
   evaluation_notes.md (1 marker). "All 49 register entries instantiated"
   is therefore TRUE and honest; the not-built ops live outside the T2R
   register, marked clearly in-package. No contradiction — recorded so
   the reviewers can verify this reading rather than flag a false
   "all built" impression.

6. **[NOTED] Deterministic stand-in parsing.**
   scan_materials splits the environment description on ";" — a
   deterministic stand-in for real text parsing (disclosed in code
   comment). The identity-marker set is likewise a stand-in (real framing
   detection is LLM-side). Both disclosed in code, not implied as real
   NLP.

## Verification before external verdicts

- phase12_conditional_packages.py self-test: PASS (all 6 ops)
- verify_phase12.py: PASS (exit 0; 30+ checks incl. schema, discipline
  guardrails, activation wiring, T2R flips, legacy)
- verify_all.py full gate: PASS (13 verifiers, exit 0)
- FAOS canonical suite: PASS (ALL LAYERS PASSED)

## Expected external input

- judge_deepseek_phase12.txt (adversarial)
- locus_validation_phase12.txt (7-check discipline)
