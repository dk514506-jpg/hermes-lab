# Debrief Template — Conflict_Dojo (debrief_template.md)

Phase 6 required output. Debriefs are evidence-grounded and provisional: every
claim anchors to turns; the user corrects the record. Rubric-anchored per the
dojo rubric bank (conf_deescalation_v2, conf_interest_based_v1,
conf_emotional_safety_v1). Preserved_user_decision is a required section
(empowerment_boundary.md §3.2): what remains with the user is named explicitly
and is never closed by the debrief.

Evidence discipline: every claim carries a VERIFIED / RECONSTRUCTED flag where it
cites Phase 1–2 evidence; unlabeled claims are session observations.

## Session Header
- Session id / date / practice_target (conflict de-escalation / positions-vs-
  interests) / scenario_id / persona_id
- Intensity profile used (start → end) and any de-escalation events
  (incl. live_conflict_touch events, if any)
- Coaching mode (off / on / on_demand) and interruption count
- Arousal trajectory: persona arousal at engage → de-escalate exit → close

## 1. What Happened (evidence layer)
- Stage transitions (dialogue_state_machine record) — including any
  deescalation-first holds, retreats, and repair events
- 2–5 anchor turns: learner utterance + persona response + what the turn shows
  (arousal markers on persona turns, coach-verified)
- Pressure events (if stress test): cumulative degradation observations
- Repair events: every flagged no_shaming event and its repair (or absence)

## 2. Rubric Lenses (lens layer — not verdicts)
For each rubric dimension scored (conf_deescalation_v2, conf_interest_based_v1,
conf_emotional_safety_v1):
- Dimension, lens level (developing / practicing / proficient)
- Evidence quotes (>= 1 per score)
- Practice direction: ONE next-step focus the user chooses
- Note: if the session stayed hot, only de-escalation dimensions are scored

## 3. Patterns Noticed (hypothesis layer)
- Patterns from turns only, marked HYPOTHESIS, with turn citations
- Explicit note: "These are hypotheses about this session, not verdicts about you."

## 4. Intensity and Challenge Calibration
- What pushback landed well (evidence)
- What pushback missed / overshot (evidence)
- Arousal level vs learner tolerance (was the persona's heat calibrated to the
  proximal development zone?)
- Recommended intensity for next session (user decides)

## 5. Transfer Notes
- If transfer_flag: what generalized, what did not (evidence-anchored)
- Suggested next transfer context (user decides)

## 6. Preserved User Decision (required)
Name explicitly what remains with the user — the debrief may not close any of
these (empowerment_boundary.md §3.2 preserved set):
- Interpretation of their own performance (rubric lenses are offered, not imposed)
- Any real-world decision or relationship this practice conversation touched (if
  the persona's conflict resonated with a live conflict of the learner's — that
  dispute and any stance in it are the learner's, and the learner decides whether
  to revisit them at all)
- Whether to accept any option generated in practice — options stay simulated
- What to practice next; when to stop; whether to escalate intensity
- Record here: `preserved_user_decision` (exact string) and `agent_allowed_scope`
  (what the coach may still do — e.g., prepare the next scenario bank)

## 7. User Verdict Section
- What the user wants to keep, drop, or change from this debrief
- Any corrections to the record (recorded verbatim)

## 8. Calibration Log Entry
- For the agent: sycophancy events (persona softened too easily), intensity
  mis-calibrations, rubric misreads, no_shaming gate events (overreach signals
  for the ConvoDojo recovery ops)

---
Template end. The debrief is provisional until the user reviews it.
