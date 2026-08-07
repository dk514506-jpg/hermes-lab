# Council Critique Rounds — quality-gating a large assembled deliverable

Validated 2026-08-06 on the Motivational Ecology campaign (docs/Ecology/Foundation/):
three critics reviewed Phases 1–3 artifacts; findings were integrated in a
revision round. The user's explicit framing: critiques should "sublate the
worse aspects and reinvigorate the best elements" — preserve the kernel,
negate the limitations, raise the level. Not polite approval, not destructive
dismissal.

## When to use

After assembling a substantial multi-part deliverable (a corpus distillation,
a wiki, a set of skill packages, a report) — either because the user asks for
a critique round, or as a self-imposed quality gate before declaring done.

## The 3-lens critic pattern

Dispatch 3 parallel subagents (delegate_task), each with a distinct lens and
a fixed output format. Lenses for a research/build campaign:

1. **Epistemology & Evidence critic** — flag-status discipline (VERIFIED /
   RECONSTRUCTED / UNVERIFIED) consistent across files? Unsupported claims
   smuggled in as fact? Retraction/integrity register complete? Descriptive-
   vs-predictive respected? Do contrary findings actually constrain the
   architecture claims, or are they decorative?
2. **Architecture & Design critic** — do the built packages instantiate the
   theories they claim? Are AtomicOps executable verbs or wishlists? Do the
   typed edges compose (seed index vs per-package edge maps)? Is the
   empowerment/atrophy boundary enforced in code, not just prose?
3. **Ecology & Governance critic** — charter fidelity (preserve questions,
   practices, judgment; continuity as enacted)? Alive or archival? Is the
   campaign registered in its own registers/atlas? Is interpretive
   sovereignty encoded AND enacted? Does the campaign embody the architecture
   it proposes (self-application gap)?

Tailor lens names to the domain, keep the three-way split: evidence, design,
governance.

## Per-critic output format (fixed)

```
## 1. The kernel (what is genuinely strong — cite files/sections)
## 2. The limitations (what is weak or wrong — cite file:section)
## 3. The missing (what would raise it a level)
## 4. Concrete revision instructions (numbered, file-level, actionable)
## 5. Verdict (one sentence)
```

Instruct critics to READ the artifacts on disk and NOT write any files — the
critique is their final message.

## Integration + revision round

1. Read all critiques; for each point decide accept / adapt / reject, with a
   reason. Trust but verify — critics catch real bugs (reversed edge
   directions, naming drift, empty safeguard columns, misattributed
   citations), but check each finding against the actual file before revising.
2. Apply the accepted revisions to disk.
3. **Verify with a durable test file, not an inline heredoc.** Create a
   persistent `verify_<thing>.py` (or extend the existing verifier) that
   asserts exactly what the revisions changed, compile it, and run it to
   EXIT=0. Inline verification gets re-flagged as unverified because there's
   no named entry point to re-run. Also re-run the structural verifier.
   Pitfall: an assertion's expected value can itself be wrong (miscounted
   entries) — when a check fails, check the TEST before blaming the artifact.
4. Resynthesize: update the README/status lines, the session journal, and
   any handoff notes with what changed and why.
5. Register the campaign in its own ecology: add QIDs to the open-questions
   register, add the project to the project atlas with relation edges, write
   handoff notes. The ecology critic will flag a campaign that governs
   everything except itself.

## Model-provider independence (user preference)

The user explicitly wants the model APIs used, not just journal APIs. Run the
critic council on the configured model, but for a genuinely independent
voice, consider pinning a cross-provider review pass (different provider/key)
so the critique is not the same model critiquing its own output.

## Known critique findings worth pre-empting

- Summary-layer status drift: "all VERIFIED" claims in a README contradicted
  by the bibliography's own UNVERIFIED/RECONSTRUCTED entries. Syntheses
  assembled from council distillations are RECONSTRUCTED at artifact level;
  VERIFIED applies to the sources they cite.
- Empty safeguard columns exactly where evidence is weakest (invented
  thresholds, un-gated low-confidence signals).
- Index vs per-package agreement hidden by direction-blind verifiers and
  whitelisted dangling edges.
- Naming drift across packages (same construct, three spellings) breaks
  cross-package wiring.
