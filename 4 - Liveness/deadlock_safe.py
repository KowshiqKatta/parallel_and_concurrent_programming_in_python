#!/usr/bin/env python3
"""
Safe deadlock demo and a fixed version.

`run_deadlock()` attempts to produce a deadlock with a small finite
number of operations. `run_fixed()` demonstrates a simple ordering
strategy to avoid deadlock by acquiring locks in a consistent order.
"""

import threading
import time
import os

def _philosopher_dead(name, first, second, counter, iterations):
    for _ in range(iterations):
        first.acquire()
        time.sleep(0.001)
        second.acquire()
        try:
            if counter['value'] > 0:
                counter['value'] -= 1
        finally:
            second.release()
            first.release()

def run_deadlock(iterations=100):
    a = threading.Lock()
    b = threading.Lock()
    c = threading.Lock()
    counter = {'value': 300}
    t1 = threading.Thread(target=_philosopher_dead, args=('A', a, b, counter, iterations))
    t2 = threading.Thread(target=_philosopher_dead, args=('B', b, c, counter, iterations))
    t3 = threading.Thread(target=_philosopher_dead, args=('C', c, a, counter, iterations))
    t1.start(); t2.start(); t3.start()
    # join with timeout to detect deadlock
    t1.join(2); t2.join(2); t3.join(2)
    deadlocked = any(t.is_alive() for t in (t1, t2, t3))
    return deadlocked

def _philosopher_fixed(name, locks, counter, iterations):
    # acquire in order of lock id to avoid circular wait
    for _ in range(iterations):
        first, second = sorted(locks, key=lambda x: id(x))
        first.acquire()
        second.acquire()
        try:
            if counter['value'] > 0:
                counter['value'] -= 1
        finally:
            second.release()
            first.release()

def run_fixed(iterations=100):
    a = threading.Lock()
    b = threading.Lock()
    c = threading.Lock()
    counter = {'value': 300}
    t1 = threading.Thread(target=_philosopher_fixed, args=('A', (a,b), counter, iterations))
    t2 = threading.Thread(target=_philosopher_fixed, args=('B', (b,c), counter, iterations))
    t3 = threading.Thread(target=_philosopher_fixed, args=('C', (c,a), counter, iterations))
    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()
    return False

if __name__ == '__main__':
    print('PID:', os.getpid())
    dl = run_deadlock()
    print('Deadlock detected (threads still alive):', dl)
    print('Running fixed ordering version...')
    fixed = run_fixed()
    print('Fixed run completed, deadlock:', fixed)
