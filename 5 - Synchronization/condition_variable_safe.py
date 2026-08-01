#!/usr/bin/env python3
"""
Safe condition variable demo — finite, repeatable coordination.

Demonstrates using `threading.Condition` for turn-taking with a finite
number of servings and timing for experiments.
"""

import threading
import time
import os

def hungry_person(person_id, lock, cond, servings, results):
    while True:
        with lock:
            while (person_id != (servings['v'] % 5)) and (servings['v'] > 0):
                cond.wait()
            if servings['v'] <= 0:
                cond.notify_all()
                break
            servings['v'] -= 1
            results.append((person_id, servings['v']))
            cond.notify_all()

def run(servings=11, people=5):
    lock = threading.Lock()
    cond = threading.Condition(lock=lock)
    s = {'v': servings}
    results = []
    threads = []
    for p in range(people):
        t = threading.Thread(target=hungry_person, args=(p, lock, cond, s, results))
        t.start(); threads.append(t)
    for t in threads:
        t.join()
    return results

if __name__ == '__main__':
    print('PID:', os.getpid())
    res = run()
    print('Results length:', len(res))
