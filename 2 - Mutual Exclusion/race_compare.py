#!/usr/bin/env python3
"""
Compare unlocked vs locked threaded increments using `race_safe`.

Run this script to see how a race condition affects the final counter
value and to measure the overhead of acquiring a lock.
"""

from race_safe import run_unlocked, run_locked

def main():
    threads = 2
    iterations = 200_000

    print(f'Running unlocked (race) with {threads} threads x {iterations} iterations')
    val_u, time_u = run_unlocked(num_threads=threads, iterations=iterations)
    print(f'  Unlocked result = {val_u}, time = {time_u:.3f}s')

    print(f'Running locked (mutual exclusion) with {threads} threads x {iterations} iterations')
    val_l, time_l = run_locked(num_threads=threads, iterations=iterations)
    print(f'  Locked result = {val_l}, time = {time_l:.3f}s')

    print('\nNote: On CPython the GIL may mask some race symptoms for simpleoperations, so results can vary across builds and platforms.')

if __name__ == '__main__':
    main()
