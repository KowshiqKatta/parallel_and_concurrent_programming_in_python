#!/usr/bin/env python3
"""
Safe multiple processes example — finite CPU work and timing.

This module provides a `run()` function that starts a number of worker
processes which each perform a finite amount of CPU-bound work. Use it
to compare timings with `multiple_threads_safe.py`.
"""

import os
import multiprocessing as mp
import time

def cpu_work(iterations: int):
    s = 0
    for i in range(iterations):
        s += i * i
    return s

def worker(iters: int):
    # perform work; result discarded to keep the example simple
    cpu_work(iters)

def run(num_workers: int = 12, iterations: int = 200_000):
    processes = []
    start = time.perf_counter()
    for _ in range(num_workers):
        p = mp.Process(target=worker, args=(iterations,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    return time.perf_counter() - start

if __name__ == '__main__':
    print('Main PID:', os.getpid())
    duration = run()
    print(f'Processes completed in {duration:.3f} s')
