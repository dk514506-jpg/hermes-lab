# Material Arrangement Scan — Evaluation Notes

## What verified (deterministic, no LLM)

- Package schema conformance: skill_node.json (layer 2, role
  environmental_scan), 4 atomic ops, edge_map (4 internal + 2
  compatible_with), state_schema (8 keys), 9-file package set.
- Atomic op schema: every op carries id/name/template/description/
  arguments/inputs/outputs/guardrails.
- Boundary discipline: no op proposes meaning imposition; identity-level
  reframes gated to explicit-confirmation candidates (Phase 11
  confirmed-Q2 path).
- T2R register: scan_materials, scan_meanings, detect_shared_elements,
  design_novelty_into_routine flipped to instantiated.
- skill_graph_index: COMB→MAS and TDF→MAS compatible_with edges
  un-quarantined (Phase 12 activation).

## What remains unverified (honest ceiling)

- Live-LLM behavior of the ops (absence register blocks runtime sessions;
  the estate's runtime is architectural).
- Real practice-theory synthesis beyond the estate's T2R rows (the lens
  is carried as the estate carries it; deeper synthesis is a wiki-side
  activity, out of package scope).
- The arrangement proposals' real-world effect (needs adoption data —
  calibration log pattern thresholds).

## Stand-in limits (Phase 12 revision round, judge W5)

- scan_materials parses the environment description by splitting on ";" —
  a deterministic stand-in for real text parsing (production would parse
  the real environment text; disclosed in code).
- Material locations are hardcoded "described" — real location extraction
  is LLM-side.
- detect_shared_elements detects overlaps only when a practice_graph with
  >= 2 practices is supplied; the examples that show bundle detection
  ("shoes serve BOTH the walk and decompression practices") are
  ILLUSTRATIVE of the intended capability, beyond what the deterministic
  executable performs with a single-practice inventory.
- Edge count: the package has 9 edges (4 decomposes_to + 3 feeds + 2
  compatible_with), not 6 as an earlier draft of this note claimed.

## Evaluation checklist (per estate convention)

- Did the package stay descriptive (never prescriptive on meaning)? — yes,
  boundary rule.
- Were identity-level reframes confirmation-gated? — yes, candidates only.
- Did the package avoid imposing arrangements? — yes, proposals are
  suggestions.
