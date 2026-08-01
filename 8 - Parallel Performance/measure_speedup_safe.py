#!/usr/bin/env python3
"""
Safe benchmarking script for measuring sequential vs parallel speedup.

This script intentionally uses moderate defaults so it completes quickly
on most machines. It provides a `run()` function that returns measured
times and speedup for programmatic experiments.
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import os
import multiprocessing as mp

def seq_sum(lo, hi):
    return sum(range(lo, hi))

def par_sum_chunked(lo, hi, chunk=50_000, workers=None):
    # Split the range into chunks and submit each chunk to the process pool.
    ranges = [(s, min(s+chunk, hi)) for s in range(lo, hi, chunk)]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(sum, range(a,b)) for a,b in ranges]
        total = sum(f.result() for f in as_completed(futures))
    return total

def run(sum_value=1_000_000, chunk=50_000, workers=None, runs=3):
    if workers is None:
        workers = max(1, mp.cpu_count() - 1)

    # Warm-up
    _ = seq_sum(1, sum_value)
    _ = par_sum_chunked(1, sum_value, chunk=chunk, workers=workers)

    # Measure sequential
    seq_time = 0.0
    for _ in range(runs):
        start = time.perf_counter()
        seq_sum(1, sum_value)
        seq_time += time.perf_counter() - start
    seq_time /= runs

    # Measure parallel
    par_time = 0.0
    for _ in range(runs):
        start = time.perf_counter()
        par_sum_chunked(1, sum_value, chunk=chunk, workers=workers)
        par_time += time.perf_counter() - start
    par_time /= runs

    speedup = seq_time / par_time if par_time > 0 else float('inf')
    efficiency = 100.0 * speedup / mp.cpu_count()

    return {
        'sum_value': sum_value,
        'chunk': chunk,
        'workers': workers,
        'seq_time': seq_time,
        'par_time': par_time,
        'speedup': speedup,
        'efficiency': efficiency,
    }

if __name__ == '__main__':
    print('PID:', os.getpid())
    res = run()
    print('Sequential time: {:.3f}s'.format(res['seq_time']))
    print('Parallel time:   {:.3f}s'.format(res['par_time']))
    print('Speedup:         {:.2f}'.format(res['speedup']))
    print('Efficiency:      {:.2f}%'.format(res['efficiency']))
