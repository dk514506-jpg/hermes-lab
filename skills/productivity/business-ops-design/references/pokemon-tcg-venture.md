# Pokémon TCG Venture — Knowledge Bank & Project State

Domain research and project state for the Chicago-based Pokémon bulk-card operation. Companion to the design memo at `/opt/data/pokemon-business/design-memo.md` (2026-08-07, v1.0). Numbers are as of Aug 2026 — verify before relying on them long-term.

## Business structure (as of 2026-08-07)
- **Owner (Chicago):** buys card sheets/bulk lots at shows; sorts & extracts value cards himself; ships bulk west. Free to buy/sell to anyone.
- **Seattle partner:** wholesaler/middleman (crew of 3–4 show buyers) → **SF enterprise buyer** (end customer). Partner channel pays ~4–8% on bulk; direct sales to the partner's buyer network pay larger splits. Partner channel requires minimum weekly volume to stay in the deal.
- **Buy-sheet (partner's tier margins):** emailed, NOT yet received — the load-bearing input for the P&L model. Parameterize `tier_rates` around it when it lands.

## 2026 bulk rate benchmarks (sources: Misprint bulk report Feb 2026; MetaTCG buylist; CLOSO 2026)
- Commons/uncommons: $15–25/1,000 to bulk buyers; $25–40/1,000 direct if sorted by set/era (vintage WOTC-era commons $40–80/1,000; set-builders pay premiums).
- Non-holo rares $0.05–0.10 bulk; reverse holos $0.05–0.15 bulk (pre-DP-era reverse holos $2–15+ — pull); holo rares $0.15–0.50 bulk, $0.25–2.00 direct; vintage holos $5–50+.
- V/EX/GX $0.25–1.00 bulk, $0.50–5.00 direct; alt arts $10–100+; SIRs $5–200+; Trainer Gallery $0.50–2.00 bulk; secret/gold rares $5–50+ (never bulk). Energy ~$5–10/1,000.
- **The $1 Rule:** pull every card scanning ≥$1; sell individually. 50 × $1–5 cards can outvalue the other 4,950 commons. Sorting by tier/era lifts bulk payout 2–3×.
- MetaTCG mail-in buylist (NM English only): C/U $20/1,000, holo rare $35/1,000, V/EX $500/1,000, VMAX/VSTAR $750/1,000. Use as the benchmark the Seattle channel must beat net of shipping.

## Channel & pricing facts
- Fees: eBay ~13%, TCGPlayer 12–15%; LGS pays only 40–60% of market ("convenience tax" — avoid).
- eBay PWE (standard envelope) $0.64–1.12 for cards <$20 vs ~$4 Ground Advantage. Tracked + packing-video/weight receipt for anything ≥$20 (dispute protection).
- Grading: only when (graded-10 value − $15–25 fee) > raw value. Almost never for bulk ops.
- Meta-timing: playable cards spike pre-tournament (documented: Iron Hands ex $8→$18 before a regional). Hold meta tier with a thesis; auto-alert on price deltas.
- Negotiation: ~10–20% of dealers will negotiate 5–10% on bulk bundles; end-of-show discounts (dealers hate packing out); cash talks. Buy below the bulk floor so extraction is pure upside.
- Market context: Pokémon cards +3,261% over two decades vs S&P +421% (Card Ladder via WSJ 2025) — BUT short-term prices are essentially random (Hilbert 2024: −4.72%/yr 2021–23). Thin, sentiment-driven market → hold policy, data over hunches.

## Pricing APIs
- **TCGplayer API** (docs.tcgplayer.com): OAuth2 client-credentials; catalog + market prices; category 3 = Pokémon. Free, application-based access.
- **PriceCharting API** (pricecharting.com/api-documentation): per-condition/grade prices + history; paid tier.
- Fallbacks: scrapers (Apify actors) — flag as lower-trust; TCGdex for card metadata.

## Time-as-money design (from design memo §2)
P0 show-floor capture: photo + voice-note only (never type at the show; ~10s/sheet, batch entry at home). P2 sort line: 3 passes (era → visual screen → $1-rule scan), only the pulled pile gets per-card attention. P4 storage: route-zoned bins (BULK-NORTH / DIRECT / GRADE / HOLD / PENDING), FIFO, one-touch. P5 shipping: weekly consolidation, flat-rate boxes, insurance thresholds. P7 learning loop: time studies → $/hr per stage; venue/vendor scorecards; era/category yield tables.

## KPI set (master metrics)
Extraction rate (extracted value ÷ purchase price — the single most informative number), floor coverage (bulk floor ÷ price paid), GMROI, margin per venue/vendor, channel mix, turnover days, $/hour per stage.

## Tech stack decision (from design memo §4)
SQLite source of truth (`/opt/data/pokemon-business/state.db`) + Google Sheets mobile capture (shared Chicago↔Seattle) + nightly sync script + TCGplayer/PriceCharting price refresh + Hermes cron for weekly reconcile/reports + git-versioned scripts + agent (Hermes) as the AI back office. Future: CV screen assist (DenseNet corner-grading per Nahar et al. 2025, Computers in Industry 164:104187; VGG-embedding identification pattern).

## Project state & next steps
- **Done:** design memo v1.0 at `/opt/data/pokemon-business/design-memo.md` (24 KB, 20 sources, annotated bibliography with VERIFIED/UNVERIFIED labels).
- **Pending inputs:** (1) friend's buy-sheet (emailed — awaiting), (2) TCGplayer dev account, (3) PriceCharting account, (4) one real week of purchase data.
- **Next build — Phase 1:** SQLite schema (purchases/venues/vendors/sheets/cards/extractions/sales/shipments/expenses/price_refs/weekly_snapshots) + Sheets capture template + import script + basic P&L. Phase 2: pricing integration + buy/no-buy calculator. Phase 3: automated weekly reports + scorecards + meta alerts. Phase 4: CV assist + time-study analytics.
- **Clean-room rule (from the hermes-lab bundle review):** every reconcile/verify script must use relative paths only, pinned deps, and pass in a clean checkout before being trusted. The hermes-lab author shipped a 14-verifier gate that failed 12/14 in a clean container (hardcoded `/home/greenknight/` paths in verifiers, machine-local wiki reads, undocumented pyyaml/jsonschema deps) — the cautionary tale.

## Key sources (condensed; full annotations in memo §7)
- Heck et al. 2026, PLOS ONE 21(3):e0334289 — Pokémon eBay field study; condition rule (5–10%/grade); thin market.
- Hilbert 2024 (College of Wooster thesis) — short-term card prices basically random.
- de Koster, Le-Duc & Roodbergen 2007, EJOR 182(2):481–501 — order picking; travel time dominates; storage assignment.
- Nahar et al. 2025, Computers in Industry 164:104187 — DL corner grading, human-in-the-loop.
- Misprint (2026-02-26) bulk report; MetaTCG buylist; CLOSO 2026 selling guide; TCGplayer/PriceCharting docs; Stord/BigCommerce 2026 AI-in-ecommerce reports (directional).
