# Insight Validation Protocol (insight_validation_protocol.md)

Layer 1 required output of the Motivational_Ecology_Agent_Research_Plan v2 §6.
Purpose: define how an insight node earns the right to leave DRAFT status and,
separately, how it earns the right to influence action. The two gates are distinct.

## Gate A — Lattice Admission (DRAFT → UNDER_REVIEW)
An insight node may enter the lattice only when ALL hold:
1. **Layers separated** — hypothesis lives in the interpretation layer; implication and
   action are derived fields, never fused.
2. **Citations present** — at least one evidence edge to a consented observation
   (observation_schema.json), with strength marked.
3. **Not identity-level** — OR flagged identity_level_flag=true and quarantined by default.
4. **No circularity** — the supporting observations are not defined by the interpretation.
5. **Worded as hypothesis** — "The pattern is consistent with…", never "The user is…".

## Gate B — Action Influence (UNDER_REVIEW → usable)
An insight may influence agent action (scenario selection, timing, scaffolding, personalization)
only when ALL hold:
1. **User verdict** = confirmed or revised (record_user_verdict), or the insight is
   explicitly marked as a trial hypothesis the user agreed to test.
2. **Evidence sufficiency** = partial or sufficient, with source diversity ≥ 2 unless
   the user explicitly waived diversity.
3. **Convergence** = emerging or schematic_equilibrium across independent observations
   (SERUM convergence criterion; equilibrium ≠ correctness).
4. **No manipulation risk** — use of the insight does not covertly steer, shame, coerce,
   or pathologize (see paternalism_and_overinterpretation_guardrails.md).
5. **Relevant and fresh** — lattice_freshness = fresh; stale insights are re-validated.
6. **Boundary respected** — Human_Empowerment_Boundary assessed the action; identity-level
   and high-meaning uses require explicit confirmation.

## Gate C — Re-Validation Triggers
Re-run validation when: the user changes a stated goal; ≥ 3 new observations contradict
an insight; the user revises any insight in the same cluster; 90 days elapse without
review (default, configurable); or a recovery operation (Undo_Interpretive_Closure,
Rebuild_Lattice_From_Raw_Observations) is invoked.

## Protocol Run Record
For each validation run, record: date, insights reviewed, evidence sets used, convergence
state, verdicts, overreach debrief notes, and the calibration delta (what the run taught
the lattice process itself).

## Calibration Rules
- User rejection rate > 30% over a rolling 8 insights ⇒ halt lattice generation, review
  for overinterpretation, and consider Rebuild_Lattice_From_Raw_Observations.
- An insight confirmed by the user replaces any conflicting agent-authored hypothesis in
  the same cluster; user wording becomes the primary citation.
- Practice logs, chat logs, and telemetry are bounded to consented sources; validation
  never expands the consent scope.
