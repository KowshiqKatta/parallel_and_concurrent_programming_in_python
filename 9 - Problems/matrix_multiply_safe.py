#!/usr/bin/env python3
"""
Safe demo for matrix multiplication challenge.

Provides a sequential multiply and a process-parallel row-worker version
that computes blocks of rows in separate processes and assembles the
final result. Defaults are chosen to complete quickly.
"""

import time
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
import random

def chunk_multiply_rows(A, B, row_start, row_end):
    num_cols_B = len(B[0])
    num_cols_A = len(A[0])
    rows = []
    for i in range(row_start, row_end):
        row = [0]*num_cols_B
        for j in range(num_cols_B):
            s = 0
            for k in range(num_cols_A):
                s += A[i][k] * B[k][j]
            row[j] = s
        rows.append((i, row))
    return rows

def seq_matrix_multiply(A, B):
    num_rows_A = len(A)
    num_cols_B = len(B[0])
    C = [[0]*num_cols_B for _ in range(num_rows_A)]
    for i in range(num_rows_A):
        for j in range(num_cols_B):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]
    return C

def par_matrix_multiply(A, B, workers=None):
    if workers is None:
        workers = max(1, os.cpu_count() - 1)
    num_rows_A = len(A)
    chunk = max(1, num_rows_A // workers)
    tasks = []
    ranges = []
    for s in range(0, num_rows_A, chunk):
        e = min(s+chunk, num_rows_A)
        ranges.append((s,e))
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(chunk_multiply_rows, A, B, s, e) for s,e in ranges]
        result_rows = []
        for f in as_completed(futures):
            result_rows.extend(f.result())
    # assemble
    C = [None]*num_rows_A
    for i,row in result_rows:
        C[i] = row
    return C

def run(n=120, workers=None):
    A = [[random.random() for _ in range(n)] for __ in range(n)]
    B = [[random.random() for _ in range(n)] for __ in range(n)]

    start = time.perf_counter()
    C_seq = seq_matrix_multiply(A, B)
    seq_time = time.perf_counter() - start

    start = time.perf_counter()
    C_par = par_matrix_multiply(A, B, workers=workers)
    par_time = time.perf_counter() - start

    return {'seq_time': seq_time, 'par_time': par_time, 'equal': C_seq == C_par}

if __name__ == '__main__':
    res = run()
    print('Sequential time: {:.3f}s'.format(res['seq_time']))
    print('Parallel time:   {:.3f}s'.format(res['par_time']))
    print('Results equal:', res['equal'])
