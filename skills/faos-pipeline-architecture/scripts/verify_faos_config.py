#!/usr/bin/env python3
"""Structural audit for FAOS-extended triage.yaml configs.

Verifies the extension blocks (field_model, evidence_ladder, shadow routes,
close passes, learning_loop, astra) and the stock-engine cross-references
(route targets exist, roles used are defined, no orphans) before the config
is claimed engine-compatible.

Usage:
    python3 verify_faos_config.py [path/to/triage.yaml]

Exit code 0 = all checks pass, 1 = failures found.
Note: structural validity != engine compatibility. This script checks the
config against ITSELF; the stock engine's dataclass types must be checked
separately (e.g. Route dict[str,str] vs dict values).
"""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

DEFAULT = Path("~/.hermes/hermes-agent/docs/triage_faos_integration.yaml").expanduser()
CANONICAL_EVIDENCE_LEVELS = ["impression", "lead", "fact", "claim", "judgment"]
CLOSE_PASSES = {"victory", "defect", "dissent", "proxy_check", "boundary_check", "transfer_status"}


def audit(path: Path) -> list[str]:
    errors: list[str] = []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    # --- required core blocks ---
    for key in ("name", "sources", "item_schema", "rubric", "research_lanes", "route", "paths", "roles", "gate"):
        if key not in data:
            errors.append(f"missing required key: {key}")

    # --- route targets resolve (primary + shadow) ---
    paths = set(data.get("paths", {}))
    for value, entry in (data.get("route", {}).get("map", {}) or {}).items():
        if not isinstance(entry, dict):
            errors.append(f"route.map[{value}] is not a dict (shadow-route extension required)")
            continue
        for key in ("primary", "shadow"):
            target = entry.get(key)
            if target and target not in paths:
                errors.append(f"route.map[{value}].{key} -> '{target}' not in paths:")

    # --- roles: every used role defined; no orphans; sources declared ---
    defined_roles = set(data.get("roles", {}))
    used_roles = {data.get("research_lanes", {}).get("role", "researcher")}
    for p in data.get("paths", {}).values():
        used_roles.add((p.get("propose") or {}).get("role", "orchestrator"))
        for stage_list in ("prep", "fulfill"):
            for s in p.get(stage_list, []):
                if isinstance(s, dict):
                    used_roles.add(s.get("role", ""))
    undefined = used_roles - defined_roles - {""}
    if undefined:
        errors.append(f"roles used but not defined: {sorted(undefined)}")
    orphans = defined_roles - used_roles - {""}
    if orphans:
        errors.append(f"orphan roles (defined, unused): {sorted(orphans)}")
    source_profiles = {s.get("profile") for s in data.get("sources", [])}
    declared_profiles = set(data.get("roles", {}).values())
    undeclared = source_profiles - declared_profiles - {None, ""}
    if undeclared:
        errors.append(f"source profiles not declared in roles: {sorted(undeclared)}")

    # --- evidence ladder ---
    ladder = data.get("evidence_ladder", {})
    levels = [l.get("key") for l in ladder.get("levels", [])]
    if levels != CANONICAL_EVIDENCE_LEVELS:
        errors.append(f"evidence ladder: got {levels}, expected {CANONICAL_EVIDENCE_LEVELS}")
    if not ladder.get("non_skip"):
        errors.append("evidence_ladder.non_skip must be true")

    # --- close passes per path ---
    for name, p in data.get("paths", {}).items():
        close = p.get("close") or {}
        passes = close.get("required_passes") or close.get("default_passes") or []
        keys = {list(pass_.keys())[0] for pass_ in passes if isinstance(pass_, dict)}
        if close and keys != CLOSE_PASSES:
            errors.append(f"paths.{name}.close missing passes: {sorted(CLOSE_PASSES - keys)}")

    # --- learning_loop ---
    ll = data.get("learning_loop", {})
    if ll.get("enabled") and "pattern_thresholds" not in ll:
        errors.append("learning_loop.pattern_thresholds missing")
    if ll.get("enabled") and not ll.get("digest_required_before_calibration"):
        errors.append("learning_loop.digest_required_before_calibration must be true (FAOS §6.9)")

    # --- astra ---
    astra = data.get("astra", {})
    for key in ("persona", "harness_skill", "circuit_map"):
        if key not in astra:
            errors.append(f"astra missing '{key}'")

    # --- field_model ---
    fm = data.get("field_model", {})
    for key in ("entity_types", "relation_types", "stakes"):
        if key not in fm:
            errors.append(f"field_model missing '{key}'")

    return errors


if __name__ == "__main__":
    path = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else DEFAULT
    if not path.exists():
        sys.exit(f"config not found: {path}")
    problems = audit(path)
    if problems:
        print(f"AUDIT FAILED ({len(problems)} issues) — {path}")
        for p in problems:
            print(f"  ✗ {p}")
        sys.exit(1)
    print(f"AUDIT PASSED — {path}")
    print("Note: structural validity != engine compatibility. Check dataclass")
    print("types against the engine source before claiming the config runs.")
