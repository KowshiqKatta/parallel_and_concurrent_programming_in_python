#!/usr/bin/env python3
"""
Safe parallel merge-sort demo using chunked sorting and k-way merge.

This avoids deep multiprocessing recursion by sorting independent chunks
in worker processes and merging results with `heapq.merge`.
"""

import random
import time
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
import heapq

def sort_chunk(chunk):
    return sorted(chunk)

def parallel_sort(array, workers=None, chunk_size=50_000):
    if workers is None:
        workers = max(1, os.cpu_count() - 1)
    chunks = [array[i:i+chunk_size] for i in range(0, len(array), chunk_size)]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(sort_chunk, c) for c in chunks]
        sorted_chunks = [f.result() for f in as_completed(futures)]
    # Merge all sorted chunks into one sorted list
    return list(heapq.merge(*sorted_chunks))

def run(n=200_000, workers=None):
    array = [random.randint(0, 10_000) for _ in range(n)]

    start = time.perf_counter()
    seq_sorted = sorted(array)
    seq_time = time.perf_counter() - start

    start = time.perf_counter()
    par_sorted = parallel_sort(array, workers=workers, chunk_size=50_000)
    par_time = time.perf_counter() - start

    return {'seq_time': seq_time, 'par_time': par_time, 'equal': seq_sorted == par_sorted}

if __name__ == '__main__':
    res = run()
    print('Sequential time: {:.3f}s'.format(res['seq_time']))
    print('Parallel time:   {:.3f}s'.format(res['par_time']))
    print('Results equal:', res['equal'])
