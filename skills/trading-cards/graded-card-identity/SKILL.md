---
name: graded-card-identity
description: Identify graded cards from cert numbers.
category: trading-cards
---

# Graded Card Identity Resolution

## When to use

You have cert numbers (PSA/BGS/SGC slabs) and need card identity: name, set, number, grade, population, label details.

## Solution space (throughput)

### 1. Batch API (fastest, needs key)

**Card Hedge** — `POST /v1/cards/details-by-certs`: up to 100 certs/req, `X-API-Key` header. Returns card desc, set, number, grade. Signup: `ai.cardhedger.com/signup` — 7-day free trial, then $49/mo. Covers Pokémon TCG, sports, Magic, 3.8M+ cards.

### 2. Official grader API (authoritative, needs account)

**PSA Public API** — `api.psacard.com/publicapi`. Bearer token, needs PSA account. Use `GetByCertNumberForFileAppend` — returns SetName + population. Main `GetByCertNumber` does NOT include SetName. Free tier ~100/day. **BLOCKER: requires PSA account.**

### 3. Photo-based AI (needs slab photos)

**Ximilar** — upload slab photo → card identity + grade + cert number + price_stats. Paid.

### 4. Manual browser (fallback, slow)

Go to `https://www.psacard.com/cert/{cert}/psa` directly. Use browser_console to extract DOM JSON. ~15–30 certs/hr. **Warning:** selenium/requests against psacard.com triggers PerimeterX (SO 75209763). Manual browser is intended path.

### 5. Offline DB cross-reference (supplementary)

`github.com/PokemonTCG/pokemon-tcg-data` — set+number → card name.

## Halting principle

Search until one clear winner emerges, remaining options are marginal, blocked-path evidence exists, and you know auth/$$ cost.

## TOS

- PSA Public API: official, sanctioned. Read EULA.
- Card Hedge: third-party, own TOS. Free trial.
- Automated scraping psacard.com: blocked by PerimeterX. Don't.
- Reddit OC scrape datasets: TOS-violating. Cross-reference only with legal awareness.

## References

See `references/` directory.
