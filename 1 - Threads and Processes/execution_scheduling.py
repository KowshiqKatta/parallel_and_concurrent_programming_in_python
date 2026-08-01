#!/usr/bin/env python3
"""
Execution scheduling example (see README in this folder).

Two threads perform repeated work controlled by a shared flag. This
example illustrates scheduler-driven interleaving and how the GIL
affects thread execution for CPU-bound loops.
"""

import threading
import time

chopping = True

def vegetable_chopper():
    name = threading.current_thread().getName()
    vegetable_count = 0
    while chopping:
        print(name, 'chopped a vegetable!')
        vegetable_count += 1
    print(name, 'chopped', vegetable_count, 'vegetables.')

if __name__ == '__main__':
    threading.Thread(target=vegetable_chopper, name='Barron').start()
    threading.Thread(target=vegetable_chopper, name='Olivia').start()

    time.sleep(1)    # chop vegetables for 1 second
    chopping = False # stop both threads from chopping
