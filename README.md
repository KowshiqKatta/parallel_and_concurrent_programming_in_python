# Parallel and Concurrent Programming in Python — Repo Guide

This repository collects short, focused Python examples and challenge problems used to teach core concurrency and parallelism concepts. The materials are organized into nine topical folders. Each folder contains the original instructional examples plus "safe" demo scripts and small comparison harnesses so you can run finite, repeatable experiments on your machine.

Purpose
- Provide a hands-on catalog of concurrency and parallelism patterns in Python (threads, locks, conditions, semaphores, barriers, futures, pools, multiprocessing patterns).
- Provide safe, runnable demos for learners to explore performance, correctness, and common pitfalls.
- Act as a study and interview prep resource: each section highlights concepts and common interview questions.

Repository structure
- `1 - Threads and Processes` — Thread lifecycle, daemon threads, scheduling, multiple threads/processes examples, and safe harnesses. Teaches thread creation, join/daemon semantics, and process vs thread decisions.
- `2 - Mutual Exclusion` — Data races and lock-based protection. Shows how unsynchronized modifications lead to incorrect shared state and how `threading.Lock` fixes races.
- `3 - Locks` — Reentrant locks, non-blocking acquire, and read-write lock patterns. Demonstrates `RLock`, `acquire(blocking=False)`, and an optional reader/writer lock (pure-Python fallback provided).
- `4 - Liveness` — Deadlock, livelock, abandoned locks, and starvation patterns. Includes safe examples that demonstrate causes and fixes (lock ordering, timeouts).
- `5 - Synchronization` — Condition variables, producer/consumer patterns (threads and processes), and semaphores. Shows how to coordinate work and avoid busy-waiting.
- `6 - Barriers` — Barrier synchronization and race-condition examples. Demonstrates structured rendezvous points for groups of workers.
- `7 - Asynchronous Tasks` — Thread and process pools, futures, divide-and-conquer parallelism. Covers `concurrent.futures` and when to use threads vs processes.
- `8 - Parallel Performance` — Measuring speedup, Amdahl-like experiments, and efficiency computations. Includes safe benchmarking harnesses and notes about measurement pitfalls.
- `9 - Problems` — Practical exercises (download images, matrix multiply, merge sort) with safe, finite implementations and compare scripts.

Key lessons taught
- Concurrency vs parallelism: threads (I/O-bound) vs processes (CPU-bound) and the Python GIL trade-offs.
- Mutual exclusion and atomicity: why data races happen and how locks, RLocks, and higher-level structures prevent them.
- Synchronization primitives: conditions, semaphores, and barriers for coordinating multiple threads/processes.
- Liveness issues: identify and fix deadlock, livelock, and starvation.
- Structured parallelism: executor pools, futures, chunking, and divide-and-conquer approaches.
- Performance measurement: how to measure speedup, avoid measurement noise, and choose task granularity.

How to use this repo (quick start)
1. Ensure you have Python 3.8+ installed.
2. From the repository root run the safe comparison scripts to try short experiments. Example (PowerShell / Windows):

```powershell
python "1 - Threads and Processes\compare_workers.py"
python "7 - Asynchronous Tasks\compare_async.py"
python "8 - Parallel Performance\compare_speedup.py"
python "9 - Problems\compare_problems.py"
```

Notes on running
- On Windows, `multiprocessing` uses spawn semantics. Always guard process-creation code with `if __name__ == '__main__':` (examples in this repo follow that pattern where needed).
- Many original instructor examples use large default sizes for demonstration; prefer the `_safe.py` scripts for quick experiments and adjust parameters (e.g., `workers`, `chunk_size`, `sum_value`) when you need longer runs.
- Network-dependent exercises (original `download_images.py`) have safe, network-free alternatives (`download_images_safe.py`) to avoid flaky runs.

Experiment ideas
- Task granularity: for CPU-bound tasks, sweep chunk sizes and measure runtime; plot speedup vs chunk size.
- Worker scaling: run the same workload with `workers` = 1, cpu_count//2, cpu_count and compute efficiency.
- I/O vs CPU: compare `ThreadPoolExecutor` vs `ProcessPoolExecutor` for the same workload type and observe where each shines.
- Liveness debugging: introduce intentional deadlocks and use the safe examples to practice detecting and fixing them.

Interview-focused checklist
- Concepts you should be able to explain:
  - The GIL and its implications for multi-threaded Python programs.
  - When to use threading vs multiprocessing vs asyncio.
  - Common synchronization primitives and their use-cases: Lock, RLock, Condition, Semaphore, Barrier.
  - Deadlock four conditions and strategies to avoid deadlock (lock ordering, timeouts, try-lock).
  - Speedup, efficiency, and Amdahl's law basics.

- Typical interview tasks to practice from this repo:
  - Fix a data race in a shared counter.
  - Implement a producer/consumer queue with a condition variable.
  - Implement a parallel matrix multiply chunked by rows.
  - Measure and explain why a parallel program does not scale (investigate overhead, contention, false sharing).

Reproducibility and measurement tips
- Run each experiment multiple times and take medians, not single runs.
- Pin down random seeds where appropriate when validating correctness.
- Use `time.perf_counter()` for wall-clock timing and avoid printing in hot loops while measuring.

Repository maintenance notes
- Files ending with `_safe.py` were added to make experiments finite and repeatable — prefer running those for benchmarks.
- Optional third-party dependency: `readerwriterlock` (used in some read/write lock examples). The repo includes a pure-Python fallback so the examples work without extra installs.

Contributing
- Small fixes, improved explanations, or additional safe harnesses are welcome. Open a PR with focused changes and include a short description and a reproducible example when relevant.

License
- This collection is intended for educational use. Add or replace with a license of your choice if you plan to redistribute widely.
