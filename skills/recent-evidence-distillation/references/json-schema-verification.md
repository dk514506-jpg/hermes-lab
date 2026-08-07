# JSON Schema Authoring & Verification Battery

Discovered authoring the Phase 5 estate schema (`ecology-learnability/0.1` in
`docs/Ecology/Foundation/Phase5_Safeguards/learnability_state_schema.json`).
Use for any schema artifact the campaign produces (package `state_schema.json`
files, indexes, estate schemas). `jsonschema` 4.26.0 is available in the
session env (`Draft7Validator`).

## The four-part validation battery (run ALL of them)

1. **Meta-schema validity** — the schema document must itself be valid draft-07:
   ```python
   from jsonschema import Draft7Validator
   errs = list(Draft7Validator(Draft7Validator.META_SCHEMA).iter_errors(schema))
   ```
   Catches structural errors, but NOT semantic ones (see pitfalls below).
2. **Realistic conformance instance** — build an instance that exercises every
   branch (per-item entries, nulls, arrays, every enum value you care about)
   and require 0 errors. This is the check that catches semantic bugs.
3. **Negative tests** — the schema must REJECT invalid data: bad enum value,
   out-of-range number, missing required property. A schema that accepts
   anything validates nothing. Assert on the error messages
   (`"'sideways' is not one of"`, `"greater than the maximum of 1"`).
4. **`$ref` integrity** — no dangling refs, all definitions reachable:
   ```python
   import re
   refs = set(re.findall(r'"\$ref": "#/definitions/(\w+)"', json.dumps(schema)))
   defined = set(schema.get("definitions", {}))
   assert refs <= defined and refs == defined
   ```

## Pitfall 1: `const` on prose fields makes snapshots unvalidatable

Using `const` for long rule/grounding/finding text forces every instance to
reproduce the schema's own prose byte-for-byte — a real snapshot with its own
wording fails validation. **`const` belongs only on true invariants**:
`schema_version`, `project` identity, short policy flags
(`"VERIFIED"`, `"RECONSTRUCTED"`). Documentation text goes in `description`.
Phase 5 hit this on 8 fields (`rule`, `grounding`, `finding`, `use`, `source`)
before the negative/conformance tests exposed it.

## Pitfall 2: `required` key without a matching property definition

`telemetry_policy.rationale` was listed in `required` but never defined as a
property. The meta-schema check passes (it doesn't cross-check this); the
conformance instance fails with `'rationale' is a required property`. Rule:
every key in `required` must have a sibling property definition. Either add
the definition or drop the requirement.

## Worked evidence trail (Phase 5)

- First run: meta-schema PASS, conformance FAIL (6 errors: rationale +
  const-prose), negative PASS. The const failures were all
  "expected <schema's own text>" — the tell that `const` was misused.
- Fix: added the `rationale` property; relaxed 8 prose fields to
  `type: string` + `description`; kept `const` on version/project/flags.
- Re-run: all four battery stages PASS; estate verifier
  (`verify_all.py`) still exit 0.

## Commit the battery as a durable script

Inline heredoc verification is ephemeral — the review loop will ask for
re-runnable evidence. Commit `council_notes/verify_phaseN.py` following the
repo convention (check() helper printing `[PASS|FAIL]`, fails list, exit 0/1,
all JSON parsed, `build_instance()` for the conformance fixture). Pattern:
`council_notes/verify_phase5.py` (18 checks).
