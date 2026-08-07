# Paternalism and Overinterpretation Guardrails (paternalism_and_overinterpretation_guardrails.md)

Layer 1 required output of the plan v2 §6. These guardrails are load-bearing: they turn
"motivation inference" from a paternalism risk into an auditable, user-correctable practice.

## 1. Status Guard
- Insights are hypotheses, not facts. Any utterance that drops the hypothesis marker
  ("the user IS…", "you avoid…", "you clearly want…") is a guardrail violation.
- The user retains interpretive sovereignty: only the user closes the question of what
  their own behavior means.

## 2. Evidence Guard
- Every insight cites observations (evidence_edge_schema.json). Uncited insight = no insight.
- Evidence sufficiency is scored; insufficient insights are held or quarantined, not used.
- Observations are consented and bounded; practice logs never become surveillance.

## 3. Identity-Level Quarantine
- Claims about who the user IS (identity) are quarantined by default (flag_identity_level_claim
  → quarantine_insight). Explicit user confirmation is required before any identity-level
  interpretation may influence action.
- Behavioral-level hypotheses may be presented as hypotheses without confirmation, but
  never as verdicts.

## 4. Anti-Manipulation Guard
- Motivational insights may never be used to manipulate, nudge covertly, shame, coerce,
  or pathologize (plan v2 §11; MI spirit gate: technical use without partnership is prohibited).
- Insights may inform what is offered, never how the user is pushed.
- No gamified or guilt-based levers derived from insights (anti-introjection, SDT guard).

## 5. Anti-Circularity Guard
- Observations must not be defined by the interpretations they support.
- The lattice must not become self-fulfilling: the agent does not steer the user toward
  the pattern the lattice predicts, then cite the steering as confirmation.

## 6. Anti-Theater Guard
- Presenting trivial observations as deep insight is "insight theater" — the lattice
  analogue of Beacock's empowerment theater (perceived agency ≠ structural empowerment,
  2026). A lattice that produces engagement without capability is a failure mode.

## 7. Anti-Surveillance Guard
- Consent scope is fixed at collection time and never silently expanded.
- Telemetry, logs, and artifacts are latticed only with opt-in; summaries the user sees
  are the whole story, not a sanitized slice.

## 8. Uncertainty Guard
- When evidence is insufficient, abstain (plan v2 §11: "maintain uncertainty and abstain
  when evidence is insufficient").
- Convergence (schematic equilibrium) is a stability criterion, not a correctness proof
  (SERUM 2026 caution); next-action prediction is a timing prior, not an action trigger
  (LongNAP: ~17% trajectory alignment, Shaikh 2026).

## 9. Retraction Discipline
- Do not build on withdrawn work (SRSUPM 2026) or retracted meta-analyses (Wang & Fan
  2025 retraction flagged in the evidence register). Evidence citations in lattices come
  only from the verified source register.

## 10. Recovery Trigger
- User rejection of an insight, repeated corrections, or a rejection rate > 30% triggers
  the recovery path: Debrief_Overinterpretation → Rebuild_Lattice_From_Raw_Observations
  or Downgrade_Confidence, and always Return_To_User_Authority.
