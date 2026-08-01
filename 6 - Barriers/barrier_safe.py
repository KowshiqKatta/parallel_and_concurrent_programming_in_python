#!/usr/bin/env python3
"""
Safe barrier demo — finite participants and timing.

Provides `run_with_barrier()` which uses a `threading.Barrier` to
coordinate threads so that certain actions happen only after all have
reached the rendezvous point.
"""

import threading
import time

def cpu_work(work_units):
    x = 0
    for work in range(work_units*100_000):
        x += 1

def run_with_barrier(pairs=5):
    bags = {'value': 1}
    lock = threading.Lock()
    participants = pairs * 2
    barrier = threading.Barrier(participants)

    def barron():
        cpu_work(1)
        barrier.wait()
        with lock:
            bags['value'] *= 2

    def olivia():
        cpu_work(1)
        with lock:
            bags['value'] += 3
        barrier.wait()

    threads = []
    start = time.perf_counter()
    for _ in range(pairs):
        threads.append(threading.Thread(target=barron))
        threads.append(threading.Thread(target=olivia))
    for t in threads: t.start()
    for t in threads: t.join()
    return bags['value'], time.perf_counter()-start

if __name__ == '__main__':
    val, dur = run_with_barrier()
    print('Final value (barrier):', val, 'time:', dur)
