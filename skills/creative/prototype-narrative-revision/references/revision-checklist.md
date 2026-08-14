# Concept Prototype Revision Checklist

Use after a user says a prototype is “rough,” “generic,” or “not descriptive enough.”

## Diagnosis

- [ ] Name the surface: usually Decide / Learn for a concept landing page.
- [ ] Identify whether the problem is composition, narrative, evidence labeling, interaction, or responsive legibility.
- [ ] Check whether the page explains the visitor experience before showing example cards.

## Narrative additions

- [ ] Show entry point → action → record/verification → next step.
- [ ] Explain return, cross-visit, and referral as behavior, not as guaranteed outcomes.
- [ ] Include one concrete route, scenario, or “what it feels like” block.
- [ ] Show the operator/merchant control boundary.

## Claim safety

- [ ] Label scenario text as `Fictional scenario`, `Illustrative role`, `DEMO`, or `Hypothesis` near the examples.
- [ ] Avoid invented prices, hours, offers, metrics, results, testimonials, endorsements, customer counts, and participation.
- [ ] Keep concept status above the fold and near any CTA.
- [ ] Keep the CTA a validation/review action, not outreach or acceptance.

## Composition and implementation

- [ ] Do not make every section a repeated card grid.
- [ ] Use deliberate type contrast and hierarchy before decorative styling.
- [ ] Highlight one meaningful state or step rather than adding arbitrary stats.
- [ ] Keep the artifact self-contained where requested.
- [ ] Add responsive breakpoints and reduced-motion handling when motion/hover is present.

## Mechanical verification

- [ ] File exists at the exact requested path.
- [ ] HTML parser sees one `html`, `head`, and `body` element.
- [ ] IDs are unique.
- [ ] Required flow and sections are present.
- [ ] Forbidden scope/location strings are absent.
- [ ] No `mailto:`, `tel:`, `fetch(`, `localStorage`, or `sessionStorage` unless explicitly authorized.
- [ ] Inline JavaScript passes `node --check`.
- [ ] Temporary verifier uses `/tmp/hermes-verify-*` and is deleted.
- [ ] Report ad-hoc verification separately from any canonical project suite.
