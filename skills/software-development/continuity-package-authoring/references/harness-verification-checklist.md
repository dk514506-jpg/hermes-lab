# Harness Verification Checklist for Continuity Packages

This checklist governs step 2 of the continuity-package-authoring process: verifying every referenced harness, board, and role structure before describing it as functional in the package.

## What "exists and functional" means

For each type of referenced artifact, the standard is:

- **Exists and functional:** the artifact is present at the claimed location and does what the package says it does. A kanban board exists at the claimed path with the right project slug. A role structure has actual prompts or bindings, not just a name. A harness repo contains a project-specific orchestrator. `delegate_task` has been tested and works.
- **Exists but not functional:** the artifact is present but doesn't do what the package claims. A kanban board exists but for a different project. A role list exists (as a design) but has no prompts or bindings. A repo exists but is a general library with no project-specific harness.
- **Doesn't exist:** no artifact at the claimed location or description.

If an artifact is "exists but not functional" or "doesn't exist," the package must say so explicitly. The next window needs to know whether it has to build the harness, reuse a different one, or operate without it.

## Verification steps by artifact type

### Role structure / operating posture

Check:
1. Does the package describe specific roles (e.g. Pip, Locus, Evidence Librarian, Methodologist)?
2. Are there actual prompts, subagent bindings, or delegate_task definitions that implement those roles?
3. Are the prompts stored somewhere accessible (files, a repo, inline in the package)?
4. Has `delegate_task` been tested in the current environment?

Verdict shapes:
- **Exists and functional:** prompts exist, delegate_task works, the roles are bound to actual spawn instructions.
- **Exists but not functional:** role names are listed but no prompts/bindings exist. This is a design, not a running system.
- **Doesn't exist:** no role structure is referenced at all (the package may not need one).

### Kanban board

Check:
1. Does the board directory exist at the claimed path?
2. Does the board have the right project slug (check `board.json`)?
3. Does the board have cards/tickets relevant to the next window's task?
4. Is the board active or archived?

Verdict shapes:
- **Exists and functional:** board at claimed path, correct slug, active, has relevant work.
- **Exists but not functional:** board exists but for a different project, or is archived, or has no relevant work.
- **Doesn't exist:** no board directory at the claimed path.

### Agentic harness repo

Check:
1. Does the referenced repo exist (verify via web access)?
2. Does the repo contain a project-specific orchestrator, or is it a general skill library?
3. Are the skills in the repo relevant to the project, or generic?
4. Is there a runtime bundle or release asset the next window would need?

Verdict shapes:
- **Exists and functional:** repo exists, contains a project-specific harness (or project-specific skills the next window can use), and any needed runtime assets are available.
- **Exists but not functional:** repo exists but is a general library with no project-specific harness. The next window can use it as a skill source but can't treat it as "the Monstare orchestrator."
- **Doesn't exist:** repo doesn't exist or isn't accessible.

### Subagent / spawn mechanism

Check:
1. Is `delegate_task` available in the current environment?
2. Has it been tested with a trivial goal (to confirm it spawns and returns usable output)?
3. What is the concurrency limit (how many subagents can run in parallel)?
4. Are there any known restrictions (leaf vs. orchestrator, tool access, duration limits)?

Verdict shapes:
- **Exists and functional:** delegate_task works, tested, concurrency limits known.
- **Exists but not functional:** delegate_task is available but has restrictions that would block the package's intended use (e.g. can't spawn the number of roles the package wants).
- **Doesn't exist:** delegate_task is not available at all.

## Recording the verification result

The package's open issues section should carry the verification result. At minimum:

- Which artifacts were checked.
- What the verdict was for each (exists and functional / exists but not functional / doesn't exist).
- If any artifact is "exists but not functional" or "doesn't exist," what the next window needs to do about it (build it, find an alternative, operate without it).

Example wording:

```
Open issue #8: The agentic orchestration harness is not built.
- Role structure: exists as a design (Pip/Locus/Evidence Librarian/etc.) but has no prompts,
  no subagent bindings, and no delegate_task definitions. Verdict: exists but not functional.
- Kanban board: the /opt/data/kanban/ board is a Poplar.agency board, not a Monstare board.
  Verdict: exists but not functional for Monstare.
- Harness repo (github.com/dk514506-jpg/hermes-lab): exists and is accessible. It is a general
  skill library with multi-agent pipeline skills (FAOS, multi-agent-pipeline, etc.) but no
  Monstare-specific orchestrator. Verdict: exists but not functional as a Monstare harness.
- delegate_task: verified functional in this session via a probe subagent.
Next window action: build the Monstare harness per the build spec in section 5 of this package.
```

## Common mistakes

1. **Assuming a role list is a running system.** A list of role names with one-line descriptions is a design. Check for prompts and bindings.
2. **Assuming a kanban board is the right board.** A board exists but for a different project. Check the slug.
3. **Assuming a repo is project-specific.** A repo exists but is a general library. Check its contents.
4. **Not testing delegate_task.** It may be available but restricted, or may not work as expected. Test it.
5. **Recording the verification in the package but not in the open issues.** The next window needs to see it in the open issues, not buried in a footnote.
