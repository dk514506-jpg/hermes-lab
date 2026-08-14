# PSA Cert Verification — Identity Backbone for Graded Cards

**Evidence label:** VERIFIED — PSA cert lookup page works via browser, returns structured identity + grade + population + recent sales for each valid cert number.

**Status:** 2026-08-13 — confirmed working. PSA cert lookup URL `https://www.psacard.com/cert` accepts a cert number, returns: card name, set, card number, variety/pedigree, grade (e.g. "GEM MT 10", "MINT 9"), year, label type (Fugitive Ink, etc.), reverse cert/barcode flag, PSA population + "higher" count, PSA estimate, and recent sales history (eBay + Fanatics, with dates and prices).

## Why this matters

The friend's buy sheets (Luke 8-1, Luke 7-25) are **financial ledgers** — they have PSA cert numbers, costs, payouts, ROI — but **no card identity** (no card name, set, number, variant, language). The PSA cert number is the join key between the ledger and the card catalog (`card_tickers` / `terminal_instruments` in the Pokemans schema).

Every PSA-graded card in those sheets can be identified by looking up its cert number on PSA's public cert verification page. This turns a financial row into a full `extractions` record with `cert_number`, `condition_type='graded'`, `grader='PSA'`, `grade=N`, plus the card identity fields.

## What PSA lookup gives you (per cert)

| Field | Example (cert 58633881) | Example (cert 65660647) |
|---|---|---|
| Cert number | 58633881 | 65660647 |
| Card name | Sabrina's Gaze | Energy Retrieval |
| Set | Yamabuki City Gym Deck | Game (Shadowless) |
| Card number | — | 81 |
| Variety/Pedigree | Yamabuki City Gym Deck | Shadowless |
| Year | 1999 | 1999 |
| Grade | MINT 9 | GEM MT 10 |
| Label type | W/ Fugitive Ink Technology | PSA Fugitive Ink Technology |
| Reverse Cert/Barcode | YES | YES |
| PSA Estimate | $94.00 | $96.00 |
| PSA Population | 785 | 170 |
| PSA Population Higher | 429 | 0 |
| Recent sales | eBay $81–$139.99 (PSA 9s) | eBay/Fanatics $60–$107 (PSA 10s) |

The "Sales of Similar Items" section shows comparable-grade actual sales — useful as a `VERIFIED` comp source if you attribute it correctly.

## How to use it in the workflow

1. **One cert at a time, manual browser lookup.** Enter the cert number on `psacard.com/cert`, read the result, record the identity fields. This is the intended public use of the tool — no automation, no scraping.
2. **Map to schema:** `card_tickers` row (condition_type='graded', grader='PSA', grade=N, cert_number=..., name=..., set_name=..., card_number=..., variant=..., language='EN') + `extractions` row (cert_number, cert_verified=0 pending human check, comp_cents=CL VALUE from sheet, comp_source='manual', condition_type='graded', grader='PSA', grade=N).
3. **Cross-check CL VALUE against PSA estimate.** Both certs checked so far (58633881, 65660647) had sheet CL VALUE below PSA estimate — suggests "CL VALUE" is either a different pricing source or a conservative number. The discrepancy is itself a data-quality signal worth tracking.
4. **Sales history as comp source.** Recent sales of same-grade cards on the PSA page are `VERIFIED` comps if recorded with source='psa_cert_page', sale_type='eBay' or 'fixed', and listing URL where available.

## Limitations

- **Raw (ungraded) cards have no PSA cert number.** PSA lookup only works for slabbed cards. Raw cards in the sheets (if any) need a different identity path — set/name/number identification via scanner apps or manual lookup.
- **PSA cert lookup is per-cert, manual.** Not automatable without scraping (which would be TOS violation). At scale you'd need the PSA API or a grading database — but those aren't free/public. For now, manual lookup is the only TOS-safe path.
- **PSA estimate ≠ market price.** The PSA estimate is PSA's own valuation, not a market transaction. Don't treat it as a `VERIFIED` market comp without an actual sale behind it. Recent sales on the page are better comps.

## TOS boundary (2026-08-13 user correction)

**PSA cert verification page (`psacard.com/cert`)** — manual, one-cert-at-a-time browser lookup is the intended public use. Safe.

**TCGplayer** — TOS restricts automated price/scrape access. New API access not being granted. The friend's "TCG" price field is a black box; do NOT scrape TCGplayer to verify prices. If you need TCGplayer prices, the TOS-safe path is the official TCGplayer mobile app (scan → read price → transcribe) or the seller portal CSV export — both designed workflows. Do not build automated synchronization against TCGplayer.

**eBay sold listings** — manual browser view OK for a human; scraping is not. Record as `VERIFIED` only if you can attribute the specific sale (listing ID, URL, date, price).

**PriceCharting and similar aggregators** — their own TOS apply. Check before treating as a data source.

**General principle:** any external pricing source must be used through its intended public interface, at human pace, with explicit attribution and confidence labeling (`VERIFIED` / `ASSUMED` / `UNVERIFIED`). When in doubt, ask the user before hitting a site programmatically.
