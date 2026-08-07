# Canonical Pattern Notes (HiSkill 9-file packages)

Condensed from the Motivational Ecology Agent Architecture ecology docs
(Phase 1 → Phase 3). Verify against the primary docs when in doubt.

## Where the pattern lives
- Canonical example rendered verbatim: `CONTEXT_BUNDLE_03_Example_Skill_Human_Empowerment_Boundary.txt`
  (9 files delimited by `===== FILE n/9: <name> =====`).
- Master rule (reconstruction note in that bundle): "keep this 9-file shape and
  swap in that skill's ROLE, AtomicOps, State Variables, Edges, preserved-decision,
  and BLOCK condition."
- `SKILL.md` standard: research plan §8 (16 sections).
- Phase 1 grounding: `Foundation_Matrix.md`, `Theory_to_Routine_Interface.md`.
- Graph seed: `Phase3_Skills/skill_graph_index.json` (node layers/roles + edge
  candidates with VERIFIED/RECONSTRUCTED flags).

## Evidence discipline
- VERIFIED = directly retrieved from cited source; RECONSTRUCTED = inference for
  agent-applicability (labeled); UNVERIFIED = not independently confirmed.
- Version/witness conflicts are ENCODED, never harmonized (e.g., TDF 12-vs-14
  domains, Michie 2005 vs Cane 2012; COM-B motivation from two traditions).
- Descriptive ≠ predictive: COM-B/TDF are organizing taxonomies; treat every
  diagnosis-to-selection step as hypothesis generation (Valens combinatorial
  retrospection: multiple routes to one target are NOT independent confirmations).

## Per-file conventions
- `SKILL.md`: H2 title; 16 `###` sections in fixed order (see umbrella SKILL.md).
- `skill_node.json`: canonical fields (id, name, version, purpose,
  applicability_states, expected_state_changes, representative_examples,
  failure_hints, support_count, source_influences) PLUS layer, role, inputs,
  outputs, state_read, state_write, triggers, completion_conditions when the
  task spec requires them. id must equal the directory name, PascalCase —
  matches `skill_graph_index.json` (the canonical example's lowercase ids do
  not survive graph joins).
- `atomic_ops.json`: id, name, template (`op | arg={arg}`), description,
  arguments, inputs, outputs, guardrails. Guardrails carry the
  empowerment/atrophy/quarantine rules per op (e.g., "Medical advice
  hard-blocked", "Social data opt-in only", "Identity-level claims require
  explicit user confirmation").
- `edge_map.json`: edges[{source, target, type, order, rationale, flag}].
  Five kinds only. INVARIANT: decomposes_to targets == atomic_ops ids.
- `state_schema.json`: {var: {type, values|enum, example}}; hypothesis-status
  booleans default true ("never emitted as fact").
- `examples.md`: "## <Skill> Examples" + "### Example N: <short title>" with
  Task / Selected AtomicOps / State transitions / Output pattern (+ sparring
  examples for practice-mode skills).
- `support_ops.md` / `recovery_ops.md`: "## Support/Recovery Operations" +
  "### <Op>" paragraphs; recovery_ops ends with a de-ossification path note.
- `evaluation_notes.md`: fidelity checks + empowerment/atrophy/quarantine checks
  + VERIFIED evidence anchors + calibration loop.

## Open item (Phase 4)
Seed `skill_graph_index.json` expresses COMB→TDF refinement as skill-to-skill
`decomposes_to`; canonical packages reserve `decomposes_to` for AtomicOps and
carry skill-to-skill refinement as `can_follow`/`supports`. Reconciliation
decision belongs to Phase 4 graph integration — do not break the canonical
shape to force agreement.

## Typical build cadence
Grounding reads → mkdir → SKILL.md first (fixes op list/state/edges) → JSON
batches → md companions → verifier run → seed-index agreement note.
Package totals observed: 10–14 ops, 24–33 edges (aligned estates run wider
due to cross-package mirrors; see estate-conventions-and-verification.md).
