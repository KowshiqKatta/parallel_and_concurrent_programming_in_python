#!/usr/bin/env python3
"""
Safe livelock demo using polite backoff and resolution.

Demonstrates threads that keep yielding to each other (livelock) and
shows how introducing randomized backoff resolves the issue.
"""

import threading
import time
from random import random
import os

def polite_worker(name, first, second, counter, iterations):
    for _ in range(iterations):
        first.acquire()
        if not second.acquire(blocking=False):
            # give up and back off
            first.release()
            time.sleep(random()/100)
            continue
        try:
            if counter['v'] > 0:
                counter['v'] -= 1
        finally:
            second.release(); first.release()

def run_resolve(iterations=200):
    a = threading.Lock(); b = threading.Lock(); c = threading.Lock()
    counter = {'v': 300}
    t1 = threading.Thread(target=polite_worker, args=('A', a, b, counter, iterations))
    t2 = threading.Thread(target=polite_worker, args=('B', b, c, counter, iterations))
    t3 = threading.Thread(target=polite_worker, args=('C', c, a, counter, iterations))
    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()
    return counter['v']

if __name__ == '__main__':
    print('PID:', os.getpid())
    remaining = run_resolve()
    print('Remaining after polite/backoff workers:', remaining)
