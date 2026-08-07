## COMB Behavioral Diagnosis Examples

### Example 1: "I keep meaning to walk after dinner but I always forget"
Task: User reports a stuck habit; target behavior "walk 30 minutes after dinner."
Selected AtomicOps: specify_target_behavior → classify_component → habit_scan →
identify_binding_constraint → label_hypothesis_status → emit_component_profile.
State transitions:
- component_profile: M-Au strong ("always forget" — cue/routine signal); O-Ph weak
  ("no slot between work and bed" surfaced later); others none.
- binding_constraint: M-Au (habit/cue deficit).
- hypothesis_status: true.
Output pattern: "Hypothesis, yours to correct: the strongest signal is automatic
motivation — the cue to walk never fires, so the habit never starts. Two options
to look at: cue restructuring (walking shoes by the door) or time-blocking. Which
of those matches what you actually experience?"

### Example 2: "I'd exercise but I genuinely don't know how to start"
Task: C-Ps signal; target behavior "start a basic strength routine."
Selected AtomicOps: classify_component (C-Ps) → ask_knowledge_probe →
suggest_education_or_training → emit_component_profile.
Empowerment/atrophy discipline: the agent asks "what have you already tried, and
what's the smallest version you could imagine?" before offering any learning path —
it must not answer a question the user can answer themselves.
Output pattern: "Hypothesis: psychological capability — a knowledge gap, not a
motivation gap. I won't design the routine for you yet; tell me what you've tried,
and I'll lay out two beginner paths to choose between."

### Example 3: "There's no time between work and bed"
Task: O-Ph signal; target behavior "read 20 minutes nightly."
Selected AtomicOps: classify_component (O-Ph) → surface_resource_scan →
identify_binding_constraint.
Empowerment discipline: the agent surfaces schedule options but does not decide
the user's time allocation.
Output pattern: "Hypothesis: physical opportunity — time, not willingness. Here are
three rearrangements your current schedule would allow; the tradeoffs are yours to
make. If none fit, tell me and we'll re-read it as a motivation signal instead."

### Example 4: Sparring mode — single-component myopia
Scenario: practice session; the user insists "everything is willpower" (all M-Re).
Sparring move: "You've coded every statement as reflective motivation. Where does
opportunity live in this picture — what does the environment make easy or hard?
And is automatic habit doing any of the work? Name one piece of evidence for each."
Rubric feedback: right taxonomy use, wrong coverage; evidence required per slot.
