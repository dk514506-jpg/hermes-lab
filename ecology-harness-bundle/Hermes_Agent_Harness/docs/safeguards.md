# Safeguards — The Estate's Rulebook

*Condensed from the Phase 5 estate (docs/Ecology/Foundation/Phase5_Safeguards/).
Full texts ship in governance/ in this package.*

## The five documents

### 1. empowerment_boundary.md — the agency rulebook

The operational form of the campaign's charter: **the agent proposes, the
user disposes.** It defines:

- **Five action modes, with precedence:** STOP > DEFER > ASK > SCAFFOLD > ACT.
- **Preserved-user-decision set** (six categories): identity-level
  interpretations, high-confidence constructs on thin evidence, anything the
  user flagged, etc. — decisions in this set are never made by the agent.
- **Ten absolute prohibitions**, each carrying its VERIFIED evidence anchor
  (e.g. no coercion, no sycophancy, no surveillance, no
  manipulation-by-insight).
- **The L1-L5 escalation ladder** — routed through the reconciled
  `recovers_with` graph edges (source = skill being recovered, target =
  recovery provider).
- **Quarantine-law interaction** — user rejection is absolute and
  unappealable by evidence.

### 2. agent_deference_rules.md — when the agent steps back

- Defer triggers (what makes the agent stop and hand back).
- **Silence as a valid action** (anchored in ProEvent/PROBE: forced
  engagement has 26-40% ceilings — engagement can't be manufactured).
- **Propose/dispose asymmetry**: the agent may propose; only the user disposes.
- Re-opening deferred decisions is always permitted (no locked choices).

### 3. learnability_state_schema.json — the estate's measurement layer

A JSON Schema (draft-07, meta-validated with negative tests) that defines
skill load across ALL skills: `skill_load_score` 0..1 canonical,
`skill_load_trend` (derived), baseline vs recent arrays, assistance_fraction,
dependency_ratio, empowerment_ratio. **Telemetry over self-report** — the
system measures, it doesn't ask.

### 4. skill_atrophy_risk_check.md — the check procedure

Operational pipeline: compute skill_load_score → baseline-vs-recent →
separate performance from capability → classify risk
(none/low/medium/high) → scaffolding response per level. The Budzyń 2025
VERIFIED warning is canonical: skill-atrophy risk rises with assistance
(28.4%→22.4% ADR when scaffolds are removed too fast).

### 5. scaffolding_fade_rules.md — the fade trajectories

- **Fade is mandatory** (F1-F4): scaffolding must decrease over time.
- Hints > answers (Bastani 2025, VERIFIED: hint-based tutor guardrail;
  +48% practice gain).
- Readiness-gate integration (Liu 2026, VERIFIED: +21%).
- Unassisted-metrics signal: only *unassisted* performance counts as
  capability evidence (Bastani +48/-17; Brynjolfsson +14/+34).
- **What never fades:** consent, the preserved-user-decision set, the
  quarantine law.

## Why this matters for agent research

Most safety work focuses on what the agent must NOT do. This estate is
explicitly about **what the agent must NOT take**: the user's judgment,
decision rights, and skill. The distinction is structural — encoded in
schemas, ops, and verifiers — not a values statement in a system prompt.
