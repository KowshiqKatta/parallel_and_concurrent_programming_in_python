# Problems — Challenge Exercises

This folder contains challenge problems from the course: downloading images, matrix multiplication, and merge sort. Each original example is preserved (kept as instructional artifacts) and a set of safe, finite demos has been added for reproducible experimentation.

## Purpose
- Present practical problem-solving exercises that apply parallel and concurrent patterns.
- Provide safe, runnable demos so learners can measure behavior without long-running tasks or network dependencies.

## Files and what they demonstrate
- `download_images.py` — Original challenge that downloads many images sequentially and with a thread pool (I/O-bound). See `download_images_safe.py` for a network-free demo.
- `matrix_multiply.py` — Sequential and process-based parallel matrix multiplication. See `matrix_multiply_safe.py` for a smaller, process-parallel demo.
- `merge_sort.py` — Sequential and process-parallel merge sort (recursive). See `merge_sort_safe.py` for a chunked parallel sorter that avoids deep recursion.

### Safe demo files (added)
- `download_images_safe.py` — Simulates downloads by writing small binary files and measures sequential vs threaded times.
- `matrix_multiply_safe.py` — Row-chunked process-parallel matrix multiplication with reasonable defaults.
- `merge_sort_safe.py` — Chunked parallel sorting using worker processes and `heapq.merge`.
- `compare_problems.py` — Runs the safe demos and prints timings/results for quick comparisons.

## Key takeaways
- Challenge problems illustrate trade-offs: I/O vs CPU-bound workloads, task granularity, and parallel overhead.
- Use safe demos for quick iteration; scale inputs and chunk sizes when you need higher-fidelity measurements.
- On Windows, `multiprocessing` uses spawn; ensure heavy process creation is guarded by `if __name__ == '__main__':`.

## How to run
Recommended quick run of all safe demos:

```powershell
python "9 - Problems\compare_problems.py"
python "9 - Problems\download_images_safe.py"
python "9 - Problems\matrix_multiply_safe.py"
python "9 - Problems\merge_sort_safe.py"
```

Adjust parameters like `num_images`, matrix size `n`, `chunk_size`, and `workers` in the `_safe` scripts to explore performance trade-offs.

## Suggested experiments
- Vary the number of worker processes/threads and plot speedup vs workers.
- Sweep chunk sizes for matrix multiplication and merge sort to see the overhead vs work trade-off.
- For `download_images.py`, compare local simulated runs to real network runs only when you have a fast, reliable connection.
