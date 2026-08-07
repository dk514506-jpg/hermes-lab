#!/usr/bin/env bash
# run_tests.sh — canonical verification entrypoint for the FAOS pipeline.
# Usage: scripts/run_tests.sh  (exit 0 = all layers pass)
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS="$(dirname "$HERE")"
FAIL=0

step() { echo; echo "=== $1 ==="; }

step "1/4 py_compile (syntax)"
python3 -m py_compile "$DOCS/faos_engine_extension.py" "$DOCS/verify_faos_pipeline.py" \
  && echo "  OK" || { echo "  FAIL"; FAIL=1; }

step "2/4 verify_faos_pipeline.py (behavioral harness)"
python3 "$DOCS/verify_faos_pipeline.py" || FAIL=1

step "3/4 faos_engine_extension.py self-test"
python3 "$DOCS/faos_engine_extension.py" >/dev/null 2>&1 \
  && echo "  SELF-TEST PASSED" || { echo "  FAIL"; FAIL=1; }

step "4/4 YAML structural checks"
python3 - "$DOCS/triage_faos_integration.yaml" <<'PY' || FAIL=1
import sys, yaml
from pathlib import Path
data = yaml.safe_load(Path(sys.argv[1]).read_text())
ok = [
    data.get("schema_version") == "faos-integration/2.0",
    len(data["route"]["map"]) == 6,
    len(data["route"]["authority_weights"]) == 6,
    all(f"S{i}" in data["state_lineage"]["states"] for i in range(10)),
    len(data["quarantine_tiers"]["tiers"]) == 11,
    len(data["absence_register"]["entries"]) == 2,
    data["absence_register"]["fail_closed"] is True,
    len(data["non_operational_registry"]["entries"]) == 2,
    "locus" in data["roles"],
    sum(1 for p in data["paths"].values()
        if any(isinstance(s, dict) and s.get("stage") == "locus_review"
               for s in p.get("fulfill", []))) == 6,
    all(v["primary"] in data["paths"] for v in data["route"]["map"].values()),
    all(v.get("shadow") is None or v["shadow"] in data["paths"]
        for v in data["route"]["map"].values()),
    "knowlege-scout" not in Path(sys.argv[1]).read_text(),
]
for label, passed in zip(
    ["schema_version", "route map 6", "weights 6", "S0-S9 lineage",
     "quarantine 11", "absence 2+fail_closed", "non-op 2",
     "locus role", "locus_review x6", "primaries resolve",
     "shadows resolve", "no typo"], ok):
    print(f"  {'✓' if passed else '✗'} {label}")
    if not passed:
        sys.exit(1)
PY

step "RESULT"
if [ "$FAIL" -eq 0 ]; then echo "ALL LAYERS PASSED"; else echo "FAILURES PRESENT"; fi
exit "$FAIL"
