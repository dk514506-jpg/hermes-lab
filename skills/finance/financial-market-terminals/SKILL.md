---
name: financial-market-terminals
description: "Build auditable market terminals and arbitrage screens."
version: 1.0.0
metadata:
  hermes:
    tags: [finance, market-data, arbitrage, factset, portfolio-analytics, provenance, point-in-time]
---

# Financial Market Terminals

## When to use

Use when building a small, auditable market-intelligence or arbitrage-analysis system modeled on professional terminals such as FactSet, especially when the underlying market is thin, heterogeneous, or not fully machine-readable.

## Product framing

Do not start by building a generic price tracker or claiming risk-free arbitrage. Identify the professional workflow being replicated:

1. **Instrument master** — normalized identity, variants, venue, currency, and condition/share class.
2. **Quote board** — source-separated observations with freshness, provenance, and confidence.
3. **Opportunity screener** — net executable edge after all costs, not headline spread.
4. **Portfolio/inventory analytics** — cost basis, exposure, realized/unrealized value, and aging.
5. **Attribution** — explain what created or destroyed P&L.
6. **Control room** — stale data, unresolved identifiers, source conflicts, missing legs, and blocked calculations.

For Pokémon, instrument identity is card + set + number + variant + language + condition. Never collapse condition or print variant into a generic card name.

## Architecture

Keep four layers distinct:

- **Raw immutable:** original payload/file, source record ID, sequence, hash, and capture metadata.
- **Canonical:** normalized instruments, quotes, trades/listings, buylist quotes, sales, fees, and events.
- **Analytics:** spreads, net edge, liquidity, attribution, risk, and portfolio values.
- **Presentation:** quote board, screeners, reports, and alerts.

Corrections and backfills are new records or explicit revisions. Never destructively rewrite raw history.

## Time and point-in-time correctness

Never use a single generic timestamp. Prefer:

- `event_ts` — when the market event occurred
- `source_ts` — when the source published it
- `receive_ts` — when capture received it
- `ingest_ts` — when internal ingestion occurred
- `available_ts` — when the record could affect a decision
- `valid_from/valid_to` — economic validity
- `known_from/known_to` — the knowledge interval for revisions

Enforce:

```text
available_ts <= decision_ts
```

Derived opportunities must retain input observation IDs, decision time, strategy version, calculation-run ID, and expiry. This prevents hindsight contamination and makes output replayable.

## Opportunity economics

```text
net_edge = sell_proceeds
         - buy_price
         - marketplace_fees
         - shipping
         - payment_fees
         - taxes
         - condition_or_slippage_reserve
         - holding_cost
```

Apply costs to both legs. Model asynchronous fills, liquidity, quantity limits, stale quotes, condition mismatch, and execution failure. A spread is not an executable opportunity until the required legs are fresh, condition-matched, and sufficiently sourced.

## Assumption discipline

When live data is unavailable, build the artifact anyway but label every assumption. Use `VERIFIED`, `ASSUMED`, and `UNVERIFIED` provenance states. Do not fabricate buylist quotes, liquidity, source timestamps, or arbitrage scores. Prefer a visible `BLOCKED` state to false precision.

Static MVPs should show historical/manual values as indicative only, missing asks/bids as explicit blanks, zero executable opportunities when inputs are missing, and the next concrete data action needed to unblock the screen.

## Completion gates and milestone language

When reviewing whether a market terminal is "complete," distinguish the deliverable explicitly:

- **Capture/accounting MVP:** purchases, extractions, sales, expenses, reconciliation, reports, backups, and committed tests.
- **Static terminal prototype:** provenance-aware schema plus presentation screens with honest `ASSUMED`/`BLOCKED` states.
- **Live market terminal:** real source observations, recurring ingestion, maintained instrument universe, freshness/conflict controls, and non-blocked two-sided quotes.
- **Operational decision system:** live terminal plus opportunity screener, inventory/portfolio, attribution, alert delivery, and observed execution feedback.

Do not call a seed-data Quote Board a live tracker. State what is complete, what remains blocked, and why. Prioritize the next milestone by decision value: real source ingestion and business-specific buylist/realized-sale data come before expanding decorative screens. A practical readiness review should check: (1) current repository/artifact state, (2) real-vs-seed data coverage, (3) recurring refresh path, (4) executable bid/ask availability, (5) terminal screens, (6) alert destination, and (7) packaging/version-control consistency.

## Field-data ingestion and decision experiments

When live quotes are unavailable, build the operator-facing capture loop rather than only a static screen:

1. Maintain a condition/variant-separated ticker universe with stable identifiers, card number, printing, language, active status, and notes.
2. Accept dated observations with nullable market and buylist sides; blank means unknown, never zero.
3. Preserve source, confidence, observed time, available time, quantity, notes, and listing evidence when available (sale type, listing ID, URL). Make imports idempotent on the source's natural observation key.
4. Separate field capture from accounting import: a store-visit log is a candidate/experiment file, not a ledger input.
5. Define a repeatable store-visit test: confirm identity and condition, record asking price and dated reference, apply a conservative condition/price reserve and time cost, then classify PASS/HOLD/REJECT.
6. Use a first-excursion checklist: budget cap, store time limit, charged phone/battery, offline templates, photo permission, sleeves/toploaders, purchase/receipt photos, and post-visit closeout.
7. Measure projected versus realized edge, false-positive rate, condition-error rate, dollars of edge per store hour, and store/vendor performance before changing the buying rule.
8. Treat spreadsheets from buyers or prior hauls as raw source artifacts first; normalize only after identity, effective date, condition, variant, and terms are reviewed. Keep unmatched rows in an exception queue.

### Raw versus professionally graded identity

Never represent a slabbed card as NM. Use `condition_type=raw` with `raw_condition` in `NM|LP|MP|HP|DMG`, or `condition_type=graded` with `grader`, numeric `grade`, optional `cert_number`, and `cert_verified`. Grader, grade, language, variant, and printing are part of the instrument identity and therefore require separate comp series, buylist terms, inventory positions, and opportunity calculations. Require the appropriate fields in ticker, extraction, observation, and store-visit imports; reject incoherent graded rows.

### Photo-identification intake

Treat scanner/app output as a candidate observation, never as an automatic purchase truth. Capture image path/hash, provider, OCR text, candidate ticker, confidence, raw/graded fields, source result IDs/URLs, and human decision in an intake layer before resolving to the canonical ticker. High-confidence exact matches may prefill a visit row; ambiguous set/variant/language/grade matches go to `HOLD` or `needs_review`. Keep the human gate before writing canonical market data, purchases, or opportunities. See `references/card-identification-research.md` and the persistent vault notes `Card Identification Workflow.md` and `First Excursion Checklist.md`.

See `references/field-ingestion-and-store-experiment.md` for the reusable workflow and starter decision rules.

## Persistent repository and vault workflow

When the user has an authenticated GitHub repository, make it the canonical cloud source before producing more downloadable archives. Store one persistent `obsidian-vault/` in the repository and edit it in place. Keep executable schemas, scripts, and templates alongside it, and generate a dependency-free webpage from the vault as a derived presentation layer. After changes: rebuild the site, run focused verification, commit, push, and verify the remote branch/ref. Do not create a new vault archive for every update unless explicitly requested. If GitHub SSH is used, verify with `ssh -T git@github.com` and `git ls-remote` before cloning or pushing.

## Condition and grading identity

For collectible cards, raw condition and professional grading are different market states and must never be collapsed. Model raw records with `condition_type=raw` plus `raw_condition` in `NM|LP|MP|HP|DMG`. Model slabbed records with `condition_type=graded`, `grader` (PSA/BGS/CGC/SGC/other), numeric `grade`, optional `cert_number`, and `cert_verified`. A graded card is never mapped to NM. Grader, grade, language, variant, and printing belong in the instrument identity and therefore in separate comp series, buylist terms, inventory positions, and opportunity calculations. Certification verification is a data-quality control; an unchecked cert remains unverified.

Store-visit capture and extraction imports should require the appropriate fields by type. Market observations should retain source listing evidence (`sale_type`, listing ID, URL) when available. Raw and graded price sources need separate mapping rules: an aggregator's generic "raw" value is not automatically NM, and a graded value is not a raw comp.

## Source hierarchy for card valuation

Use the strongest evidence appropriate to the decision: realized business sales and confirmed buylist quotes first; then multiple exact-match completed marketplace sales; then aggregated guides such as Card Hedge or PriceCharting; then active asks as replacement-cost context only. A single latest sold listing is evidence, not “true value.” Prefer a condition/grade-matched recent sample with median, low/high, usable-count, recency, and net-of-fees/shipping/reserve calculations. Preserve original listing IDs/URLs and confidence labels. TCGplayer price guides are useful retail references, but do not assume new API access: current developer documentation says new API access is no longer being granted, so verify access and terms before designing an integration.

## Verification

For schema artifacts:

1. Execute SQL in an isolated in-memory SQLite database.
2. Assert required tables, indexes, and views exist.
3. Check constraints such as nonnegative prices, valid conditions, and quote ordering.

For generated Quote Boards:

1. Execute the generator, not merely inspect an old HTML file.
2. Assert expected instrument counts and source-fixture totals.
3. Assert provenance badges, blocked-state markers, point-in-time/net-edge text, and links.
4. Assert no external scripts when the artifact is dependency-free.
5. Verify latest Obsidian links and package/archive contents.

Call this **ad-hoc verification of changed behavior** unless the canonical suite also ran and passed. Do not claim suite-green from a temporary checker.

## Obsidian/project integration

Keep executable SQL, generators, and HTML in the project root. Keep explanatory notes in one persistent Obsidian vault. When a GitHub repository is available, make that repository the canonical cloud source: store `obsidian-vault/` once, edit it in place, and commit/push note changes rather than producing a new downloadable vault archive for every update. Generate a dependency-free webpage from the current vault as a presentation layer; the webpage is derived and must not become a second editable source. Link the vault Home note to current artifacts and maintain human-readable schema and Quote Board notes. Before delivery, rebuild the site and verify the generated artifact against the current vault.

### Persistent repository handoff

When migrating a local project into an authenticated GitHub repository, verify SSH identity and remote access first, then copy the vault, source scripts, schemas, templates, and generated static artifacts while excluding runtime databases, reports, backups, and secrets. Configure Git author identity only after confirming the user’s requested name/email. Push, verify the remote branch SHA, and report exact canonical paths. Do not create replacement vault archives for routine edits.

### Photo-identification intake

Photo recognition belongs in an intake layer, not directly in the canonical instrument or accounting ledger. Capture image path/hash, provider, OCR text, candidate ticker, recognition confidence, raw-vs-graded fields, source result IDs/URLs, and a human decision (`pending`, `accepted`, `rejected`, `needs_review`). Use confidence gates: high-confidence exact matches may prefill; ambiguous matches must be held for review. Preserve image/result evidence and never let a scanner’s price or condition estimate automatically authorize a purchase. The project’s `card_image_candidates` table and `Card Identification Workflow` note implement this pattern.

### Condition and grading identity

For collectible cards, raw condition and professional grading are different market states and must never be collapsed. Model raw records with `condition_type=raw` plus `raw_condition` in `NM|LP|MP|HP|DMG`. Model slabbed records with `condition_type=graded`, `grader` (PSA/BGS/CGC/SGC/other), numeric `grade`, optional `cert_number`, and `cert_verified`. A graded card is never mapped to NM. Grader, grade, language, variant, and printing belong in the instrument identity and therefore in separate comp series, buylist terms, inventory positions, and opportunity calculations. Certification verification is a data-quality control; an unchecked cert remains unverified.

See `references/card-identification-research.md` for the provider comparison, research notes, pilot design, and source hierarchy captured from the card-scanner investigation.

## References

- `references/factset-style-terminal.md` — condensed product mapping, schema pattern, controls, and research citations from the terminal-building workflow.

#finance #market-data #arbitrage #factset-analog #data-governance
