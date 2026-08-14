# Stdlib Data-Tracker Pattern (small-business operations tracker)

The `/opt/data/pokemon-business` tracker built in Phase 1–2: a card-buying
operation's purchase/process/sell system. The pattern generalizes to any
small-business tracker that must be zero-dependency, portable, and able to
prove its own books.

## Architecture

```
schema.sql            canonical DDL (sqlite3)
config/*.json         parameterized assumptions + mode switches
templates/*.csv       capture templates (Sheets-importable)
sample_data/*.csv     realistic sample week
scripts/
  common.py           REPO-root resolution (relative paths), cents()/dollars(),
                      load_config(), tier_floor()
  init_db.py          create/reset DB from schema.sql (--reset)
  import_data.py      idempotent CSV import (INSERT OR IGNORE)
  calc_floor.py       show-floor buy/no-buy calculator (bulk floor + extraction estimate)
  price_refresh.py    pluggable price layer (manual | tcgplayer | pricecharting)
  reconcile.py        weekly P&L + the balance GATE (exit 0/1)
  report.py           markdown + self-contained HTML with stdlib SVG charts
  charts.py           bar/line/coverage/flow SVG renderers (no matplotlib)
  verify_pipeline.py  clean-room gate for the whole tracker
```

Rules that made it work:
- **Money = INTEGER cents** everywhere (`Decimal(str(x))*100` → int). Float
  money breaks reconciliation; int cents makes the gate exact.
- **Natural UNIQUE keys on every importable table.** `INSERT OR IGNORE` is
  only idempotent with a UNIQUE constraint — without it, re-import silently
  duplicates rows and doubles totals (a real bug caught by the gate).
  Purchases: (date, vendor_id, price); sales: (date, purchase_id, route,
  gross, fees, shipping, buyer); extractions: (date, purchase_id, card, set,
  number); expenses: (date, category, amount, note).
- **The gate recomputes totals independently.** `revenue − fees − shipping −
  cogs − expenses` computed two ways must match, and per-purchase `Σ cogs ≤
  price paid` is asserted. It caught, in day one: a wrong purchase reference
  in sample data ($120 COGS vs $40 paid), the duplicate-import bug, and a
  JSON key-type display bug (below).

## KPIs worth tracking (the business version)

- Floor coverage % = bulk-tier value ÷ price paid (buy-side discipline)
- **Extraction rate % = extracted comp value ÷ price paid** — the master KPI;
  it rescues buys the floor math alone calls bad
- GMROI = gross margin ÷ average inventory cost; inventory at cost =
  Σ purchases − Σ cogs (opening + purchases − cogs = closing)
- Channel mix: net contribution per sales route
- Venue scorecards: spend vs bulk floor vs net per venue

## Stdlib SVG charts (self-contained HTML reports)

`charts.py` renders bar (grouped), line (trend), coverage (bars + 100%
reference line, color-coded), and flow-diagram SVGs as strings. Validate with
`xml.etree.ElementTree.fromstring` in verification. The HTML report embeds
them inline — no `<script>`, no `src=`, no external assets; the only
`http://` occurrences are the SVG `xmlns` namespace. File opens in any
browser, works offline, shareable as-is.

## The clean-room verify script

`verify_pipeline.py` checks, in order: no absolute paths in scripts (the
anti-drift sweep), schema tables present, config parses with canonical keys,
templates have canonical headers, sample CSVs parse, price layer mode valid +
refresh exits 0, reconcile gate passes. Fresh-copy test (the strongest
portability proof): `shutil.copytree` the tree to a temp dir excluding
`data/` + `reports/`, run the full documented sequence there, expect exit 0
at every step, then `rmtree` the temp dir.

## Parameterized assumptions (the "proceed with assumptions" pattern)

Where real inputs are pending (a partner's rate sheet, API keys), ship with
documented ASSUMED values in config (`"_comment": "ASSUMED ... swap-in
point"`), keep the config keys canonical so only values change, and state the
assumptions explicitly in the README and every report footer. Users who say
"proceed with assumptions and build" want the system NOW with visible swap
points — not a blocked build waiting on inputs.
