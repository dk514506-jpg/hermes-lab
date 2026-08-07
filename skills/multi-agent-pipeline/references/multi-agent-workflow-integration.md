# Multi-Agent Pipeline Reference

Detailed notes on the tonbistudio/hermes-multi-agent-workflow template
as reference implementation.

## Architecture Deep Dive

The template ships a complete worked example: finding AI-agent pain points
from X and Reddit, then either building a fix or making an explainer video.
Key design decisions extracted from the source:

### Config-Driven Everything (triage.yaml)

- **Sources** define scouts: one profile per source (e.g. xresearch for X,
  webresearch for Reddit/YouTube), each with its own cron schedule and query.
  Schedules are staggered to avoid thundering herd on the Kanban board.
- **Item schema** defines the structured fields a scout emits. Fields like
  `why_it_may_matter`, `agent_solvable_or_explainable`, `solution_gap`,
  `strategic_fit` are consumed by the scoring rubric and routing classifier.
- **Rubric** has named dimensions, each with a max score and a hint string
  the LLM uses to judge. The engine sums the dimensions and compares to
  threshold. LLM mode is fully general; heuristic mode is keyed to reference
  dimension names.
- **Research lanes** run in parallel using Hermes Kanban's parent-task fan-in.
  The `classifier_lane` is the one lane whose output the router reads — all
  other lanes provide context but don't drive routing.
- **Route map** maps classification values to path names. Every value must be
  a key under `paths:`. Unknown values raise ValueError (fail loud).

### Fat Engine in Detail

The `engine/` package contains:

- `config.py` — loads and validates triage.yaml into typed dataclasses
- `engine.py` — TriageEngine class: dedup, score, research_specs, route,
  prep_specs, fulfillment_specs, _injected_constraints
- `scoring.py` — rubric_prompt(), score_from_breakdown() for LLM mode,
  score_candidate_heuristic() for deterministic mode
- `routing.py` — route_from_classification() — pure dict lookup with
  ValueError on unknown keys
- `dedup.py` — token-cosine with configurable thresholds; embedding-ready
- `item_vault.py` — one markdown file per tracked item
- `kanban_store.py` — writes the Hermes Kanban board
- `intake_parser.py` — parses scout reports

The engine returns `TaskSpec` dataclasses (title, body, role, parents,
workspace_kind, workspace_path) rather than touching the board directly.
Side effects live in `proposal_actions.py` (gate handler) and the
orchestrator skill.

### Kanban as the Coordination Bus

The entire pipeline runs on ONE Hermes Kanban board:
- Scout creates an intake card
- Orchestrator creates a triage card + research fan-out cards
- Research cards complete → route card fan-ins (parented to ALL research
  cards, so the kernel fires it when the last one finishes)
- Prep chain cards are sequentially parented
- Gate pauses until human reply
- Fulfillment chain runs in a persistent workspace directory

## References

- Repo: https://github.com/tonbistudio/hermes-multi-agent-workflow
- AGENTS.md: https://raw.githubusercontent.com/tonbistudio/hermes-multi-agent-workflow/main/AGENTS.md
- Architecture doc: https://raw.githubusercontent.com/tonbistudio/hermes-multi-agent-workflow/main/docs/01-architecture.md
- Full config reference: https://raw.githubusercontent.com/tonbistudio/hermes-multi-agent-workflow/main/docs/03-config-reference.md
- Security docs: https://raw.githubusercontent.com/tonbistudio/hermes-multi-agent-workflow/main/docs/06-security.md
