# Architecture — The Five Layers and Their Seams

*From the full campaign archive (docs/Ecology/Foundation/). Condensed for the
proof-of-concept package.*

## The five layers

### 1. The Motivational Lattice (insight engine)

A directed graph of observations → insights → evidence edges. Every insight
node is a **hypothesis**, never a verdict. The lattice enforces:

- **Quarantine tiers Q0-Q5.** Q2 = identity-level claims default to
  quarantine until explicitly cleared. Q3 = user-rejected insights are
  removed from active use *regardless of evidence strength* — rejection is
  absolute and unappealable by evidence (empowerment boundary §6).
- **Trigger policy T1-T6.** Insights fire skill-selection triggers only when
  confidence gates + user-consent prerequisites pass. Prediction ceilings are
  wired as *timing-only* gating (e.g. 17-26% next-action alignment — a
  ceiling, not a floor to be gamed).

### 2. The Skill Graph (8 packages, 90 files)

| Package | Purpose |
|---|---|
| Human_Empowerment_Boundary | the agency rulebook — five modes, preserved decisions |
| COMB_Behavioral_Diagnosis | capability/opportunity/motivation-behavior diagnosis |
| TDF_Barrier_Facilitator_Grid | 12-vs-14 domain barrier coding (witness conflict PRESERVED) |
| SDT_Need_Support_Check | autonomy/competence/relatedness support |
| MI_Ambivalence_Conversation | motivational interviewing structure |
| Proximal_Practice_Selector | skill-load tracking, atrophy risk, readiness gates |
| Motivational_Lattice_Generator | the lattice's write path |
| ConvoDojo_Practice_Sparring | the dojo executor |

Every package carries the same 9-file skeleton: SKILL.md, skill_node.json,
atomic_ops.json, edge_map.json, state_schema.json, examples.md, support_ops.md,
recovery_ops.md, evaluation_notes.md. AtomicOps carry inputs/outputs/
guardrails; recovery ops encode fail-closed halt states.

### 3. The Safeguards (Phase 5 estate)

Five documents bind the whole estate (see docs/safeguards.md for detail):
empowerment_boundary, agent_deference_rules, learnability_state_schema,
skill_atrophy_risk_check, scaffolding_fade_rules.

### 4. The Practice Dojos (5 environments × 7 artifacts)

Conversation, Coaching, Ambivalence, Conflict, Workplace. Each dojo has a
dialogue state machine (entry/exit conditions, hard gates), persona config
(boundary-ruled, sanitized), rubric (lens-not-verdict), intensity profile
(user-agreement required), in-session coaching rules (hint-not-answer),
debrief template (preserved-user-decision section), and transfer scenarios.

### 5. Evidence + Logs

78-source evidence base with per-entry VERIFIED/RECONSTRUCTED/UNVERIFIED
flags; a retraction register (exiled, never cited); an append-only runtime
log schema (dojo_session, skill_load_snapshot, calibration_event,
boundary_gate_outcome) with consent scoping — practice data stays in
practice.

## The seams (where the layers connect)

- Lattice → skills: insight triggers T1-T6 select skills via the graph.
- Skills → safeguards: every skill node carries `boundary_gate: required`.
- Dojos → lattice: practice logs are declared *observations* for the lattice.
- Logs → calibration: every session's outcome is user-arbitrated; nothing
  self-arbitrates.

## What "RECONCILED" means (the single-source-of-truth decision)

The skill graph index is declared a **curated canonical subset** of the
reconciled Phase 4 graph. Package-scope edges live in package edge_maps;
cross-skill edges live in the index. Divergence between them is *documented,
not hidden* — the outside judges confirmed this is honest handling of a
problem most projects hide.
