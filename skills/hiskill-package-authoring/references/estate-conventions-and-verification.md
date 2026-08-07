# Estate Conventions & Verification (extending an existing HiSkill estate)

Rules discovered while building the second wave of packages
(SDT_Need_Support_Check, MI_Ambivalence_Conversation, Proximal_Practice_Selector)
into an estate where COMB/TDF already existed. Canonical bundle ≠ estate ground
truth: read what is actually BUILT before writing.

## The estate schema is a UNION
The verbatim canonical example (CONTEXT_BUNDLE_03) uses a minimal schema, but
the built estate (COMB/TDF, enforced by `_verify_skills.py`) uses canonical
fields PLUS extension fields:
- `skill_node.json` adds: `layer` (int, from seed index), `role` (string),
  `inputs{required, optional}`, `outputs{primary, secondary}`, `triggers[]`,
  `completion_conditions[]`, `state_read[]`, `state_write[]`.
- `atomic_ops.json` ops add: `name` (Title Case), `inputs{arg: type}`,
  `outputs{...}`, `guardrails[list]` (carry the empowerment/atrophy/quarantine
  rule per op).
- `edge_map.json` edges carry: `rationale` on EVERY edge + `flag`
  ("VERIFIED (source)" / "RECONSTRUCTED (...)" provenance) on theory-derived
  edges; decomposes_to edges also carry `order`.
Inspect an existing conforming package (COMB_Behavioral_Diagnosis) and the
verifier's NODE_REQ/OP_REQ to extract the exact union before writing.

## id casing: PascalCase
`skill_node.json` id == directory name == `skill_graph_index.json` node id
(PascalCase, e.g. `SDT_Need_Support_Check`). The canonical example uses
lowercase ("human_empowerment_boundary") but the built estate and the seed
index use PascalCase — Phase 4 graph joins depend on it, and the estate
verifier asserts `node.id == dirname`. After normalizing, grep the package for
stale lowercase references.

## Edge direction semantics
`(A -> B, can_follow)` reads "B can follow A": the SOURCE precedes the target.
Evidence from the estate's own maps:
- `(COMB -> TDF, can_follow)` "14-domain grid refines the six-component profile"
- `(TDF -> PPS, can_follow)` "barrier grid -> proximal practice design"
- `(TDF -> MI, can_follow)` "Intentions/Emotions/Behavioural-Regulation barriers -> evocation"
Errors made in practice (all caught by writing the rationale first, then
checking direction):
- PPS can_follow encoded backwards: PPS->TDF instead of TDF->PPS.
- SDT->COMB instead of COMB->SDT (COMB already authored COMB->SDT).
- MI->TDF instead of TDF->MI (TDF already authored TDF->MI).
- SDT->MLG instead of MLG->SDT (MLG authors MLG->SDT supports/compatible_with).
Rules: the SKILL.md `can_follow` prose lists only OUTGOING edges; incoming
predecessors live in edge_map.json as mirrors, not in the prose list.
`compatible_with` is near-symmetric (direction less critical). can_follow
pairs CAN be genuinely bidirectional: COMB authors `(COMB->MI, can_follow)`
with a note that the register's `(MI->COMB)` is also valid — mirror both when
the counterpart says so.

## Cross-package mirroring norm
Every cross edge between two built packages appears as the IDENTICAL
(source, target, type) tuple in BOTH packages' edge_map.json (COMB/TDF do
this). When a legacy package already authored a tuple involving your skill
(e.g., COMB->SDT, TDF->SDT, TDF->MI, COMB->PPS supports, TDF->PPS supports),
mirror it verbatim into your map. Author your own outgoing edges in both maps.
Verify with a mirror audit over all built packages; a package whose counterpart
is not yet built (HEB, Feedback_Ecology_Map, Material_Arrangement_Scan,
Autopoietic_Boundary_Check, Post_Close_Calibration_Debrief) cannot mirror —
leave those one-sided.

## recovers_with directionality (open item)
Canonical convention: provider -> skill — the recovery op or repairing skill
is the source, the skill being recovered is the target:
- `(Return_To_Spirit -> MI_Ambivalence_Conversation, recovers_with)`
- `(SDT_Need_Support_Check -> MI_Ambivalence_Conversation, recovers_with)` = SDT
  repairs MI's discord
The seed `skill_graph_index.json` records the reverse tuple
`(recovers_with, MI, SDT)`. Encode per canonical; document the divergence as a
Phase 4 open item. Do NOT mirror a recovers_with edge into the target's map
when that would read as "target recovered by source" (semantic inversion).

## Shared verifier workflow
`Phase3_Skills/_verify_skills.py` may predate newer packages and encode a
schema (NODE_REQ/OP_REQ) that only older packages satisfy. Workflow:
1. Read the verifier + one conforming package to extract the REAL schema.
2. Build to the union schema (above).
3. Extend the verifier's SKILLS list to include your packages, with a comment
   naming non-conforming packages and why (they may be canonical-9 in shape
   but lack the extension fields).
4. Re-run it after every mutation; then run a supplementary audit:
   - all 16 SKILL.md sections present AND in order
   - no duplicate (source, target, type) tuples
   - decomposes_to targets == atomic_ops ids (verifier does this)
   - mirror audit: every cross edge among built packages mirrored in both maps;
     every legacy-authored tuple involving your skills present in your maps
5. Seed-index agreement: flagged edges whose (type, source, target) matches a
   skill_graph_index.json edge count as agreement (1 match per package
   observed; MI reaches 2 once COMB->MI is mirrored).

## Multi-agent ownership discipline
Packages in Phase3_Skills may be built by different agents. Edit ONLY your own
packages. When a counterpart authors a shared edge, mirror it on your side;
never rewrite another package's files. Flag their pending alignment instead:
as of the second wave, ConvoDojo_Practice_Sparring and
Motivational_Lattice_Generator are canonical-9 but lack the extension fields
and use lowercase self-ids in their OWN edge_maps while referencing siblings
in PascalCase — they need schema alignment + id normalization before joining
the estate verifier.
