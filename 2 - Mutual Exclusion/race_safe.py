#!/usr/bin/env python3
"""
Safe race demonstration — compare unlocked vs locked increments.

Provides `run_unlocked()` and `run_locked()` functions that perform a
finite number of increments across multiple threads. Use these for
repeatable experiments instead of the infinite or very large loops in
the original examples.
"""

import threading
import time
from typing import Tuple

def _worker_unlocked(counter: dict, iterations: int):
    for _ in range(iterations):
        counter['value'] += 1

def _worker_locked(counter: dict, lock: threading.Lock, iterations: int):
    for _ in range(iterations):
        with lock:
            counter['value'] += 1

def run_unlocked(num_threads: int = 2, iterations: int = 200_000) -> Tuple[int, float]:
    counter = {'value': 0}
    threads = []
    start = time.perf_counter()
    for _ in range(num_threads):
        t = threading.Thread(target=_worker_unlocked, args=(counter, iterations))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return counter['value'], time.perf_counter() - start

def run_locked(num_threads: int = 2, iterations: int = 200_000) -> Tuple[int, float]:
    counter = {'value': 0}
    lock = threading.Lock()
    threads = []
    start = time.perf_counter()
    for _ in range(num_threads):
        t = threading.Thread(target=_worker_locked, args=(counter, lock, iterations))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return counter['value'], time.perf_counter() - start

if __name__ == '__main__':
    print('Unlocked run (race expected)')
    val, dur = run_unlocked()
    print(f'  Result = {val}, time = {dur:.3f}s')

    print('Locked run (no race)')
    val, dur = run_locked()
    print(f'  Result = {val}, time = {dur:.3f}s')
