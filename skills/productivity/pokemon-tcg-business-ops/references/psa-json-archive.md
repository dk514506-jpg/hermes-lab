# PSA JSON Archive Structure — Per-Cert Lookup Files

**Evidence label:** VERIFIED — 7 lookup files created and archived 2026-08-13; schema applies cleanly in SQLite 3.53.4; DB counts confirmed (7 instruments, 7 tickers, 13 observations, 2 sources).

**Status:** 2026-08-13 — established. This reference documents the JSON archive shape, the privacy-strip-before-commit pattern, and the DB archival mapping. It complements (does not replace) `psa-cert-verification.md`, which covers the browser lookup workflow itself.

## When to use

Use this reference when archiving PSA cert verification results into the Pokemans repo as JSON files under `data/psa-lookups/`, and when mapping those results into the terminal schema (`terminal_instruments`, `card_tickers`, `terminal_market_observations`).

## Archive directory convention

```
Pokemans/data/psa-lookups/
  100143924.json   # named by cert number
  100473153.json
  ...
```

One file per cert. Filename = cert number. This makes re-ingest, dedup, and git-diff trivial.

## JSON shape (per-cert lookup file)

```json
{
  "cert": "100143924",
  "lookup_date": "2026-08-13",
  "card_name": "Gholdengo ex",
  "set_name": "PAR En-Paradox Rift",
  "card_number": "252",
  "variant": "Special Illustration Rare",
  "language": "EN",
  "year": 2023,
  "grade_text": "GEM MT 10",
  "grade": 10.0,
  "grader": "PSA",
  "psa_estimate": 174.00,
  "population": 1288,
  "population_higher": 0,
  "label_type": "PSA Fugitive Ink Technology",
  "reverse_cert": true,
  "recent_sales": [
    {"price": 175.00, "date": "2026-08-10", "source": "eBay BestOffer", "cert": "108681024"},
    {"price": 182.50, "date": "2026-08-10", "source": "eBay Auction", "cert": "107928972"}
  ]
}
```

### Field notes

| Field | Source | Notes |
|---|---|---|
| `cert` | PSA page | Primary key; also the join key to the buy sheet |
| `lookup_date` | Today | ISO date; used for `created_at` / `observed_at` |
| `card_name`, `set_name`, `card_number`, `variant` | PSA page | Instrument identity fields |
| `language` | PSA page / inferred | Default `EN` unless Japanese/etc. |
| `year` | PSA page | Set year; used for `era` |
| `grade_text`, `grade` | PSA page | Human-readable + numeric; `grade` is a REAL 1–10 |
| `grader` | Always `PSA` for these lookups | |
| `psa_estimate` | PSA page | Nullable — Flying Pikachu V #134241953 has no estimate |
| `population`, `population_higher` | PSA page | Population context for the estimate |
| `label_type` | PSA page | e.g. `PSA Fugitive Ink Technology` |
| `reverse_cert` | PSA page | Boolean; `true` if barcode on reverse |
| `recent_sales` | PSA page | Array of recent sale comps (price, date, source, cert) |

## Privacy strip before commit

**Critical:** the buy sheets (Luke 8-1, Luke 7-25) carry the friend's private financial data — `CL VALUE`, `cost`, `payout`, `roi`. If you add a `sheet_context` block to a lookup JSON during the lookup campaign, **strip it before committing to GitHub**:

```python
data.pop('sheet_context', None)
```

The `sheet_context` block (if present during active lookup) looks like:

```json
"sheet_context": {
  "sheet": "sheet-8-1",
  "cl_value": 150.00,
  "cost": 140.00,
  "payout": 135.00,
  "roi": -5.00
}
```

This is the friend's private ledger data — keep it local only. The PSA data (card identity, grade, estimate, population, recent sales) is public and safe to commit.

## `.gitignore` pairing

Commit a `.gitignore` at repo root that excludes:

```
data/state.db
*.csv
```

- `data/state.db` — the local SQLite DB with the friend's financial data baked into `terminal_market_observations` (CL VALUE observations). Keep local.
- `*.csv` — the original buy sheet CSVs are private. Keep local.

The PSA JSONs in `data/psa-lookups/` are public (no `sheet_context`) and safe to commit.

## DB archival mapping

When archiving into the terminal schema, map JSON fields as follows:

### `terminal_instruments`

| JSON field | Column | Notes |
|---|---|---|
| `cert` | `cert_number` | |
| `card_name` | `card_name` | |
| `set_name` | `set_name` | |
| `card_number` | `card_number` | |
| `variant` | `variant` | Default `"unspecified"` if missing |
| `language` | `language` | Default `"EN"` |
| `grade` | `grade` | REAL |
| `grader` | `grader` | `"PSA"` |
| `year` | `era` | |
| `tier` (if computed) | `tier` | |
| today | `active_from`, `created_at` | ISO date / ISO timestamp |
| — | `condition_type` | `"graded"` |
| — | `cert_verified` | `0` (pending human check) |

### `card_tickers`

Same identity fields as `terminal_instruments`, plus:
- `ticker` — suggested format: `{set_name}-{card_name}-psa{grade}.{cert[:6]}` (slugified, lowercased)
- `condition_type` — `"graded"`
- `active` — `1`
- `notes` — `"PSA cert lookup {lookup_date}."`

### `terminal_market_observations`

Two observations per card (when data available):

1. **PSA estimate** (source = `psa-cert-lookup`):
   - `market_cents` = `psa_estimate * 100`
   - `source_confidence` = `"ASSUMED"` (PSA estimate is PSA's valuation, not a market transaction)
   - `notes` = `"PSA estimate. Pop: {population}."`

2. **Sheet CL VALUE** (source = `luke-buylist-sheets`):
   - `market_cents` = `sheet_context.cl_value * 100`
   - `source_confidence` = `"ASSUMED"`
   - `notes` = `"CL VALUE from {sheet_context.sheet}."`
   - Only if `sheet_context` was captured during lookup. Since `sheet_context` is stripped before commit, this observation is written to the DB during archival but is not in the committed JSON.

### `terminal_sources`

Two source records:

1. `luke-buylist-sheets` — type `manual`, notes describe the two CSV sheets.
2. `psa-cert-lookup` — type `manual`, URI `https://www.psacard.com/cert`, notes describe the manual browser lookup.

## Example: the 7-lookup campaign (2026-08-13)

| Cert | Card | Set | # | Variant | Grade | PSA Est | Pop |
|---|---|---|---|---|---|---|---|
| 100143924 | Gholdengo ex | PAR En-Paradox Rift | 252 | SIR | 10 | $174 | 1,288 |
| 100473153 | Tangela | Mew En-151 | 178 | Illustration Rare | 8 | $19 | 838 |
| 100643330 | Jack | One Piece OP01-Romance Dawn | 102 | Alt Art | 10 | $71 | 243 |
| 117389921 | Green's Exploration | Sun & Moon Unbroken Bonds | 209 | — | 10 | $204 | — |
| 134241953 | Flying Pikachu V | Celebrations | 006 | Standard | 10 | — | 2,961 |
| 152311952 | Green's Exploration | Sun & Moon Unbroken Bonds | 209 | — | 10 | $204 | — |
| 75716523 | Primal Groudon ex | Japanese Premium Champion Pack | 073 | Premium Champion Pack | 10 | $256 | 243 |

Notes:
- **100643330 (Jack)** is One Piece, not Pokémon — flagged as non-Pokémon "TCG" contamination in the sheet.
- **117389921 and 152311952** are the same card (Green's Exploration) bought twice — duplicate card detection on identity, not just cert.
- **134241953 (Flying Pikachu V)** has no PSA estimate — only the sheet CL VALUE observation is recorded.

## Pitfalls

- **Don't commit `sheet_context`.** Always strip before `git add`. The friend's CL VALUE / cost / payout / ROI is private.
- **Don't commit `state.db`.** It contains CL VALUE observations from the sheets. Keep it local; `.gitignore` it.
- **PSA estimate ≠ market price.** The PSA estimate is PSA's valuation. Record it as `ASSUMED` confidence, not `VERIFIED`. Recent sales on the PSA page are better comps if you attribute them with listing IDs.
- **One cert at a time, manual.** No automation, no scraping. TOS-safe path only.
- **Duplicate detection on card identity, not just cert.** 117389921 and 152311952 are different certs for the same card — useful financial context (two slabs of the same card).

## See also

- `psa-cert-verification.md` — the browser lookup workflow (how to navigate to `psacard.com/cert`, what fields to read, TOS boundaries).
- `schema_terminal.sql` — the terminal schema this archive maps into.
- `financial-market-terminals/references/sqlite-check-constraint-pitfall.md` — the SQLite 3.53.4 CHECK constraint ordering bug that `schema_terminal.sql` hit and was fixed for.
