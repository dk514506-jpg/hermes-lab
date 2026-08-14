# FactSet-style terminal, cybernetics, and database translation

## Product target

A small domain-specific market-intelligence terminal should reproduce the useful analytical workflows of an institutional portfolio platform: quote/market state, opportunity screening, portfolio exposure, benchmark-relative comparison, performance attribution, risk/scenario analysis, and data-quality/workflow controls.

The product is not a generic low-latency trading engine. For a thin, condition-sensitive market such as Pokémon cards, execution confidence, identity normalization, provenance, liquidity, and net realized economics matter more than speed alone.

## Closed-loop framing

- **Environment/plant:** venues, listings, sources, buyers, sellers, network paths, and changing market regimes.
- **Sensors:** quotes, listings, realized sales, buylist quotes, sequence/timestamp data, feed health, and inventory events.
- **State estimator:** normalized cross-source market state with freshness, confidence, and identity status.
- **Controller:** screener, buy/no-buy decision, routing, listing, holding, and reject/circuit-breaker logic.
- **Feedback:** fills, time-to-sale, slippage, disputes, stale data, source conflicts, rejects, and P&L attribution.

Design implication: data quality is part of the decision control loop. A stale or incorrectly mapped observation can create a false opportunity, so freshness and identity checks need hard trading thresholds.

## Layers

1. **Raw immutable:** source payload/file, source record ID, venue/channel, sequence, event/source/receive/ingest timestamps, hash, schema version, capture session.
2. **Canonical:** instruments/variants, venues, quotes, trades/sales, listings, buylist quotes, fees, sessions/events, and identity mappings.
3. **Analytics:** net spreads, liquidity, marks, exposure, benchmarks, attribution, stress tests, and opportunity scores.
4. **Presentation:** quote board, screener, portfolio, attribution, and control room.

Do not destructively overwrite raw or historical observations. Model corrections as new revisions or events and rebuild projections.

## Temporal and lineage controls

Use explicit time dimensions:

- `event_ts`: when the economic event occurred
- `source_ts`: when the source published it
- `receive_ts`: when capture received it
- `ingest_ts`: when pipeline stored it
- `available_ts`: when it could affect a decision
- `valid_from/to`: economic validity
- `known_from/to`: knowledge validity
- `decision_ts`: strategy decision time
- `execution_ts`: order/listing/sale execution time

A record may affect a historical decision only when `available_ts <= decision_ts`. This prevents hindsight from later corrections, backfills, or identity mappings.

For every derived signal or opportunity, preserve:

- input observation IDs
- source and record IDs
- mapping/normalization transformations
- fees and assumptions
- strategy/model version
- calculation run ID
- data snapshot or file hash
- confidence and quality flags

## Quality and observability

Track both operational and epistemic observability.

- **Operational:** feed status, errors, rate limits, reconnects, queue depth, refresh duration.
- **Epistemic:** quote age, source disagreement, unresolved identity, missing condition, stale state, sample size, provenance completeness, and whether a net opportunity survives costs.

Recommended controls:

- maximum quote/observation age
- minimum identity confidence
- maximum source disagreement
- required buylist or liquidation assumption
- minimum liquidity/time-to-sale evidence
- explicit disablement when thresholds fail
- reconciliation of transactions, fees, inventory, and P&L

## Database shape

Minimum concepts:

```text
instruments / instrument_variants
sources / venues / identity_mappings
market_observations / realized_sales / buylist_quotes
inventory_lots / positions / transactions / fees
opportunities / opportunity_inputs
benchmarks / portfolio_snapshots / attribution_facts
quality_flags / calculation_runs / raw_events
```

The central opportunity object must be explainable: it should show the exact observations, costs, assumptions, and timestamps used to produce the score. Keep theoretical spread, executable spread, and realized return separate.

## Useful authoritative references

- FactSet Portfolio Analytics: https://www.factset.com/solutions/portfolio-analytics
- W3C PROV Overview: https://www.w3.org/TR/prov-overview
- NIST Data Provenance: https://csrc.nist.gov/glossary/term/data_provenance
- OpenTelemetry signals: https://opentelemetry.io/docs/concepts/signals/
- Apache Beam time domains/watermarks: https://beam.apache.org/documentation/programming-guide/#the-time-domain
- FIX Online Specification: https://www.fixtrading.org/online-specification/
- Basel Committee BCBS 239 principles for effective risk data aggregation/reporting: https://www.bis.org/publ/bcbs239.htm
- Apache Iceberg snapshots/time travel/schema evolution: https://iceberg.apache.org/docs/latest/
- Chen, “The Entity-Relationship Model”: https://doi.org/10.1145/320434.320440

## Scope caution

These cross-domain recommendations are design synthesis. Cite the underlying source for a factual claim, and label local architecture decisions as recommendations rather than presenting them as direct requirements from FactSet, cybernetics, or a standards body.
