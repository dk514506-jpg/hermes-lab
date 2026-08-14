# Locus & Council — definitions and verdict grammar

Source of truth: the user's hermes-lab repo (`dk514506-jpg/hermes-lab`,
clone at `/opt/data/hermes-lab`; runtime bundle snapshot at
`/opt/data/bundle-fix`). Read the live files before each review — they are
the canonical definitions.

## Locus — the Validator-Steward peer

- Where: `skills/astral-research-harness/SKILL.md` §7.3a (and FAOS §11.5,
  `skills/faos-pipeline-architecture/SKILL.md` Pitfalls section).
- Role: dedicated validator-steward; **never executes work** — adjudicates
  admissibility and transition integrity.
- Reviews: route validity, shadow promotions, evidence-ladder compliance,
  state-lineage edges, quarantine tiers, instrumented-close completeness,
  dissent records.
- Verdicts: `ADMISSIBLE` / `REVISE` / `BLOCKED`.

## The 7 checks (locus_review_spec)

From `faos_canonical/faos_engine_extension.py` (also
`Phase10_Integration/faos_engine_extension.py`), method `locus_review_spec`:

1. `route_valid` — primary path exists and is licensed
2. `shadow_recorded` — the shadow (alternative path) was monitored; an
   explicit no-shadow finding satisfies this
3. `evidence_ladder_ok` — no skipped evidence levels
4. `state_lineage_ok` — no prohibited edges / no skipped lineage
5. `quarantine_ok` — no non-operational tier running in runtime
6. `close_complete` — all passes populated (for our reviews: no missing
   essential passes — tests, backup, alerting)
7. `dissent_recorded` — dissent recorded, or an explicit no-dissent finding

Verdict mapping used in the 2026-08-08 tracker review: 3/7 ❌
(quarantine/state-lineage via placeholder-price writes, close_complete via
missing tests/backup/alerting) → REVISE.

## Council seats (reconciled single-home mapping, 2026-08-07)

From `skills/multi-agent-pipeline/SKILL.md` role table + reconciled
`skills/astral-research-harness/SKILL.md` §7.1 (arcs start at home
signature — one planet, one home):

| Seat | Home signature | Mandate in a review |
|---|---|---|
| Scout | Mercury/Scorpio → Jupiter/Moon | Detect hidden patterns; find what others miss (dead code, unused tables, duplicate concepts) |
| Researcher | Jupiter/Moon in Pisces → Venus/Taurus | Receive the whole field; preserve source texture — what does the system FAIL to capture? |
| Orchestrator | Saturn/Capricorn → Sun/Capricorn | Sequence; define limits; authorize transitions — pipeline order, deferred work, gates |
| Validator | Venus/Taurus → Saturn/Capricorn | Rank evidence; define limits; refuse overclaiming — labels, junk writes, credential hygiene |
| Builder | Sun/Capricorn → Mars/Capricorn | Produce finished output; execute cleanly — code smells, duplication, fragile cleverness |
| Tester | Mars/Capricorn → Venus/Taurus | Cut weak claims; preserve quality — order "what breaks first"; what the gate does NOT check |

Plus an **outside judge** (adversarial, holistic pass) — in the user's
campaign this is a separate model/role ("DeepSeek outside judge"); in
practice, write it as a distinct critical voice naming the structural
pattern and the single most consequential finding.

## Review document shape (the format that worked)

```
# Council Review — <system> (Phases …)
Reviewers: Council (Scout · Researcher · Orchestrator · Validator · Builder
           · Tester) + Locus (7-check) + outside judge (adversarial)
Date / Artifacts reviewed (paths)

0. Method — one paragraph; verdict line up front (REVISE · score)
1. Seat findings — F1..Fn, each evidence-cited (file:line)
2. Locus 7-check verdict — table of the 7 checks → ✅/❌ → verdict
3. Outside judge (adversarial, holistic) — the "workbench vs bench" pass
4. Consolidated revision list — P0 / P1 / P2, every finding mapped
5. Score — credits and debits named explicitly
6. Revision status (added after implementation) — finding → action →
   ✅ verified; re-score
```

Deliver under `reviews/` in the target repo; link via
`/api/files/download?path=<repo-relative-path>` (dashboard managed-files).
