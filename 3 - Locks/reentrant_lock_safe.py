#!/usr/bin/env python3
"""
Safe RLock demo — finite re-entrant locking and timing.

Demonstrates `threading.RLock()` in a finite, repeatable experiment.
"""

import threading
import time
import os

def _make_counters():
    return {'garlic': 0, 'potato': 0}

def add_garlic(counters, lock):
    with lock:
        counters['garlic'] += 1

def add_potato(counters, lock):
    with lock:
        counters['potato'] += 1
        # re-entering the same lock via nested call
        add_garlic(counters, lock)

def worker(counters, lock, iterations):
    for _ in range(iterations):
        add_garlic(counters, lock)
        add_potato(counters, lock)

def run(num_workers: int = 2, iterations: int = 5000):
    counters = _make_counters()
    lock = threading.RLock()
    threads = []
    start = time.perf_counter()
    for _ in range(num_workers):
        t = threading.Thread(target=worker, args=(counters, lock, iterations))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return counters, time.perf_counter() - start

if __name__ == '__main__':
    print('PID:', os.getpid())
    counters, dur = run()
    print('Counters:', counters)
    print(f'Duration: {dur:.3f} s')
