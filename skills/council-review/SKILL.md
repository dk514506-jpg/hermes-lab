---
name: council-review
description: "Run Locus and the Council review on built work."
---

# Council Review (Locus + Council seats)

The user's QA apparatus for reviewing built work, from their hermes-lab
"Motivational Ecology" campaign. When asked to have "Locus and the Council"
review something, run it faithfully: read the real definitions, seat critique
+ Locus 7-check + adversarial outside-judge pass, then a prioritized revision
list and an honest score. The user values this over flattery — "honest,
evidence-based critique... over flattery"; lead with the sharpest findings,
never praise-pad.

## Read the definitions first (don't improvise)

- **Locus** — the Validator-Steward peer: `astral-research-harness/SKILL.md`
  §7.3a (repo `dk514506-jpg/hermes-lab`). Never executes work; adjudicates
  admissibility; verdicts ADMISSIBLE / REVISE / BLOCKED.
- **The 7 checks** — `faos_engine_extension.py` `locus_review_spec()`:
  route_valid · shadow_recorded · evidence_ladder_ok · state_lineage_ok ·
  quarantine_ok · close_complete · dissent_recorded.
- **Council seats** — `multi-agent-pipeline/SKILL.md` role table
  (single-home system): Scout (detect hidden patterns — finds what others
  miss), Researcher (receive the whole field — what does the system fail to
  capture), Orchestrator (sequence, define limits, authorize transitions —
  process and pipeline), Validator (rank evidence, refuse overclaiming —
  labels, junk in the source of truth), Builder (produce cleanly — code
  smells), Tester (cut weak claims — what breaks first).
- Full mapping + verdict grammar: `references/locus-and-council-definitions.md`.

## Process (what worked, 2026-08-08)

1. **Gather the artifacts and evidence.** The review document cites file:line
   for every finding (e.g. `schema.sql:33`, `price_refresh.py:27`). Run quick
   probes to confirm suspicions before writing them as findings (dead code,
   untracked secrets, unused tables).
2. **Seat findings, numbered F1..Fn.** One subsection per seat. Scout finds
   dead weight and duplicate concepts; Validator checks evidence labels AND
   whether the engine writes junk (placeholder rows, zero prices) and whether
   credentials are at risk; Tester orders "what breaks first" and asks what
   the committed gate does NOT check.
3. **Locus 7-check table** — each check → finding → ✅/❌, then verdict.
   REVISE is the honest default whenever P0s are open; explicit no-dissent
   counts as a recorded finding for `dissent_recorded`.
4. **Outside judge (adversarial, holistic).** One paragraph naming the
   structural pattern: "a well-built workbench on an unversioned, unbacked,
   unmonitored bench." Name the single most consequential finding (for the
   tracker it was: the master-KPI loop doesn't close — extraction measured,
   COGS not computed from it).
5. **Consolidated revision list** — P0 (structure: version control, secrets
   at risk, data-integrity loop, backup) / P1 (quality loop: committed tests
   over ceremony, schema consolidation, alerting, promised-but-unshipped
   automation) / P2 (craftsmanship). Every finding maps to an item.
6. **Score + re-score.** Initial score with named credits and debits; after
   the user approves implementation, record a revision-status table
   (finding → action → ✅ verified with evidence) and a re-score.
7. **Deliver** the review doc as a file under `reviews/` and link it via the
   managed-files URL (`/api/files/download?path=...`) — raw container paths
   don't render as links.

## Pitfalls

- The seats have REAL definitions — reading them takes ~2 minutes and makes
  the review faithful; hand-rolling a generic "AI council" loses the point
  and the user can tell.
- Keep every finding evidence-cited; the user verifies them.
- P0 must precede new builds — "the marketplace design inherits the bench
  problem." Structural debt first, features second.
- The revision list must be actionable (numbered, prioritized, mapped to
  findings) — the user implements from it directly.

## Rebuild-versus-patch gate

After a hostile review, explicitly decide whether the artifact should be patched
or whether its architecture must be retired while preserving its ideas. Use
**patch** only when defects are local and the runtime lineage, minimum use path,
safety route, evidence boundary, and state model are coherent. Recommend a
**kernel rebuild** when two or more load-bearing contradictions exist, such as:

- competing state lineages or unresolved source-of-truth precedence;
- contradictory required/optional minimums;
- safety language without an explicit bypass route;
- declared measurement/firewall rules without a runnable data boundary;
- hidden thresholds inside a count-free or anti-metric ethic;
- semantic taxonomies that interpret experience before description;
- burden claims based on estimates rather than a tested minimum path.

When rebuilding, preserve the strongest concepts in a short design note, but do
not carry the old document's architecture forward by accretion. Define one
canonical lineage, a minimum kernel, explicit safety-first routing, reversible
states including `unresolved` and `support`, and a separate research protocol.
Treat the old artifact as an archive/source of hypotheses, not as the runtime.

## Minimal-kernel acceptance gate

For a rebuilt human-facing instrument, require a fresh-reader exercise before
adding cards or theory. The exercise must test: use without the reference
manual; safety uncertainty as a hard bypass; ambiguous/multiple state handling;
legitimate pause/support/unresolved exits; burden/extra-work perception; and
carry-forward state without hidden records. A structural verifier may check the
kernel's required sections and forbidden legacy mechanisms, but it cannot
substitute for this live usability exercise.
