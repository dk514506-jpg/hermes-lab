## Support Operations
Use these when prerequisites are missing before sparring can proceed.

### Configure_Persona
Select or assemble a persona from the sanitized persona bank. Sanitization checks
(Ma 2025): no demographic stereotypes, no degrading priming, no inference from lattice
insights about the user. If no suitable persona exists, build one via persona_config.yaml
and run the sanitization audit before use.

### Select_Rubric
Choose the rubric matching the practice target (MI fidelity, coaching inquiry, conflict
de-escalation, negotiation framing). Rubrics are lenses: every dimension anchors to
utterance-level evidence. If the target lacks a rubric, build one with the user and mark
it provisional.

### Set_Intensity
Agree the starting pushback level (1–5) and escalation policy with the user before the
session. Intensity is user-owned: the user can lower it at any time.

### Scenario_Selector
Pick a scenario from the bank matched to the practice target and desired context
(work / family / clinical / negotiation). Custom scenarios allowed; transfer scenarios
are marked with transfer_flag=true.

### Interrupt_Coach
User-controlled coaching interruption: pause the persona, deliver an in-session hint,
then resume from the same stage (immersion preserved). The user decides whether and when
to interrupt; coaching is on_demand by default.

### Persona_Bank_Sanitizer
Audit personas for bias and degrading priming before any session (Ma 2025). Runs
automatically at configure_persona; flagged personas are quarantined, not deleted, and
can be repaired.

### Readiness_Gate
Before a high-stakes stress test, confirm the user's readiness and consent (Liu 2026
state-timing: interventions should align to user state, not the agent's schedule).
