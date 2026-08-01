#!/usr/bin/env python3
"""
Safe multiple threads example — finite CPU work and timing.

This module provides a `run()` function that starts a number of threads
which each perform a finite amount of CPU-bound work. It is intended
for safe, repeatable experiments and timing comparisons with the
`multiple_processes_safe.py` runner.
"""

import os
import threading
import time

def cpu_work(iterations: int):
    s = 0
    for i in range(iterations):
        s += i * i
    return s

def worker(iters: int):
    cpu_work(iters)

def run(num_workers: int = 12, iterations: int = 200_000):
    threads = []
    start = time.perf_counter()
    for _ in range(num_workers):
        t = threading.Thread(target=worker, args=(iterations,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return time.perf_counter() - start

if __name__ == '__main__':
    print('Process ID:', os.getpid())
    duration = run()
    print(f'Threads completed in {duration:.3f} s')
