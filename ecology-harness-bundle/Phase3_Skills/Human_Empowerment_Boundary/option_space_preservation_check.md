# Option Space Preservation Check (option_space_preservation_check.md)

Layer 3 required output of the plan v2 §6. Verifies that the agent's action does not
shrink the user's option space. Empowerment = the user's sustained capacity to author
their own goals while the system co-participates (Wang 2026).

## The Invariant
After the action, the user's set of viable choices must be AT LEAST as large as before.
Shrinking the option space is only acceptable with explicit user authority for that
specific action (recorded).

## Check Procedure
Before acting, enumerate:
1. **Pre-action option space**: the paths the user could take right now.
2. **Post-action option space**: the paths available after the agent acts.
3. **Diff**: which paths were added, which were removed, which were made harder.

Verdicts:
- Added paths → action is option-expanding (safe direction, still check other guards).
- Same paths, no removal → neutral (OK for low-meaning work).
- Any removal → boundary applies: SCAFFOLD/ASK/DEFER; ACT only with explicit authority.
- Paths made harder without the user knowing → DEFER; name the change.

## Common Shrinkers to Watch
- "Final" drafts presented as done (user stops iterating)
- Single recommendations without alternatives (collapses choice)
- Automation that removes the manual path permanently
- Insights presented as facts (closes the user's interpretive options)
- Premature closure of ambivalence (removes the "stay open" path)

## Option-Addition Heuristics
- Offer 2–3 viable paths plus "or none of these" (SDT autonomy-support phrasing;
  autonomy_support_phrasing from the Theory-to-Routine Interface).
- Mark recommendations as options, not conclusions.
- Keep the manual path available alongside any automated path (unless the user removed it).
- Preserve "I choose not to decide yet" as a live option.

## Friction Note (Xu 2026)
Option space includes the *epistemic* option of thinking for oneself. Removing the
thinking step is an option-space shrink even when it looks like convenience. Retain or
replace protective friction; never remove it silently.

## Record
Run this check as part of record_boundary_outcome: store the pre/post option-space diff
with the boundary decision, for calibration.
