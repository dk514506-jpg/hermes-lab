## Evaluation Notes
Assess this skill using the following checks (mapped to plan §8 evaluation criteria and
Layer 1 operating rules):
- Does every insight cite supporting observations? (uncited insights must be discarded)
- Are observation, interpretation, implication, and action kept in separated layers?
- Is every interpretation explicitly marked as a hypothesis, never a fact?
- Are identity-level interpretations quarantined by default and only activated on
  explicit user confirmation?
- Does the lattice grant the user revision, rejection, quarantine, and correction rights
  — and are user verdicts recorded and propagated?
- Is evidence sufficiency scored per insight (insufficient / partial / sufficient)?
- Is the convergence criterion honest — is schematic_equilibrium treated as stability,
  not correctness (SERUM caution)?
- Is next-action prediction used only as a timing prior, never as an action trigger
  (LongNAP ~17% alignment caution)?
- Is manipulation risk assessed, and are insights never used to steer covertly?
- Are practice logs and telemetry bounded to opted-in sources (no surveillance)?
- Is the lattice rendered so the user can verify inferences from the evidence themselves
  (learnability / no insight-dependency)?
- Is the Beacock 2026 guard applied — perceived agency / engagement is not treated as
  motivation truth?
- Do rejected insights disappear from active use regardless of evidence strength?
- Does the lattice avoid self-fulfilling behavior (acting on an insight until the user
  conforms)?
- Does it record overinterpretation events for later calibration?

Layer 1 artifact checks:
- observation_schema.json exists and matches captured observations.
- insight_node_schema.json carries evidence citations, confidence, identity flag, quarantine.
- evidence_edge_schema.json models observation→insight citation links.
- motivation_lattice.md renders all four layers.
- insight_validation_protocol.md is followed and its run is recorded.
- paternalism_and_overinterpretation_guardrails.md is enforced, not decorative.
