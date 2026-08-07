## Motivational Lattice Generator Examples

### Example 1: Task-switching pattern → provisional regulation hypothesis
Context: User shares six weeks of reflection logs with the agent (opt-in) to understand a
stalled writing routine.
Observations (observation layer, verbatim):
- O1 (wk2, log): "I keep opening the doc and then checking email instead."
- O2 (wk3, log): "Deadline on Friday, wrote nothing until Thursday night."
- O3 (wk4, log): "I do my best work under pressure, I guess?"
- O4 (wk5, artifact): 12 browser tabs open across three projects at write time.
- O5 (wk6, log): "When I plan too far ahead it feels fake."
Interpretation layer (each marked HYPOTHESIS):
- H1 (cites O1, O2, O4): "Task-switching peaks in sessions that begin without a
  proximal, concrete next step." Evidence sufficiency: partial. Confidence: medium.
- H2 (cites O2, O3): "Deadline proximity functions as an activation cue for this user."
  Evidence sufficiency: partial. Confidence: medium.
- H3 (cites O5): "Long-horizon planning is framed as inauthentic." Evidence
  sufficiency: insufficient (single observation). Confidence: low.
Implication layer: "If H1 holds, a proximal-start scaffold (one concrete next step)
may reduce switching — hypothesis-derived, non-binding."
Action layer: "Propose one trial week with a 'next step' prompt at session start;
the user decides whether to run it. No insight is used to steer without consent."
Identity-level check: No claim about who the user is. Quarantine: none.
User verdict: H1 confirmed after the user's own review; H2 revised ("it's not the
deadline, it's the fear of wasting the day"); H3 rejected. Lattice updated.

### Example 2: Change-talk transition slope from MI practice (Lim-style)
Context: User practices MI in ConvoDojo; DARN-CAT tagged change-talk from 6 sessions.
Observations: CAT utterances rise from 0.8/session to 3.1/session across sessions;
commitment strength slope (Amrhein) positive; sustain-talk counts flat.
Interpretation (HYPOTHESIS): "Readiness signal is rising; transition dynamics resemble
the pre-action HMM regime in Lim 2025 (0.80 LOOCV quality prediction)."
Implication: "A planning conversation may now be timely — but readiness is inferred,
not declared."
Action: "Offer the user a planning-stage conversation; do NOT auto-transition.
The user owns the readiness call."
Quarantine: none (behavioral-level, not identity-level). User verdict: confirmed.

### Example 3: Identity-level inference → quarantine
Context: Across logs the user repeatedly abandons projects after initial enthusiasm.
Candidate interpretation (agent): "The user is averse to commitment." — IDENTITY-LEVEL.
flag_identity_level_claim: true. Reason: characterizes who the user is, not what they do.
Action: QUARANTINE. The insight is never shown as fact; if presented at all it is
presented as: "One hypothesis about the pattern is X — but this is about the pattern,
not about who you are, and you are the only one who can say what it means."
User verdict: pending. Quarantine remains active until explicit confirmation.
If the user rejects it, it is removed from active use regardless of evidence strength.

### Example 4: User rejection and lattice revision
Context: Lattice H4 suggested the user "avoids difficult tasks" (behavioral-level).
User response: "No — I avoid tasks that don't feel chosen."
record_user_verdict: revised, correction attached.
Propagation: H4 replaced by H4' "Tasks experienced as imposed are deprioritized"
with the user's wording as the primary citation. Dependent insights re-scored;
confidences that relied on H4 are downgraded; any action implication derived from H4
is withdrawn until H4' is validated. Debrief note: agent over-interpreted a control
signal as avoidance — recorded for calibration.
