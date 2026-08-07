#!/usr/bin/env python3
"""Single-entry verification for the WHOLE campaign — the full gate.

Run: python3 council_notes/verify_all.py
Chains EVERY build-time verifier plus the shipped harness verifier, in
dependency order, and fails on any nonzero exit. This is the gate the
Calibration_Log verifier register and Evaluation_Rubric.md §3 describe:
"verify_all.py → every verifier; all must exit 0."

REWRITTEN 2026-08-06 (Phase 8 judge round, DeepSeek finding): the previous
version chained only three verifiers (it was scoped to the Phase 4 changed
paths) while the documentation claimed the full chain. This version runs
the complete set. Calibration_Log row #17.

Chain (dependency order):
  1. verify_packages.py          — per-package op schema (all 8 packages)
  2. verify_phase3.py            — Phase 3 structural (8×9 files, 16 sections)
  3. verify_critique_revisions.py— post-critique Phase 3/4 fixes
  4. verify_phase4.py            — Phase 4 graph/lattice reconciliation
  5. verify_phase5.py            — Phase 5 safeguards + truthfulness guards
  6. verify_phase6.py            — Phase 6 dojos (all 5, generic + owned)
  7. verify_phase7.py            — Phase 7 harness (12 check families)
  8. verify_phase8.py            — Phase 8 evaluation artifacts
  9. verify_phase9.py            — Phase 9 Valens × Ecology meld artifacts
  10. verify_integration.py      — Phase 10 FAOS × Ecology integration
  11. verify_phase11.py          — Phase 11 BCW/BCT intervention layer
  12. verify_phase12.py          — Phase 12 conditional package activation
  13. verify_phase13.py          — Phase 13 live wire (skill module + first session)
  14. verify_harness.py          — shipped consumer-facing verifier (in-tree)
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
HARNESS_VERIFIER = os.path.join(ROOT, "..", "Hermes_Agent_Harness", "verify", "verify_harness.py")

# (name, path) — every verifier that must exit 0
VERIFIERS = [
    ("verify_packages.py", os.path.join(ROOT, "..", "Phase3_Skills", "verify_packages.py")),
    ("verify_phase3.py", os.path.join(ROOT, "verify_phase3.py")),
    ("verify_critique_revisions.py", os.path.join(ROOT, "verify_critique_revisions.py")),
    ("verify_phase4.py", os.path.join(ROOT, "verify_phase4.py")),
    ("verify_phase5.py", os.path.join(ROOT, "verify_phase5.py")),
    ("verify_phase6.py", os.path.join(ROOT, "verify_phase6.py")),
    ("verify_phase7.py", os.path.join(ROOT, "verify_phase7.py")),
    ("verify_phase8.py", os.path.join(ROOT, "verify_phase8.py")),
    ("verify_phase9.py", os.path.join(ROOT, "verify_phase9.py")),
    ("verify_integration.py", os.path.join(ROOT, "..", "Phase10_Integration", "verify_integration.py")),
    ("verify_phase11.py", os.path.join(ROOT, "..", "Phase11_Intervention", "verify_phase11.py")),
    ("verify_phase12.py", os.path.join(ROOT, "..", "Phase12_Activation", "verify_phase12.py")),
    ("verify_phase13.py", os.path.join(ROOT, "..", "Phase13_Wiring", "verify_phase13.py")),
    ("verify_harness.py (in-tree)", HARNESS_VERIFIER),
]

failures = []
print("=== FULL CAMPAIGN VERIFICATION GATE ===")
for name, path in VERIFIERS:
    if not os.path.exists(path):
        print(f"[FAIL] {name} — MISSING: {path}")
        failures.append(name)
        continue
    r = subprocess.run([sys.executable, path], capture_output=True, text=True)
    tail = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()
    ok = r.returncode == 0
    print(f"[{'PASS' if ok else 'FAIL'}] {name} — {tail}")
    if not ok:
        failures.append(name)

print()
if failures:
    print(f"GATE FAILED: {len(failures)} verifier(s) failed: {failures}")
    sys.exit(1)
print("FULL CAMPAIGN GATE: ALL VERIFIERS PASS — exit 0")
