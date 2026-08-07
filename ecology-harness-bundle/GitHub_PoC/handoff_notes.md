# Handoff Notes — Hermes Agent Harness (Ecology Foundation Campaign)

> **HARNESS HANDOFF.** This is the Phase 7 harness handoff, adapted from the
> Foundation handoff at `docs/Ecology/Foundation/handoff_notes.md`. Same
> content; paths below point at the packaged harness tree (`skills/`,
> `lattices/`, `routines/`, `evidence/`, `logs/`) instead of the loose
> Foundation layout. Source artifacts remain untouched in the Foundation tree;
> this harness is the distribution copy.

Project: Motivational Ecology Agent Architecture
Campaign: Valens-style reconstruction, Phases 1-7 (+ critique/revision rounds)
Date: 2026-08-06
Status: Phases 1-2 assembled (RECONSTRUCTED syntheses over VERIFIED sources);
Phase 3 built (90 files, structurally verified); Phase 4 RECONCILED (graph +
lattice integration) and verified; Phase 5 COMPLETE at spec/verification level (safeguards, Council-built,
reviewed, revised, verified); Phase 6 COMPLETE at spec/verification level (practice dojos, Council-built,
reviewed, revised, verified); Phase 7 COMPLETE at spec/verification level (Hermes Agent Harness packaged:
skills/, lattices/, routines/, evidence/, logs/, README, skill_graph_index.json,
handoff); Phase 8 COMPLETE at spec/verification level (evaluation artifacts,
outside-judged, revisions integrated, Calibration_Log 22 rows); critique round
COMPLETE; revision rounds applied. Runtime layer: acceptance test user-approved
(n=1 session); boundary-gate execution layer is Phase 9.

## Purpose

What a fresh agent (or Dallas) needs to re-enter this inquiry from disk,
without the parent's context window. Continuity as enacted, not stored.

## How the Campaign Ran

1. **Council method:** 4 delegations of 3 parallel subagents each (Phase 1
   foundations, Phase 2 recent evidence, Phase 3 skill build, critique round).
   Each member read primary sources, verified claims, and returned a fixed-
   format deliverable. Live transcripts and summaries under
   `~/.hermes/cache/delegation/`.
2. **Journal-API probing:** OpenAlex, PubMed, arXiv, Semantic Scholar probed
   via `council_notes/phase2_api_probe.py` (+ test harness
   `test_phase2_probe.py`) → `evidence/phase2_api_seed.md` (registry) and
   the `.jsonl` raw dump in `council_notes/`. Rate-limit handling: exponential
   backoff honoring Retry-After; the probe's one-time bug (pre-encoding %22)
   is documented in the subagent-created skill
   `recent-evidence-distillation`.
3. **Model APIs:** Nous Portal `deepseek/deepseek-v4-flash-0731` verified live
   (the build-day model; distinct from unversioned `deepseek/deepseek-v4-flash`).
   Anthropic key recovered from `~/Desktop/API Keys` (old .env keys were
   rotated); claude-sonnet-4-5 verified.
4. **Assembled artifacts** (now packaged in this harness tree):
   - Phase 1 (in Foundation/, not packaged): Foundation_Matrix.md,
     Construct_Map.md, Theory_to_Routine_Interface.md
   - Phase 2: evidence/Recent_Evidence_Digest.md,
     evidence/Annotated_Bibliography.md (78 entries),
     evidence/Contrary_Findings_and_Limits.md, evidence/phase2_api_seed.md
   - Phase 3: skills/ (8 packages × 9 files + extras), skill_graph_index.json
     (harness root, RECONCILED v1.0)
   - Phase 4: lattices/ (lattice_index.json, MLG schema files,
     insight_trigger_policy.md, skill_lattice_interface.md,
     T2R_traceability.json)
   - Phase 5: safeguards ship in the harness governance/ layer (copied from
     Foundation/Phase5_Safeguards/) and bind the
     harness via its README governance section
   - Phase 6: routines/ (five dojos × 7 artifacts + routines/README.md
     integration index)
   - Governance: harness README.md; 03_Open_Questions_Register.txt (Q6-Q11
     added), 05_Project_Atlas.txt (campaign registered) in Foundation/

## Critique Round Verdicts (2026-08-06)

Three critics (evidence, architecture, ecology) reviewed everything. Their
full critiques are in `council_notes/`:
`critique_0_evidence_epistemology.txt`, `critique_1_architecture_design.txt`,
`critique_2_ecology_governance.txt`.

- **Kernel (preserved):** numeric fidelity of digest↔bibliography; integrity
  register; witness-conflict preservation; COMB/MI/Lattice/PPS packages
  (binding-constraint op, spirit gate, commitment slope, measurable atrophy
  state); quarantine law transposed to the motivational domain; interpretive
  sovereignty encoded as five action modes.
- **Limitations (revised this round):** README "all VERIFIED" claim corrected;
  ~25% provenance flagged RECONSTRUCTED-secondhand; Strack & Deutsch flag
  reconciled; Phase-2 imports in Construct_Map flagged; M-Au/C-Ps classifier
  ambiguity documented; invented thresholds relabeled as observed/calibration;
  empty safeguard columns filled (compress_to_COMB, readiness_gate);
  Voigt/AgentForge attribution fixed; Integrity Exclusions split into
  retracted vs unverifiable; campaign registered in its own ecology (Q6-Q11,
  Atlas entry, this handoff file).
- **Deferred to Phase 5+ (documented, not fixed):** BCW/BCT layer scope decision
  (uninstantiated ops); NPT/practice-theory ops (deferred packages); HEB
  runtime execution-layer enforcement (declaration + policy done in Phase 4);
  per-op numeric confidence thresholds in the packages.

## Phase 4 — Graph and Lattice Integration (2026-08-06)

- **Outputs:** skill_graph_index.json v1.0 (RECONCILED, harness root),
  lattices/lattice_index.json, lattices/skill_lattice_interface.md,
  lattices/insight_trigger_policy.md.
- **Decisions (all recorded in the artifacts):**
  1. Edge keys normalized to source/target everywhere.
  2. recovers_with: source = skill being recovered, target = recovery
     provider; kind discriminator (cross-skill vs internal).
  3. Node ids PascalCase matching dirnames; boundary_gate: required on all 8.
  4. TDF binding_constraint renamed binding_constraint_comb (collision fix).
  5. skill_load_score canonical (PPS writes, HEB derives trend).
  6. Dangling edges to deferred skills quarantined in the index.
  7. HEB gate declared on every skill_node + specified in policy docs.
- **Revision round (user-requested):** verifier made direction-sensitive;
  T2R updated (48 entries: 39 instantiated, 9 deferred); ConvoDojo
  check_psychological_safety and MI agree_direction/prioritize registered in
  SKILL.md + edge_maps; verify_critique_revisions.py updated to assert the
  resolved Phase 4 state; Open Questions Register Q9 marked RESOLVED, Q11
  PARTIALLY RESOLVED, Q10 restored.
- **Verification:** verify_phase4.py (32 checks) + verify_packages.py (all 8,
  0 failures) + verify_phase3.py + verify_critique_revisions.py — all green.

## Phase 5 — Empowerment and Learnability Safeguards (2026-08-06)

- **Council:** deleg_dc680006, three members on the 0731 build (deepseek-v4-
  flash-0731 via nous provider — the model flip Dallas requested).
- **Outputs (5):** empowerment_boundary.md, agent_deference_rules.md,
  learnability_state_schema.json (ecology-learnability/0.1),
  skill_atrophy_risk_check.md, scaffolding_fade_rules.md — all in
  Phase5_Safeguards/, mirrored to harness governance/). Plus council_notes/
  verify_phase5.py (21 checks).
- **Review round (user-requested):** I read all five critically and verified
  every citation against the Phase 1-2 artifacts. Two truthfulness fixes:
  (1) Jose 2025 is an OPINION article per the digest quality register — was
  cited as plain VERIFIED in skill_atrophy_risk_check.md, now carries the
  opinion/commentary caveat; (2) CALM-IT (Nguyen 2026) is a preprint — now
  flagged in scaffolding_fade_rules.md text and evidence register. Both locked
  in as durable verifier guards.
- **Skills:** no new skills created this phase (the Council wrote deliverables
  + verifier only).
- **Kanban:** Dallas requested the real Hermes kanban. Board init done; this
  session is a delegated-child context so CLI mutations are (correctly)
  blocked — setup script prepared at council_notes/setup_kanban.sh for Dallas
  to run in his own terminal (`hermes kanban boards create ecology --switch`
  + 5 Phase 5 tasks + link). Visual dashboard: `hermes dashboard` → Kanban tab.

## Phase 6 — Practice Dojo Routines (2026-08-06)

- **Council:** deleg_751b9d89, three members on the 0731 build. A: Conversation
  + Coaching dojos; B: Ambivalence + Conflict dojos; C: Workplace dojo +
  integration README.
- **Outputs (36 files):** routines/ with five dojos × 7 artifacts
  (dialogue_state_machine.json, persona_config.yaml, rubric.json,
  sparring_intensity_profile.json, in_session_coaching_rules.md,
  debrief_template.md, transfer_scenario_set.md) + routines/README.md
  integration index. 15 personas, 15 rubrics, 33 stage families.
- **Design decision:** dojos are CONTENT packages for the existing
  ConvoDojo_Practice_Sparring node — no new graph nodes (RECONSTRUCTED, per
  the Phase 5 handoff "Phase 6 builds the ConvoDojo layer").
- **Review + revision (planned before executing, per Dallas's request):**
  plan was (A) update README status table from DECLARED placeholders to
  verified inventories, (B) create durable verifier, (C) update continuity
  records. Executed: README §1 now shows all five VERIFIED with real
  inventories; verify_phase6.py (the Council's version, which was superior to
  mine — kept theirs); 2 transfer sets (Conversation, Coaching) gained
  missing VERIFIED evidence anchors (EasyMED 2025, AgentForge 2026, Voigt
  2025) after the verifier caught their absence. ALL PASS, 0 failures.
- **Skills:** no new skills created by this Council.
- **Kanban note:** Dallas asked about the gateway portal
  (persona-sol-9522.agents.nousresearch.com) — answered: that is the NOUS
  PORTAL (subscription/inference/profiles), not the Hermes kanban. Kanban is
  local (SQLite ~/.hermes/kanban.db), visual via `hermes dashboard` → Kanban
  tab. Worker-profile decision pending Dallas's input; setup_kanban.sh ready.

## Phase 7 — Hermes Agent Harness Packaging (2026-08-06)

- **Council:** deleg (phase 7), three members with disjoint subtrees — no
  sibling races: A = README.md + logs/ + council_notes/verify_phase7.py;
  B = skills/ + skill_graph_index.json + lattices/; C = routines/ + evidence/
  + this handoff_notes.md.
- **Outputs:** the packaged harness tree (see the tree in this header):
  README.md (orientation, install path, layer interconnect, governance,
  workflow), skill_graph_index.json (RECONCILED v1.0, single source of
  truth), skills/ (8 packages × 9 core files), lattices/ (5 artifacts),
  routines/ (5 dojos × 7 artifacts + README.md), logs/ (log-schema note +
  .gitkeep, runtime-populated), evidence/ (4 files), handoff_notes.md (this
  file).
- **Workflow:** Pip generates files locally for download; Dallas saves or
  uploads them into OneDrive/SharePoint. Runtime consumes the harness: lattice
  → skill graph → safeguards → dojos, with the Phase 5 safeguards binding
  everything and the HEB gate enforced at the execution layer (see Next
  Actions).
- **Verification:** verify_phase7.py (harness-level: tree structure, 8
  required entries, skills 8 × 9, JSON/YAML parse, lattices 5, routines 5 × 7,
  evidence 4, README sections) chained into verify_all.py. All green.

## Open Questions (see 03_Open_Questions_Register.txt Q6-Q11)

Q6 TDF 12-vs-14 runtime versioning | Q7 reward-undermining vs reward design |
Q8 OneDrive/SharePoint write path | Q9 prediction-ceiling confidence gates
(RESOLVED at policy level; op-level thresholds Phase 5) |
Q10 campaign self-application / skill_load | Q11 HEB runtime enforcement
(PARTIALLY RESOLVED: declaration + policy; execution layer Phase 7 harness
wiring)

## Next Actions (when resuming)

1. Read this file, then the harness README, then the register/atlas updates.
2. Upload the harness tree to OneDrive/SharePoint (Q8) — Pip generates,
   Dallas saves/uploads.
3. Phase 8: Evaluation and Calibration (Evaluation_Rubric.md,
   Skill_Package_QA_Checklist.md, Motivational_Lattice_QA_Checklist.md,
   Practice_Dojo_QA_Checklist.md, Calibration_Log.md) against the 10 plan
   criteria; same Council → outside-judge → integrate → continuity loop.
4. Deferred skills: Material_Arrangement_Scan, Feedback_Ecology_Map,
   Autopoietic_Boundary_Check — then activate quarantined edges.
5. HEB runtime execution-layer gate (declaration + policy done; the actual
   enforcement mechanism is the Phase 7 harness wiring — wire the gate into
   the runtime consumer path).
6. Per-op numeric confidence thresholds in the packages (insight_trigger_policy
   T1-T6 cutoffs wired into atomic_ops).
7. Campaign self-application: one unassisted user task per phase; track
   Dallas's skill_load (Q10) — start with reviewing handoff_notes.md and the
   critique verdicts.
8. Kanban: run council_notes/setup_kanban.sh in a parent terminal to create
   the ecology board + Phase 5 tasks; view via hermes dashboard. Worker-
   profile decision pending Dallas's input.
9. Session journal: `~/Documents/digital_brain/valens_wiki/journal/2026-08-06.md`.
