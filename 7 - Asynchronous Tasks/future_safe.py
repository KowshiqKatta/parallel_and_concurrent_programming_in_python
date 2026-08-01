#!/usr/bin/env python3
"""
Safe future demo — show non-blocking result handling and timeout.
"""

from concurrent.futures import ThreadPoolExecutor, TimeoutError
import time
import os

def long_task():
    time.sleep(1)
    return 'ready'

def run():
    with ThreadPoolExecutor() as ex:
        fut = ex.submit(long_task)
        try:
            result = fut.result(timeout=2)
        except TimeoutError:
            result = 'timeout'
    return result

if __name__ == '__main__':
    print('PID:', os.getpid())
    print('Future result:', run())
