# Feedback Ecology Map — Recovery Ops

Recovery operations for when an embedding assessment goes wrong.

## re_anchor_coherence
If a coherence reading mis-attributed the user's meaning (user corrects
the agent), re-anchor to the user's framing; the correction feeds the
calibration log (user_correction pattern threshold = 2).

## downgrade_cmo_hypothesis
If a CMO hypothesis is contradicted by new evidence, downgrade it on the
evidence ladder (claim → lead) rather than defending it. Hypothesis
status is always revisable; the ladder is the mechanism.

## partial_embedding_recovery
If only some mechanisms can be assessed (runtime signals missing), report
what is known and surface the rest as open_probes — never fabricate a
participation or collective-action reading from no signal.

## history_gap_recovery
If normalization_state_history is empty, start the trajectory at the
current assessment and mark the series as starting-now (no retroactive
fabrication of past embedding).
