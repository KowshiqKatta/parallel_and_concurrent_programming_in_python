#!/usr/bin/env python3
"""
Run safe problem demos and print comparative timings.
"""

from download_images_safe import run as run_downloads
from matrix_multiply_safe import run as run_matmul
from merge_sort_safe import run as run_mergesort

def main():
    print('Running download images demo...')
    d = run_downloads()
    print('  seq: {:.3f}s  par: {:.3f}s  bytes: {}'.format(d['seq_time'], d['par_time'], d['total_bytes']))

    print('\nRunning matrix multiply demo...')
    m = run_matmul()
    print('  seq: {:.3f}s  par: {:.3f}s  equal: {}'.format(m['seq_time'], m['par_time'], m['equal']))

    print('\nRunning merge sort demo...')
    s = run_mergesort()
    print('  seq: {:.3f}s  par: {:.3f}s  equal: {}'.format(s['seq_time'], s['par_time'], s['equal']))

if __name__ == '__main__':
    main()
