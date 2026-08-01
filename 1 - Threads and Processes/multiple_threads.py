#!/usr/bin/env python3
"""
Multiple threads example (see README in this folder).

Starts several threads that run busy loops. In CPython this will not
achieve true multi-core parallelism for CPU-bound work because of the
GIL — compare with the `multiple_processes.py` example.
"""

import os
import threading

# a simple function that wastes CPU cycles forever
def cpu_waster():
    while True:
        pass

# display information about this process
print('\n  Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)

print('\nStarting 12 CPU Wasters...')
for i in range(12):
    threading.Thread(target=cpu_waster).start()

# display information about this process
print('\n  Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)
