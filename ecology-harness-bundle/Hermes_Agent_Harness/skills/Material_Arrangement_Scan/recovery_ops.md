# Material Arrangement Scan — Recovery Ops

Recovery operations for when a scan goes wrong or the environment changes.

## restore_material_inventory
If a materials scan is incomplete or the environment changed mid-scan,
re-run the inventory from the current environment description (never from
a stale cache).

## revert_arrangement_proposal
If a proposal was adopted and then reversed by the user, record the
reversal and its reason — the reversal is data, not failure.

## re_anchor_meanings
If a meaning framing was mis-attributed (user corrects the agent's
reading), re-anchor to the user's correction; the correction feeds the
calibration log (user_correction pattern threshold = 2).

## partial_scan_recovery
If only part of the environment is described, complete what is known and
surface the missing pieces as open_probes — never guess the unseen
environment.
