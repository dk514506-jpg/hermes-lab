---
name: hiskill-package-authoring
description: Use when building or QA'ing 9-file HiSkill skill packages.
---

# HiSkill Package Authoring

### Purpose
Build and verify complete 9-file HiSkill skill packages: `SKILL.md` plus eight
companion files that make a method graph-operable (AtomicOps, typed edges, state
schema, support/recovery ops, evaluation). This is the Phase 3 "method-to-skill
translation" workflow of the Motivational Ecology Agent Architecture (and any
HiSkill-style estate that follows the same master-document pattern).

### Trigger Conditions
- User asks to build a skill package "per the canonical pattern" or "as per the
  master document" (e.g., `COMB_Behavioral_Diagnosis`, `SDT_Need_Support_Check`,
  `MI_Ambivalence_Conversation`, ...).
- User asks to QA or verify existing packages in a Phase3_Skills directory.
- Extending the skill graph (adding edges/skills) where skill_node.json and
  edge_map.json must stay in agreement with `skill_graph_index.json`.

### Grounding Discipline (non-negotiable)
Read these Phase 1 artifacts BEFORE writing anything:
1. The canonical example package (the 9-file pattern rendered verbatim).
2. `Foundation_Matrix.md` — per-framework VERIFIED evidence, critiques, limits.
3. `Theory_to_Routine_Interface.md` — the AtomicOp/edge candidate registers and
   per-construct rows for Empowerment boundary / Atrophy check / Quarantine.
4. The research plan §8 — the `SKILL.md` 16-section standard; §6 for the
   per-Layer required outputs (extra-file policy, below).
5. `Construct_Map.md` — tension register (autonomy vs directive technique →
   empowerment boundary arbitrates) + "Implications for the Skill Graph".
6. `Recent_Evidence_Digest.md` — post-2024 evidence by search area; each skill
   cites its grounding with author-year keys (Beacock 2026, Bastani 2025, Lim 2025…).
Rules:
- Every construct, op, and edge must trace to a register row or matrix cell.
- Attach `VERIFIED` / `RECONSTRUCTED` flags to evidence-dependent claims; encode
  witness conflicts as metadata, never harmonize them (e.g., TDF 12-vs-14).
- Every skill carries the empowerment/atrophy/quarantine triad: what the agent
  may do automatically vs what stays with the user; what capability must not
  atrophy; what must not be applied without user confirmation.

### The Nine-File Shape
```
SKILL_NAME/
  SKILL.md
  skill_node.json
  atomic_ops.json
  edge_map.json
  state_schema.json
  examples.md
  support_ops.md
  recovery_ops.md
  evaluation_notes.md
```
The 9 core files are the floor — never fewer. Extra files ARE allowed when the
plan §6 layer outputs specify them for that skill's layer (Layer 1 lattice: 6
artifacts; Layer 3 empowerment: 5; Layer 5 dojo: 7). evaluation_notes.md should
list the layer artifacts as checks. Verifiers must run in "extras allowed" mode
(scripts/verify_package.py does: it lists extras as INFO, not FAIL).

### SKILL.md Section Standard (16 sections, H2 title)
Purpose, Trigger Conditions, Inputs, Outputs, State Variables, Atomic Operations,
Typed Edges, Empowerment Boundary, Learnability / Skill-Atrophy Check,
Motivational-Lattice Interface, Conversational / Practice Mode, Guardrails,
Failure Modes, Recovery Operations, Examples, Handoff Notes.
Heading level DIVERGES across sources: the research plan §8 renders sections as
`##`, the verbatim canonical bundle renders them as `###`. Either level is
accepted; verifiers must match both (`## X` or `### X`).

- `skill_node.json`: id, name, version, layer, role, purpose, inputs{required,
  optional}, outputs{primary, secondary}, state_read, state_write, triggers,
  completion_conditions, applicability_states, expected_state_changes,
  representative_examples, failure_hints, support_count, source_influences.
- `id` casing: PascalCase, matching the directory name AND
  `skill_graph_index.json` (the canonical example bundle uses lowercase, but
  the built estate and the seed index use PascalCase — Phase 4 graph joins
  depend on it). Grep the package for stale lowercase ids after normalization.
  Optional extensions: layer, role (the seed index carries both), inputs{required,
  optional}, outputs{primary, secondary}, state_read, state_write, triggers,
  completion_conditions. Verifiers must NOT require the extensions — requiring
  them fails canonical-built packages.
- Canonical floor for each op in `atomic_ops.json`: id, template
  (`op | arg={arg}`), description, arguments. Optional extensions: name, inputs,
  outputs, guardrails. Template strings must mirror the arguments dict.
- `edge_map.json`: skill_id + edges[{source, target, type, order}] with
  `rationale` on every edge and `flag` (VERIFIED/RECONSTRUCTED + source) on
  theory-derived edges.
- `state_schema.json`: each variable {type, values/enum, example}.

### Typed Edges & Invariants
- Only 5 edge kinds: decomposes_to, can_follow, compatible_with, supports,
  recovers_with.
- INVARIANT: the set of `decomposes_to` targets in edge_map.json must EXACTLY
  equal the set of atomic_ops ids (one decomposes_to per op, in order).
- Skill-to-skill refinement (e.g., COMB→TDF) is carried as `can_follow` /
  `supports`, NOT as skill-level `decomposes_to` — the canonical package
  reserves `decomposes_to` for AtomicOps. The seed `skill_graph_index.json`
  may express it as skill-level decomposes_to; that collision is a Phase 4
  reconciliation item, not a reason to break the canonical shape.
- DIRECTION SEMANTICS: `(A→B, can_follow)` reads "B can follow A" — the SOURCE
  precedes the target (register: TDF→PPS = "barrier grid → practice design").
  Write the rationale FIRST, then make the direction agree with it. The
  SKILL.md `can_follow` prose lists only OUTGOING edges. Errors made in
  practice: PPS can_follow encoded backwards (PPS→TDF instead of TDF→PPS),
  SDT→COMB instead of COMB→SDT, MI→TDF instead of TDF→MI, SDT→MLG instead of
  MLG→SDT. `compatible_with` is near-symmetric (direction less critical);
  can_follow pairs CAN be genuinely bidirectional (COMB authors COMB→MI with
  a note that the register's MI→COMB is also valid).
- MIRRORING NORM: a cross edge between two built packages appears as the
  IDENTICAL (source, target, type) tuple in BOTH packages' edge_map.json
  (COMB/TDF do this). When a legacy package already authored a tuple involving
  your skill (e.g., COMB→SDT, TDF→SDT, TDF→MI, COMB→PPS supports), mirror it
  verbatim into your map; author your own outgoing edges in both maps. Run a
  mirror audit over all built packages after any edge change.
- recovers_with direction — RESOLVED in Phase 4 (2026-08-06): for CROSS-SKILL
  edges, source = the skill being recovered, target = the recovery provider
  (matches English "A recovers with B"; matches the seed index). Example:
  `MI_Ambivalence_Conversation -> SDT_Need_Support_Check` = MI's discord is
  repaired via SDT's autonomy support. For INTERNAL edges (recovery op →
  skill), source = the recovery op, target = the skill it repairs (e.g.,
  `Return_To_Spirit -> MI_Ambivalence_Conversation`). Every recovers_with
  edge carries a `kind` discriminator: `cross-skill` or `internal`. This
  supersedes the pre-Phase-4 convention (provider→skill) that the first build
  used; packages were normalized in Phase 4 and verify_packages.py now checks
  agreement direction-sensitively.

### Build Workflow
1. Read the four grounding artifacts (above).
2. `mkdir -p <Phase3_Skills>/SKILL_NAME/`.
3. Write SKILL.md first (it fixes the op list, state vars, and edges that the
   JSON files must mirror). Then skill_node.json + atomic_ops.json, then
   edge_map.json + state_schema.json, then the three md companions.
4. Batch independent `write_file` calls in the same turn (2–4 files per batch).
5. Verify (below). Fix any drift before reporting.

### Verification
Run the portable verifier — it checks core-9 presence (extras allowed), JSON
parse, canonical floor fields, edge/op consistency, both SKILL.md heading
levels, and that every recovers_with source resolves to a defined op heading or
the skill's own id:
```
python3 scripts/verify_package.py <dir1> <dir2> ...   # or: run in the Phase3_Skills dir to scan all packages
```
When working in the Ecology tree, ALSO run the project verifier
`docs/Ecology/Foundation/Phase3_Skills/verify_packages.py` (must exit 0) — it
adds YAML parse, edge-endpoint resolution against known skills, and
direction-sensitive seed-index agreement (Phase 4: all ids PascalCase, no
snake-case mapping needed).
Then cross-check flagged edges against `skill_graph_index.json` (seed agreement;
skip edges where BOTH endpoints are unbuilt skills) and confirm the skill_node
`layer`/`role` match the seed index.

Verifier pitfalls (Phase 4-5 lessons):
- **atomic_ops.json shape is NOT stable across the estate.** It may be a bare
  list OR a dict with an `ops` (or `atomic_ops`) key (schema 0.2 — ConvoDojo
  is dict-form after its Phase-4 rewrite). A verifier that hardcodes
  `json.load(...)["id"]` crashes on dict-form files (real defect: the estate
  verifier tracebacked on ConvoDojo until given an `ops_of(pkg)` helper).
  Loader: `d = json.load(open(p)); ops = d["ops"] if isinstance(d, dict) else d`.
- **Seed-index agreement must be direction-sensitive for directed edge types.**
  `recovers_with`, `can_follow`, `decomposes_to`, `supports` compare as exact
  (source, target) tuples; only `compatible_with` may use set equality.
  Direction-blind checks false-PASS reversed edges — the exact weakness the
  architecture critic flagged; fixed in the Phase 4 verifier revision.
- **Use the single entry point for cross-phase verification:**
  `council_notes/verify_all.py` chains every per-phase verifier + JSON parses
  + py_compile in one process with one exit code. A pile of separate verifier
  runs invites "re-run for evidence" churn.

### Build Status (2026-08-06, updated Phase 4)
Phase3_Skills contains all 8 first-build packages: Human_Empowerment_Boundary
(Layer 3, 14 files), COMB_Behavioral_Diagnosis (14 ops / 27 edges),
TDF_Barrier_Facilitator_Grid (10 ops / 23 edges), SDT_Need_Support_Check
(10 ops / 29 edges), MI_Ambivalence_Conversation (14 ops / 34 edges —
focusing ops added), Proximal_Practice_Selector (9 ops / 31 edges),
Motivational_Lattice_Generator (Layer 1, 15 files, 12 ops), ConvoDojo_
Practice_Sparring (Layer 5, 16 files, 13 ops — safety op added). All nodes
PascalCase, all boundary_gate=required. Seed index v1.0 marks all 8 "built";
Phase 4 added lattice_index.json, skill_lattice_interface.md,
insight_trigger_policy.md, T2R_traceability.json. Deferred (3):
Material_Arrangement_Scan, Feedback_Ecology_Map, Autopoietic_Boundary_Check —
edges to them are quarantined until built. Full table:
references/ecology-build-status.md

### Pitfalls
- The `terminal` tool REJECTS inline heredoc Python that contains `&` (e.g., set
  intersection `a & b`), misreading it as shell backgrounding. Write the script
  with `write_file` and run `python3 script.py` — never inline heredocs for
  scripts containing `&`.
- Section headings in SKILL.md must be exactly `### <Name>` (H2 title per the
  canonical pattern) — the verifier greps for them.
- Don't enumerate large inventories (e.g., all 84 TDF constructs) from memory;
  reference the canonical source and carry representative constructs only.
- Keep skill_node.json, edge_map.json, and skill_graph_index.json in agreement
  after any edge change; note the agreement in the summary.
- Per-package totals land ~12–14 ops, ~24–28 edges (aligned estates run wider,
  29–33 edges, due to cross-package mirrors); wildly off counts usually mean a
  file was missed or ops were duplicated.
- A shared estate verifier (`Phase3_Skills/_verify_skills.py`) may predate newer
  packages and encode a DIFFERENT schema than the canonical bundle. Read the
  verifier AND one conforming package (e.g., COMB_Behavioral_Diagnosis) to
  extract the real estate schema — it is the UNION of canonical + extension
  fields — before writing. After building, extend the verifier's SKILLS list
  (with a comment naming non-conforming packages and why), and re-run it plus a
  supplementary audit: 16 sections present AND in order, no duplicate edge
  tuples, decomposes_to↔ops coverage, mirror audit across packages.
- Multi-agent estates: packages in the same directory may be built by different
  agents. Edit ONLY your own packages; mirror legacy-authored edge tuples into
  yours; never rewrite another package's files — flag their pending alignment
  instead (e.g., ConvoDojo/MLG are canonical-9 but lack extension fields and
  use lowercase self-ids in their own edge_maps).
- Every recovers_with source in edge_map.json must resolve: to a defined
  `### Name` heading in recovery_ops.md/support_ops.md, or to the skill's own id
  (seed-convention cross-skill edge). An undefined source fails verification —
  this was a real defect caught post-build (edge referenced an op that
  recovery_ops.md never defined).
- Op headings must be machine-resolvable: `### Return_To_User_Authority`, NOT
  `### Return_To_User_Authority (via X)` — parentheticals break `^### (.+)$`
  parsing. Put qualifiers in the body.
- Seed direction convention — RESOLVED in Phase 4 (2026-08-06): the seed index
  and ALL package edge_maps now agree on `source`/`target` keys (no more
  from/to) and on recovers_with direction (source=recovered skill, target=
  recovery provider) with kind discriminators. Phase 4 also normalized node
  ids to PascalCase matching dirnames, renamed TDF's `binding_constraint` to
  `binding_constraint_comb`, quarantined edges to deferred skills, and
  declared `governance.boundary_gate: required` on every skill_node.json.
  New builds must follow the Phase 4 conventions; verify with
  `council_notes/verify_all.py` (single entry point chaining all verifiers).
- Case normalization — Phase 4 (2026-08-06) normalized all node ids to
  PascalCase matching directory names; the seed index and every package now
  agree. New builds: use PascalCase skill ids matching the dirname; cross-
  package checkers no longer need snake-case mapping (legacy PASCAL2SNAKE
  maps in old verifiers were removed).
- Ground truth first: skill examples and the reference build-status table can
  lag the actual tree. List the Phase3_Skills directory before assuming what
  exists; a package named in examples may not be present yet (or may have been
  superseded by Phase 4 normalization).

### Support Files
- `references/canonical-pattern-notes.md` — condensed knowledge bank: canonical
  pattern locations, field conventions, evidence discipline, open items.
- `references/estate-conventions-and-verification.md` — union schema, id
  casing, edge direction semantics, cross-package mirroring, verifier workflow.
- `references/ecology-build-status.md` — which packages exist in Phase3_Skills,
  layer-extras mapping (plan §6), seed-edge agreement table, Phase 4 open items.
- `scripts/verify_package.py` — statically re-runnable package verifier.

### Examples
Building all five conforming packages end-to-end:
`COMB_Behavioral_Diagnosis` (14 ops / 28 edges), `TDF_Barrier_Facilitator_Grid`
(10 ops / 24 edges), `SDT_Need_Support_Check` (10 ops / 29 edges),
`MI_Ambivalence_Conversation` (12 ops / 33 edges), `Proximal_Practice_Selector`
(9 ops / 31 edges): grounding reads → SKILL.md first → JSON batches → verifier
pass (exit 0) → seed-index agreement note (1 flagged match per package) →
mirror audit. See references/canonical-pattern-notes.md for field details and
references/estate-conventions-and-verification.md for edge semantics, id
casing, and the verification workflow.
