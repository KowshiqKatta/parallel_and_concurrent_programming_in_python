#!/usr/bin/env python3
"""
Safe thread-pool demo — finite, timed tasks.

Runs many small I/O-bound tasks using a ThreadPoolExecutor and returns
the elapsed time.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import threading
import os

def task(n):
    # simulate light work
    return threading.current_thread().getName(), n

def run(num_tasks=200, workers=8):
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(task, i) for i in range(num_tasks)]
        for f in as_completed(futures):
            _ = f.result()
    return time.perf_counter() - start

if __name__ == '__main__':
    print('PID:', os.getpid())
    print('Thread pool time:', run())
