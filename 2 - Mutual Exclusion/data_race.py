#!/usr/bin/env python3
"""
Data race example (see README in this folder).

Two threads increment a shared counter without synchronization. This
can lead to incorrect results due to a race condition. The original
example uses a large number of iterations — use the safe demo files
for repeatable experiments.
"""

import threading

garlic_count = 0

def shopper():
    global garlic_count
    for i in range(10_000_000):
        garlic_count += 1

if __name__ == '__main__':
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print('We should buy', garlic_count, 'garlic.')
