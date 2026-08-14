# Poplar.agency Campaign + Operations Architecture

## 1. Operating thesis

Poplar is a neighborhood customer-growth service, not a rewards-tech or NFT product. It helps a small group of complementary businesses fill unused capacity, create a reason to return, and measure whether the campaign produced profitable incremental behavior.

Core loop:

`unused capacity -> targeted invitation -> visit -> recognition/progress -> permissioned follow-up -> return visit -> referral/network participation`

The system should optimize contribution margin and staff time, not registrations, token issuance, scans, or impressions.

### Design assumptions

- Initial market: Chicago neighborhood, 3–5 independent restaurants/bars/retailers.
- Initial customer experience: paper passport + merchant QR/mobile page; no app download and no crypto wallet.
- Poplar owns campaign operations and reporting; merchants own offers, staff execution, POS transactions, and customer-facing service.
- Pilot data is private by default. Public pages contain only business, campaign, offer, and route information.
- Legal/privacy details require counsel for the exact jurisdictions and channels; this document is an operating design, not legal advice.

## 2. Shared campaign architecture

Every campaign is a versioned object with a measurable hypothesis.

### Campaign brief (required fields)

- Campaign ID, name, neighborhood, owner, participating merchants, version, status.
- Objective: e.g., increase Tuesday 4–6pm visits at three merchants.
- Audience and eligibility: geography, prior participation, age/service constraints where relevant.
- Offer rules: valid windows, minimum spend, exclusions, redemption limit, expiration, stacking rules.
- Ritual: passport stamp, numbered artifact, event credential, or wallet pass.
- Distribution: partner channels, QR placements, email/SMS/push only where permission and channel rules permit.
- Baseline period/control comparison and target thresholds.
- Budget: creative, printing/artifacts, media, Poplar labor, merchant subsidy.
- Instrumentation: campaign QR IDs, source codes, stamp IDs, redemption codes, POS reconciliation method.
- Stop conditions: margin below floor, staff burden above ceiling, fraud, complaint rate, or no evidence of incremental lift.

### Campaign lifecycle

1. Discover: merchant interview, capacity map, offer economics, baseline data.
2. Design: campaign brief, service blueprint, creative, consent copy, tracking plan.
3. Approve: merchant signs offer economics, staff procedure, data-sharing terms, and support boundaries.
4. Launch: test every QR/code, train staff, issue a one-page runbook.
5. Operate: daily exception queue; no manual attention to routine events.
6. Reconcile: match issued/stamped/redeemed events to merchant records and labor logs.
7. Learn: weekly pulse; end-of-campaign contribution-margin report and decision.
8. Archive: freeze results, retain only necessary records, record lessons for next version.

### Campaign templates

- **Slow-Period Pass:** visit during an off-peak window; earn a stamp; unlock a profitable return offer within 7–14 days.
- **Neighborhood Passport:** complete a route across complementary merchants; reward the completed behavior, not isolated discount hunting.
- **Event Relic Series:** event attendance yields a physical artifact and optional digital credential; completion unlocks access or recognition.
- **Founding Cohort:** serialized first-100 passports with durable status and member events. Never imply investment or financial return.
- **Cross-business challenge:** visit 3 of 5 businesses in a defined period; reward can be experiential, merchandise, or a controlled offer.

## 3. Service catalog

### Tier A — Campaign Sprint (fixed-scope)

**Deliverable:** campaign brief, offer economics, creative/QR kit, staff runbook, tracking setup, launch, and post-campaign report.

**Merchant supplies:** baseline sales/traffic proxy, offer approval, staff champion, POS/reconciliation export where available.

**Success gate:** all instrumentation tested; staff can execute in under 30 seconds per eligible visit; target economics signed off.

### Tier B — Campaign Operations Retainer

**Deliverable:** calendar management, partner coordination, creative refreshes, exception handling, weekly pulse report, monthly business review.

**Boundary:** Poplar operates the campaign system; it does not become the merchant's general manager, customer-service desk, ad-account owner of record, or POS support provider.

### Tier C — Neighborhood Network Program

**Deliverable:** multi-merchant route, shared passport/credential system, cross-merchant reporting, events, and network-level learning.

**Commercial model:** platform/operations fee plus transparent campaign costs; merchant-level results and network-level results are separated.

### Add-ons

- Physical artifact design/production.
- Wallet pass issuance/update (after pilot validation).
- Event production.
- POS integration or data reconciliation.
- Creative production and paid media management.
- Secure NFC/authenticated premium artifacts only when the value and fraud risk justify it.

## 4. Human/service operating model

### Poplar roles

- **Account/campaign lead:** scope, merchant approvals, economics, weekly decision.
- **Field operator:** installs QR/signage, trains staff, audits physical artifacts, photographs evidence.
- **Creative/content:** campaign identity, offer copy, print and mobile assets.
- **Data/ops:** event ledger, reconciliation, QA, reporting, retention/deletion jobs.
- **Engineering (fractional):** deploys stable primitives, access control, integrations, incident response.

One person may hold several roles initially, but every campaign must have named owners.

### Merchant roles

- Designated champion and backup.
- Staff executes the stamp/scan/redemption script.
- Merchant owns offer validity, inventory/availability, POS truth, refunds, customer complaints about food/service, and compliance with its sector obligations.

### Standard operating rhythm

- Monday: capacity/offer review and upcoming campaign exceptions.
- Daily during live campaigns: automated anomaly queue; 10-minute operator check.
- Weekly: merchant pulse (distribution, participation, redemptions, staff friction, early repeat signal).
- End: reconciliation, margin calculation, learnings, renewal/stop decision.

## 5. Hardware and software stack

### Pilot stack (recommended)

- Serialized paper passports, custom stamps, table tents/window decals.
- QR codes resolving to short, campaign-specific server URLs; every placement has a source ID.
- Mobile web pages; responsive, low-bandwidth, no app download.
- Managed database (Postgres) or SQLite for a very small single-operator pilot; versioned schema and additive migrations.
- Admin console with role-based access; merchant view limited to its own records.
- CSV/POS exports before direct integrations.
- Transactional email provider only after consent and unsubscribe flows are tested.
- Git repository, staging environment, backups, error monitoring, and scheduled reports.

### Production hybrid (only after proof)

- Paper/NFC physical artifact with QR fallback.
- Apple Wallet/Google Wallet pass for utility, status, and permitted notifications. Apple documents passes as dynamic representations of paper/plastic items, including store cards, coupons, tickets, and generic passes; creation, signing, distribution, and updates require a server workflow.
- Walletless digital credentials for collectible/attendance use cases; avoid requiring a wallet for routine loyalty.
- Optional AT Protocol public records for business, offer, event, route, stamp design, and opt-in achievement objects. Keep customer identity, exact visits, spending, and segmentation private.
- Secure NFC (e.g., authenticated dynamic messages) only for scarce/high-value artifacts; ordinary NFC is a locator, not proof of authenticity.

### Explicit non-goals for v1

No custom mobile app, custom blockchain, custom PDS/App View/relay, payment rail, NFC payment terminal, or automated POS integration before campaign economics and staff workflow are validated.

## 6. Core data model

Use opaque UUIDs; separate tenant/merchant access at every query boundary.

- `organizations`: Poplar, merchants, vendors; legal name, timezone, status.
- `users`: staff/admin identities, role, organization, MFA state.
- `merchants`: profile, address, hours, capacity notes, POS system, operating contacts.
- `campaigns`: objective, dates, hypothesis, status, owner, version, budget, baseline/control definition.
- `campaign_merchants`: merchant-specific role, offer, capacity window, approved copy, economics.
- `offers`: validity, min spend, exclusions, inventory cap, funding split, expiration, terms.
- `artifacts`: type, serial, batch, issued timestamp, status, optional secure-element metadata; never store secrets on a cheap tag.
- `placements`: QR/source code, location/channel, campaign version, active interval.
- `participants`: pseudonymous participant ID, optional contact endpoint, source, consent status; avoid collecting name unless needed.
- `consents`: participant, purpose, channel, notice/version, timestamp, method, withdrawal timestamp, evidence.
- `events`: immutable event ledger: scan, issue, stamp, claim, redemption, referral, attendance; actor/source, campaign, merchant, timestamp, device-risk signals, idempotency key.
- `redemptions`: offer, merchant, participant, event, POS reference, gross sale band/amount where permitted, refund/void state.
- `communications`: message, audience rule, channel, consent snapshot, send/delivery/unsubscribe/complaint status.
- `labor_logs`: campaign, stage, person, start/end, exception type; used to price operations.
- `costs`: production, media, labor, subsidies, vendor fees, merchant co-funding.
- `reports`: immutable report version, inputs, calculation version, generated timestamp, recipients.
- `audit_log`: actor, action, object, before/after hash or diff, timestamp.

Rules: event records are append-only; corrections are compensating events. Every externally triggered event has an idempotency key. Raw contact data is separated from analytics and encrypted/access-controlled.

## 7. Consent, privacy, and security

- Collect the minimum needed: a pseudonymous participant ID is sufficient for stamps; contact information is optional and purpose-specific.
- Present a short, plain-language notice at capture: what is collected, why, who receives it, retention, and how to withdraw/delete.
- Keep purposes separate: campaign operations, service communications, and marketing. Do not silently turn a stamp into marketing permission.
- Record consent evidence with purpose, channel, notice version, timestamp, and withdrawal. Unsubscribe/withdrawal must be as easy as opt-in; suppress immediately.
- Do not publish identifiable customer trails, exact visit histories, spending, or segments. Public records are limited to business/offer/event/route data and explicitly opt-in achievements.
- Treat QR/NFC URLs as discoverable and copyable. Validate claims server-side with session/participant checks, one-time or rate-limited redemption, expiration, and redemption history.
- Merchant staff receive least-privilege accounts; MFA for admins; no shared passwords; quarterly access review.
- Encrypt in transit and at rest where supported; secrets in a managed secret store, never in tags, QR payloads, source control, or reports.
- Retention schedule: raw operational events only as long as needed for reconciliation/disputes; aggregate campaign metrics retained longer; delete/anonymize on schedule and on valid request subject to legal/accounting exceptions.
- Incident plan: detect, contain, preserve evidence, assess affected data, notify merchant/processor/users/regulators as required, rotate credentials, and document a postmortem.

FTC small-business guidance frames a sound data-security plan as take stock, scale down, lock it, pitch it, and plan ahead. ICO PECR guidance is a useful reminder that electronic marketing by phone, email, or text has channel-specific requirements; for Chicago operations, apply the relevant US federal/state/local rules and counsel review rather than copying UK rules.

## 8. Reporting and KPI contract

Every report must show definition, numerator/denominator, source, date range, exclusions, and confidence/limitations.

### Funnel

- Distribution/source: placements, impressions where available, QR scans/taps by source.
- Participation: unique participants, issued passports, stamps/claims, completion rate.
- Conversion: redemptions, redemption rate, average ticket or spend band, void/refund rate.
- Return: second visit at 14/30/60 days; cohort definition and baseline comparison.
- Economics: incremental contribution margin, campaign cost, artifact cost, merchant subsidy, Poplar labor, cost per incremental visit, payback.
- Network: cross-merchant completion, referrals, merchant retention, concentration risk.
- Operations: staff seconds per event, exception rate, support tickets, data completeness, fraud/duplicate rate.

### Decision thresholds (set per campaign)

Before launch, record a margin floor, maximum staff burden, target incremental visits, acceptable redemption cost, and stop threshold. Do not call a visit “incremental” merely because it had a QR scan; use a baseline period, source cohort, matched comparison, or controlled offer when feasible. Report attribution confidence as high/medium/low.

## 9. Support boundaries and escalation

### Poplar owns

Campaign configuration, QR/mobile pages, campaign ledger, standard reports, staff runbook/training, campaign-related participant communications, and first-line troubleshooting of Poplar components.

### Merchant owns

Offer truth, pricing, availability, staff execution, POS records, refunds, food/service quality, age/ID checks, taxes, alcohol compliance, employee management, and customer complaints about the merchant's service.

### Third-party/vendor owns

Payment processing, email/SMS delivery, wallet signing infrastructure, hosting uptime, and their own compliance/security obligations under contract.

Severity: P0 suspected data/security incident or campaign-wide outage (immediate containment); P1 redemption/offer failure affecting live customers (same-day); P2 degraded reporting or non-blocking defects (next business day); P3 feature request (planned backlog). Every incident has owner, timeline, customer/merchant impact, workaround, and closure note.

## 10. Engineering gates

### Gate 0 — economics and consent

Approved campaign brief, offer margin model, baseline/control method, data inventory, notice/consent copy, retention decision, and merchant sign-off.

### Gate 1 — experience rehearsal

Three end-to-end rehearsals on real phones (slow connection included): discover -> scan -> stamp/claim -> redemption -> return offer -> opt-out. Staff can complete routine action within target time; QR fallback works.

### Gate 2 — data correctness

Idempotency tests, tenant isolation tests, access-control tests, timezone/date-boundary tests, duplicate scan/redemption tests, refund/void handling, audit-log assertions, and report fixture tests.

### Gate 3 — security/privacy

Secret scan, dependency audit, MFA/admin review, encrypted transport, backup restore test, deletion/suppression test, abuse/rate-limit test, and threat model for copied QR/NFC.

### Gate 4 — operational readiness

Runbook printed/shared, escalation contacts confirmed, support hours stated, vendor status checked, monitoring active, rollback/kill switch tested, and staff backup trained.

### Gate 5 — launch and post-launch

Launch only from tagged/versioned release. First-day smoke check; daily anomaly review; end report reproducible from frozen inputs. Any schema/report change increments calculation version and reruns fixtures.

## 11. Phased implementation

### Phase 1 (1 week): design the pilot

Select neighborhood and 3 merchants; interview capacity/staff; choose one slow-period campaign; price offer and artifacts; define baseline, consent, and stop conditions.

### Phase 2 (1 week): paper/QR prototype

Produce passports/stamps, mobile pages, source-coded QR placements, event ledger, staff runbook, and basic dashboard. Test with internal participants.

### Phase 3 (2 weeks): live pilot

Run one campaign per merchant; Poplar performs daily exception review and weekly pulse; collect labor and reconciliation data; maintain a small control/baseline comparison.

### Phase 4 (1 week): decision

Calculate contribution margin, incremental return confidence, staff burden, fraud/support issues, and merchant renewal. Stop, revise, or standardize; do not add infrastructure based on vanity metrics.

### Phase 5 (2–4 weeks): production primitives

Harden auth/tenant isolation, retention jobs, backups, report versioning, vendor contracts, and optional Wallet pass. Add AT/public records only if portability/discovery is a validated need.

## 12. Risk register

| Risk | Early signal | Mitigation/owner |
|---|---|---|
| Discount attracts low-margin bargain hunters | redemptions up, contribution margin down | off-peak/min-spend/expiry rules; campaign lead |
| Staff friction kills adoption | seconds/event and complaints rise | one-touch runbook, physical placement, backup staff |
| QR/NFC copying or replay | duplicate serials, abnormal velocity | server validation, idempotency, rate limits, risk queue; engineering |
| Cross-merchant data leakage | merchant sees other merchant records | tenant tests, least privilege, review; engineering |
| Consent complaint or unwanted messages | unsubscribes/complaints | purpose/channel-specific consent and suppression; ops |
| Attribution overclaim | no baseline/control, inconsistent POS data | label confidence, reconcile exports, report limitations |
| Vendor outage | delivery or wallet failures | QR/paper fallback, status checks, exportable ledger |
| Scope creep into custom platform | engineering before repeat proof | gates and explicit non-goals; account lead |
| Physical supply/installation failure | missing stock or damaged signage | batch inventory, field audit, reorder buffer |
| Merchant churn | champion disengaged, slow approvals | named owner/backup, weekly review, clear ROI report |

## 13. Source notes (annotated)

1. **VERIFIED — Federal Trade Commission, “Protecting Personal Information: A Guide for Business.”** https://www.ftc.gov/business-guidance/resources/protecting-personal-information-guide-business. Used for the minimum-data/security lifecycle: take stock, scale down, lock it, pitch it, plan ahead. Federal small-business guidance; adapt to the actual legal environment.
2. **VERIFIED — Information Commissioner’s Office, “Direct marketing and privacy and electronic communications.”** https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/. Used as a concrete official reference showing that phone/email/text marketing and cookies/electronic communications have channel-specific requirements. UK source; not a substitute for US counsel.
3. **VERIFIED — Apple Developer Documentation, “Wallet Passes.”** https://developer.apple.com/documentation/walletpasses. Used to constrain the Wallet design: passes can represent store cards/coupons/tickets, be distributed and updated, and require a server-side build/sign/distribution workflow.
4. **RECONSTRUCTED — Poplar operating synthesis.** Campaign lifecycle, service boundaries, event-ledger model, phased gates, and KPI contract are design inferences for the stated neighborhood-agency model, not claims that a source independently validates them.
5. **RECONSTRUCTED — Neighborhood loyalty network patterns.** The paper passport first, QR fallback, private customer data, and delayed use of NFC/AT Protocol follow the loaded Poplar design guidance and should be validated in the pilot before production commitment.

## Definition of done for a first pilot

A pilot is complete only when three merchants can run the same documented flow without Poplar improvisation; every event can be reconciled or explicitly marked missing; consent and suppression evidence exists for every marketing contact; the report distinguishes observed from incremental behavior; staff labor and campaign costs are included; and a written stop/revise/scale decision is made against pre-registered thresholds.

## Recommendation

Build the paper + QR + private ledger pilot now. Treat Wallet passes as a convenience layer after the repeat-visit loop works. Treat public protocol records, secure NFC, and deep POS integrations as gated experiments—not the product itself.
