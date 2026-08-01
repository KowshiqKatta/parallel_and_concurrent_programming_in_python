#!/usr/bin/env python3
"""
Safe divide-and-conquer sum that materializes the sum instead of
returning futures; uses a process pool for parallelism.
"""

from concurrent.futures import ProcessPoolExecutor
import os
import time

def chunk_sum(lo, hi):
    return sum(range(lo, hi))

def parallel_sum(lo, hi, chunk=100_000, workers=4):
    starts = list(range(lo, hi, chunk))
    tasks = [(s, min(s+chunk, hi)) for s in starts]
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(chunk_sum, a, b) for a,b in tasks]
        total = sum(f.result() for f in futures)
    return total, time.perf_counter() - start

if __name__ == '__main__':
    print('PID:', os.getpid())
    total, dur = parallel_sum(1, 1_000_000)
    print('Total sum:', total, 'time:', dur)
