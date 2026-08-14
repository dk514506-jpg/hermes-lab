---
name: project-context-recovery
description: "Use when recovering context for a placeholder repository."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [project-context, repository, session-history, requirements-recovery, github]
    related_skills: [github-repo-management, github-pr-workflow]
---

# Project Context Recovery

Use when a repository URL or project codename refers to work started in an earlier conversation, especially when the repository appears empty, scaffold-only, or differently named.

## Workflow

1. Inspect the destination first: clone/open it and inspect status, branches, recent commits, top-level files, README, and ignored/generated content. Do not modify it yet.
2. Treat names as aliases. Repository brand, internal product name, campaign name, and working title may differ.
3. Search conversation history for the repository name, working title, distinctive phrases, and major deliverables. Prefer original requirements and completed artifacts over guesses.
4. Recover the smallest authoritative brief: problem, audience, goals, scope, constraints, decisions, deliverables, and validation criteria. Preserve uncertainty.
5. Restore documentation before implementation. For a placeholder repo, add a README and strategy/specification document recording recovered context, labeled as working strategy when requirements are exploratory.
6. Verify existence, size/line count, expected sections, links, and repository status. Review the opening and section outline for truncation or malformed content.
7. Commit and push only the recovered, requested work. Use a descriptive commit, verified authentication, and intended branch. Confirm the remote branch SHA.
8. Report exactly what was recovered and changed. If no context is recoverable, ask for the brief instead of inventing requirements.

## Cost-aware execution and collaboration

Before a costly research, delegation, or build step, state the smallest useful action and its expected value. Prefer deterministic inspection, file reads, search, and mechanical verification over another model call. Batch independent recovery searches, cap delegated turns/output, and reuse recovered evidence. Stop when the recovered brief, requested artifacts, and verification gates pass; do not add cosmetic iterations merely to keep working.

For multi-agent recovery, keep the main agent as integrator and decision owner. Assign independent agents bounded roles (for example: evidence recovery, implementation, or QA), require each handoff to specify inputs, output path/schema, evidence standard, budget, forbidden actions, and verification, and independently verify every claimed file, commit, URL, or remote side effect.

If the recovered project needs a durable knowledge layer, separate responsibilities: versioned repository artifacts are the implementation source, an Obsidian vault is the linked knowledge layer, and a Kanban board is the execution queue. Do not duplicate private customer data into a public repository.

## Quality gates

- Repository contents were inspected before editing.
- Context came from searchable prior conversation or a user-provided source.
- README links agree with files that exist.
- No credentials or private customer data entered the repository.
- Any public-example claims are labeled as verified, unverified, inference, or open question.
- Delegated outputs were checked as artifacts rather than accepted as self-reports.
- The working tree is clean after pushing, and the remote branch matches the reported commit.

## Pitfalls

- Assuming an initial commit means the project has no prior requirements.
- Treating the repository slug as the complete project identity.
- Starting implementation before restoring the product brief.
- Claiming a push succeeded without checking the remote branch.
- Reconstructing requirements from imagination when history is unavailable.

## Supporting detail

See `references/recovery-case-study.md` for a concise example of alias resolution, session-history recovery, documentation restoration, and remote verification.
