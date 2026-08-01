#!/usr/bin/env python3
"""
Compare threaded vs process workers using the safe runners.

Runs `multiple_threads_safe.run()` and `multiple_processes_safe.run()`
sequentially and reports elapsed time for each. Use this to observe
the difference in wall-clock time for CPU-bound work under threads
and processes on your machine.
"""

from multiple_threads_safe import run as run_threads
from multiple_processes_safe import run as run_processes

def main():
    num_workers = 12
    iterations = 200_000

    print(f'Running {num_workers} threads (each {iterations} iterations)')
    t_time = run_threads(num_workers=num_workers, iterations=iterations)
    print(f'Threads elapsed: {t_time:.3f} s')

    print(f'Running {num_workers} processes (each {iterations} iterations)')
    p_time = run_processes(num_workers=num_workers, iterations=iterations)
    print(f'Processes elapsed: {p_time:.3f} s')

    print('\nNote: Results depend on CPU cores, OS scheduling, and Python build.')

if __name__ == '__main__':
    main()
