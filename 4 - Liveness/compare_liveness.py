#!/usr/bin/env python3
"""
Run liveness safe demos and summarize results.

Executes deadlock detection, abandoned-lock safe run, livelock resolution,
and starvation distribution demo, printing concise results for each.
"""

from deadlock_safe import run_deadlock, run_fixed
from abandoned_lock_safe import run as run_abandoned
from livelock_safe import run_resolve
from starvation_safe import run as run_starvation

def main():
    print('Checking deadlock scenario...')
    dead = run_deadlock()
    print('  Deadlock detected:', dead)
    print('  Running fixed ordering version...')
    run_fixed()
    print('  Fixed run finished.')

    print('\nTesting abandoned-lock safe variant...')
    v = run_abandoned()
    print('  Counter after safe run:', v)

    print('\nTesting livelock resolution...')
    rem = run_resolve()
    print('  Remaining after livelock-safe run:', rem)

    print('\nTesting starvation distribution...')
    rem2 = run_starvation()
    print('  Remaining after starvation-safe run:', rem2)

if __name__ == '__main__':
    main()
