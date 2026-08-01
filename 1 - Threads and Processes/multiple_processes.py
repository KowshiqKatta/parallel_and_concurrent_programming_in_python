#!/usr/bin/env python3
"""
Multiple processes example (see README in this folder).

This script starts multiple OS processes that run a busy loop. It's
intended to demonstrate how `multiprocessing` can utilize multiple
CPU cores (unlike CPU-bound threads under the GIL). Use with care —
these processes will consume CPU until killed.
"""

import os
import threading
import multiprocessing as mp

# a simple function that wastes CPU cycles forever
def cpu_waster():
    while True:
        pass

print('Hi! My name is', __name__)
if __name__ == '__main__':
    # display information about this process
    print('\n  Process ID: ', os.getpid())
    print('Thread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)

    print('\nStarting 12 CPU Wasters...')
    for i in range(12):
        mp.Process(target=cpu_waster).start()

    # display information about this process
    print('\n  Process ID: ', os.getpid())
    print('Thread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)
