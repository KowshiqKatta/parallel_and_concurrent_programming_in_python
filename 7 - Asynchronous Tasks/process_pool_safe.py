#!/usr/bin/env python3
"""
Safe process-pool demo — finite, timed tasks.

Runs CPU-light tasks in a ProcessPoolExecutor to illustrate process
parallelism and measure elapsed time.
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import os

def task(n):
    # small CPU-bound work
    s = 0
    for i in range(100_000):
        s += i
    return os.getpid(), n

def run(num_tasks=80, workers=4):
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(task, i) for i in range(num_tasks)]
        for f in as_completed(futures):
            _ = f.result()
    return time.perf_counter() - start

if __name__ == '__main__':
    print('PID:', os.getpid())
    print('Process pool time:', run())
