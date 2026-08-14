# Lakeview Loop Review Notes

## Review signal

Two independent critiques of a concept-only neighborhood campaign prototype converged on the same issue: the artifact was visually credible and careful about privacy, evidence, and non-participation, but it was more narrative than product or operating system.

## Accepted corrections

- Keep the approved journey: **Discover → visit → collect/record → return → cross-visit → refer**.
- Treat four named businesses as public research examples, not partners or participants.
- Keep Momo Factory limited to **3202 N Broadway**.
- Avoid generic credits, points, balances, universal scores, exchange rates, or implied reward currencies.
- Use a contextual passport/progress layer: marks, stamps, codes, visit records, and approved next actions.
- Allow independent entry points; do not imply a fixed sequence between merchants.
- State one working pilot hypothesis while retaining other behaviors as secondary configurable modules.
- Add a fixture-only state transition (`DEMO DATA`) that creates no profile, offer, reward, or customer record.
- Add a compact operator view: approve, verify, review.
- Narrow “no customer data” language to exclude intentional passport/contact/profile collection while acknowledging hosting/security logs.
- Surface internal-only/publication-review status above the fold.
- Make validation CTA a review worksheet, not a lead form.
- Add missing accessible relationships and focus behavior for dialogs.

## Reusable review questions

### Product / merchant operations

- What is the single primary behavior hypothesis?
- What does staff actually do, and what is the fallback?
- Who approves copy, eligibility, capacity, margin, and exceptions?
- What does the merchant receive in return?
- What is measured, and what stops the pilot?

### UX / governance

- Can a visitor understand what happens today without interpreting jargon?
- Is the named organization clearly non-affiliated and non-participating?
- Are factual names/addresses traceable to a canonical evidence record?
- Does the prototype show a real fixture state transition without collecting data?
- Are privacy claims precise about intentional collection versus hosting logs?
- Does the dialog move focus, restore focus, and explain that nothing is submitted?

## Operational readiness package

Before treating the system as real, produce and approve:

1. Publication/permission record.
2. Pilot charter with owner/RACI, dates, objective, cohort, budget, and stop conditions.
3. Approved interaction/offer specification with eligibility, capacity/margin guardrails, expiry, exclusions, abuse controls, and exception policy.
4. Staff SOP with verification, QR fallback, disputes, escalation, training, and support.
5. Private ledger schema with role-based access, auditability, export, backups, and reconciliation.
6. Privacy/consent package with data inventory, legal basis, cross-merchant boundary, retention/deletion, and incident response.
7. Measurement plan with baseline, definitions, attribution, sample/window, and go/no-go thresholds.
8. Governance gate for evidence, permission, economics, staff usability, privacy, accessibility, security, and final-copy approval.

## Proven verification pattern

For a standalone HTML revision, create a temporary script under `/tmp/hermes-verify-*`, then check:

- file exists;
- exactly one `html`, `head`, and `body` start tag;
- IDs are unique;
- required canonical flow and disclaimer strings exist;
- forbidden scope strings are absent;
- outreach and browser-storage hooks are absent when prohibited;
- inline JavaScript passes `node --check`;
- responsive CSS contains the intended breakpoint rules.

Run the verifier, report its exit code/output, and delete the temporary script. Call it targeted ad-hoc verification unless the repo has a canonical suite.