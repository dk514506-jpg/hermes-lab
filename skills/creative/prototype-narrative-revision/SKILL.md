---
name: prototype-narrative-revision
description: Use when a concept prototype feels rough or under-described.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [design, prototype, html, landing-page, narrative, ux, revision]
---

# Prototype Narrative Revision

Use this class-level skill when an existing prototype is broadly correct but feels rough, thin, generic, or not descriptive enough. The goal is not cosmetic polish alone: make the intended experience legible, persuasive, and bounded by the project's factual/privacy constraints.

## Core principle

A concept page is a **Decide / Learn** surface. Visitors need to understand:

- what the idea is;
- who experiences it;
- what they do step by step;
- what the operator or merchant controls;
- what is illustrative versus verified;
- what the next validation decision is.

If the current page jumps from a hero directly to a grid of cards, it often needs a narrative/composition pass before more styling.

## Workflow

1. **Read the source brief and existing artifact.** Extract audience, locked claims, forbidden claims, scope boundaries, required flow, and CTA behavior. Treat the current page as a design hypothesis, not as authority.
2. **Name the surface and diagnose the gap.** For a concept landing page, choose Decide / Learn. Identify whether the weakness is composition, narrative, evidence labeling, interaction, or responsive legibility. Do not solve a narrative problem with colors alone.
3. **Map the missing story.** Write a compact visitor/operator sequence: entry point → action → verification/record → next step → return/cross-visit/referral. If that story is not visible on the page, add one descriptive section such as “What the experience feels like” or “How it works.”
4. **Use bounded scenario copy.** Add concrete, plausible actions and handoffs, but never invent factual business details, prices, hours, offers, results, endorsements, testimonials, customer counts, or participation. Prefer labels such as `Fictional scenario`, `Illustrative role`, `DEMO`, `Hypothesis`, and `Validate`.
5. **Vary composition intentionally.** Avoid making every section the same card grid. Use one dominant story block, one compact route or sequence, one highlighted state/step, and merchant/example cards only where comparison is useful.
6. **Choose typography deliberately.** A concept presentation can benefit from editorial display typography paired with a restrained system sans body. Use type contrast and spacing to establish hierarchy before adding decorative elements.
7. **Make the CTA a validation gate.** A concept CTA should invite review, hypothesis testing, or permission discussion; it must not imply outreach, acceptance, partnership, or live participation.
8. **Preserve privacy boundaries.** If showing a passport, ledger, route, or progress view, make it visibly illustrative and ensure the prototype does not collect data, contact anyone, or require an external service unless explicitly authorized.
9. **Verify after editing.** Check file existence, HTML structure, unique IDs, required sections/flow, forbidden-scope absence, scenario labeling, absence of outreach/storage hooks, inline JavaScript syntax, and responsive CSS breakpoints. Use a focused temporary verifier under `/tmp/hermes-verify-*`, run it, and remove it.

## Quality bar

A successful revision should make a first-time reader able to answer, without external explanation:

- “What happens first?”
- “What does the visitor actually do?”
- “Why would they return or cross-visit?”
- “What is the merchant’s role?”
- “Which parts are only hypotheses?”
- “What would need validation before launch?”

## Pitfalls

- Do not respond to “rough” by merely increasing border radii, shadows, gradients, or card count.
- Do not add fake metrics or invented operational facts to make a presentation feel credible.
- Do not hide disclaimers in a footer when named real businesses appear; label fictional scenario copy near the examples and keep concept status above the fold.
- Do not turn a validation CTA into a mailto, contact form, booking flow, or implied merchant outreach without explicit authorization.
- Do not claim browser/visual verification unless it actually occurred; report mechanical checks separately.
- Do not overwrite a major revision without preserving a prior version when the project requires comparison; for small repo revisions, follow existing conventions.

## Related support file

See `references/revision-checklist.md` for a reusable diagnostic and acceptance checklist.
