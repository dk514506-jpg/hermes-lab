# Atmosphere + owned-web stack map for Poplar.agency

## Executive recommendation

Use a deliberately split stack rather than trying to make one product do everything:

- **Front office:** an owned, conventional website with **Inlay** installed if access is available; use it as the client/site editing layer. Keep the public domain, markup, CSS, routes, and hosting under Poplar/client control.[5]
- **Community / relationship layer:** pilot **Roomy** for Poplar’s internal/client community and neighborhood cohorts. Treat it as an experimental Atmosphere-native collaboration space, not the system of record.[1][2]
- **Back office:** use **NocoDB** (or Appsmith over Postgres) for a practical CRM, client pipeline, campaign tracker, venue inventory, and service operations. NocoDB is the faster database-shaped starting point; Appsmith is stronger when custom workflows and operational UIs are needed.[11][12]
- **Email:** start with **Plunk** for transactional + lifecycle messaging, or **Keila** when newsletter/editorial workflows and privacy-first campaign authoring matter more. Keep **comail** as a strategic Atmosphere experiment, not the only outbound channel.[9][13][14]
- **Automation:** use **Airglow** for low-risk event-driven AT Protocol automations (e.g., cross-posting, logging, record creation); do not make it the core business workflow engine until reliability, ownership, and data retention are proven.[8]
- **Identity/data ownership:** defer running a Poplar PDS until there is a concrete need for portable identities or a neighborhood social product. Self-hosting a PDS is feasible, but AppViews/relays are materially more resource-intensive.[6][7]

## Decision table

| Tool | What it is / best use | Poplar placement | Decision |
|---|---|---|---|
| **Inlay** | Embedded editing layer inside a developer-built site: click-to-edit real page content, drafts, comments, notes, activity, restore points, collections, scheduled publishing, server-side auth/validation.[5] | Front office | **Best-fit front-office experiment / likely default** if private access and operational maturity check out. It preserves the agency’s design system instead of replacing it with a builder. Caveat: site says it is privately distributed and not self-installable today.[5] |
| **Roomy** | Atmosphere-native “freeform communications playground,” with chat-to-thread-to-space structure and shared AT Protocol identity/membership possibilities.[1] | Client/community layer; internal coordination | **Pilot.** Good for a high-context neighborhood cohort, creative working group, or client council. Do not replace CRM/project records; its value is sociality and sense-making, not deterministic operations. |
| **Skilld / Plasma** | Sovereign operational AI platform: event→decision→action with traceability, on customer infrastructure; EUPL and self-hostable. Skilld claims production deployments since 2018, and offers managed operation.[3] Plasma Cloud pricing is €15k onboarding plus per-node monthly fees.[4] | Back office / optional later | **Reference architecture, not near-term purchase.** Too heavy for Poplar’s initial scale, but valuable as a model for auditable “situations,” staged Observe→Propose→Execute authority transfer, and owned operational data. |
| **ATP.tools** | Search results did not reliably resolve a distinct Atmosphere / AT Protocol product; the strongest hit was Allied Tool Products, an unrelated industrial-tool company.[unverified] | None | **Do not adopt yet.** Confirm exact URL/name before evaluating. The likely intended tool may be another AT Protocol project. |
| **PDS (AT Protocol)** | Personal Data Server stores AT Protocol repositories/identity; official docs support self-hosting and account migration. PDS is the most approachable self-hosted layer; relays are bandwidth-intensive and AppViews resource-intensive.[6][7] | Identity/data layer | **Later / only with a product reason.** Consider for Poplar-owned identity, neighborhood directory, or portable loyalty graph. Start with a hosted PDS and domain handles before operating infrastructure. |
| **comail** | Cooperative email infrastructure for atproto: custom-domain identity, shared SMTP relay, dual DKIM, sender warming, signed operator/member labels; currently one relay and federation is roadmap.[9] | Email / optional experiment | **Watch + small pilot.** Interesting for domain-owned, cooperative sending reputation and Atmosphere-native identity. Not yet a mature sole ESP; maintain a normal fallback (Plunk/Keila). |
| **Airglow** | AT Protocol event automations: listen to Jetstream, match lexicon/conditions, then webhook, write a PDS record, or post to Bluesky.[8] | Automation / optional experiment | **Pilot low-risk workflows.** Good for event fan-out and cross-app glue; keep business-critical writes in a directly owned database with retries/audit logs. |
| **Aether** | Earlier open-source peer-to-peer Reddit-like communities without servers, with public moderation/audit concepts; the cited project’s funding essay is from 2019.[10] | Optional experiment / research | **Do not build on it now.** Useful conceptual precedent for community-owned, non-extractive spaces and moderation transparency; verify current maintenance and compatibility before any commitment. |
| **Appsmith** | Open-source low-code platform for custom internal apps, data-backed UIs, workflows, integrations, RBAC/audit/SSO in enterprise tiers.[11] | Back office | **Strong alternative / complement.** Use when operations need custom screens, approvals, dashboards, or API actions rather than spreadsheet-like records. |
| **NocoDB** | Spreadsheet interface over new or existing Postgres/MySQL, with grid/Kanban/gallery/form/calendar views, APIs/SQL, and operational use cases.[12] | Back office | **Best practical starting point.** Model clients, venues, campaigns, offers, assets, deliverables, contacts, and outcomes in Postgres-backed tables; add Appsmith only for workflows that outgrow views/forms. |
| **Plunk** | AGPL open-source/self-hostable email platform for transactional email, campaigns, workflows, segments, analytics, inbound email, and custom domains; advertises $0.001/email and unlimited contacts.[13] | Back office / client communications | **Default email candidate.** Strong lifecycle automation and product-email fit. Verify deliverability, unsubscribe/consent, backups, and operational burden before production. |
| **Keila** | Open-source newsletter platform with visual/Markdown/MJML authoring, forms, segmentation, API, privacy controls, and self-hosting.[14] | Front-office content marketing / email | **Choose for editorial newsletters.** Better than Plunk when clients need polished, recurring newsletters and hands-on campaign editing. |
| **Outline** | Open-source team knowledge base/wiki with collaborative editing, comments, search, integrations, custom domain, and self-hosting.[15] | Back office knowledge | **Useful optional companion.** Good for Poplar playbooks, client onboarding, campaign retrospectives, SOPs, and research. Keep canonical operational records in the database. |

## Front office

### Recommended shape

1. **Public site:** Poplar-owned code, domain, analytics, forms, and hosting.
2. **Editing:** Inlay where available. Its key advantage is that editors work directly in the real page/CSS, with drafts, comments, collections, SEO templates, scheduled publishing, and restore points.[5]
3. **Editorial email:** Keila for newsletter-heavy clients; Plunk for transactional/lifecycle messages.[13][14]
4. **Community:** Roomy as a branded/high-touch space for neighborhood cohorts, not as the public website.[1]
5. **Optional Atmosphere identity:** custom-domain AT handle / hosted PDS first; self-host only once the use case is validated.[6]

### Why this matters for an agency

Inlay’s model is particularly aligned with Poplar: the agency still owns design and implementation quality, while clients get a low-friction editing experience. It is not a generic website builder; the vendor explicitly says the developer builds markup/CSS/routes/hosting and the editor adds editing.[5]

## Back office

### Minimum viable operating system

- **NocoDB/Postgres:** clients, prospects, venues, contacts, campaigns, offers, events, assets, invoices, tasks, permissions, and outcome metrics.[12]
- **Appsmith:** custom intake, campaign launch checklist, approval console, reporting dashboard, and integrations where forms/views are insufficient.[11]
- **Outline:** SOPs, playbooks, client briefs, creative standards, and decision logs.[15]
- **Plunk:** automated lead acknowledgement, onboarding, reminders, event confirmations, and lifecycle sequences.[13]
- **Airglow/webhooks:** only non-critical cross-posts and AT record fan-out initially.[8]

### Data boundary

The operational database should remain the source of truth for client and campaign state. AT Protocol/PDS records can be a portable social/community projection, not the authoritative ledger. This avoids coupling revenue-critical operations to an emerging ecosystem and preserves the ability to export/migrate.

## Optional experiments (90-day horizon)

1. **Roomy neighborhood council:** invite 10–30 trusted participants; test whether chat→threads→knowledge artifacts improves campaign collaboration versus Slack/Discord.[1]
2. **Atmosphere identity pilot:** create one Poplar custom-domain handle and test login portability across compatible apps; no PDS operations yet.[6]
3. **Airglow event bridge:** when a selected AT record appears, write an internal audit/event record and optionally notify a channel. Test retries, duplicate handling, and revocation.[8]
4. **comail sender pilot:** one low-volume opt-in list, with conventional ESP fallback; measure deliverability, complaint handling, DNS setup, and portability.[9]
5. **Inlay client pilot:** one low-risk brochure/restaurant site; test editor permissions, drafts, mobile editing, restore, SEO, forms, and handoff.[5]
6. **Plasma design exercise:** translate one Poplar recurring situation (“new lead responds,” “campaign asset late,” “offer redemption anomaly”) into Map→Observe→Propose→Execute; do not deploy Plasma yet.[3]
7. **Aether watchlist:** only research maintenance/current community; no production dependency.[10]

## Alternatives worth keeping in the comparison set

- **Community/collaboration:** Zulip or Discourse are established alternatives; Roomy itself names both as strong functional comparators.[1]
- **Back office:** NocoDB + Appsmith is the owned/open stack; a conventional managed CRM/project tool may be preferable if the agency lacks ops capacity.
- **Email:** Plunk for product/lifecycle, Keila for newsletters; Mautic/listmonk are additional mature self-hosted alternatives when marketing automation or high-volume list operations dominate.
- **Knowledge:** Outline for a polished wiki; a plain Git/Markdown knowledge base is more portable but less client-friendly.
- **Community identity:** hosted Bluesky/ATProto first; self-host PDS only when portability or branded identity creates measurable value.

## Adoption sequence

**Phase 1 — own the basics:** public website, domain/DNS, Postgres/NocoDB, backups, consent model, email provider, and simple analytics.

**Phase 2 — make the agency operable:** Appsmith internal consoles, Outline playbooks, Plunk/Keila templates, and repeatable client onboarding.

**Phase 3 — add atmosphere:** Roomy pilot, custom-domain AT identity, Airglow bridge, then comail pilot if deliverability is acceptable.

**Phase 4 — earn sovereignty:** evaluate hosted→self-hosted PDS migration; consider Plasma-like event/decision traces only where a recurring operational situation has enough volume and cost to justify it.

## Risks / unknowns

- **Product ambiguity:** “ATP.tools” could not be identified reliably from public search; do not infer its identity.
- **Private distribution:** Inlay is not publicly self-installable today; access, pricing, support, and data model need diligence.[5]
- **Emerging ecosystem:** Roomy, Airglow, comail, and Atmosphere integrations may change quickly; require export, backups, and fallback paths.[1][8][9]
- **Operational burden:** self-hosting email, PDSs, and low-code apps creates patching, backups, deliverability, abuse, and authentication responsibilities.
- **Fit mismatch:** Plasma is compelling for high-value, recurring operational decisions but likely overkill for a small agency’s first CRM/workflow layer.[3][4]

## Sources

[1] https://a.roomy.space/
[2] https://blog.roomy.space/values
[3] https://skilld.cloud
[4] https://skilld.cloud/plasma-cloud
[5] https://tryinlay.com
[6] https://atproto.com/guides/self-hosting
[7] https://github.com/bluesky-social/pds
[8] https://airglow.run
[9] https://comail.at
[10] https://aether.app/blog/2019-09-10-new-funding-model-for-oss
[11] https://www.appsmith.com
[12] https://www.nocodb.com
[13] https://www.useplunk.com
[14] https://www.keila.io
[15] https://www.getoutline.com

Note: “ATP.tools” remains unverified because public search did not yield a reliable match to a distinct tool/product.
