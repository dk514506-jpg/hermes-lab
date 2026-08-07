## ConvoDojo Practice Sparring Examples

### Example 1: MI practice with calibrated escalation
Target: MI evoking (change talk elicitation).
Scenario: "Colleague considering a career change" (scenario bank, work context).
Persona: "Sam, 40s, ambivalent mid-career professional" (sanitized persona bank).
Intensity profile: start 2, escalate to 4 with user consent; escalation policy:
"push deeper reflections only when the user sustains ≥2 complex reflections per 5 turns."
Staging (dialogue_state_machine.json):
- engage: rapport; exit when user makes 2+ open questions.
- explore: sustain talk expected; persona offers realistic resistance.
- challenge: persona raises counterpoints calibrated to intensity 3.
- consolidate: summary + commitment probe.
Session events:
- Turn 14: user asks a closed question; coach (on_demand) interrupts with
  "That's a closed question — try the open version. Want to redo the turn?"
  (coach_interrupt; user controls whether to take the hint).
- apply_rubric_lens: rubric dimensions (open questions %, complex reflections %,
  reflection-to-question ratio, sustain-talk handling). Ratio 0.6 → Aimi target 0.84
  noted as a practice direction, not a verdict.
- calibrate_pushback: user handles two counterpoints well → intensity 4.
Debrief (debrief_template.md): evidence quotes per dimension; user decides next session
focus. Transfer scenario queued: same skill, family context.

### Example 2: Pre-deployment adversarial stress test
Target: conflict de-escalation pattern about to be used in a real team meeting.
Setup: run_adversarial_stress_test with three adversarial personas: (a) dismissive
manager, (b) looping aggrieved colleague, (c) high-pressure time-constrained exec.
Cumulative pressure: each persona escalates across turns; pattern must hold de-escalation
moves (reflection, agenda-setting, pause-offer) under pressure.
Judging: multi-agent judges aligned to humans r=0.82 score the pattern; degradation
under cumulative pressure is the measured quantity.
Outcome: pattern holds at pressure levels 1–3, degrades at level 4 (reflections drop,
interruptions rise). Result: deployment gated to "revise pattern for pressure level ≥4"
— the user decides whether to revise, rehearse more, or deploy as-is with awareness.
Stress test gates patterns, not people; the user retains the deployment call.

### Example 3: Transfer scenario (generalization)
Target: coaching inquiry skills practiced in workplace context.
Transfer scenario (transfer_scenario_set.md): same skill, parent-teacher meeting context.
Run: run_transfer_scenario; rubric re-applied.
Result: open-question fluency transfers, but "authority-handling" dimension scores lower
in the family context — the persona bank's parental persona differs in resistance style.
Debrief notes the generalization gap; next practice targets the gap. Transfer results
are evidence for the learner, not a grade.

### Example 4: Sycophancy guard in action
Event: persona begins agreeing with every user suggestion ("That's a great idea!" x5).
Detection: sycophancy_risk = high (agreement rate > 80% across 10 turns while user
produces no new reasoning).
Action: orchestration function recalibrates — persona raises a grounded counterpoint
from its own config (not from lattice insights about the user); agreement rate returns
to profile. Note: productive challenge is the orchestration function's job, not the
persona's personality. Recorded in sycophancy_risk_notes for calibration.
