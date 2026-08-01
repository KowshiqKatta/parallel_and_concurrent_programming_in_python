# Liveness — Examples and Notes

This folder contains examples that illustrate liveness problems in concurrent programs: deadlock, abandoned locks, livelock, and starvation. The examples are adapted from an instructional course (screenshot provided by the user) and include safe, finite demos to experiment with and learn from.

## Purpose
- Explain common liveness hazards that can prevent programs from making progress.
- Show practical illustrations and safe fixes/patterns to avoid these hazards.
- Provide repeatable, finite demos suitable for experimentation.

## Files and what they demonstrate
- `deadlock.py` — Classic circular-wait deadlock scenario (Dining Philosophers style). Threads acquire locks in different orders which can lead to deadlock.
- `abandoned_lock.py` and `abandoned_lock-midpoint.py` — Examples showing how exceptions or incorrect lock handling can leave locks in an inconsistent state; demonstrate `try/finally` and context managers.
- `livelock.py` — Threads repeatedly yield/back off and prevent progress (livelock), often solved with randomized backoff or changing the protocol.
- `starvation.py` — Demonstrates how some threads may be perpetually denied access under heavy contention.

### Safe demo files (added)
- `deadlock_safe.py` — Finite deadlock attempt with timeout-based detection and `run_fixed()` demonstrating a fixed lock-ordering strategy.
- `abandoned_lock_safe.py` — Shows safe patterns (try/finally) to avoid abandoned locks and ensure releases even on exceptions.
- `livelock_safe.py` — Demonstrates polite backoff and randomized waits to resolve livelock.
- `starvation_safe.py` — Runs many threads with finite iterations and prints per-thread results to observe distribution.
- `compare_liveness.py` — Runs the safe liveness demos and prints concise results for comparison.

## Key takeaways
- Deadlock arises from circular wait; avoid it via lock ordering, timeouts, or lock hierarchies.
- Always release locks (use `try/finally` or `with`) to prevent abandoned locks, especially when exceptions may occur.
- Livelock is different from deadlock — threads are actively yielding but not making progress; randomized backoff or changing the protocol mitigates it.
- Starvation happens when scheduling or contention biases prevent some threads from obtaining resources; fairness mechanisms or redesign can help.

## How to run these examples
Prefer the safe demos for learning and experiments. Examples:

```powershell
python "4 - Liveness\compare_liveness.py"
python "4 - Liveness\deadlock.py"
python "4 - Liveness\abandoned_lock.py"
python "4 - Liveness\livelock.py"
python "4 - Liveness\starvation.py"
```

Notes:
- The original examples may loop until a large count; use the `_safe.py` variants for finite, repeatable runs.
- Some liveness issues are non-deterministic and depend on scheduling; run experiments multiple times to observe behavior.

## Suggested experiments / next steps
- Modify `deadlock_safe.py` to add timeouts or use `acquire(timeout=...)` and observe behavior.
- Instrument `starvation_safe.py` to log per-thread wait times and visualize fairness.
- Implement higher-level approaches (e.g., message passing, task queues) to avoid shared-lock contention entirely.

## Attribution
Examples are based on an instructional course; the user provided a screenshot of the course contents to clarify the learning goals for the `Liveness` section.


