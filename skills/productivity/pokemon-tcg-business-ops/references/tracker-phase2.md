# Tracker layout — rev 2 state (Council-reviewed, 2026-08-08)

All under `/opt/data/pokemon-business/`. Stdlib-only; money in integer cents;
git-managed (`data/`, `reports/`, `backups/`, `config/secrets.json` ignored).

## Pipeline (documented order — this exact order is the contract)
```
init_db [--reset] → import_data [--purchases/--sales/--expenses/--extractions]
→ price_refresh → reconcile → report → backup_db → unittest discover → verify_pipeline
```
- `init_db.py` — creates `data/state.db` from `schema.sql`; `--reset` wipes.
- `import_data.py` — idempotent CSV import. Idempotency REQUIRES the natural
  UNIQUE keys in schema.sql; tables without them silently duplicate on re-import
  (real bug caught twice).
- `price_refresh.py` — price layer. mode=manual (default): guidance, exit 0.
  mode=tcgplayer: validates the OAuth token, then FAILS LOUDLY with nothing
  written until market-price wiring lands (Phase B) — **never writes
  placeholder rows** (Council F12). Keys load from `config/secrets.json`
  (gitignored), referenced by pricing.json's `secrets_file`. No dead code
  (`_post_json` removed, F2).
- `reconcile.py` — the gate. **Computed COGS (F5):** per purchase, basis =
  price paid; a sale with linked extractions books cogs = min(Σ linked comps,
  remaining basis); remainder sales cap at remaining basis; declared cogs only
  when nothing is linked. Computed values are MATERIALIZED onto sales rows.
  WARNs (not fails) on declared-vs-comps mismatch and comps-vs-gross
  overstatement. Gate: Σ allocated cogs ≤ paid per purchase; recomputed net ==
  net profit. Per-purchase KPIs land in `purchase_kpis` (F14); weekly
  `weekly_snapshots.kpi_json` is summary-only. Inventory + GMROI = gross margin
  ÷ avg inventory.
- `report.py` — single data-prep layer, two renderers (md + HTML) (F15/F16);
  no conditional-shape branches. Meta calendar from `config/meta_events.json`
  surfaces events ≤60 days out (Worlds 2026 window; NAIC 2027 Chicago).
  Venue/channel nets subtract materialized cogs. HTML: KPI cards, P0–P7 flow,
  venue bars, coverage + extraction-rate charts, realized-vs-held, channel mix,
  weekly trend, top cards, flags.
- `backup_db.py` — sqlite `.backup()` → `backups/state-<ts>.db`, keeps newest 10.
- `tests/test_tracker.py` — committed unittest suite (F8): cents/tier_floor
  math, import idempotency, known-good reconciliation numbers, purchase_kpis,
  chart XML validity, HTML structure (≥7 svg, no script/src, complete, no
  `height=-`), backup. Runs in an isolated temp DB (build_db unlinks the temp
  file each test). **Suite must NOT invoke verify_pipeline** (recursion — the
  gate runs the suite).
- `verify_pipeline.py` — clean-room gate: relative-paths sweep, schema tables
  (rev-2 set: venues, vendors, purchases, sales, expenses, weekly_snapshots,
  extractions, card_tickers, price_history, purchase_kpis), tier_rates
  completeness, 4 templates, 4 sample CSVs, pricing.json mode + secrets.json
  presence, price_refresh exit 0, **unittest suite pass**, report-artifact
  checks (F10), reconcile gate exit 0.
- `calc_floor.py` — buy/no-buy at the show. `--extraction_estimate` adds
  pulled-card value: GO if floor covers; else GO if floor + estimate ≥ price;
  else NO-GO with the missing value stated.
- `charts.py` — stdlib SVG renderers. **bar_chart has a true zero baseline**
  (negatives draw below the line; naive max-scaling emitted negative-height
  rects). Validate with `xml.etree.ElementTree.fromstring`.
- `check_hub_links.py` — hub link health (HEAD checks; ok/bot-blocked/broken;
  bot-blocked 400/403/429 = real sites, fine in a browser).

## Schema (rev 2)
- `sheets` / `shipments` / `price_refs` DROPPED (F1 dead weight, F3 duplicate
  table).
- `card_tickers` — ticker PK, name, set_name, era, tier, condition (share
  class — never mix conditions in one series), notes.
- `price_history` — ticker FK, date, market_cents, buylist_cents, source,
  UNIQUE(ticker,date). THE canonical price table (marketplace moat: we
  accumulate history because PriceCharting has none).
- `purchase_kpis` — purchase_id PK, week, floor_cents, coverage_pct,
  extraction_value_cents, extraction_rate_pct, realized_cents, held_cents.
- Every importable table has a natural UNIQUE key (purchases:
  date+vendor+paid; sales: date+purchase+route+gross+fees+shipping+buyer;
  expenses: date+cat+amt+note; extractions: date+purchase+card+set+number).

## Configs
- `config/tier_rates.json` — ASSUMED 2026 buylist rates; friend's sheet swaps
  `rate_cents` (keys canonical). Units: per_1000 vs per_card.
- `config/pricing.json` — `mode`: manual|tcgplayer|pricecharting +
  `secrets_file` pointer. Keys NEVER inline.
- `config/meta_events.json` — tournament/show dates for the meta calendar.
- `config/secrets.json` — GITIGNORED API credentials.

## Sample data (delete before real use)
One week (2026-08-03): 4 purchases, 5 sales, 3 expenses, 6 extractions.
Story: purchase #3 (65% floor coverage) rescued by 130% extraction rate;
purchase #2 sold to local at a loss (bad buy — flagged). Rev-2 known-good
numbers (computed COGS): **cogs $325.00, net −$41.76, extraction $137.00,
GMROI 0.30**; purchase_kpis p3 rate 130 / p4 rate 70. Sales.csv cogs are
pre-aligned to the computed rule (85/35/52) so the suite runs WARN-free.

## Bugs the gates caught (don't reintroduce)
1. Wrong purchase_id in sample sales → COGS $120 vs $40 paid → gate FAILED.
2. Missing UNIQUE keys → re-import duplicated sales/expenses/extractions.
3. JSON round-trip turns int dict keys into strings → `.get(p["id"])` on
   snapshot data returned 0; use `str(p["id"])` (fixed structurally by
   purchase_kpis).
4. `sqlite3.Row` has no `.get()` — use `row["k"]` / `or` chains.
5. Gate runs the test suite → tests must never invoke the gate (recursion).
6. Negative series in max-scaled bar charts → negative-height rects.
7. Tests patching `common.REPO` don't redirect modules that bound REPO at
   import — patch the module attr (`report.REPO = tmp`) and unlink the temp DB
   per test.

## Ops / automation
- Cron `d6e60f79581b` — Weekly Pokemon business ops (Sat 08:00): reconcile →
  report → backup → verify, gate-checked summary. `3f22541f5153` — Monthly hub
  link health (1st 09:00, no_agent shim `~/.hermes/scripts/
  check_hub_links_shim.py` → repo script). Both deliver='local' (saved to the
  cron list; NOT messaged in TUI) — wire a gateway target for real alerts.
- Review record: `reviews/council-review-2026-08-08.md` (6.8 → 8.3/10, all 14
  findings closed). Marketplace design: `marketplace-design.md` (FactSet-style
  concept map; Phase A build pending: ticker seed + marketplace.html).
