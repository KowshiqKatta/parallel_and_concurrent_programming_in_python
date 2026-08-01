# Locks — Examples and Notes

This folder contains focused Python examples that demonstrate lock primitives and patterns: re-entrant locks (`RLock`), non-blocking `Lock.acquire()`, and reader-writer locks. The code is adapted from an instructional course (screenshot provided by the user) and is intended for learning and safe experimentation.

## Purpose
- Illustrate `threading.RLock()` for re-entrant locking.
- Show non-blocking `Lock.acquire(blocking=False)` to attempt a critical section without waiting.
- Demonstrate reader-writer locking; the original example uses a third-party package, but a pure-Python safe demo is included here.

## Files and what they demonstrate
- `reentrant_lock.py` — Example showing nested lock acquisition using `threading.RLock()`.
- `nonblocking_acquire.py` — Demonstrates `Lock.acquire(blocking=False)` so threads can try the critical section and do other work if busy.
- `readwrite_lock.py` — Uses the `readerwriterlock` third-party package to demonstrate a fair reader-writer lock where many readers can access concurrently and writers gain exclusive access.

### Safe demo files (added)
- `reentrant_lock_safe.py` — Finite, timed demo using `threading.RLock()` (re-entrant behavior with nested lock acquisition).
- `nonblocking_acquire_safe.py` — Finite, timed demo using non-blocking `Lock.acquire()` with a target count.
- `readwrite_lock_safe.py` — Pure-Python `RWLock` implementation and demo (no external deps).
- `compare_locks.py` — Runs the three safe demos and prints timings/results for quick comparisons.

## Dependencies
- The original `readwrite_lock.py` imports `readerwriterlock` (a third-party package). To run the original example, install it with:

```powershell
pip install readerwriterlock
```

Alternatively, run the included pure-Python `readwrite_lock_safe.py` which has no external dependencies.

## Key takeaways
- `RLock` allows the same thread to acquire a lock multiple times safely, useful for nested calls.
- Non-blocking `acquire()` lets a thread try the critical section and do other work if it's busy, enabling more responsive designs.
- Reader-writer locks optimize for many-readers/few-writers scenarios by allowing concurrent reads while preserving exclusive writes.
- Locks solve race conditions by serializing access, but they introduce contention and potential performance trade-offs.

## How to run these examples
Open a terminal in this workspace and run the safe demos or the originals. Examples:

```powershell
python "3 - Locks\compare_locks.py"
python "3 - Locks\reentrant_lock.py"
python "3 - Locks\nonblocking_acquire.py"
python "3 - Locks\readwrite_lock.py"   # requires `readerwriterlock` or run the safe demo instead
```

Notes:
- Prefer the `_safe.py` scripts for repeatable experiments.
- Adjust thread counts and iterations in the safe demo scripts to suit your machine.

## Suggested experiments / next steps
- Replace the pure-Python `RWLock` with the `readerwriterlock` package and compare fairness/performance.
- Measure latency of non-blocking vs blocking acquire under high contention.
- Experiment with `threading.RLock()` in real nested code paths to see when it's necessary.

## Attribution
Examples are based on an instructional course; the user provided a screenshot of the course contents to clarify the learning goals for the `Locks` section.

