## Summary

Rebase the Motivational Ecology campaign's cosmotechnic and human-agency documentation on the current Monstare v5 position.

### Changed

- Adds `docs/campaign/Monstare_Cosmotechnic_V5_Rebase.md`.
- Rewrites the campaign overview to distinguish the verified legacy estate from the unvalidated Monstare runtime prototype.
- Rewrites Phase 13 around the v5 Kernel's safety-first, single-lineage, explicit-state boundary.
- Updates `skills/motivational-ecology/SKILL.md` with current safety, user-owned telos, evidence, cosmotechnic, and capability-boundary rules.
- Uploads pertinent local skills:
  - evidence-matrix-orchestration
  - evidence-matrix-charting-qc
  - council-review
  - continuity-package-authoring
- Adds `scripts/verify_monstare_v5_rebase.py`.

### Current boundary made explicit

This branch does not claim that the Motivational Ecology estate is a validated human-facing intervention. Deterministic demonstrations are not human evidence; declared safeguards are not automatically enforced safeguards; FAOS claim clearance does not authorize use toward a person.

## Verification

- `python scripts/verify_monstare_v5_rebase.py` — PASS
- Local source anchors reviewed: canonical matrix, Epithet Register, Stakes Register, Open Charges Register, v4 Council/Locus reviews, and v5 Kernel.

## Review note

This is a documentation/harness rebase. No external service deployment or live human-facing session was performed by this change.

## Branch

`docs/cosmotechnic-v5-rebase`

## Commit

`23ca710`

## Proposed next step after review

Exercise the Monstare v5 Kernel on one concrete component with a fresh reader, including safety-uncertainty and ambiguous/multiple-state cases, before expanding the runtime harness.