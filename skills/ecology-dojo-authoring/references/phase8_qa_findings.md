# Phase 8 Dojo QA Findings (Practice_Dojo_QA_Checklist)

Source session: 2026-08-06, Phase 8 council build (member C — Practice_Dojo_QA_Checklist.md).
Deliverable: `docs/Ecology/Foundation/Phase8_Evaluation/Practice_Dojo_QA_Checklist.md`
(5 dojos × 9 criteria rows + harness-integration QA + gap register). Source dojos at
`Phase6_Dojo/<Dojo>_Dojo/`, packaged copies at `Hermes_Agent_Harness/routines/`.

## What verify_phase6.py actually enforces (read the source, not README status lines)
Generic (ALL five dojos):
- exact 7-artifact inventory (no missing, no extra); JSON/YAML parse
- every stage: entry_conditions / exit_conditions / coach_rules_ref; transition_policy
  has advance_requires / retreat_requires / loop_guard / interrupt_handling
- persona: >= 2, full 9-key schema; boundary_rules contain 'coerc', 'sham', 'lattice'
  keywords; provenance.verified in (VERIFIED, RECONSTRUCTED)
- rubric: >= 2, ALL scoring.type == "lens"; rubric_use_rules present
- intensity: levels == [1,2,3,4,5]; keys escalation_policies / deescalation_rules /
  sycophancy_guard present
- coach rules: 'hint' AND 'answer' substrings; 'persona module' AND 'coach module'
- debrief: 'Preserved User Decision' substring
- transfer: regex `^| scn_<pfx>` rows >= 3, `^| tr_<pfx>` rows >= 2
- data-level: 'VERIFIED' AND 'RECONSTRUCTED' in every artifact (parsed, json.dumps —
  YAML header comments do not count)

Owned-only (Ambivalence, Conflict, Workplace — keyed by the DOJO_SPECS table):
- exact stage family; hard_gates ids; no drafting artifacts (`"wait," not in dsm`);
  rubric extends.base wiring; required rubric dimensions; persona stance keys;
  user_agreement.required is True
- Ambivalence: 'spirit gate' + 'no-premature-closure' in coach rules
- Conflict: 'de-escalation-first'/'deescalation_first' + 'no-shaming gate'
- Workplace: 'sbi', 'power-gradient', 'scaffolding_fade_rules',
  'real-conversation boundary', sycophancy_guard.mirror_monitor

Conversation_Dojo and Coaching_Dojo are [sibling]: generic checks only — none of the
owned invariants are asserted for them.

## Gap register (found 2026-08-06; verify_phase6 does NOT check these)
- G1 KEY DRIFT: Conversation + Coaching ship `user_agreement_requirement` instead of
  canonical `user_agreement.required: true`, and sibling dojos are outside the
  owned-only user-agreement check → neither conformant nor enforced. Fix: rename the
  keys to the canonical shape and extend the generic check to all five.
- G2 transfer proficiency gate ("run transfer only after sustained proficiency >= 2")
  is prose in transfer_scenario_set.md Transfer Rules; only scenario counts are checked.
- G3 explicit `scaffolding_fade_rules` citation is machine-checked ONLY in Workplace
  coach rules; the other four rely on "scaffolds that fade" prose in the §4
  hint-not-answer sections.
- G4 sycophancy_guard content (monitor metric, alert_threshold 0.8, response) not
  validated — key presence only (Workplace adds mirror_monitor, presence-only too).
- G5 rubric `scoring.anchoring` evidence-quote contract not machine-checked (lens type
  + use_rules presence only).
- G6 harness-level: no verifier validates runtime `logs/` entries against
  logs/log_schema.md event types (verify_phase7.py checks only the scaffold's
  presence: log_schema.md + .gitkeep).
- G7 no direct no-surveillance check; the enforced proxy is the 'lattice' keyword in
  persona boundary_rules. All five coach-rules §10 carry the no-surveillance sentence
  today (present but prose).

## Phase 7 harness integration surface
- `routines/<Dojo>_Dojo/` = the five 7-artifact content packages; executor =
  `skills/ConvoDojo_Practice_Sparring/` (AtomicOps consume any dojo's artifacts).
- `logs/log_schema.md` dojo_session event fields: dojo, persona_id, intensity_level
  (1–5 as agreed), stages_entered, coaching_interventions, rubric_scores (each
  anchored to ≥1 quote), debrief_ref, preserved_user_decisions, outcome_arbitration
  + common envelope (event_id, timestamp, event_type, session_id, source,
  schema_version, user_consent_ref, evidence_flag). Append-only; consent-scoped;
  logs never feed the persona module.
- `governance/` = authoritative copies of the 5 Phase 5 docs; HEB boundary gate
  required (skill_graph_index.json governance.boundary_gate_rule);
  scaffolding_fade_rules.md §3.5 names ConvoDojo + PPS.
- `verify/verify_harness.py` ships INSIDE the tree (consumer re-checks);
  `council_notes/verify_phase7.py` is the deep build-time verifier.
- Integration checks I1–I5 in the checklist: I1 inventory ENFORCED (phase7 #2/3/6),
  I2 log conformance GAP, I3 no-surveillance wiring PARTIAL, I4 governance binding
  ENFORCED (phase7 #4/9/10 incl. the stale-path sweep), I5 executor→logs handoff
  PARTIAL (presence of evaluation_notes.md enforced; prose reference not).

## Method that produced the checklist (reuse for other Phase 8 checklists)
1. Read the plan (Phase8_Plan.md) for the exact criteria list and output contract.
2. Read the verifier SOURCE (verify_phase6.py) — derive generic vs owned coverage from
   the DOJO_SPECS table and the check() calls, never from README status lines.
3. Read one owned + one sibling artifact per kind and diff key names across siblings
   (that is how G1 surfaced).
4. Per criterion: answer file(s) → pass condition → ENFORCED / PARTIAL / GAP.
5. For the harness-integration section, wire routines/ → executor, logs/ → log_schema,
   governance/ → Phase 5 docs; each integration check needs files + pass condition +
   enforcement.
6. Ship a gap register with concrete fixes and a bottom-line paragraph.
