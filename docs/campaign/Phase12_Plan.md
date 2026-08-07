# Phase 12 Plan — Conditional Package Activation (Material_Arrangement_Scan + Feedback_Ecology_Map)

Project: Motivational Ecology Agent Architecture
Plan date: 2026-08-07
Status: PLAN — written before execution. Dallas directive: "proceed with
building the two conditional packages."

## Trigger (governance checkpoint satisfied)

DEFERRED_PACKAGES.md activation criteria for both packages: "When a
practice-theory synthesis is available, OR USER REQUESTS home-lab
application" / "When NPT evidence is digested, OR USER REQUESTS." Dallas
requested both → the user-request branch of the trigger is MET. The
governance note additionally requires: a stated trigger (met), a review
against the Phase 5 safeguards, and a verifier extension before edges
un-quarantine (delivered in D4 below).

## What the packages are (grounded in Theory_to_Routine_Interface.md)

### D1 — Material_Arrangement_Scan (practice-theory; Shove et al. 2012)

The practice-theory lens on WHY a routine sticks: a practice persists when
its MATERIALS (physical/digital environment), COMPETENCES (skills), and
MEANINGS (framings) hold together in a bundle. The package scans the
user's environment through this lens and proposes rearrangements —
"cues supplement, not replace, practice" (T2R row 94).

4 atomic ops (T2R register, all currently UNINSTANTIATED):
1. scan_materials — "Where does the cue live in your environment?"
   (T2R row 115). Inventory the physical/digital environment description
   into practice_graph[].materials. User rearranges; agent proposes.
2. scan_meanings — user's framing of activities (T2R row 96). Outputs
   practice_graph[].meanings. Meaning-making is user-owned (Charter:
   preserve judgment); identity-level reframes require explicit
   confirmation (Phase 11 confirmed-Q2 path applies).
3. detect_shared_elements — bundles (T2R row 116): one competence
   serving two practices. Outputs the overlap map that makes
   rearrangement economical (change one element, benefit two practices).
4. design_novelty_into_routine — the design op: propose material/
   arrangement changes that respect the "cues ≠ replacement" rule
   (novelty enters via arrangement, never by imposing meaning).

Layers: 2 (sits on top of COMB diagnosis layer 1). Role: environmental_scan.

### D2 — Feedback_Ecology_Map (NPT embedding-work; May & Finch 2009)

The Normalization Process Theory lens on embedding a new routine: a
practice becomes normal through four generative mechanisms — Coherence
(sense-making), Cognitive Participation (enrolment), Collective Action
(operational work), Reflexive Monitoring (appraisal). The package maps
where a routine is in its embedding trajectory and what feedback loops
exist.

2 atomic ops (T2R register, currently UNINSTANTIATED):
1. assess_coherence — NPT mechanism 1 (T2R rows 64/109): "Does this
   routine make sense as part of your life?" Outputs
   normalization_state[] (meaning, differentiation, internalization).
   User defines meaning; agent never supplies it — asks.
2. form_cmo_hypothesis — realist-eval op: Context-Mechanism-Outcome
   hypothesis for why embedding is or isn't taking hold. Outputs the
   CMO candidate for calibration (hypothesis status, never verdict —
   Valens P4/P10 discipline).

(assess_participation/assess_collective_action/assess_monitoring from
T2R rows 65-67 remain REGISTERED-not-built: they read signals the estate
does not yet generate at runtime — recorded, not deferred-blocked.)

Layers: 2. Role: embedding_map.

### D3 — Package scaffolding (9 files each, matching estate schema)

Each package gets the full file set: SKILL.md, skill_node.json,
atomic_ops.json, edge_map.json, state_schema.json, examples.md,
support_ops.md, recovery_ops.md, evaluation_notes.md — matching the
existing packages' schema (verified against COMB).

### D4 — Activation wiring (governance checkpoint)

1. skill_graph_index.json: the 4 quarantined_edges (COMB→MAS,
   TDF→MAS, COMB→FEM, TDF→FEM) move from quarantined to live.
2. T2R_traceability.json: the 6 register ops flip to instantiated
   (scan_materials, scan_meanings, detect_shared_elements,
   design_novelty_into_routine, assess_coherence, form_cmo_hypothesis).
3. Verifier extension: verify_phase12.py — package schema conformance,
   op counts, T2R flips, quarantine-edge un-quarantine, plus behavioral
   checks of each package's ops (deterministic, no LLM).
4. verify_all.py chains verify_phase12.py (12 → 13 verifiers).

## Decisions already made (binding)

- Dallas: build both packages now (user-request trigger met).
- Practice-theory lens is DESCRIPTIVE, never prescriptive on meaning:
  "cues supplement, not replace, practice"; meanings are user-owned;
  identity-level reframes require explicit confirmation (Phase 11 R3
  path). 
- NPT: user defines meaning; agent asks, never supplies. CMO
  hypotheses are hypotheses (evidence-ladder claim level), never
  verdicts.

## Out of scope

- Autopoietic_Boundary_Check (indefinite hold — philosophy kept as
  philosophy)
- assess_participation / assess_collective_action / assess_monitoring
  (registered, not built: runtime signals not yet generated)
- Live LLM runtime sessions (absence register still blocks — the
  packages are estate artifacts + deterministic verifier evidence)

## Decision points for Dallas (bite-sized)

- P12-D1: approve the 4-op Material_Arrangement_Scan as specified?
- P12-D2: approve the 2-op Feedback_Ecology_Map as specified?
- P12-D3: approve activating all 4 quarantined edges + 6 T2R flips
  together (rather than per-package)?
