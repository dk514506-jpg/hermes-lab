# Judge-Round Playbook

Worked example and reference for cross-provider critique rounds.
Source: Ecology campaign Phase 7 harness review, 2026-08-06.

## Brief template (judge_brief.txt)

```
You are an independent architecture reviewer (<Model>, independent of the
campaign's build process). Critique <TARGET> at <ABSOLUTE_PATH>.

Read the README.md, <key index files>, and survey the <layer dirs> (list
files; sample 2-3 <representative files>).

Assess:
1. <Axis 1> (e.g. packaging completeness for the deployment target)
2. <Axis 2> (e.g. layer interconnectivity)
3. <Axis 3> (e.g. discoverability for a fresh reader)
4. <Axis 4> (e.g. governance coherence)
5. Gaps, duplications, inconsistencies

Be specific and honest — name real files. Return a structured critique:
- What is strong (with evidence)
- What is weak or missing (with specifics)
- 3-5 concrete improvement recommendations

Do NOT invent file contents; only report what you actually read.
Write your full critique to <OUTPUT_PATH>
```

## Invocation (background, tracked)

```bash
# terminal tool, background=true, notify_on_complete=true:
hermes chat -q "Read the judge brief at <abs>/judge_brief.txt and execute it fully. Write your complete critique to <abs>/judge_<provider>_<target>.txt" -m claude-sonnet-4-5 --provider anthropic
```

For a SECOND judge: same brief file, different provider
(`-m deepseek-v4-flash --provider deepseek`), different output path. Override
the output path in the -q text ("instead of the deepseek path mentioned in the
brief") so both judges don't collide on one file.

## Verified provider table (2026-08-06)

| Provider | Model | Result |
|---|---|---|
| anthropic | claude-sonnet-4-5 | WORKS — deepest read (77KB critique of a 141-file tree) |
| deepseek | deepseek-v4-flash | WORKS — did real machine checks (edge-set diff, path grep, count tallies) |
| gemini | gemini-2.0-flash | 429 RESOURCE_EXHAUSTED (quota) — check `hermes auth list` / billing first |
| openai-api | gpt-4o / gpt-4o-mini / gpt-4.1 | 400 "Unsupported parameter: 'reasoning.effort'" — config.yaml has reasoning_effort: medium; OpenAI models that don't accept it fail. Not a key problem: a fresh key from ~/Desktop/API Keys authenticated fine, then hit the param 400. |

## Failure transcript (what actually happened, in order)

1. Foreground `hermes chat -q "<300-word inline brief>"` timed out at 300s —
   the judge was reading the tree; default timeout too short.
2. Retry with `nohup ... > file 2>&1 &` and the full inline prompt → died with
   "bash: unexpected EOF while looking for matching quote" + a conda plugin
   crash report. Two separate processes died the same way. Root cause: long
   inline prompt + nohup + conda's bash hooks = quote explosion.
3. Fix: wrote the brief to judge_brief.txt; invoked with a short -q pointing
   at the file; background=true via the terminal tool. Both judges completed
   (3-8 min each). Conda init chatter appeared in captured stdout but was
   harmless shell startup noise.

## Verifying judge findings (don't trust, check)

The DeepSeek judge machine-diffed package edge_maps against the index and
reported "75 cross-skill edges absent." My own full diff (including op-level
edges) found 206 absent. The judge's finding was directionally correct and its
conclusion (index is a curated subset, not the full edge set) was right — but
the number was undercounted. Always re-run the counting yourself before
integrating; the fix (relabel the index as curated canonical subset) is the
same either way, but the honest number goes in the record.

## Judge-value notes

- Two independent providers converging on the same finding = confirmed; fix
  first. Claude and DeepSeek independently flagged: (R1) Phase 5 safeguards
  missing from the packaged tree despite README claims, (R2) graph index
  inconsistent with package edge maps, (R3) quarantine expressed only in the
  index, (R5) verifier not shipped in-tree. Each was verified true.
- Judges that "list files, sample 2-3, machine-check X" produce integrable
  critiques. Judges that only read the README produce vibes. Put the sampling
  and machine-check instructions IN THE BRIEF.
- Convergent "what is strong" verdicts are the kernel to preserve — both
  judges called the harness production-ready, well-governed, evidence-
  disciplined. That anchored the revision round (fix the gaps, keep the core).
