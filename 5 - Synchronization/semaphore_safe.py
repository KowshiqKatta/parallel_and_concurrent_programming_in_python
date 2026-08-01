#!/usr/bin/env python3
"""
Safe semaphore demo with finite workers and resource limit.

Shows using `threading.Semaphore` to limit concurrent access and
measures overall elapsed time.
"""

import threading
import time
import random
import os

def worker(sem, work_time=0.1):
    with sem:
        time.sleep(random.uniform(work_time, work_time*2))

def run(num_workers=10, slots=3):
    sem = threading.Semaphore(slots)
    threads = []
    start = time.perf_counter()
    for i in range(num_workers):
        t = threading.Thread(target=worker, args=(sem, 0.05))
        t.start(); threads.append(t)
    for t in threads: t.join()
    return time.perf_counter() - start

if __name__ == '__main__':
    print('PID:', os.getpid())
    d = run(); print('Duration:', d)
