#!/usr/bin/env python3
"""
Safe producer-consumer demos (threads + processes) with finite work.

Provides `run_threads()` and `run_processes()` functions for
repeatable experiments and timing comparisons.
"""

import time
import queue
import threading
import multiprocessing as mp
import os

def run_threads(num_items=20, buffer=5):
    q = queue.Queue(maxsize=buffer)
    def producer():
        for i in range(num_items):
            q.put(f'Bowl #{i}')
            time.sleep(0.02)
        # send sentinel for two consumers
        q.put('done'); q.put('done')

    def consumer():
        while True:
            item = q.get()
            if item == 'done':
                break
            time.sleep(0.03)

    threads = []
    start = time.perf_counter()
    for _ in range(2):
        t = threading.Thread(target=consumer); t.start(); threads.append(t)
    p = threading.Thread(target=producer); p.start(); p.join()
    for t in threads: t.join()
    return time.perf_counter() - start

def _proc_producer(q, num_items):
    import time
    for i in range(num_items):
        q.put(f'Bowl #{i}')
        time.sleep(0.02)
    q.put('done'); q.put('done')

def _proc_consumer(q):
    import time
    while True:
        item = q.get()
        if item == 'done': break
        time.sleep(0.03)

def run_processes(num_items=20, buffer=5):
    q = mp.Queue(buffer)
    start = time.perf_counter()
    consumers = [mp.Process(target=_proc_consumer, args=(q,)) for _ in range(2)]
    for c in consumers: c.start()
    p = mp.Process(target=_proc_producer, args=(q, num_items)); p.start(); p.join()
    for c in consumers: c.join()
    return time.perf_counter() - start

if __name__ == '__main__':
    print('PID:', os.getpid())
    t = run_threads(); print('Threads time:', t)
    p = run_processes(); print('Processes time:', p)
