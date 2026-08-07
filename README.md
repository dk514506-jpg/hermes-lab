# Hermes Lab — Dallas's Skill Library

Custom skills built and refined in the Hermes home lab (Linux, Nous Portal
backed). These encode the lab's working procedures: astrological persona
research, the Motivational Ecology campaign, Valens anthology reconstruction,
multi-agent pipeline orchestration, and evaluation/QA workflows.

## What's inside

All skills follow the agentskills.io open standard (SKILL.md + references/).
Install any of them into your own Hermes agent with:

```bash
hermes skills install <owner>/hermes-lab/skills/<skill-name>
```

Or add this repo as a tap to browse and install everything:

```bash
hermes skills tap add <owner>/hermes-lab
hermes skills search ecology
```

### The skills

| Skill | What it does |
|---|---|
| astral-research-harness | Always-on research assist for the Capricorn-Scorpio-Taurus-Pisces persona cluster |
| astro-persona-profiles | Manage planetary persona profiles + YAML enrichment |
| ecology-dojo-authoring | Build/QA Ecology doc-tree deliverables (dojos, QA checklists) |
| ecology-evaluation-qa | Applied QA checklists for Ecology phases |
| faos-pipeline-architecture | Design/audit FAOS-governed multi-agent pipelines |
| multi-agent-pipeline | Config-driven multi-agent triage pipelines |
| valens-anthologies-reconstruction | Read/distill the Valens Anthologies corpus |
| cross-provider-critique | Outside judges from other LLM APIs |
| llm-evaluation-audit | Audit LLM-generated evaluations against their rubrics |
| recent-evidence-distillation | Distill recent evidence into verified structured reviews |
| large-corpus-ingestion | Ingest corpora via manifest + selective reads |
| hiskill-package-authoring | Build/QA 9-file HiSkill skill packages |
| self-hosted-web-deployment | Deploy web services with Tailscale, auth, systemd |

## Notes

- Machine-specific absolute paths have been scrubbed to `~/` references.
- The Valens *corpus* (book text + artifacts) is intentionally NOT included —
  ask Dallas if you want access to that material directly.
- Built with Hermes Agent (https://hermes-agent.nousresearch.com) — Nous
  Research's self-improving agent framework.
