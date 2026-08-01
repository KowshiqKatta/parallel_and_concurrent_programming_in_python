#!/usr/bin/env python3
"""
Demonstrate abandoned lock issues and safe patterns.

Shows an unsafe function that raises an exception while holding a lock
and a safe variant that uses `try/finally` or `with` to ensure release.
"""

import threading
import time
import os

def unsafe_worker(lock, counter):
    lock.acquire()
    # simulate work
    counter['v'] += 1
    if counter['v'] == 5:
        raise RuntimeError('simulated error')
    lock.release()

def safe_worker(lock, counter):
    try:
        lock.acquire()
        counter['v'] += 1
        if counter['v'] == 5:
            raise RuntimeError('simulated error')
    finally:
        if lock.locked():
            lock.release()

def run():
    lock = threading.Lock()
    counter = {'v': 0}
    threads = []
    for _ in range(6):
        t = threading.Thread(target=safe_worker, args=(lock, counter))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return counter['v']

if __name__ == '__main__':
    print('PID:', os.getpid())
    v = run()
    print('Final counter (safe):', v)
