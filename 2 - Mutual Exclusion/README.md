# Mutual Exclusion — Examples and Notes

This folder contains concise Python examples that illustrate data races and basic mutual exclusion using locks. The code is adapted from an instructional course (screenshot provided by the user) and is intended for learning and safe experimentation.

## Purpose
- Demonstrate how concurrent access to shared data can produce incorrect results (data races).
- Show how `threading.Lock()` enforces mutual exclusion to prevent races.
- Provide small, safe experiments for comparing unlocked vs locked behavior and measuring lock overhead.

## Files and what they demonstrate
- `data_race.py` — Two threads increment a shared counter without synchronization. This demonstrates a data race; the final result may be less than expected.
- `mutual_exclusion.py` — Uses a `threading.Lock()` (named `pencil`) to serialize increments and prevent the race.

### Safe demo files (added)
- `race_safe.py` — Finite, timed threaded increments with two modes: `run_unlocked()` (no lock) and `run_locked()` (with `threading.Lock`). Use these for repeatable experiments.
- `race_compare.py` — Small harness that runs both modes from `race_safe.py` and prints the final counter values and elapsed times.

## Key takeaways
- Concurrent updates to shared mutable state can interleave and lose updates — this is a data race.
- A `Lock` provides mutual exclusion: only one thread may hold the lock at a time, preventing simultaneous updates.
- Mutual exclusion ensures correctness but may add overhead; measuring both modes helps reason about the trade-off.
- Even with the GIL, race conditions can occur for non-atomic or multi-step operations; do not rely on the GIL for correctness.

## How to run these examples
Open a terminal in this workspace and run the scripts. Examples:

```powershell
python "2 - Mutual Exclusion\data_race.py"
python "2 - Mutual Exclusion\mutual_exclusion.py"
python "2 - Mutual Exclusion\race_compare.py"
```

Notes:
- `data_race.py` uses a very large iteration count; prefer `race_compare.py` for safe, repeatable experiments.
- You can adjust `threads` and `iterations` in `race_compare.py` to match your machine and explore trade-offs.

## Suggested experiments / next steps
- Vary the number of threads and iterations in `race_compare.py` and observe the results.
- Replace the global counter with operations that are non-atomic (e.g., multiple variable updates) to see more pronounced races.
- Explore `threading.RLock()`, `Semaphore`, or higher-level primitives (e.g., `queue.Queue`) for different coordination patterns.

## Attribution
Examples are based on an instructional course; the user provided a screenshot of the course contents to clarify the learning goals for the `Mutual Exclusion` section. Use these examples for educational purposes and adapt them for hands-on exploration.

## Python / environment
- Recommended: Python 3.8 or newer.
- Uses only the standard library (`threading`, `time`). No external dependencies required.
