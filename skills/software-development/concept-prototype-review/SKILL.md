---
name: concept-prototype-review
description: Use for reviewing concept prototypes before pilotization.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [concept-prototype, product-review, operationalization, UX, governance, privacy, merchant-validation]
platforms: [linux, macos, windows]
---

# Concept Prototype Review & Operationalization

Use this class-level skill when a user asks to review, critique, revise, or operationalize a concept-only website or product artifact, especially one naming real organizations or modeling a future pilot.

## Core principle

Separate three layers and never let them blur:

1. **Narrative layer** — what the concept helps a visitor imagine.
2. **Fixture/demo layer** — what can be clicked locally using fictional, labeled state.
3. **Operational layer** — what would require evidence, permission, merchant approval, privacy controls, staff procedures, and a private system of record.

A polished narrative is not an operational pilot. State that distinction in the artifact and in the final report.

## Workflow

1. **Read canonical sources first.** Inspect the project plan, campaign brief, operations architecture, evidence register/dossier, and current artifact. Extract non-negotiable constraints before proposing changes.
2. **Write the canonical mechanic in one sentence.** If the user corrects concept drift, restate the approved mechanic before editing. Remove newly introduced abstractions that imply unsupported economics, universal currency, shared liability, or participation.
3. **Choose one primary behavior hypothesis.** If the plan leaves several behaviors open, frame one as the working pilot hypothesis and keep events, referrals, offers, repeat visits, or cross-visits as secondary configurable modules. Do not make all behaviors equally primary.
4. **Critique from independent angles.** For significant revisions, use at least two bounded reviews: (a) product/merchant-operations and (b) UX/content/governance. Ask reviewers to return prioritized findings without editing. Treat outputs as recommendations, then verify and adjudicate them yourself.
5. **Integrate only accepted findings.** Good prototype upgrades commonly include: clearer audience split, concrete fixture-based state transition, compact operator view, measurement definitions, stop conditions, publication/permission status, evidence labels, privacy wording, and modal accessibility.
6. **Keep real-organization language conservative.** Prefer “public research examples,” “illustrative roles,” and “proposed layer.” Avoid “partner,” “participating,” “client,” endorsement, or affiliation language unless permission is verified. Never invent prices, hours, offers, results, testimonials, or operating facts.
7. **Model progress without accidental points economics.** A passport/mark/progress abstraction should describe contextual visit records or approved next actions—not fungible credits, balances, universal scores, exchange rates, or implied rewards. A merchant-issued mark is not transferable across merchants unless a separately approved rule exists.
8. **Keep demos fixture-only.** A useful local prototype may let a reviewer select an example and record a fictional event, then show progress and a next-step placeholder. Label every state `DEMO DATA`; do not collect leads, customer profiles, or live submissions. Do not use localStorage/sessionStorage when the brief requires no customer data.
9. **Add the operator moment.** Show what Poplar or the operator would approve, verify, and review: behavior goal, staff action, fallback, exception handling, approval owner, measurement, burden, margin, consent, and incident boundaries. Avoid invented duration or performance figures.
10. **Handle privacy precisely.** Say “does not intentionally collect passport, contact, or customer-profile data” rather than claiming no data exists; hosting/security logs may still exist. Before live operation, define data inventory, roles, consent, retention, deletion, export, access, vendors, and incident response.
11. **Resolve publication gates.** If source docs say internal-only or not authorized for publication, surface that above the fold. Before external distribution, resolve permission for names, addresses, logos, factual descriptions, quotes, case-study language, and participation.
12. **Verify mechanically.** Check file existence, HTML structure, unique IDs, required canonical flow, prohibited scope strings, forbidden outreach/storage hooks, inline JS syntax, responsive breakpoints, and critical interaction labels. Use a temporary verifier under `/tmp/hermes-verify-*`, run it, and clean it up. Report that this is targeted ad-hoc verification unless a canonical suite exists.

## Operationalization gate

Do not call the system real or operational until these artifacts exist and are approved:

- publication/permission record;
- pilot charter with owner/RACI, dates, objective, cohort, budget, and stop conditions;
- approved interaction/offer specification with eligibility, capacity/margin guardrails, expiry, exclusions, abuse controls, and exception handling;
- staff SOP with verification, QR fallback, disputes, escalation, training, and support;
- private ledger schema with role-based access, auditability, export, backups, and reconciliation;
- privacy/consent package with data inventory, legal basis, cross-merchant boundary, retention/deletion, and incident response;
- measurement plan with baseline, definitions, attribution, sample/window, and go/no-go thresholds;
- governance gate for evidence, permission, economics, staff usability, privacy, accessibility, security, and final-copy approval.

Start with one primary behavior and one or two authorized locations. Use ordinary web, QR, manual verification, and a private ledger before adding wallets, NFC, federation, blockchain, or other heavy infrastructure.

## Common pitfalls

- Treating a visual passport as a loyalty currency.
- Making four merchants look sequential when they are independent entry points.
- Using “partner locations” while also saying participation is unconfirmed.
- Showing a static passport illustration while claiming the prototype demonstrates a flow.
- Making the visitor story much more concrete than the merchant operating moment.
- Claiming “no customer data” without acknowledging hosting/security logs.
- Creating a lead form or outreach CTA in an artifact that is not authorized for contact.
- Adding invented business details to make a presentation feel believable.
- Adding more technology before the primary behavior, permission, SOP, privacy, and measurement gates are resolved.
- Claiming browser or suite verification without actual tool output.

## Related support

- `references/lakeview-loop-review.md` — condensed review findings and accepted prototype revision patterns from a real concept-only campaign artifact.

## Relationship to other skills

Use with `claude-design` for visual composition and interaction design, and with `verification-gates` for stricter clean-room gate design. This skill owns the concept-to-pilot reasoning and governance layer; it does not replace those skills.
