# FactSet-style terminal research notes

## Product mapping

FactSet Portfolio Analytics emphasizes data integration, reconciliation, standardization, workflow checks, exposures, risk, benchmark-relative metrics, performance, attribution, scenario analysis, and stress testing. For a small Pokémon terminal, map these to instrument identity, source-separated quotes, net executable opportunity screening, inventory exposure, lot/channel attribution, and a data-quality control room.

Source: https://www.factset.com/solutions/portfolio-analytics

## Market microstructure implications

- Shleifer & Vishny, “The Limits of Arbitrage,” *Journal of Finance* 52(1), DOI: https://doi.org/10.1111/j.1540-6261.1997.tb03807.x — convergence can be risky and capital/funding constraints matter.
- Glosten & Milgrom, “Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders,” DOI: https://doi.org/10.1016/0304-405X(85)90044-3 — asymmetric information is a structural source of spreads.
- Hasbrouck, “Measuring the Information Content of Stock Trades,” DOI: https://doi.org/10.1111/j.1540-6261.1991.tb03749.x — trade information and price impact unfold over time.
- Almgren & Chriss, “Optimal Execution of Portfolio Transactions,” DOI: https://doi.org/10.21314/JOR.2001.041 — execution balances market impact against timing risk.
- Bailey, Borwein, López de Prado & Zhu, “The Probability of Backtest Overfitting,” DOI: https://doi.org/10.21314/JCF.2016.322 — repeated strategy searches create false positives; record strategy/version/trial provenance.

## Database implications

At minimum preserve:

```text
instrument identity: card, set, number, variant, language, condition
observation: source, source_record_id, event_ts, source_ts, receive_ts,
             ingest_ts, available_ts, valid_from/to, known_from/to,
             bid, ask, market, last_sale, quantity, confidence
opportunity: decision_ts, expiry, strategy_version, input IDs,
             gross edge, fees, shipping, reserves, net edge, status
inventory: acquisition, quantity, cost basis, comp, sale, route, aging
controls: stale, conflict, unresolved identity, missing leg, calculation run
```

Use raw immutable, canonical normalized, analytics, and presentation layers. Corrections are new records, not overwrites.

## Point-in-time rule

Only data with `available_ts <= decision_ts` may influence a historical signal. Distinguish economic validity from when the system learned or stored the fact.

## Assumption discipline

When live feeds are unavailable, render a useful static artifact with explicit `ASSUMED` values and `BLOCKED` opportunities. Never invent buylist bids, liquidity, source timestamps, or arbitrage scores.

## Validation pattern

Execute the SQL in isolated SQLite, execute the generator, assert exact fixture counts/totals and semantic markers, validate vault wikilinks, then rebuild the archive. Call it ad-hoc verification unless the canonical suite ran.

## Related

See the class skill `financial-market-terminals/SKILL.md` for the reusable workflow.
