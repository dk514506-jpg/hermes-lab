---
name: pokemon-tcg-business-ops
description: "Operate the user's Pokemon card sourcing tracker."
---

# Pokémon TCG Business Ops

## The venture (durable structure)
- Owner buys card sheets/bulk lots at shows around Chicago, sorts & extracts in Chicago, ships the remainder west.
- Seattle friend = consolidator/middleman with a tier buy-sheet; 4–8% channel to the SF enterprise top buyer. Sustained volume is required to stay in the channel.
- Owner has freedom to sell to anyone: the Seattle channel is the liquidity floor; extracted singles go direct (larger split) or online (eBay ~13%, TCGPlayer ~13.5% fees).
- Margin lives in extraction, not cardboard: the **$1 Rule** (pull every card scanning ≥$1), sorted bulk pays 2–3× unsorted. Whoever extracts captures the real margin.

## The system (Phases 1 + 1.5 + 2 built, lives at /opt/data/pokemon-business/)
- Stdlib-only (clean-room rule), integer-cents money, relative paths, exit-code gates everywhere.
- Quickstart: `init_db` → `import_data` (purchases/sales/expenses/extractions CSVs; idempotent via natural UNIQUE keys) → `price_refresh` (manual mode by default) → `reconcile` (balance GATE, exit 0; also extraction KPIs, inventory, GMROI) → `report` (markdown + self-contained HTML with 7 SVG charts) → `verify_pipeline` (clean-room gate incl. pricing config). `calc_floor` = show-floor buy/no-buy calculator (v2 takes `--extraction_estimate`).
- Config: `config/tier_rates.json` — tier rates are **ASSUMED 2026 buylist averages**; the friend's buy sheet swaps in via `rate_cents` (keys are canonical — do not rename). `config/pricing.json` — price layer mode: `manual` (default, no keys) | `tcgplayer` | `pricecharting`; keys flip on live refresh.
- Extraction log: `extractions.csv` (card, set, condition, comp, sale_id, route) feeds the master KPI.
- Templates: CSV capture (purchases/sales/expenses/extractions), Google-Sheets-importable.
- Reports: `reports/week-<monday>.md` + `.html` (P0–P7 workflow diagram, venue bars, floor-coverage chart with 100% line, extraction-rate chart, realized-vs-held, channel mix, weekly trend, top-cards table, GMROI card).
- Full tracker layout in `references/tracker-phase2.md`.

## Weekly workflow (P0–P7)
P0 show capture (photo + voice-note; never type at the show) → P1 intake → P2 sort & extract ($1 Rule + era screen: vintage holos $5–50+, pre-DP reverse holos $2–15+, alt arts/SIRs/secret rares always pull) → P3 value & route → P4 route-zoned storage (FIFO, one-touch) → P5 ship (weekly consolidation, insurance ≥$20, packing-video + weight receipt) → P6 reconcile gate → P7 learn (venue scorecards, time studies).

## KPIs
- **Floor coverage** = bulk floor ÷ price paid (<70% flagged; <100% means extraction upside must close the gap).
- **Extraction rate** = extracted value ÷ purchase price — LIVE (reconcile/report: per-purchase %, realized vs held split).
- **GMROI** = gross margin ÷ average inventory cost — LIVE in reconcile/report (signal improves with weeks of history).
- Margin per venue, channel mix, turnover days.
- Hold policy: short-term card prices are basically random (Hilbert 2024) — meta-hold tier only, thesis-required, auto-alert on spikes.

## Roadmap / pending
- **Pending input**: friend's tier buy-sheet (emailed) → update `config/tier_rates.json`; everything recomputes.
- **Pending keys**: TCGplayer dev account (free, application-based) + PriceCharting (paid tier) → flip `config/pricing.json` mode from `manual` to live refresh.
- Phase 3: weekly cron ops (reconcile + report auto-run Saturday), kanban lot status, KPI dashboard, meta-timing alerts.
- Phase 4: CV screen assist (DenseNet corner-grading reference), time studies → $/hr per stage.

## Community & events hub
- `community-hub.html` (repo root) — tournament schedule, Chicago card shows (buying surface), weekly leagues/LGS, community links, market tools. All links live-checked with honest ✓/⚠/dead labels and a "dates move — official hub wins" caveat.
- **NAIC 2027 is Chicago** — June 18–20, 2027, McCormick Place. Biggest event of the season in the owner's city: plan inventory and the week around it.
- Meta-timing: playable prices climb ~2–3 weeks before majors (Worlds, NAIC) — the hub's tournament section is the pricing radar; pull staples into spike windows.

## Delivering artifacts to the owner
Raw container paths and MEDIA: markers do NOT render as clickable links in the dashboard. Use the managed-files download URL: `https://<HERMES_DASHBOARD_PUBLIC_URL>/api/files/download?path=<path-relative-to-/opt/data>` (e.g. `pokemon-business/reports/week-….html`); the dashboard Files tab is `<public-url>/files`. The owner's dashboard session cookie authenticates the download.

## Market knowledge bank
See `references/pokemon-market-research.md` — condensed 2026 bulk rates, buylist numbers, platform fees, sourcing/negotiation levers, and the key academic sources with evidence labels.
