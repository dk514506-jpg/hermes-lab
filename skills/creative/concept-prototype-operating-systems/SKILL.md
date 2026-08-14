---
name: concept-prototype-operating-systems
description: Use when revising operating concept artifacts.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [concept-prototype, ux, operations, pitch-deck, governance, privacy]
platforms: [linux, macos, windows]
---

# Concept Prototype Operating Systems

Use this skill when building or revising a concept website, interactive prototype, or pitch artifact that combines a customer-facing experience with merchant/operator workflows, especially when real businesses, locations, public examples, or future pilot claims are involved.

## Core principle

Preserve the canonical domain model before making the presentation more persuasive. A compelling abstraction must not silently introduce new economic, legal, or operational semantics.

For neighborhood campaign concepts, default to the narrowest supported model:

- contextual visit record;
- mark, stamp, code, or manual verification;
- configured next action;
- merchant-specific offer, event, reward, or referral only when approved.

Do not turn a passport/progress metaphor into a universal points, credits, balance, or transferable-value economy unless the source brief explicitly authorizes those semantics.

## Workflow

1. **Read the source of truth first.** Inspect the project plan, campaign brief, operations architecture, evidence dossier, and existing artifact. Extract the approved journey, scope exclusions, evidence labels, publication status, and non-negotiable language.
2. **Name the primary behavior hypothesis.** If the concept has multiple possible behaviors, select one working hypothesis for the prototype and make other behaviors secondary/configurable. Do not present four incompatible merchant economics as one coherent live offer.
3. **Separate the audiences.** Distinguish visitor narrative, merchant validation, operator workflow, and the agency's managed service. A landing page can contain all four, but each must have clear labels and a clear promise.
4. **Use public examples safely.** Real businesses remain public research examples until permission is granted. Avoid words that imply partnership, affiliation, endorsement, participation, or acceptance. Keep exact location scope explicit when a particular location is required.
5. **Make static metaphors testable.** If a passport, dashboard, or progress layer is otherwise abstract, add a small fixture-only interaction: record a demo event, show a contextual next action, and reset it. State visibly that it creates no live profile, offer, reward, or customer record. Never add live collection, lead capture, analytics, or outreach to a concept artifact without authorization.
6. **Show the operating layer.** Include the staff action, verification method, QR/manual fallback, exception path, approval owner, measurement definitions, privacy boundary, and stop/go gates. Do not invent staff duration, prices, hours, capacity, outcomes, or willingness to participate.
7. **Plan for operationalization.** Create a separate pilot-readiness artifact with assumptions, product contract, pilot charter, interaction specification, staff SOP, private ledger schema, privacy/consent gate, measurement plan, governance gates, and explicit not-approved actions.
8. **If a pitch deck is requested, front-load operating credibility.** Put the staff SOP, measurement plan, pilot path, privacy, and governance into the main narrative rather than hiding them in an appendix. Treat the deck as internal until permission status changes.
9. **Verify mechanically.** Use a focused temporary verifier with a `hermes-verify-` prefix. Check artifact existence, HTML structure, unique IDs, required journey terms, forbidden scope/location strings, invented-claim vocabulary, interaction syntax, responsive breakpoints, and inline JavaScript syntax. Clean up the verifier afterward. Report this as ad-hoc targeted verification, not a project-wide suite.

## Required status language

For concept-only artifacts, make the following visible above the fold and near any CTA:

- concept demonstration / internal concept;
- not live;
- public research examples, not confirmed participants;
- review before external sharing;
- no live customer data or submission from the fixture;
- merchant approval and permission are release gates.

Use narrower privacy wording than “collects no customer data” when hosting may create access/security logs. Prefer: “This prototype does not intentionally collect passport, contact, or customer-profile data. Hosting and security logs may still exist according to the deployment provider's policy.”

## Semantic anti-drift checks

Before finalizing, confirm:

- the approved journey remains intact;
- independent locations are not falsely presented as a required sequence;
- progress does not imply monetary value or a universal balance;
- named examples are not represented as partners or participants;
- exact location scope is preserved;
- no invented prices, hours, results, testimonials, endorsements, offers, or metrics appear as facts;
- no contact form, email, phone, fetch, storage, or live tracking was added unintentionally;
- any demo values are labeled `DEMO DATA`;
- the modal/CTA is a review worksheet, not an unapproved lead form;
- the artifact remains usable at responsive breakpoints and keyboard-accessible for primary interactions.

## Companion references

- `references/lakeview-loop-review-pattern.md` — critique synthesis, accepted revisions, and operationalization checklist from the Lakeview Loop class of work.

## Pitfalls

- A disclaimer does not fully neutralize implied affiliation; “possible partner locations” can still read as a partnership claim. Prefer “public research examples used to illustrate the concept.”
- A static passport illustration can be emotionally persuasive but product-ambiguous. Define what is recorded, who verifies it, what next actions exist, and what is explicitly not active.
- Do not select one behavior per merchant merely because the businesses differ. Choose one primary pilot behavior and make the rest configurable.
- Do not claim the prototype is a customer-flow implementation if it has only anchors and static cards. Either narrow the claim or add a fixture-only state transition.
- Modal dialogs need focus movement to the close control, focus restoration to the trigger, keyboard escape behavior, and a review-only explanation.
- If the source brief is concept-only and not authorized for publication, do not generate a public merchant-facing deck by default. Produce an internal planning deck or ask for permission status.
- When the environment lacks a PPTX generation stack, produce a self-contained HTML deck as the next artifact rather than claiming a PPTX exists; verify the slide count, controls, structure, content, and JavaScript syntax.
