# Parallel Performance — Measure Speedup

This folder focuses on measuring parallel performance (speedup and efficiency) for a simple summation workload. The original instructor example uses a recursive divide-and-conquer approach with a process pool; safe demo scripts have been added to make experiments repeatable on typical machines.

## Purpose
- Illustrate sequential vs parallel execution time for a CPU-bound workload.
- Teach speedup and efficiency concepts and how to measure them practically in Python.

## Files and what they demonstrate
- `measure_speedup.py` — Original recursive divide-and-conquer example (returns futures when given a pool). See the header for notes; this file is kept as an instructional artifact.
- `measure_speedup_safe.py` — Added safe benchmark that materializes the sum using chunked parallelism and returns measured timings and speedup. Use this for experiments.
- `compare_speedup.py` — Simple harness that runs the safe benchmark with different worker counts and prints results.

## Key takeaways
- Speedup = T_sequential / T_parallel. Values greater than 1 indicate a parallel benefit.
- Efficiency = Speedup / number_of_cores (expressed as a percentage); shows how well the program uses available cores.
- Parallel overhead and task granularity matter: too-small tasks increase overhead and reduce speedup.

## How to run
Run the safe benchmark and compare harness (recommended):

```powershell
python "8 - Parallel Performance\measure_speedup_safe.py"
python "8 - Parallel Performance\compare_speedup.py"
```

Notes:
- The safe runner defaults are conservative so the script finishes quickly. Increase `sum_value` and adjust `chunk` in `measure_speedup_safe.py` for more substantial experiments.
- On Windows, `multiprocessing` uses spawn semantics; keep `if __name__ == '__main__':` guards when invoking process pools.

## Suggested experiments
- Sweep `chunk` sizes to observe the trade-off between task overhead and parallel work.
- Vary `workers` (see `compare_speedup.py`) to measure scaling across CPU counts.
- Plot runtime vs workers and compute efficiency to visualize Amdahl-like behaviour.
