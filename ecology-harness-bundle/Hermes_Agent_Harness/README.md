# Hermes Agent Harness — Motivational Ecology Agent Architecture

Project: Motivational Ecology Agent Architecture
Phase: 13 — Live Wire (Estate → Hermes Skill Module)
Date: 2026-08-07
Status: PACKAGED mirror of the canonical estate (GitHub_PoC/) — synced
through Phase 13; verified by `council_notes/verify_all.py` (14 verifiers).

## What This Is

This directory is the packaged **Motivational Ecology Agent Architecture**: the
governed skill library, method graph, practice routines, evidence base, and
runtime log contract built across Phases 1-13 of the Ecology Foundation
campaign. It is the MIRROR of the canonical estate at GitHub_PoC/ (the
canonical tree is the source of truth; this tree is the consumer-facing copy).
As of Phase 13, the estate is also wired into the Hermes harness as the
`motivational-ecology` skill (see ~/.hermes/skills/motivational-ecology/).

The packaged tree (the required inventory, enforced by the verifier):

| Entry | Role |
|---|---|
| `README.md` | This orientation manual. |
| `skill_graph_index.json` | RECONCILED v1.0 skill graph (Phase 4) — single source of truth for skill nodes and typed edges. |
| `skills/` | The TEN built skill packages (8 original + Material_Arrangement_Scan + Feedback_Ecology_Map, Phase 12). |
| `lattices/` | The motivational lattice layer (index, MLG schemas, trigger policy, interface, traceability). |
| `routines/` | The five Phase 6 practice dojos, executed through ConvoDojo_Practice_Sparring. |
| `governance/` | The five Phase 5 estate safeguards (empowerment boundary, deference rules, learnability schema, atrophy check, fade rules) + `valens_operating_logics.md` (Phase 9 meld — first-class governance layer, mirror of GitHub_PoC). |
| `meld/` | The Phase 9 Valens × Ecology meld record (charter + principle-coverage audit + witness run scripts; mirror of GitHub_PoC/meld/). |
| `docs/` | Phase 3 architecture + safeguards + valens-principles + verification (mirror of GitHub_PoC/docs/). |
| `logs/` | Runtime-populated log store; the contract is `logs/log_schema.md` (scaffold ships empty). |
| `evidence/` | The verified evidence base the whole architecture cites. |

> **Corpus pointer (Phase 9 meld):** the Valens corpus is a frozen archive
> at `~/.hermes/hermes-agent/docs/Valens Anthologies/` (Riley translation +
> 115 reconstruction artifacts), deliberately OUTSIDE this estate (operating
> logics only; corpus frozen — Dallas Q1.1/Q1.5). The estate's operational
> form is `governance/valens_operating_logics.md`; Valens is a source about
> METHOD, not findings, and the corpus is exempt from evidence flags
> (historical archive).
| `handoff_notes.md` | Campaign handoff, adapted for the harness. |

Provenance: Phases 1-2 assembled from VERIFIED council distillations
(synthesis = RECONSTRUCTED at artifact level); Phase 3 built the eight HiSkill
packages; Phase 4 reconciled the graph and integrated the lattice; Phase 5
added the empowerment/learnability safeguards; Phase 6 built the five practice
dojos. Phase 7 packages all of it; Phase 8 (evaluation and calibration) builds
on this tree.

## How It Interconnects

The architecture is a closed loop, never a closed circle — the user's verdict
arbitrates every pass. The flow runs **lattice → skill graph → safeguards →
dojos → evidence**, with `logs/` as the runtime feedback channel.

1. **Lattice drives the method.** `lattices/lattice_index.json` holds the
   observation / interpretation / evidence-edge layers and quarantine tiers
   Q0-Q5; the MLG schema files (`observation_schema.json`,
   `insight_node_schema.json`, `evidence_edge_schema.json`) define its data
   shapes; `lattices/insight_trigger_policy.md` sets the operational trigger
   thresholds T1-T6; `lattices/skill_lattice_interface.md` is the seam into the
   skill graph (node-kind domains, edge-type domains, insight-trigger matrix,
   confirmation/quarantine rules, skill chaining, HEB gate);
   `lattices/T2R_traceability.json` traces register ops to package ops
   (52 entries; 49 instantiated + 3 registered-not-built — all register
   candidates resolved as of Phase 12).
2. **The skill graph routes method.** Root `skill_graph_index.json` is the
   RECONCILED v1.0 graph: the eight skill nodes and typed edges
   (`can_follow`, `compatible_with`, `decomposes_to`, `recovers_with`,
   `supports`), deferred nodes, quarantined edges, and the governance block
   (`boundary_gate_rule`, `enforcement`).
3. **Safeguards bind everything.** The Phase 5 estate controls — five
   documents in `governance/` (`empowerment_boundary.md`,
   `agent_deference_rules.md`, `learnability_state_schema.json`,
   `skill_atrophy_risk_check.md`, `scaffolding_fade_rules.md`) — are
   estate-scope and govern every layer below: no AtomicOp executes without
   the boundary gate; scaffolding fades per the fade rules; skill_load is
   tracked against the estate schema. (Package-local copies of the boundary
   and deference rules also ride inside `skills/Human_Empowerment_Boundary/`;
   the `governance/` copies are authoritative for the harness.)
4. **Dojos practice the method.** `routines/` holds five dojo content packages
   (Conversation_Dojo, Coaching_Dojo, Ambivalence_Dojo, Conflict_Dojo,
   Workplace_Dojo — each a seven-artifact package) executed through the shared
   operating skill `skills/ConvoDojo_Practice_Sparring/`. ConvoDojo pairs with
   `skills/Proximal_Practice_Selector/` for sparring-scaffold fading; it
   `recovers_with` Human_Empowerment_Boundary on sparring overreach; MLG
   `can_follow` into ConvoDojo.
5. **Evidence anchors everything.** `evidence/` (Recent_Evidence_Digest.md,
   Annotated_Bibliography.md, Contrary_Findings_and_Limits.md,
   phase2_api_seed.md) is the verified base every artifact cites. Digests and
   syntheses are RECONSTRUCTED at the artifact level; VERIFIED applies to the
   sources they cite.
6. **Logs close the loop.** At runtime, `logs/` receives dojo session logs,
   skill_load snapshots, calibration events, and boundary-gate outcomes (per
   `logs/log_schema.md`). Practice logs become consent-scoped **observations**
   for the lattice (skill_lattice_interface.md §1.1); lattice insights feed
   scenario/intensity selection only with user consent — the persona is never
   scripted from lattice insights about the user.

## Install/Use

**Consuming `skills/`.** Each package is a self-contained directory in the
campaign's HiSkill 9-file shape (SKILL.md, skill_node.json, atomic_ops.json,
edge_map.json, state_schema.json, examples.md, support_ops.md, recovery_ops.md,
evaluation_notes.md, plus layer extras). To install a package into Hermes, copy
its directory into a Hermes skills location (e.g. `~/.hermes/skills/<package>/`
or the profile skills dir) — the SKILL.md frontmatter drives skill loading.
Alternatively, read the packages as the method graph: `skill_graph_index.json`
is the wiring diagram, each package's `skill_node.json` + `atomic_ops.json` +
`edge_map.json` describe what the node does, how it chains, and how it
recovers. Consumers may install any subset; the graph index remains the
source of truth for how the installed subset interconnects.

**Running `routines/`.** A dojo is content, not a new skill node: all five
execute through `ConvoDojo_Practice_Sparring` (the shared executor in
`skills/`). A practice session follows its AtomicOps: select_scenario →
configure_persona → set_intensity_profile (with the user; intensity is never
assumed) → open_stage/advance_stage → generate_interlocutor_turn →
coach_interrupt → apply_rubric_lens → calibrate_pushback →
debrief_session → run_transfer_scenario (after sustained proficiency),
with check_psychological_safety running throughout. The executor consumes each
dojo's seven artifacts (dialogue_state_machine.json, persona_config.yaml,
rubric.json, sparring_intensity_profile.json, in_session_coaching_rules.md,
debrief_template.md, transfer_scenario_set.md) and obeys the coach/persona
separation invariant: the persona generates turns and never evaluates; the
coach controls staging, intensity, and feedback; the coach recommends, the
user decides.

**Reading the Skill Graph.** `skill_graph_index.json` uses five typed edges
(see skill_lattice_interface.md §1.3 for the full table):
- `decomposes_to` — a skill breaks down into its AtomicOps (or a coarse node
  refines into a finer one, e.g. COMB → TDF).
- `can_follow` — sequential composition: "B can follow A" (source precedes
  target).
- `compatible_with` — parallel coexistence, no order required.
- `supports` — one node conditions another's operation.
- `recovers_with` — source = skill being recovered, target = recovery
  provider; `kind: cross-skill` (skill→skill) or `kind: internal`
  (recovery op → skill).
The index is the curated canonical subset of the reconciled Phase 4 graph;
per-package `edge_map.json` files carry the full local edge set (including
op-level edges), and package edges absent from the index are package-scope by
default. Edges to deferred skills are quarantined (index `quarantined_edges`
and per-package `quarantine` markers) until those packages are built.

**Verification is build-time enforced.** `council_notes/verify_phase7.py`
(in the Foundation tree, chained into verify_all.py) ran clean before this
tree was packaged; a lightweight `verify/verify_harness.py` ships inside the
harness so a consumer can re-check JSON/YAML parse and the required inventory
after local edits. Runtime consumers otherwise trust the packaged tree.

**How `logs/` gets populated.** Nothing is written here at install time — the
scaffold ships with `log_schema.md` (the contract) and a `.gitkeep`. At
runtime, the ConvoDojo executor appends dojo session logs; PPS/HEB write
skill_load snapshots and boundary-gate outcomes; calibration events are
appended by calibration runs. The exact event types and required fields are in
`logs/log_schema.md`; consumers write only entries conforming to it, and only
with consent scoping — logs are observations, never surveillance.

## Governance

- **Phase 5 safeguards bind everything.** The five Phase 5 documents are
  estate-scope: they govern the skill library, the lattice, the dojo layer
  (explicitly named in scaffolding_fade_rules.md §3.5), and the logs. Estate
  scope wins over package-local statements; conflicts are recorded, not
  harmonized (Valens discipline).
- **HEB boundary gate required.** No AtomicOp executes on high-meaning tasks
  (identity, values, commitments, interpretive closure) without a
  Human_Empowerment_Boundary check first (skill_graph_index.json governance;
  skill_lattice_interface.md §6; empowerment_boundary.md §7). Runtime
  enforcement is the Phase 5+ wiring commitment; until then the gate is
  declared and enforced by the verifier and the estate rules.
- **Evidence discipline.** VERIFIED = source fetched (abstract at minimum);
  RECONSTRUCTED = agent-applicability inference, labeled; UNVERIFIED =
  search-only record. Syntheses assembled from council distillations are
  RECONSTRUCTED at the artifact level. Contrary findings are preserved, not
  harmonized; retracted work is register-only. **Insights are hypotheses** —
  labeled, logged, user-correctable, and outcome-arbitrated, never facts
  about the user. Thresholds are calibration anchors, not study-validated
  doctrine; revisions require new VERIFIED evidence.
- **Verification gate.** `council_notes/verify_phase7.py` (in the campaign
  council_notes, chained into verify_all.py) enforces the required inventory:
  tree entries, 8 skill packages × 9 core files, JSON/YAML parse, graph edge
  validity, lattice artifacts, 5 dojos × 7 artifacts, evidence files, README
  sections. The harness is not uploaded until it exits 0.

## Workflow

1. **Pip generates locally.** The Council builds and revises the tree locally
   under `docs/Ecology/Foundation/Hermes_Agent_Harness/`; all edits happen on
   the local copy. Inventory counts are per the verifier, not asserted here.
2. **Dallas uploads.** Dallas saves/uploads the verified tree into
   OneDrive/SharePoint — the harness estate. The uploaded tree is the
   distribution copy; the local tree remains the source of truth.
3. **Runtime consumes.** Hermes reads the estate copy: skills install into the
   Hermes skills dir, routines run through ConvoDojo_Practice_Sparring, logs
   accrete under `logs/` per the schema, and the lattice refresh loop feeds
   back (consent-scoped).
4. **Revision loop.** Per campaign standing instruction: a cross-provider
   outside-judge round (Claude + one more API) reviews the harness for
   packaging completeness, discoverability, and governance coherence;
   critiques are integrated; the tree is re-verified (verify_phase7.py) and
   re-uploaded; continuity records are updated.
