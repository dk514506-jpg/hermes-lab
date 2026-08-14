# Field Ingestion and Store-Buying Experiment

## Capture model

Use three separate artifacts:

1. **Ticker universe:** canonical identity — card, set, number, printing/variant, language, condition, active status.
2. **Observation file:** dated market or buylist values. Market and buylist are nullable independently; blank is unknown and zero is a real price.
3. **Store-visit log:** candidate cards and experiment metadata. It is not an accounting import.

A normalized observation should carry `date`, `ticker`, `source`, `confidence`, `observed_at`, `available_at`, optional `quantity`, and notes. Imports should be idempotent on `(ticker, date, source)` or the source's documented natural key.

## Spreadsheet handoff

Preserve a buyer's original spreadsheet unchanged as a dated raw artifact. Normalize only after reviewing identity, condition, variant, effective date, quantity limits, and terms. Mark directly confirmed quotes `VERIFIED`; estimates remain `ASSUMED`. Keep unmatched rows in an exception queue rather than silently dropping them.

## Store-visit test

Before each visit, set a budget, time limit, and reserve. At the store, confirm card identity and condition, record asking price and quantity, capture a dated reference value and expected exit bid, then classify each candidate:

- **PASS:** verified identity; high condition confidence; expected net edge clears the chosen dollar/percentage hurdle; executable exit is plausible.
- **HOLD:** a plausible edge exists but buylist, condition, variant, or liquidity remains unresolved.
- **REJECT:** edge is negative or too uncertain, the exit route is weak, or handling time destroys economics.

A starter rule can require at least $5 net edge or 25% of cost after a 20% condition/price reserve, but treat this as an experiment hypothesis. Measure projected versus realized edge, false positives, condition errors, time to exit, and edge per store hour before changing it.

## Verification language

If a focused checker is blocked or not actually executed, report that limitation; do not convert a written script into a claimed verification result. Distinguish canonical suite-green from ad-hoc verification and from unverified changes.
