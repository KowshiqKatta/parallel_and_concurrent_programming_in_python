#!/usr/bin/env python3
"""
Pure-Python read-write lock demo (no external deps).

Provides a simple `RWLock` class and a timed demo showing multiple
readers and fewer writers. This is intended as a safe alternative to
the `readerwriterlock`-based example.
"""

import threading
import time
import os

WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

class RWLock:
    def __init__(self):
        self._lock = threading.Lock()
        self._read_ready = threading.Condition(self._lock)
        self._readers = 0
        self._writer = False

    def acquire_read(self):
        with self._lock:
            while self._writer:
                self._read_ready.wait()
            self._readers += 1

    def release_read(self):
        with self._lock:
            self._readers -= 1
            if self._readers == 0:
                self._read_ready.notify_all()

    def acquire_write(self):
        with self._lock:
            while self._writer or self._readers > 0:
                self._read_ready.wait()
            self._writer = True

    def release_write(self):
        with self._lock:
            self._writer = False
            self._read_ready.notify_all()

def reader(marker: RWLock, idn: int, state: dict):
    name = f'Reader-{idn}'
    while state['today'] < len(WEEKDAYS)-1:
        marker.acquire_read()
        # simulate read
        print(name, 'sees that today is', WEEKDAYS[state['today']])
        marker.release_read()
        time.sleep(0.01)

def writer(marker: RWLock, idn: int, state: dict):
    name = f'Writer-{idn}'
    while state['today'] < len(WEEKDAYS)-1:
        marker.acquire_write()
        state['today'] = (state['today'] + 1) % 7
        print(name, 'updated date to', WEEKDAYS[state['today']])
        marker.release_write()
        time.sleep(0.02)

def run(num_readers: int = 8, num_writers: int = 2):
    marker = RWLock()
    state = {'today': 0}
    threads = []
    start = time.perf_counter()
    for i in range(num_readers):
        t = threading.Thread(target=reader, args=(marker, i, state))
        t.start()
        threads.append(t)
    for i in range(num_writers):
        t = threading.Thread(target=writer, args=(marker, i, state))
        t.start()
        threads.append(t)
    # wait for writers to finish moving through days
    for t in threads:
        t.join()
    return time.perf_counter() - start

if __name__ == '__main__':
    print('PID:', os.getpid())
    dur = run()
    print(f'Duration: {dur:.3f} s')
