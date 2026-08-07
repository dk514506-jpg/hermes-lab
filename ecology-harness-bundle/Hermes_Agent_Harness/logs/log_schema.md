# logs/ — Runtime Log Schema (contract)

Project: Motivational Ecology Agent Architecture
Layer: Hermes_Agent_Harness/logs/ (Phase 7)
Date: 2026-08-06
Status: SCAFFOLD — schema contract; the store is populated at runtime only
(nothing is written here at install time; `.gitkeep` keeps the scaffold in
version control).

This directory is the runtime log store for the harness. Every entry written
here MUST conform to the event types and required fields below. Consumers
(ConvoDojo_Practice_Sparring, Proximal_Practice_Selector,
Human_Empowerment_Boundary, calibration runs) append entries; nothing is
edited in place (append-only; corrections are new entries referencing the
superseded event_id).

Evidence discipline applies to logs as observations: runtime records are
ground truth for what happened (flag VERIFIED where the entry is a direct
machine record, RECONSTRUCTED where an interpretation is attached), and any
inference in a log (trend, risk class, insight trigger) is a HYPOTHESIS,
user-correctable. Consent scoping per empowerment_boundary.md §4.2: capture
is consent-scoped and never surveillance — practice data stays in practice
(lattice Q5_SURVEILLANCE_RISK).

## Common envelope (all entries)

| Field | Required | Meaning |
|---|---|---|
| `event_id` | yes | Unique id, e.g. `dlg-20260806-001a`. |
| `timestamp` | yes | ISO-8601 UTC, e.g. `2026-08-06T21:14:00Z`. |
| `event_type` | yes | One of: `dojo_session`, `skill_load_snapshot`, `calibration_event`, `boundary_gate_outcome`. |
| `session_id` | yes | The runtime session / conversation id. |
| `source` | yes | Component writing the entry (skill node id or executor), e.g. `ConvoDojo_Practice_Sparring`, `Human_Empowerment_Boundary`. |
| `schema_version` | yes | `ecology-log/0.1` (RECONSTRUCTED calibration anchor, not study-validated). |
| `user_consent_ref` | yes | Consent scope under which capture happens (or `none`); practice capture is consent-scoped. |
| `evidence_flag` | yes | `VERIFIED` (direct machine record) or `RECONSTRUCTED` (interpretation attached). |

## Event types and their required fields

### 1. `dojo_session` — dojo practice session log (written by ConvoDojo_Practice_Sparring)
- `dojo` — dojo id, e.g. `Ambivalence_Dojo`.
- `persona_id` — persona used (persona module generates turns only).
- `intensity_level` — 1-5 as agreed with the user (user_agreement.required).
- `stages_entered` — stage ids traversed, in order.
- `coaching_interventions` — list of coach module interventions (hints, not answers).
- `rubric_scores` — rubric lens scores, each anchored to ≥1 utterance-level quote; scores are inputs, never verdicts.
- `debrief_ref` — link to the debrief record; debrief is provisional until the user reviews.
- `preserved_user_decisions` — deferred/stopped decisions recorded per agent_deference_rules.md §2.1.
- `outcome_arbitration` — the user's verdict on the session (user arbitrates every pass).

### 2. `skill_load_snapshot` — skill_load observation (written by Proximal_Practice_Selector / Human_Empowerment_Boundary)
- `skill_node` — the node measured.
- `skill_load_score` — canonical 0..1 per `learnability_state_schema.json` (ecology-learnability/0.1).
- `assistance_fraction` — assistance share for the track.
- `dependency_ratio` / `empowerment_ratio` — the inverse-pair ratios per the estate schema.
- `trend` — derived (baseline vs recent track); a HYPOTHESIS, not a fact.
- `track` — `baseline` or `recent`.
- `trigger` — why the snapshot was taken (scheduled / user-requested / dojo-session-derived).
- `fade_rung` — current scaffold ladder rung (5→0) per scaffolding_fade_rules.md, if in a fade context.

### 3. `calibration_event` — threshold / parameter calibration (written by calibration runs)
- `calibrated_parameter` — what was recalibrated (e.g. `insight_trigger_T3_threshold`, `intensity_escalation_step`, `fade_rung_timing`).
- `old_value` / `new_value` — before/after.
- `rationale` — reasoning; RECONSTRUCTED (calibration anchors are hypotheses, not doctrine).
- `evidence_anchor` — VERIFIED evidence cited for the change, or `none` (then the change is explicitly provisional).
- `user_consent` — yes/no; recalibration affecting the user is user-owned.
- `outcome_prediction` — predicted effect, later arbitrated against the next snapshot.

### 4. `boundary_gate_outcome` — HEB boundary-gate decision record (written by Human_Empowerment_Boundary)
- `task_context` — whether the task is high-meaning (identity, values, commitments, interpretive closure).
- `heb_mode` — mode selected: ACT / SCAFFOLD / ASK / DEFER / STOP (empowerment_boundary.md).
- `gate_decision` — PASS / ESCALATE / BLOCK (no AtomicOp executes on high-meaning tasks without the check).
- `atomic_ops_attempted` — ops gated, and their disposition.
- `escalation_ladder_level` — L1-L5 if escalation occurred.
- `preserved_user_decision_categories` — categories touched from the preserved_user_decision set.
- `deferral_record_ref` — link to the defer/stop record per agent_deference_rules.md.

## Governance notes
- Logs are observations for the motivational lattice (skill_lattice_interface.md
  §1.1) — change-talk signals may trigger insight formation per
  insight_trigger_policy T3, but enter conversation only via evocation, never
  as accusation.
- Logs never feed the persona module (persona priming degrades performance and
  embeds bias — Ma 2025, VERIFIED).
- Schema version `ecology-log/0.1` is RECONSTRUCTED; revisions require new
  VERIFIED evidence and are themselves calibration events.
