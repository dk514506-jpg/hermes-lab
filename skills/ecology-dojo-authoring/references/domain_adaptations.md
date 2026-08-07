# Domain Adaptations: Ambivalence_Dojo + Conflict_Dojo (Phase 6)

Session detail from building the two domain dojos under
`docs/Ecology/Foundation/Phase6_Dojo/` (2026-08-06). Kept here so future domain
dojos (or QA of these two) start from the verified designs instead of re-deriving.

## Ambivalence_Dojo (MI-style ambivalence practice; learner = interviewer)
- **Stage family** (task-mandated, differs from the 5-stage sparring core):
  `engage / discern-ambivalence / explore-both-sides / evoke-change-talk / consolidate / close`.
  No planning stage BY DESIGN — planning is gated behind readiness in real MI and
  the dojo trains no-premature-closure (Karve 2025 readiness ceiling, Eiroa-Solans
  2025 24h decay, both VERIFIED).
- **Hard gates** in `transition_policy.hard_gates`:
  - `spirit_gate` — technique-without-spirit turns flagged before any technique
    feedback (Kuchipudi 1990; Miller & Rose 2009 empathy r=.82, canonical anchors).
  - `no_premature_closure` — consolidate entry requires `commitment_slope != falling`
    AND both sides explored; premature closure auto-retreats (Defer_Planning).
  - `no_argument_against_resistance` — arguing sustain talk holds the stage
    (empowerment_boundary.md §4 prohibition 5).
- **Rubrics** (3): `amb_mi_fidelity_v1` EXTENDS `mi_fidelity_v1` (+darn_cat_evocation,
  commitment_slope_response, no_premature_closure); `amb_spirit_gate_v1`
  (observational spirit dimensions + spirit_gate_verdict); `amb_sustain_talk_navigation_v1`
  (sustain_talk_reflection, no_argument_count, sustain_talk_invitation, roll_with_resistance,
  balance_preservation). All lens-type scoring — keep the schema value `"lens"` even
  for gate-flavored rubrics; declare gate semantics in rubric_use_rules instead.
- **Personas** (3): p_maia_career, p_devon_exercise, p_robin_caregiving. Each carries
  stance.change_talk_affinity + sustain_talk_affinity and a `dynamics` block
  (change_talk_profile buckets/triggers, sustain_talk_profile themes/triggers,
  evocation_levers, closure_signal) — provisional orchestrator guidance, RECONSTRUCTED.
- **Intensity tuning**: sustain-talk depth IS the pushback (level 4-5 deepens to
  relapse history / identity doubts). De-escalation rule `live_decision_touch`: if
  the persona's sustain talk lands on the learner's OWN live decision, pause and
  check in. `sycophancy_guard` monitors change-talk concession rate, not agreement.

## Conflict_Dojo (de-escalation + positions-vs-interests; learner = practitioner)
- **Stage family** (task-mandated): `engage / de-escalate / separate-positions-from-interests / reframe / generate-options / close`.
  De-escalation comes BEFORE interest work: exit `de-escalate` requires
  `persona_arousal_level <= medium`; if arousal re-rises mid-stage, auto-retreat to
  de-escalate (`deescalation_first` guard).
- **Hard gates**: `no_shaming` (identity attacks flagged, stage holds until repair —
  repair is a rubric dimension, not a failure), `no_forced_agreement` (close never
  requires agreement; unresolved options are a valid halt), `deescalation_first`.
- **Rubrics** (3): `conf_deescalation_v2` EXTENDS `conflict_deescalation_v1`
  (+arousal_recognition, repair_after_miss); `conf_interest_based_v1`
  (positions_vs_interests, reframing_quality, reframe_accuracy_check, option_generation,
  criteria_elicitation, agreement_pressure_check — Fisher & Ury canonical anchor);
  `conf_emotional_safety_v1` (validation_without_shaming, no_personal_attack,
  affect_labeling, space_holding, learner_self_regulation).
- **Personas** (3): p_marcus_arch, p_elena_vendor, p_ines_sibling. Stance carries
  `position` (stated demand), `interests` (hidden from learner, visible to
  orchestrator), `hot_buttons`, `deescalation_levers`. Boundary rule: blunt about
  the DISPUTE, never about the user's identity — even at intensity 5.
- **Intensity tuning**: arousal + positional rigidity IS the pushback. De-escalation
  rule `live_conflict_touch` (practice reactivates a real learner conflict -> pause).

## Verification outcome (council_notes/verify_phase6.py, 200 checks)
- Owned dojos (Amb + Con): 100% green — inventory, parse, exact stage families,
  hard gates, extends bases, required dimensions, boundary keywords (coerc/sham/
  lattice) per persona, data-level VERIFIED+RECONSTRUCTED flags in all 14 files.
- Sibling dojos (Workplace/Conversation/Coaching): all passed EXCEPT 2 findings —
  Conversation and Coaching `transfer_scenario_set.md` lacked data-level
  VERIFIED+RECONSTRUCTED flags (transfer markdown files are easy to miss; add a
  flags line, e.g. "Transfer design: RECONSTRUCTED application of the VERIFIED
  practice evidence").
- Scenario id prefixes per dojo (read from files, never derived from name slices):
  scn_amb_/tr_amb_, scn_conf_/tr_conf_, scn_wk_/tr_wk_, scn_convo_/tr_convo_,
  scn_coach_/tr_coach_.

## Coordination lessons from this build (multi-agent parallel campaign)
- `council_notes/verify_phase6.py` was a CONTESTED path: two sibling subagents
  wrote it while this work ran; two blind writes clobbered theirs. Untracked files
  are unrecoverable via git; sibling sessions don't show in session_search.
- Resolution used: unify into the phase-level verifier (one verifier per phase,
  verify_all.py convention) with per-dojo DOJO_SPECS config and [owned]/[sibling]
  check attribution; then stop touching the contested path. Run output is the
  durable evidence — capture it, a sibling may overwrite the script afterward.
- Sibling artifacts change mid-session (Workplace_Dojo went failing -> passing
  between probe and final run) — re-probe before final verification.
- Drafting artifacts leak: a "wait, X not Y" self-correction landed inside
  dialogue_state_machine.json content; verifier check `"wait," not in json.dumps(...)`
  catches it.
