#!/usr/bin/env python3
"""
Compare asynchronous strategies: thread pool, process pool, futures, and parallel sum.

Runs the safe demos and prints timings to help learners compare trade-offs.
"""

from thread_pool_safe import run as run_threads
from process_pool_safe import run as run_processes
from future_safe import run as run_future
from divide_and_conquer_safe import parallel_sum

def main():
    print('Running ThreadPool demo...')
    t = run_threads()
    print(f'  ThreadPool time: {t:.3f}s')

    print('Running ProcessPool demo...')
    p = run_processes()
    print(f'  ProcessPool time: {p:.3f}s')

    print('Running Future demo...')
    f = run_future()
    print(f'  Future result: {f}')

    print('Running Parallel Sum demo...')
    total, dur = parallel_sum(1, 1_000_000)
    print(f'  Parallel sum time: {dur:.3f}s, total: {total}')

if __name__ == '__main__':
    main()
