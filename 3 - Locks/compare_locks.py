#!/usr/bin/env python3
"""
Compare lock behaviors using the safe demos in this folder.

Runs the RLock, non-blocking acquire, and read-write safe demos and
prints summarized timings. Use this to quickly observe relative
behaviors on your machine.
"""

from reentrant_lock_safe import run as run_rlock
from nonblocking_acquire_safe import run as run_nonblocking
from readwrite_lock_safe import run as run_rw

def main():
    print('Running RLock demo...')
    counters, t_r = run_rlock()
    print('  RLock counters:', counters)
    print(f'  Time: {t_r:.3f}s')

    print('Running non-blocking acquire demo...')
    count_nb, t_nb = run_nonblocking()
    print('  Final count:', count_nb)
    print(f'  Time: {t_nb:.3f}s')

    print('Running read-write lock demo...')
    t_rw = run_rw()
    print(f'  Time: {t_rw:.3f}s')

if __name__ == '__main__':
    main()
