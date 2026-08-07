# Skill-Lattice Interface v1.0

Project: Motivational Ecology Agent Architecture — Phase 4: Graph and Lattice Integration
Date: 2026-08-06
Status: RECONCILED — companion to skill_graph_index.json v1.0 and lattice_index.json v0.1
Evidence discipline: VERIFIED / RECONSTRUCTED flags; insights are hypotheses; user retains interpretive sovereignty.

## Purpose

Define how the motivational lattice (Layer 1: observations → insights) and
the hierarchical skill graph (Layer 2: skill packages + AtomicOps + typed
edges) connect. This is the seam the plan's Phase 4 questions ask about:
which insights may trigger which skills, which require confirmation, which
skills can follow each other, which support missing prerequisites, and which
recover from failure.

## 1. The Interface Contract

### 1.1 Direction of Flow

```
observations (user logs, reflections, artifacts, telemetry)
   │  capture_observation (MLG op; consent-scoped)
   ▼
motivation lattice (insight nodes H*, evidence edges, quarantine tiers)
   │  insight_trigger_policy (this interface)
   ▼
skill graph (skill packages; AtomicOps execute with boundary gate)
   │  skill outputs become new observations (ConvoDojo practice logs,
   │  MI change-talk logs, COMB profiles) — the lattice refreshes
   ▼
revised lattice (schematic equilibrium; SERUM-style convergence)
```

The loop is bidirectional: lattice insights steer skill selection; skill
outcomes (and their logs) feed back into the lattice as observations.
Closed-loop — but never closed-circle: the user's verdict is the arbitration
point at every pass.

### 1.2 Node-Kind Domains (Phase 4 normalization)

| Node kind | Examples | Lives in |
|---|---|---|
| skill | COMB_Behavioral_Diagnosis, MI_Ambivalence_Conversation | skill_graph_index.json nodes |
| atomic_op | classify_component, elicit_change_talk | atomic_ops.json per package |
| recovery_op | Downgrade_To_Scaffold, Return_To_User_Authority | recovery_ops.md / edge_map kind=internal |
| observation | O-001 (user utterance, log entry) | lattice (observation_schema.json) |
| insight | H-003 (provisional hypothesis) | lattice (insight_node_schema.json) |
| evidence_edge | E-007 (insight → observation, strength, provenance) | lattice (evidence_edge_schema.json) |

### 1.3 Edge Type Domains (Phase 4 decision 2)

| Edge type | Domain | Direction semantics |
|---|---|---|
| decomposes_to | skill → atomic_op | skill decomposes into its ops |
| can_follow | skill → skill | sequential composition |
| compatible_with | skill → skill | parallel coexistence, no order |
| supports | skill → skill | one conditions the other's operation |
| recovers_with | skill → skill (kind=cross-skill) OR recovery_op → skill (kind=internal) | source = entity being recovered; target = recovery provider |

## 2. Insight-Trigger Matrix

Which lattice states may trigger which skills. Full policy in
insight_trigger_policy.md; this is the operational summary.

| Lattice signal | Evidence anchor | May trigger | Confirmation gate |
|---|---|---|---|
| Knowledge/skill gap (C-Ps pattern) | COM-B classifier output | TDF_Barrier_Facilitator_Grid, COMB_Behavioral_Diagnosis | insight user_verdict = confirmed |
| Regulatory style (introjected/identified/intrinsic) | Li 2025 VERIFIED; Lim 2025 VERIFIED | SDT_Need_Support_Check | labeled inference, user-correctable |
| Change-talk / ambivalence pattern | Lim 2025 HMM dynamics VERIFIED; AnnoMI | MI_Ambivalence_Conversation | via evocation only, never accusation |
| Atrophy/dependency risk | Bastani 2025, Budzyń 2025 VERIFIED | Proximal_Practice_Selector | objective telemetry over self-report |
| Identity-level claim | quarantine tier Q2 | Human_Empowerment_Boundary | explicit user confirmation MANDATORY |
| Practice-element / embedding state | practice theory, NPT (deferred) | Material_Arrangement_Scan, Feedback_Ecology_Map | n/a until built |

## 3. Confirmation and Quarantine Rules

1. **Insights are hypotheses.** No insight enters the skill graph as fact.
   The MLG op `label_hypothesis_status` and `present_lattice_for_review` gate
   this.
2. **Identity-level claims default to quarantine (Q2).** Any insight with
   `identity_level_flag = true` requires explicit user confirmation before
   ANY skill may consume it. This transposes the Valens quarantine law:
   VERIFIED_STRUCTURE ≠ PERMITTED_APPLICATION.
3. **User rejection is absolute.** An insight the user rejects
   (user_verdict = rejected) is removed from active use regardless of
   evidence strength (MLG `quarantine_insight` + `record_user_verdict`).
4. **No manipulation.** Insights never steer the user toward agent-chosen
   outcomes; the empowerment boundary governs all use of inferred insights.
5. **No surveillance.** Practice logs and observations are evidence for the
   user's own development, never converted into surveillance (MLG
   surveillance_risk state).
6. **Confidence gates.** Low-confidence lattice signals (next-action
   alignment 17-26%, Shaikh 2026 VERIFIED) inform timing, never license
   autonomous action.

## 4. Skill-Chaining Rules (which skills can follow which)

From skill_graph_index.json v1.0 edges:

- COMB_Behavioral_Diagnosis → TDF_Barrier_Facilitator_Grid (decomposes_to,
  VERIFIED) — diagnosis refines into the 14-domain grid.
- TDF_Barrier_Facilitator_Grid → Proximal_Practice_Selector (can_follow) —
  barrier grid informs proximal practice design.
- MI_Ambivalence_Conversation → COMB_Behavioral_Diagnosis (can_follow) —
  ambivalence resolution can refine the diagnosis (reverse pass).
- TDF_Barrier_Facilitator_Grid → COMB_Behavioral_Diagnosis (can_follow) —
  grid → revised component profile.
- SDT_Need_Support_Check supports MI_Ambivalence_Conversation (autonomy
  support conditions evocation quality).
- COMB_Behavioral_Diagnosis compatible_with Motivational_Lattice_Generator
  (lattice insights inform component profile).

## 5. Support and Recovery Wiring

- **Missing prerequisites (supports):** SDT_Need_Support_Check supplies the
  motivational quality the COM-B Motivation bucket leaves undifferentiated;
  Human_Empowerment_Boundary supports every skill via the boundary gate
  (declared required on all nodes, Phase 4 decision 7).
- **Recovery (recovers_with, cross-skill):**
  - MI_Ambivalence_Conversation recovers_with SDT_Need_Support_Check
    (discord → autonomy-support repair)
  - ConvoDojo_Practice_Sparring recovers_with Human_Empowerment_Boundary
    (sparring overreach → boundary reset)
  - COMB_Behavioral_Diagnosis recovers_with Human_Empowerment_Boundary
    (overreach/premature closure → boundary reset)
  - TDF_Barrier_Facilitator_Grid recovers_with Human_Empowerment_Boundary
    (identity overreach/paternalism → boundary reset)

## 6. The HEB Gate (Phase 4 decision 7)

- Every skill_node.json declares `governance.boundary_gate = required`.
- Rule: **No AtomicOp executes on high-meaning tasks (identity, values,
  commitments, interpretive closure) without a Human_Empowerment_Boundary
  check first.**
- Enforcement today: declaration-level (all 8 nodes). Runtime wiring
  (execution-layer enforcement) is Phase 5+; the policy is fully specified
  here and in insight_trigger_policy.md so implementation is mechanical.

## 7. Open Items

- Numeric trigger thresholds (per insight_trigger_policy.md).
- Deferred-skill edges (Material_Arrangement_Scan etc.) — quarantined in the
  index until built; triggers activate then.
- skill_load_score → skill_load_trend conversion op (PPS writes, HEB
  derives) — documented in T2R_traceability.json canonical_state_variables.
