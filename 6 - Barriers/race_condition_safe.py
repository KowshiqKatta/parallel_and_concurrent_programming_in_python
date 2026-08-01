#!/usr/bin/env python3
"""
Safe race-condition demo — finite, repeatable updates.

Provides `run_no_barrier()` which performs the same operations as the
original example but returns the final value for verification and
timing.
"""

import threading
import time

def cpu_work(work_units):
    x = 0
    for work in range(work_units*100_000):
        x += 1

def run_no_barrier(pairs=5):
    bags = {'value': 1}
    lock = threading.Lock()

    def barron():
        cpu_work(1)
        with lock:
            bags['value'] *= 2

    def olivia():
        cpu_work(1)
        with lock:
            bags['value'] += 3

    threads = []
    start = time.perf_counter()
    for _ in range(pairs):
        threads.append(threading.Thread(target=barron))
        threads.append(threading.Thread(target=olivia))
    for t in threads: t.start()
    for t in threads: t.join()
    return bags['value'], time.perf_counter()-start

if __name__ == '__main__':
    val, dur = run_no_barrier()
    print('Final value (no barrier):', val, 'time:', dur)
