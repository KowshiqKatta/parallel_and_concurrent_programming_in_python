#!/usr/bin/env python3
"""
Thread pool example (see README in this folder).

Uses `concurrent.futures.ThreadPoolExecutor` to run many small tasks
concurrently. Threads are useful for I/O-bound work; for CPU-bound
tasks prefer process pools.
"""

import threading
from concurrent.futures import ThreadPoolExecutor

def vegetable_chopper(vegetable_id):
    name = threading.current_thread().getName()
    print(name, 'chopped vegetable', vegetable_id)

if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=5)
    for vegetable in range(100):
        pool.submit(vegetable_chopper, vegetable)
    pool.shutdown()
