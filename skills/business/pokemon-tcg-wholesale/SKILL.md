---
name: pokemon-tcg-wholesale
description: "Use for Pokemon TCG wholesale: sourcing, margins, tracking."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [pokemon, tcg, wholesale, resale, collectibles, business, margin, inventory]
---

# Pokemon TCG Wholesale & Resale

Domain playbook for Pokemon card buying/selling/flipping work. Numbers below are 2025-2026-era benchmarks from reseller guides — always re-check current market prices (TCGPlayer market, eBay sold) before acting on them. Detail + sources in `references/market-research.md`.

## The supply chain (middleman model)

Typical chain: **card-show floor buyers** → **wholesaler/consolidator** (sorts, packs, ships) → **top buyer / enterprise customer** (retail channel). The middleman's economics:

- 4-8% margin on shipped bulk to the top buyer is THIN — it's a volume game, not a per-card game.
- Larger splits on **direct sales** to specific buyers — the margin upside lives in curation/selection, not in bulk flow.
- Everyone upstream of the top buyer is selling labor (sorting, selecting, packing, shipping) as much as cardboard.

## Key economics (benchmarks)

- **Bulk:** commons/uncommons $15-20 per 1,000 cards; code cards ~$0.35-0.50 each; holo rares $0.05-0.08; V/ex/ultra rares $0.50-0.75. Bulk moves to dedicated bulk buyers (Safari Zone, Full Grip Games, Derium's) — flat-rate boxes, PayPal, fast.
- **Selection is the money:** pull every $20+ single OUT of a binder lot before the rest hits bulk ("partial binder lot"). Bundling the whole binder prices the good cards as free bulk.
- **Never sort bulk for individual sale** — a documented failure case netted ~$1.50/hour. Move bulk by the thousand or not at all.
- **Retail platforms:** eBay ~13% fees (standard envelope $0.64-1.12 makes sub-$20 singles viable; always use eBay **sold** listings, never active, for pricing); TCGPlayer for playable/meta volume (12-15%); Local Game Stores pay 40-60% of market — a "convenience tax" to avoid unless desperate.
- **Grading:** $15-25/card, months of turnaround. Grade only if (graded-10 value − fee) > raw value. A PSA 9 that trades ~raw is a money-loser after fees.
- **Meta-game arbitrage:** tournament results spike card prices (documented: $8 card → $18 as a regional approached). Watch TCGPlayer market price, PriceCharting, PSA population.
- **True wholesale input** (sealed product) requires: registered business (LLC/sole prop), state tax/resale cert, case-quantity minimums. Distributors: Alliance Game Distributors, GTS Distribution, Southern Hobby Supply (US).

## Sourcing channels

Card shows (dealer tables, end-of-day deals), estate/collection buys (FB Marketplace, local ads — negotiate 60-80% of value), liquidation pallets (Liquidation.com, B-Stock — steep discounts, uncertain condition/mix), authorized distributors (requires reseller credentials). Beware counterfeits on Alibaba/grey-market "retail pack" sources.

## Data capture & tracking (design seeds)

The venture needs visibility at four levels:

1. **Lot ledger** (per purchase): date, source/vendor, show name, set mix, card count, total cost, condition distribution, photos. → enables cost-per-card and vendor quality ranking.
2. **Shipment log** (per box to buyer): card count, weight, insured value, buyer, shipping cost, declared value, payout, margin %. → per-buyer profitability.
3. **Singles tracker** (per curated card): set+number (unique ID), condition, buy price, sell platform, sell price, fees, net, days held. → $/hour per selection effort.
4. **KPIs**: gross margin per lot, margin after shipping, $/hour of selection labor, bulk-vs-singles revenue split, turnaround time, vendor hit-rate (lots bought vs value found).

Tooling: start with a spreadsheet (Google Sheets) — zero friction, shareable with the crew — then graduate to SQLite + a scan app when volume demands. TCGplayer Pro and PriceCharting have market-data APIs worth wiring up later.

## Current venture context

User's active setup (see memory for current details): friend = Seattle wholesaler/middleman (crew of 3-4 show buyers → top buyer + enterprise customer in San Francisco); user = Chicago sourcing node who buys sheets/lots at shows, **sorts and extracts value cards himself**, and ships the remainder west to the friend.

Strategic framing (settled with the user):
- The friend's 4-8% channel is the **floor, not the ceiling** — it is a volume/turnover engine that keeps the relationship warm (minimum weekly volume required) while the extracted singles go direct (higher splits, or any buyer the user chooses — he has full freedom to sell where he pleases).
- **Whoever extracts the $1+ cards owns the real margin.** If sheets ship unextracted, the downstream buyer captures it. Extraction happens at the user's Chicago processing step.
- The friend's tier buy-sheet is the **load-bearing input** — pending (he is emailing it). It parameterizes bulk-floor math, floor coverage, and the buy/no-buy calculator. Until it lands, use the benchmark rates in `references/bulk-rates-2026.md`.

**Authoritative design:** `/opt/data/pokemon-business/design-memo.md` — full schema (10-table SQLite), KPI set, tech stack, P0–P7 process architecture, roadmap. Master KPI = **extraction rate** (extracted value ÷ purchase price); also floor coverage, GMROI, margin per venue, $/hour per stage, channel mix, turnover days. Tracker Phase 1 (schema + Sheets capture + P&L) is the agreed next build.

## Pitfalls

- Condition misrepresentation → return claims; photograph front/back, state condition honestly (eBay "Scan to List" defaults to Mint — verify).
- Packaging protocol for singles: penny sleeve → top loader/card saver → team bag → cardboard sandwich; tracking on anything over $20; video + recorded weight for high-value shipments (wins INR disputes).
- Shipping cost is a margin killer on heavy bulk — flat-rate boxes only.
- No resale cert → can't buy wholesale, and you owe sales tax on retail sales; set up the entity before scaling.
