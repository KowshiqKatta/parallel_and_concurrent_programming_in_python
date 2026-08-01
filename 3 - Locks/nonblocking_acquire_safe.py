#!/usr/bin/env python3
"""
Safe non-blocking acquire demo — finite run and timing.

Demonstrates `Lock.acquire(blocking=False)` in a repeatable experiment.
"""

import threading
import time
import os

def worker(shared, lock, target):
    name = threading.current_thread().getName()
    items_to_add = 0
    while shared['count'] < target:
        if items_to_add and lock.acquire(blocking=False):
            shared['count'] += items_to_add
            items_to_add = 0
            time.sleep(0.01)
            lock.release()
        else:
            time.sleep(0.005)
            items_to_add += 1

def run(num_workers: int = 2, target: int = 50):
    shared = {'count': 0}
    lock = threading.Lock()
    threads = []
    start = time.perf_counter()
    for i in range(num_workers):
        t = threading.Thread(target=worker, args=(shared, lock, target), name=f'Worker-{i}')
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return shared['count'], time.perf_counter() - start

if __name__ == '__main__':
    print('PID:', os.getpid())
    count, dur = run()
    print('Final count:', count)
    print(f'Duration: {dur:.3f} s')
