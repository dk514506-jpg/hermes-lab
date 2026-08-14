---
name: neighborhood-loyalty-networks
description: "Use for neighborhood loyalty network design."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [local-marketing, loyalty, restaurants, NFC, QR, blockchain, AT-Protocol, Web3]
    category: business
---

# Neighborhood Loyalty Networks

Use when designing local customer-growth services for restaurants, bars, retailers, and other small businesses that fill slow periods and cultivate repeat customers through shared neighborhood campaigns, physical/digital collectibles, and measurable loyalty loops.

## Core framing

Position the product as a **local customer-growth and membership network**, not as an NFT or blockchain product:

> Turn unused capacity into repeat customers through shared neighborhood campaigns, collectible membership, and measurable return visits.

Behavioral loop: unused capacity → targeted invitation → visit → physical/digital recognition → permissioned follow-up → second visit → referral/network participation.

Blockchain, AT Protocol, NFC, QR, Wallet passes, and event credentials are implementation layers. Customer-facing value is access, recognition, convenience, belonging, and useful rewards.

## Evidence-first design and case-study governance

When real businesses are used as examples, treat them as public case studies—not clients, partners, endorsers, or participants—until directly confirmed. Before making a client-facing claim, create a source-linked register and label each statement `VERIFIED`, `UNVERIFIED`, `INFERENCE`, or `MERCHANT QUESTION`. Do not invent offers, prices, hours, results, testimonials, partnerships, customer counts, or participation.

Run a geography/coherence gate before designing a shared route: verify each location through an official or directly attributable source, resolve duplicate or conflicting locations, and do not name a neighborhood campaign until the participating businesses are geographically coherent. Keep unresolved location identity as an explicit blocker rather than smoothing it over in the campaign narrative.

Recommended evidence sequence:

1. Establish the business identity, official channel, location, service/category, and source date.
2. Separate direct-source facts from marketplace/search-result leads; secondary listings remain unverified until corroborated.
3. Record merchant questions covering permission, current operations, slow periods, capacity, margins, and customer-data boundaries.
4. Only then propose campaign mechanics, economics, or public-facing copy.
5. Recheck every claim before release; the source register is evidence, not endorsement.

## Multi-agent operating pattern

For research-heavy Poplar work, use a four-role council: the main Hermes agent owns decomposition, canonical synthesis, evidence acceptance, architecture, secrets, and release approval; a Hermes sub-agent performs bounded source inspection and implementation; a fast research model produces broad discovery, structured comparisons, and alternatives; and a sub-$0.50 utility model handles only mechanical extraction, tagging, deduplication, link/schema checks, and checklist QA. Every handoff must specify objective, source boundary, evidence standard, exact output path/schema, cost/time budget, forbidden actions, verification test, and escalation condition.

Never accept a sub-agent's self-report as proof: independently check the actual file, diff, URL, or structured result. Do not delegate final strategy, external publication, client contact, secrets, privacy/legal judgment, budget commitments, production deployment, destructive changes, or final acceptance of work an agent created itself.

### Proven execution sequence

When the user authorizes proceeding after a geography or scope decision, execute rather than re-opening settled questions:

1. Record the decision in the architecture-of-record, decision log, and relevant research dossier; preserve unresolved merchant permission as a separate gate.
2. Convert evidence into a campaign brief, operations architecture, and merchant-validation interview instrument before building.
3. Build a reversible, self-contained concept prototype from those approved artifacts. Mark it visibly as a concept and public-example demonstration.
4. Keep real businesses as hypotheses: do not invent offers, prices, hours, results, endorsements, or participation. Exclude out-of-scope locations explicitly rather than leaving ambiguous references in copy.
5. Independently verify the artifact on disk and in Git. Check required sections, required entities, scope boundaries, disclaimer text, absence of data-capture/outreach hooks, and JavaScript syntax. For inline scripts, extract the script to a temporary `.js` file and run `node --check`; process substitution may fail because Node needs a real filesystem path.
6. Report exact artifact paths, verification results, and commit IDs. Do not call an ad-hoc verifier a project-wide test suite when no canonical suite exists.

For the Lakeview/N Broadway pattern, use Poplar-owned web + QR and a private operational ledger as the default pilot architecture; keep AT Protocol/Atmosphere components optional until app-level maturity, privacy, export, moderation, and fallback checks are complete.

## Concept integrity and abstraction control

Treat the approved campaign brief and operations architecture as the semantic contract. Before extrapolating a prototype, write down the authorized mechanic and preserve its vocabulary. A shared neighborhood layer may connect independent locations without implying a fixed sequence, but do not silently upgrade a passport/progress/check-in model into a universal points, credits, balance, or prize economy. That stronger abstraction creates new assumptions about valuation, funding, liability, transferability, thresholds, inventory, expiration, and cross-merchant settlement. If those ideas are useful, label them as a separate hypothesis and ask for approval; otherwise use the source vocabulary: marks, stamps, codes, check-ins, recorded visits, progress, configured offers, events, rewards, return prompts, cross-visits, and referrals.

For concept-only presentation copy, increase descriptiveness through fictional scenarios, visitor states, illustrative roles, and operational questions—not invented business facts or new economic mechanics. Keep independent partner examples independent: the shared layer can provide discovery and progress while each merchant retains its own service, approval, offer, and verification boundaries.

## Design principles

1. Measure incremental off-peak visits, redemption, second visits, contribution margin, referrals, and staff effort—not token issuance.
2. Use the lowest-friction layer for each job: QR fallback; Wallet for everyday utility/notifications; NFC for tactile interaction; walletless credentials for collectibles; POAP-style credentials for attendance; AT Protocol for public portable records.
3. Make the physical artifact emotionally valuable: custom stamps, special paper, numbered cards, coins, pins, tokens, and event relics make progress visible and shareable.
4. Control reward economics with slow-period windows, minimum spend, profitable behaviors, referral conditions, and expiring return windows.
5. Protect privacy: public records describe businesses, offers, events, routes, and opt-in achievements; keep customer identity, contacts, exact visits, spending, and segmentation private by default.
6. Do not confuse AT Protocol with a blockchain. AT provides signed repositories, DIDs, Lexicons, federation, and portability; it does not provide global consensus or native payment settlement.
7. Prototype the experience before infrastructure: 3 businesses, paper passports, stamps, QR pages, and a private ledger first; add credentials, Wallet passes, and AT records only after the visit/return loop works.

## Recommended architecture

### Pilot

- One neighborhood and 3–5 businesses
- Serialized paper passport with custom stamps
- Merchant QR codes and mobile pages
- Shared passport progress page
- Private event/redemption database
- One slow-period campaign per business
- Follow-up and second-visit offer
- Simple merchant reporting

### Production hybrid

- Physical passport, NFC card, or merchant plaque with QR fallback
- Apple Wallet/Google Wallet pass for utility, status, and notifications
- Walletless digital credential via Crossmint or equivalent
- POAP-style event attendance collectible
- Private CRM/redemption database
- Public business/event/offer records in AT Protocol
- App View for map, routes, pages, and public collections
- Optional secure NFC for scarce/high-value artifacts

## Physical authenticity

Basic NFC tags should open a server URL and identify the object; never put sensitive data or valuable secrets directly on a cheap tag. Validate valuable claims server-side with account/session checks, one-time codes, rate limits, and redemption history.

For premium passports or scarce rewards, secure NFC such as NTAG 424 DNA can generate tap-unique authenticated messages using AES-128/Secure Dynamic Messaging. Specialty ink, embossing, UV marks, microtext, serials, and holograms are visual/anti-counterfeit layers, not cryptographic signatures unless a trusted reader verifies them.

## AT Protocol design

Give the agency, neighborhood, and participating businesses DIDs/handles. Define custom Lexicons for `business`, `offer`, `event`, `stamp`, `route`, `challenge`, and `reward`. Store public profiles, events, offers, stamp designs, routes, and opt-in achievements as signed records. Render them through an App View into webpages, maps, merchant pages, and collections. Use standard.site for interoperable publishing where useful. Keep private customer and transaction data off the public network. Anchor to a conventional blockchain only when portable ownership, external verification, or shared settlement justifies added complexity.

AT records are structured signed data, not HTML stored on-chain; webpages are rendered by an App View or normal frontend.

## Campaign templates

- **Slow-Period Pass:** visit in a defined off-peak window, receive a stamp/credential, unlock a return offer within 7–14 days.
- **Neighborhood Passport:** collect merchant stamps and complete a route across complementary businesses.
- **Event Relic Series:** each event yields a physical artifact plus attendance credential; completing a series unlocks access.
- **Founding Cohort:** numbered first-100 passports with durable status, member events, and referral privileges; never market them as investments.
- **Cross-business challenge:** reward visits across multiple merchants, not only repeat purchases at one business.

## Required reporting

For every pilot report distribution/source, scans/taps, claims, redemptions, incremental off-peak visits, average ticket, repeat visit at 14/30/60 days, referrals, opt-ins, estimated contribution margin, campaign cost, artifact cost, and staff time. Compare against a baseline/control period whenever feasible.

## Pitfalls

- Selling “NFT coupons” instead of a measurable customer relationship.
- Building a custom PDS, App View, relay, smart contract, or payment rail before validating the physical/digital ritual.
- Publishing identifiable customer trails by default.
- Treating a copied QR/NFC URL as authenticity proof.
- Adding dedicated NFC payment hardware before POS and volume justify certification/integration.
- Assuming AT Protocol automatically supplies discovery, rendering, moderation, payments, or permanence.
- Using discounts that acquire bargain hunters but do not create profitable repeat behavior.
- Making customers download an app or manage crypto wallets for routine loyalty.

## References

See `references/atproto-passport-architecture.md` for protocol, physical-authenticity, and hybrid-stack research notes.
