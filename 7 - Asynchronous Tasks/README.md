# Asynchronous Tasks — Examples and Notes

This folder demonstrates asynchronous task patterns in Python: thread pools, process pools, futures, and divide-and-conquer parallelism. Examples are adapted from an instructional course (screenshot provided by the user) and now include safe, finite demos for learners to experiment with.

## Purpose
- Show how to use `ThreadPoolExecutor` and `ProcessPoolExecutor` for concurrent and parallel execution.
- Demonstrate `Future` objects and how to obtain results asynchronously.
- Provide a divide-and-conquer pattern for large parallel computations using process pools.

## Files and what they demonstrate
- `thread_pool.py` — Example using `ThreadPoolExecutor` to submit many small tasks (suitable for I/O-bound work).
- `process_pool.py` — Example using `ProcessPoolExecutor` for CPU-bound tasks to utilize multiple cores.
- `future.py` — Demonstrates submitting work and using the returned `Future` to retrieve results while the main thread performs other work.
- `divide_and_conquer.py` — Recursive divide-and-conquer summation example using a process pool (original returns futures; safe demo materializes sums).

### Safe demo files (added)
- `thread_pool_safe.py` — Finite, timed thread-pool run collecting results.
- `process_pool_safe.py` — Finite, timed process-pool run for CPU work.
- `future_safe.py` — Future example showing `result(timeout=...)` semantics.
- `divide_and_conquer_safe.py` — Chunked parallel sum that materializes results for a safe benchmark.
- `compare_async.py` — Runs the safe demos and prints timings/results for easy comparison.

## Key takeaways
- Use thread pools for I/O-bound concurrency and process pools for CPU-bound parallelism.
- `Future` lets you submit work and obtain results later; use `as_completed()` to handle completed tasks incrementally.
- Divide-and-conquer parallelism can scale large computations but requires careful chunking and overhead trade-off consideration.

## How to run these examples
Prefer the safe demos for reliable experiments. Examples:

```powershell
python "7 - Asynchronous Tasks\compare_async.py"
python "7 - Asynchronous Tasks\thread_pool.py"
python "7 - Asynchronous Tasks\process_pool.py"
python "7 - Asynchronous Tasks\future.py"
python "7 - Asynchronous Tasks\divide_and_conquer.py"
```

Notes:
- On Windows, `multiprocessing` and `ProcessPoolExecutor` use spawn semantics; guard process-creation code under `if __name__ == '__main__':` as in the examples.
- Adjust `num_tasks`, `workers`, and chunk sizes in the `_safe` scripts to match your machine and explore performance trade-offs.

## Suggested experiments / next steps
- Compare throughput and latency between thread and process pools with varying task granularity.
- Use `as_completed()` in `thread_pool_safe.py` or `process_pool_safe.py` to process results as they finish.
- Explore async/await for high-level I/O concurrency when integrating network or disk I/O.
