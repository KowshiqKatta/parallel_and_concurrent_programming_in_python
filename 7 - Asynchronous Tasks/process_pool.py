#!/usr/bin/env python3
"""
Process pool example (see README in this folder).

Uses `concurrent.futures.ProcessPoolExecutor` to run tasks in separate
processes. Process pools are suitable for CPU-bound tasks and can
utilize multiple cores.
"""

import os
from concurrent.futures import ProcessPoolExecutor

def vegetable_chopper(vegetable_id):
    pid = os.getpid()
    print(pid, 'chopped a vegetable', vegetable_id)

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=5) as pool:
        for vegetable in range(100):
            pool.submit(vegetable_chopper, vegetable)
