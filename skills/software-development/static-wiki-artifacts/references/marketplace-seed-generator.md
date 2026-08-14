# Data-backed static marketplace artifact

## Proven pattern

For a static marketplace page backed by an existing tracker:

1. Read the canonical SQLite extraction table (`extractions`) or an equivalent CSV; do not manually duplicate values into HTML.
2. Normalize each record to a stable ticker: card name + set + condition. Conditions are separate share classes.
3. Keep an explicit mapping only where source names need stable slugs. Fail loudly when an expected seed row is absent.
4. Render historical extraction comps as `ASSUMED` snapshots unless they are current, source-verified market observations.
5. Show pending fields rather than inventing buylist, spread, momentum, or live quote values.
6. Add a rerunnable `build_*.py` script beside the project scripts and expose it in the README quickstart.
7. Verify by executing the generator and checking source-derived row count, total, provenance badges, pending markers, expected links, and no `<script>` tags.

## Common trap

A generated page can be structurally valid while still claiming too much. A total such as `$137.00` may be correct as the sum of historical extraction snapshots while being invalid as a current portfolio valuation. Label the metric with its exact meaning and source date.

## Vault boundary

When Obsidian is used as the editable wiki, keep the operational SQLite database and generator in the parent project. Link to the generated HTML from `Home.md` and `Project Artifacts.md`; do not duplicate executable state into prose notes.
