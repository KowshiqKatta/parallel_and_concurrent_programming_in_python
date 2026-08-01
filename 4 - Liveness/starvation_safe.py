#!/usr/bin/env python3
"""
Safe starvation demo — show unfairness under contention.

Runs multiple threads competing for the same locks and reports per
thread counts so you can observe distribution of work.
"""

import threading
import time
import os

def philosopher(name, lock, counter, iterations):
    eaten = 0
    for _ in range(iterations):
        with lock:
            if counter['v'] > 0:
                counter['v'] -= 1
                eaten += 1
    print(name, 'took', eaten, 'pieces')

def run(num_threads=30, iterations=200):
    lock = threading.Lock()
    counter = {'v': num_threads * iterations}
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=philosopher, args=(f'T{i}', lock, counter, iterations))
        t.start(); threads.append(t)
    for t in threads:
        t.join()
    return counter['v']

if __name__ == '__main__':
    print('PID:', os.getpid())
    remaining = run()
    print('Remaining:', remaining)
