# Barriers — Examples and Notes

This folder contains short examples demonstrating the use of barriers
and a simple race-condition scenario. The code is adapted from an
instructional course (screenshot provided by the user) and includes
safe, finite demos to experiment with and compare behavior.

## Purpose
- Illustrate `threading.Barrier` for coordinating a group of threads at
  a rendezvous point.
- Show how ordering and rendezvous can affect final results compared to
  no-barrier execution.

## Files and what they demonstrate
- `barrier.py` — Shows a Barrier coordinating pairs of shoppers so that
  certain operations happen after all participants reach the barrier.
- `race_condition.py` — A simple race/coordination example for shared
  updates (used for comparison with the barrier pattern).

### Safe demo files (added)
- `race_condition_safe.py` — Finite, timed no-barrier run returning the
  final value for verification.
- `barrier_safe.py` — Finite, timed run that uses `threading.Barrier`.
- `compare_barriers.py` — Runs both safe demos and prints final values
  and timings for easy comparison.

## Key takeaways
- A `Barrier` synchronizes N threads so that each waits for the group
  before proceeding — useful for phase-based algorithms.
- Barriers help enforce ordering constraints and can simplify reasoning
  about coordinated phases of work.
- Use barriers carefully: they introduce a point where all participants
  must arrive; a missing participant will cause others to block.

## How to run these examples
Prefer the safe demos for repeatable experiments. Examples:

```powershell
python "6 - Barriers\compare_barriers.py"
python "6 - Barriers\barrier.py"
python "6 - Barriers\race_condition.py"
```

Notes:
- The safe demos return final values and timings so you can compare
  runs deterministically and rerun experiments with different sizes.

## Suggested experiments / next steps
- Vary the number of pairs/participants in the safe demos and observe timings.
- Introduce a faulty participant (never arrives) to see barrier blocking.
- Combine barriers with other primitives (locks, conditions) for multi-phase algorithms.