#!/usr/bin/env python3
"""
Safe demo for image downloading challenge.

This script simulates downloading images (no network required). It
creates small binary files and returns total bytes downloaded. Both
sequential and threaded versions are provided for timing comparisons.
"""

import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def _fake_download(image_number, out_dir='tmp_images'):
    os.makedirs(out_dir, exist_ok=True)
    # simulate variable network delay
    time.sleep(0.01 + (image_number % 5) * 0.005)
    data = bytes((image_number % 256,) * 1024)  # 1 KB of predictable bytes
    path = os.path.join(out_dir, f'image_{image_number:03d}.bin')
    with open(path, 'wb') as f:
        f.write(data)
    return len(data)

def seq_download_images(image_numbers):
    total = 0
    for n in image_numbers:
        total += _fake_download(n)
    return total

def par_download_images(image_numbers, workers=8):
    total = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(_fake_download, n) for n in image_numbers]
        for f in as_completed(futures):
            total += f.result()
    return total

def run(num_images=40, workers=8):
    image_numbers = list(range(1, num_images+1))
    # warm-up
    seq_download_images(image_numbers[:5])
    par_download_images(image_numbers[:5], workers=workers)

    start = time.perf_counter()
    seq_total = seq_download_images(image_numbers)
    seq_time = time.perf_counter() - start

    start = time.perf_counter()
    par_total = par_download_images(image_numbers, workers=workers)
    par_time = time.perf_counter() - start

    assert seq_total == par_total
    return {'seq_time': seq_time, 'par_time': par_time, 'total_bytes': seq_total}

if __name__ == '__main__':
    res = run()
    print('Sequential time: {:.3f}s'.format(res['seq_time']))
    print('Parallel time:   {:.3f}s'.format(res['par_time']))
    print('Total bytes:', res['total_bytes'])
