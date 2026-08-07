#!/usr/bin/env python3
"""Verify HiSkill skill packages (canonical 9-file pattern + allowed extras).

Usage:
    python3 verify_package.py [dir1 dir2 ...]
    # with no args: scan every subdir of the cwd that contains a SKILL.md

Checks per package:
    1. all 9 canonical core files present (extra files ALLOWED — plan §6 layer
       outputs; extras are listed as INFO, not failed)
    2. every .json parses; skill_node carries the canonical floor fields and its
       id matches the dir name case-insensitively (snake_case vs PascalCase)
    3. atomic_ops: unique ids; each op carries id + description (canonical floor);
       missing template/arguments warn
    4. edge_map: only the 5 typed edge kinds; decomposes_to targets EXACTLY equal
       atomic_ops ids (set and count)
    5. SKILL.md contains all 16 standard sections at `## X` OR `### X` level
       (plan §8 renders `##`, canonical bundle renders `###`)
    6. every recovers_with source resolves to a `### Name` heading in
       recovery_ops.md or support_ops.md, or to the skill's own id
       (seed-convention cross-skill edge); unresolved sources FAIL

Exit 0 if all packages pass, 1 otherwise. Prints per-package PASS/FAIL lines.
"""
import json
import os
import re
import sys

CORE_FILES = ["SKILL.md", "skill_node.json", "atomic_ops.json", "edge_map.json",
              "state_schema.json", "examples.md", "support_ops.md",
              "recovery_ops.md", "evaluation_notes.md"]
NODE_FLOOR = ["id", "name", "version", "purpose"]
OP_FLOOR = ["id", "description"]
SKILL_MD_SECTIONS = ["Purpose", "Trigger Conditions", "Inputs", "Outputs",
                     "State Variables", "Atomic Operations", "Typed Edges",
                     "Empowerment Boundary", "Learnability / Skill-Atrophy Check",
                     "Motivational-Lattice Interface", "Conversational / Practice Mode",
                     "Guardrails", "Failure Modes", "Recovery Operations",
                     "Examples", "Handoff Notes"]
EDGE_TYPES = {"decomposes_to", "can_follow", "compatible_with", "supports", "recovers_with"}


def verify(skill_dir: str) -> int:
    fails = 0
    label = os.path.basename(skill_dir.rstrip("/"))

    present = set(os.listdir(skill_dir))
    missing = [f for f in CORE_FILES if f not in present]
    if missing:
        print(f"FAIL {label}: missing core files {missing}")
        fails += 1
    extras = sorted(present - set(CORE_FILES))
    if extras:
        print(f"INFO {label}: extra files (allowed per plan s6) {extras}")

    def load(name):
        try:
            return json.load(open(os.path.join(skill_dir, name)))
        except Exception as e:  # noqa: BLE001
            print(f"FAIL {label}: {name} does not parse: {e}")
            fails += 1
            return None

    node = load("skill_node.json")
    if node is not None:
        missing = [k for k in NODE_FLOOR if k not in node]
        if missing:
            print(f"FAIL {label}: skill_node missing canonical floor {missing}")
            fails += 1
        node_id = node.get("id", "")
        if node_id and node_id.lower() != label.lower():
            print(f"FAIL {label}: skill_node id {node_id} != dir name {label} (case-insensitive)")
            fails += 1

    ops = load("atomic_ops.json") or []
    op_ids = [o["id"] for o in ops]
    if len(op_ids) != len(set(op_ids)):
        print(f"FAIL {label}: duplicate op ids")
        fails += 1
    for o in ops:
        missing = [k for k in OP_FLOOR if k not in o]
        if missing:
            print(f"FAIL {label}: op {o.get('id')} missing {missing}")
            fails += 1
        for soft in ("template", "arguments"):
            if soft not in o:
                print(f"WARN {label}: op {o.get('id')} lacks canonical '{soft}'")

    edges = (load("edge_map.json") or {"edges": []})["edges"]
    et = [e["type"] for e in edges]
    illegal = set(et) - EDGE_TYPES
    if illegal:
        print(f"FAIL {label}: illegal edge types {sorted(illegal)}")
        fails += 1
    if et.count("decomposes_to") != len(op_ids):
        print(f"FAIL {label}: decomposes_to count {et.count('decomposes_to')} != ops {len(op_ids)}")
        fails += 1
    dt = {e["target"] for e in edges if e["type"] == "decomposes_to"}
    if dt != set(op_ids):
        print(f"FAIL {label}: decomposes_to mismatch {sorted(dt ^ set(op_ids))}")
        fails += 1

    # every recovers_with source must resolve: op heading, or the skill's own id
    headings = set()
    for r in ("recovery_ops.md", "support_ops.md"):
        if r in present:
            headings |= set(re.findall(r"^### (.+)$", open(os.path.join(skill_dir, r)).read(), re.M))
    self_ids = {label.lower()}
    if node is not None:
        self_ids.add(node.get("id", "").lower())
    for e in edges:
        if e["type"] == "recovers_with":
            src = e["source"]
            if src not in headings and src.lower() not in self_ids:
                print(f"FAIL {label}: recovers_with source '{src}' is not a defined op heading and not the skill id")
                fails += 1

    if load("state_schema.json") is None:
        fails += 1

    md = open(os.path.join(skill_dir, "SKILL.md")).read()
    missing_sections = [s for s in SKILL_MD_SECTIONS
                        if f"### {s}" not in md and f"## {s}" not in md]
    if missing_sections:
        print(f"FAIL {label}: SKILL.md missing sections {missing_sections}")
        fails += 1

    if fails == 0:
        print(f"PASS {label}: core files ok, JSON valid, {len(op_ids)} ops, "
              f"{len(edges)} edges ({et.count('decomposes_to')} decomposes_to), "
              f"{len(SKILL_MD_SECTIONS)} SKILL.md sections")
    return 1 if fails else 0


def main() -> int:
    args = sys.argv[1:]
    if not args:
        args = [d for d in sorted(os.listdir("."))
                if os.path.isdir(d) and os.path.exists(os.path.join(d, "SKILL.md"))]
    if not args:
        print("No skill package directories found.")
        return 1
    total = sum(verify(a) for a in args)
    print("\nRESULT:", "ALL CHECKS PASSED" if total == 0 else f"{total} FAILURES")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
