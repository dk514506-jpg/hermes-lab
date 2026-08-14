# AT Protocol Neighborhood Passport Notes

## Protocol facts

AT Protocol uses DIDs, domain handles, signed data repositories, Merkle Search Trees, Lexicons, PDSes, relays, and App Views. Repository updates are self-authenticating and verifiable; AT records are structured data, not HTML stored on a blockchain. Public records can be rendered by an App View into merchant pages, maps, event views, and collections.

Custom Lexicons can define interoperable records for businesses, offers, events, stamps, routes, challenges, and rewards. Namespaces are published through domain-based DNS TXT records. The emerging `standard.site` Lexicons show how independent publishing applications can share records and receive enhanced rendering in Bluesky-compatible clients.

AT Protocol is not a conventional blockchain: it has no global consensus transaction order, native token settlement, or automatic permanence guarantee. Use a separate chain only when portable ownership, external verification, or settlement clearly justifies the added cost.

## Physical authenticity

A basic NFC tag is a physical-to-digital pointer/identifier, not cryptographic proof. Use server-side validation, accounts or one-time codes, rate limits, and redemption history for valuable rewards. QR is the universal fallback.

NXP NTAG 424 DNA supports AES-128, Secure Unique NFC/Secure Dynamic Messaging, tap-unique authenticated URLs, counters, encrypted data, and mutual authentication. This is appropriate for scarce founding passports, premium artifacts, anti-counterfeit rewards, or high-value access—not ordinary low-value stamps.

Special paper, UV ink, microtext, embossing, serials, holograms, and custom stamps provide visual ritual and anti-counterfeit cues. They become cryptographic signatures only if a trusted digital system verifies a cryptographic component.

## Suggested hybrid architecture

```text
paper passport + custom stamp + NFC/QR
  → verification API
  → private redemption/CRM event ledger
  → optional Crossmint walletless credential or POAP-style event credential
  → Apple/Google Wallet update
  → public AT business/event/offer/opt-in achievement record
  → App View renders neighborhood pages and passport routes
```

Keep customer contact details, exact visit trails, purchase data, and segmentation private by default. Publish business profiles, events, offers, stamp designs, routes, aggregate activity, and explicitly opt-in achievements.

## Prototype order

1. Three local businesses, paper passport, custom stamps, QR pages, private ledger, and one slow-period/second-visit campaign.
2. Add NFC passport card or merchant plaques and walletless credentials.
3. Add Wallet passes and event collectibles.
4. Define and publish custom Lexicons; create business identities and an App View.
5. Add secure NFC and external blockchain anchoring only after demand and economics justify it.

## Research sources

- AT Protocol overview: https://atproto.com/guides/overview
- AT data repositories: https://atproto.com/guides/data-repos
- AT self-hosting: https://atproto.com/guides/self-hosting
- Publishing Lexicons: https://atproto.com/guides/publishing-lexicons
- AT stack: https://atproto.com/guides/the-at-stack
- Standard.site interoperability: https://atproto.com/blog/standard-site-bluesky-timeline
- NXP NTAG 424 DNA datasheet: https://www.nxp.com/docs/en/data-sheet/NT4H2421Gx.pdf
- Bluesky AT Protocol overview: https://docs.bsky.app/docs/advanced-guides/atproto
