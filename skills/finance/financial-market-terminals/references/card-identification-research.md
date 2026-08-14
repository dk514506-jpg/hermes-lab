# Card identification and valuation research

## Operating conclusion

Use photo recognition as a candidate-generation and lookup accelerator. Do not let a recognition result write directly to the canonical instrument master, price history, purchase ledger, or buy decision. Preserve the image/result evidence and require human confirmation of identity, variant, language, raw condition or graded identity, and exit path.

## Commercial examples reviewed

- **TCGplayer mobile app** — provider documentation says the app scans cards, shows current Market Price, supports all TCGs on its marketplace, and can upload scanned inventory for eligible sellers. Strong first pilot because it is directly tied to a US marketplace; not proof of condition accuracy or API availability.
- **PokeScope** — Pokémon-focused scanner claiming instant identification and prices from TCGplayer, eBay, CardMarket, and other sources. Useful candidate for a Pokémon-specific pilot; claims are provider-reported and need measurement.
- **Ludex** — broad sports/TCG scanner claiming photo identification and daily-updated prices. Useful comparison tool; app-store feedback includes warnings that some displayed prices can be materially wrong, reinforcing the human gate.
- **Pokéllector** — Pokémon collection/scanner product with prices and history from around the web. Useful identity/collection reference; not sufficient as the business valuation source without comp inspection.
- **PriceCharting photo search** — image search can help identify cards and then surface ungraded/graded guide values. Useful fallback, especially for vintage; generic ungraded values are not automatically NM.
- **Ximilar** — API-oriented collectible recognition provider describing card detection/cropping, Pokémon recognition in English/Japanese/Chinese, OCR, grading, and pricing add-ons. Consider only after terms, cost, latency, and benchmark results are reviewed.
- **CardSight** — API-oriented provider claiming multi-card detection, slab recognition, parallel recognition, and source-linked pricing. Consider as a custom integration candidate; verify coverage, terms, and the claimed accuracy on our cards.

## Technical patterns

- Commercial apps generally combine card detection/cropping, OCR or visual matching, canonical card catalog lookup, and a price-source lookup.
- Collectors describes a progression from perceptual hashing to ORB/keypoints and then CNN feature vectors plus approximate-nearest-neighbor search for high-volume card identification. This supports a future visual-search architecture but is not a reason to build custom CV before the pilot.
- Ximilar and CardSight represent the API/service path: outsource recognition and maintain our own canonical identity, provenance, and decision layer.
- A Stanford CS231n Pokémon detection paper shows pretrained vision models can detect cards, but sleeves, glare, occlusion, backs, and multiple-card scenes remain practical failure modes.
- A grading preprint describes controlled imaging, alignment, flat-field correction, classification, and defect detection. It supports the distinction between identity and condition, but phone photos should not be treated as professional grading.
- Apple Vision OCR provides text plus confidence on-device. OCR is useful for names/numbers/cert labels but does not by itself solve exact variant matching.
- Human-in-the-loop guidance supports confidence thresholds and escalation to a reviewer when the model is uncertain.

## Pilot protocol

Test 50–100 cards across vintage, modern, holo/reverse holo, full-art, Japanese/English, and slabbed cards. For every attempt record true identity/source, top candidate/confidence, time to result, manual correction, variant/language accuracy, raw condition or grader/cert handling, price-source availability, false-positive type, and whether the result would have changed the buying decision.

Choose by **correct accepted decisions per minute**, not recognition speed alone. A useful provider must save time after correction and pricing verification, not merely produce a fast plausible name.

## Integration design

1. Phone capture creates an image file and hash.
2. Provider result is stored in `card_image_candidates` with provider, OCR, candidate ticker, confidence, grade fields, and source IDs/URLs.
3. High-confidence results prefill the store-visit form; medium/low results become `needs_review`.
4. Human confirms card identity and condition/grade; only then is `resolved_ticker` set and an observation eligible for import.
5. Price observations retain `sale_type`, listing ID, and URL where available.
6. Accepted cards enter normal purchase/extraction accounting separately.

## Source hierarchy for valuation

Use confirmed buylist quotes and realized business sales first. Then use multiple exact-match completed marketplace sales. Then use aggregated guides such as Card Hedge or PriceCharting. Active asks are replacement-cost context, not proof of executable proceeds. A latest sold listing is evidence, not a universal true value. Use condition/grade-matched samples with median, low/high, usable count, recency, and net-of-fees/shipping/reserve calculations.

## Caveats

All commercial performance and accuracy statements above are provider-reported unless explicitly identified as a research or professional engineering source. The project has not yet run the pilot or validated provider terms/API access. TCGplayer’s current developer documentation states that new API access is not being granted, so do not design around a new TCGplayer API credential without confirming access.

## Sources

1. https://seller.tcgplayer.com/mobile-app
2. https://pokescope.app/
3. https://www.ludex.com/faq/
4. https://apps.apple.com/us/app/pokellector-card-collector/id600580227
5. https://www.pricecharting.com/page/app
6. https://blog2.collectors.com/image-search/
7. https://www.ximilar.com/blog/build-your-own-trading-card-game-identifier-with-our-api/
8. https://cardsight.ai/solutions/identification
9. https://cs231n.stanford.edu/2024/papers/real-time-pokemon-card-detection-from-tournament-footage.pdf
10. https://www.researchsquare.com/article/rs-8098898/v1.pdf
11. https://developer.apple.com/documentation/vision/recognizing-text-in-images
12. https://www.onlogic.com/blog/human-in-the-loop-machine-learning
13. https://ai.cardhedger.com/price-guide/category/pokemon
