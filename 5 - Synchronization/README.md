# Synchronization — Examples and Notes

This folder contains examples demonstrating synchronization primitives in Python: condition variables, producer-consumer coordination using queues (threads and processes), and semaphores. The examples are adapted from an instructional course (screenshot provided by the user) and now include safe, finite demos for experimentation.

## Purpose
- Demonstrate coordination patterns that let threads/processes wait, notify, and exchange data safely.
- Show common primitives: `Condition`, `Queue` (producer/consumer), and `Semaphore`.
- Provide safe, repeatable demos suitable for measuring behavior and learning.

## Files and what they demonstrate
- `condition_variable.py` — Uses `threading.Condition` to implement turn-taking for multiple waiting threads.
- `producer_consumer_threads.py` — Producer and consumer coordinated with `queue.Queue` in threads; uses sentinel values for shutdown.
- `producer_consumer_processes.py` — Process-based producer/consumer using `multiprocessing.Queue` showing how processes can run CPU-bound consumers.
- `semaphore.py` — Demonstrates `threading.Semaphore` to limit concurrent access to a resource (charging stations).

### Safe demo files (added)
- `condition_variable_safe.py` — Finite condition-variable demo that records results for verification.
- `producer_consumer_safe.py` — Provides `run_threads()` and `run_processes()` for timed, finite producer/consumer experiments.
- `semaphore_safe.py` — Finite semaphore demo measuring elapsed time with configurable slots.
- `compare_synchronization.py` — Runs the safe demos and prints concise timings/results to compare behaviors.

## Key takeaways
- `Condition` allows threads to wait for predicates and be notified when state changes; use it with an associated lock.
- `queue.Queue` is a thread-safe buffer that simplifies producer-consumer patterns; `multiprocessing.Queue` provides the same idea across processes.
- `Semaphore` controls concurrency by limiting the number of simultaneous holders of a resource.
- Use sentinel values or other shutdown protocols to gracefully stop consumers.

## How to run these examples
Prefer the safe demo scripts for repeatable runs. Examples:

```powershell
python "5 - Synchronization\compare_synchronization.py"
python "5 - Synchronization\condition_variable.py"
python "5 - Synchronization\producer_consumer_threads.py"
python "5 - Synchronization\producer_consumer_processes.py"
python "5 - Synchronization\semaphore.py"
```

Notes:
- The process-based producer/consumer shows how to offload CPU-bound work to processes; `multiprocessing` requires spawn semantics on Windows.
- Adjust item counts, buffer size, and worker counts in the `_safe` scripts to explore throughput and latency trade-offs.

## Suggested experiments / next steps
- Compare latency and throughput between threaded and process-based producers/consumers with larger payloads.
- Add instrumentation (timestamps, queue lengths) to `producer_consumer_safe.py` and plot results.
- Experiment with `Condition` predicates to implement different scheduling policies.

## Attribution
Examples are based on an instructional course; the user provided a screenshot of the course contents to clarify the learning goals for the `Synchronization` section.