# Threads and Processes — Examples and Notes

This folder contains short, focused Python examples that demonstrate core differences, behaviours, and usage patterns for threads and processes. The code is adapted from an instructional course (screenshot provided by the user) and is intended for learning and experimentation.

## Purpose
- Provide compact, runnable examples that illustrate thread lifecycle, daemon threads, CPU-bound behaviour under threads vs processes, and basic execution scheduling.
- Serve as a hands-on supplement to learning about concurrency and parallelism in Python.

## Files and what they demonstrate
- `daemon_thread.py` — Demonstrates a daemon `threading.Thread` that runs in the background while the main thread finishes. Shows how daemon threads are killed when the main program exits.
- `thread_lifecycle.py` — Shows creating a `Thread` subclass, starting a worker thread, checking `is_alive()`, and using `join()` to wait for completion. Illustrates thread lifecycle methods and synchronization by waiting.
- `execution_scheduling.py` — Two threads concurrently run a loop controlled by a shared boolean flag. Demonstrates scheduler-driven interleaving and how threads alternate work when the GIL is present.
- `multiple_threads.py` — Starts many CPU-wasting threads (busy loops). Useful to observe that CPU-bound threads do not achieve true parallelism in CPython due to the GIL.
- `multiple_processes.py` — Starts multiple OS processes doing the same CPU-wasting work. Demonstrates how multiple processes can run on multiple CPU cores and bypass the GIL.

### Safe runners (added)
- `multiple_threads_safe.py` — Finite, timed threaded workload suitable for experiments.
- `multiple_processes_safe.py` — Finite, timed process-based workload suitable for experiments.
- `compare_workers.py` — Small harness that runs the safe threaded and process runners sequentially and prints elapsed time for each.

## Key takeaways
- Threads are lightweight and share memory; processes have separate memory and provide true parallelism for CPU-bound work.
- Daemon threads exit automatically when the main program ends; non-daemon threads keep the program alive until they finish or are joined.
- The GIL prevents CPU-bound Python threads from running in true parallel on multiple cores; use `multiprocessing` for CPU-bound parallelism.
- Thread lifecycle methods (`start()`, `is_alive()`, `join()`) let the main thread coordinate worker threads.
- Busy-waiting (infinite loops) is an anti-pattern for cooperative programs; use proper synchronization primitives or sleep/yield to avoid hogging CPU.

## How to run these examples
Open a terminal in this workspace and run the individual scripts with the Python interpreter you use for learning (Python 3.8+ recommended). Examples:

```powershell
python "1 - Threads and Processes\daemon_thread.py"
python "1 - Threads and Processes\thread_lifecycle.py"
python "1 - Threads and Processes\execution_scheduling.py"
python "1 - Threads and Processes\multiple_threads.py"
python "1 - Threads and Processes\multiple_processes.py"
```

Notes:
- `multiple_threads.py` and `multiple_processes.py` intentionally create CPU-wasting loops — run them with care and terminate (Ctrl+C) when you want to stop them.
- To observe multi-core parallelism, run `multiple_processes.py` and monitor CPU usage with your OS tools (Task Manager on Windows).

## Suggested experiments / next steps
- Modify the CPU-waster to do observable work (e.g., increment a counter and sleep briefly) to see scheduler behaviour.
- Replace busy loops with `time.sleep()` or `threading.Event()` waits to learn cooperative multitasking.
- Measure real speedup by implementing a CPU-bound function (e.g., matrix multiply) and comparing `threads` vs `multiprocessing.Pool` runs.
- Introduce locks and shared data to study race conditions and mutual exclusion.

To run the safe comparison harness:

```powershell
python "1 - Threads and Processes\compare_workers.py"
```

## Attribution
The examples in this folder are based on an instructional course; the user provided a screenshot of the course contents to clarify the learning goals for the `Threads and Processes` section. Use these examples for educational purposes and adapt them for hands-on exploration.

## Python / environment
- Recommended: Python 3.8 or newer.
- These examples use only the standard library (`threading`, `multiprocessing`, `time`, `os`). No external dependencies needed.

---
