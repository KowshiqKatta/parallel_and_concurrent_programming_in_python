#!/usr/bin/env python3
"""
Compare barrier vs no-barrier behavior using safe demos.

Runs both `race_condition_safe.run_no_barrier()` and
`barrier_safe.run_with_barrier()` and prints the final values and
timings for easy comparison.
"""

from race_condition_safe import run_no_barrier
from barrier_safe import run_with_barrier

def main():
    print('Running no-barrier run...')
    val1, t1 = run_no_barrier()
    print(f'  No-barrier final value: {val1} (time {t1:.3f}s)')

    print('Running barrier run...')
    val2, t2 = run_with_barrier()
    print(f'  Barrier final value: {val2} (time {t2:.3f}s)')

    print('\nNote: Both runs use a lock for atomic updates; the barrier enforces ordering around the rendezvous point.')

if __name__ == '__main__':
    main()
