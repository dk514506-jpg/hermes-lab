---
name: self-contained-html-reports
description: "Generate self-contained HTML reports with stdlib SVG charts."
---

# Self-Contained HTML Reports (stdlib SVG)

## When to use
- Need charts/graphs/diagrams in a report but can't or won't install matplotlib, JS chart libs, or CDN assets.
- The deliverable must open offline, be shareable as one file, or run in a clean-room / zero-dependency environment.
- A script regenerates the report periodically (weekly ops, dashboards, CI artifacts).

## Pattern
- Render every chart as an inline SVG string from Python stdlib only: grouped bar charts, line charts (with negatives), coverage bars with a dashed reference line, and horizontal flow diagrams.
- Minimal inline CSS in a `<style>` block; plain `<table>` for data; KPI cards as flex divs.
- Self-containment rules: no `<script>`, no `src=`, no external stylesheets/fonts. The only `http://` occurrences should be SVG `xmlns` namespace identifiers — grep to confirm.
- Validate every SVG by XML-parsing it (`xml.etree.ElementTree.fromstring`) in the verification step — cheap and catches malformed markup that eyeballing misses.
- Working renderer: `scripts/charts.py` (bar_chart, line_chart, coverage_chart, flow_diagram — all return SVG strings). Copy or import it.

## Pitfalls
- SVG `xmlns="http://www.w3.org/2000/svg"` is a namespace identifier, not an external resource — do not treat it as a self-containment violation.
- Truncate long labels (venue names, week strings) to ~14–16 chars in axis renders; use `viewBox` so charts scale to any browser width.
- Line charts with negative values: compute the span around `mid = (hi+lo)/2`, not from zero, or positive values get squished into the top half.
- Keep money as integer cents end-to-end; format at render time (`f"${c/100:,.2f}"`).
- Color-code thresholds (green/amber/red) in coverage charts; draw dashed reference lines with a legend label (e.g. "100% floor").
- Add `<title>` tooltips inside SVG rects/circles for hover detail — free interactivity with zero JS.

## Files
- `scripts/charts.py` — working stdlib SVG renderer (bar, line, coverage, flow + SVG frame helper), validated in use.
