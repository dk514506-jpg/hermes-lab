---
name: business-ops-design
description: "Use when designing a small business ops/tracking system."
---

# Small-Business Operations Design (buy / process / sell)

Design an operating system for a small physical business where the agent is the integral back office: data capture, reconciliation, reporting, decision support. Deliverable is a research-backed design memo the business can build from. Session-specific domain knowledge lives in `references/` (e.g., `references/pokemon-tcg-venture.md`).

## When to use
- "Design a tracker/system for my X business", "how do we track Y efficiently", "maximize time as money"
- User expects: background research with real sources, a design memo, and a tech stack they can actually build

## Method

### 1. Research before design (the user often asks for this explicitly)
- Academic + practitioner split. Academic: search journals directly (web_search with paper/author terms); verify citation details by fetching the full text or citation page — never cite from a snippet alone. Practitioner: buylists, API docs, industry reports, fee schedules — the actual numbers the business runs on.
- **Evidence-label every source** (VERIFIED = fetched; UNVERIFIED = search record only; RECONSTRUCTED = inference beyond source). Flag vendor-reported stats (Gartner/McKinsey/secondary reports) as directional, not doctrine.
- Deliver a numbered annotated bibliography as a memo section — one annotation per source saying WHAT it is used for, plus the label.

### 2. Memo structure (proven shape)
1. Executive summary — the 3–4 research-grounded economic facts that drive everything
2. Business organization implied by the economics (roles; agent-as-back-office split: human does physical work, agent does information work)
3. Process architecture P0..Pn — each stage with its time-as-money innovation and its data capture
4. Data model + KPI set
5. Tech stack (small-business defaults below)
6. Implementation roadmap (phased, week-sized)
7. Risk register
8. Sources + annotated bibliography

### 2a. Strategy-document handoff
When the user asks to compile a business concept into a strategy document, produce the artifact rather than only summarizing the conversation. The document should combine the business proposition, customer/merchant marketing strategy, product architecture, software and hardware choices, operating model, KPIs, phased workstream, pilot design, validation gates, risks, and source notes. Write it to the requested durable location, then verify existence, size, and the presence of the major requested sections before reporting completion. If a delivery or upload step is blocked by authentication or platform setup, report the blocker plainly and give the exact next credential/setup action; do not claim the artifact was published remotely.

### 3. Time-as-money patterns (the creative core)
- **Exception-based processing:** per-item attention ONLY on the value pile; the bulk flows without individual handling (e.g., the Pokémon "$1 Rule": only pulled cards get scanned — 50 × $1–5 items can outvalue 4,950 bulk items).
- **Capture where time is cheapest:** at the expensive location (show floor, field), capture photos + voice notes only; do data entry at home in one batch. Never type on the clock.
- **One-touch flow + route-zoned storage:** travel time dominates picking cost (order-picking literature, de Koster et al. 2007); store by destination so packing pulls from one zone with zero re-sorting; each item handled once per stage.
- **Work-measurement feedback:** log stage timestamps; compute standard time (observed × rating ÷ (1 − allowance)) and $/hour per stage after ~4 weeks; kill or redesign stages under target.
- **Defaulted routing, exceptions only:** the operator sees anomalies, not routine decisions.

### 4. KPI selection
Master metrics: margin-return-on-inventory (GMROI = gross margin ÷ avg inventory cost), value-recovery/extraction rate, per-venue/per-vendor margin, channel mix, inventory turnover days, $/hour per process stage. Pick one "single most informative number" per business (e.g., extraction rate = extracted value ÷ purchase price).

### 5. Tech stack defaults for a 1–2 person business
- SQLite as single source of truth (single file, zero ops) + a phone-friendly capture surface (Google Sheets) synced nightly by script
- Pricing/market data via official APIs where available (e.g., TCGplayer category 3, PriceCharting); scraper fallback flagged as lower-trust
- Cron for the weekly reconcile + report generation; the agent executes the runs and produces the reports
- Git-versioned repo for schema + scripts; additive migrations
- **Clean-room verification rule (hard-won):** any reconciliation/verification script must (a) use relative paths only — zero machine-specific references, (b) have pinned, documented deps (requirements.txt + uv/venv), (c) be run in a clean checkout before it is trusted. A gate that only passes on your machine manufactures false confidence.

### 6. Domain knowledge bank
Session-specific research and project state go in `references/` — condensed numbers, source attribution, business structure, pending inputs, roadmap. Keep SKILL.md generic; keep the domain in references.

## Pitfalls
- **Deliver the research synthesis immediately, in the same response arc.** When the user asks you to "do research" as part of the engagement, produce the synthesized findings (numbered levers, benchmarks, sources) in that turn — not "I did research, we'll hash it out later." Deferring the synthesis reads as having skipped the deliverable; the user will (rightly) ask "did you actually do any research?"
- Don't build tooling before the economics are understood — the rate table / buy-sheet is the load-bearing input; parameterize the system around it.
- Don't skip the annotated bibliography when the user asked for research.
- Don't claim a system is "verified" until the gate passes in a clean environment — for the full audit/repair mechanics (portable resolvers, SKIP-vs-FAIL, anti-drift manifests, clean-room CI), see the `clean-room-verification` skill.
