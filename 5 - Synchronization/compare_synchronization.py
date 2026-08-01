#!/usr/bin/env python3
"""
Run safe synchronization demos and summarize timings.

Executes condition variable, producer-consumer (threads/processes),
and semaphore safe demos and prints concise timings/results.
"""

from condition_variable_safe import run as run_condition
from producer_consumer_safe import run_threads, run_processes
from semaphore_safe import run as run_semaphore

def main():
    print('Running condition variable safe demo...')
    res = run_condition()
    print('  Served entries:', len(res))

    print('Running producer-consumer (threads)...')
    t_time = run_threads()
    print(f'  Threads time: {t_time:.3f}s')

    print('Running producer-consumer (processes)...')
    p_time = run_processes()
    print(f'  Processes time: {p_time:.3f}s')

    print('Running semaphore demo...')
    s_time = run_semaphore()
    print(f'  Semaphore time: {s_time:.3f}s')

if __name__ == '__main__':
    main()
