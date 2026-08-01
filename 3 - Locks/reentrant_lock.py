#!/usr/bin/env python3
"""
Reentrant lock example (see README in this folder).

Demonstrates `threading.RLock()` (re-entrant lock) where a thread
that already holds the lock can acquire it again. This is useful when
one locked function calls another that also acquires the same lock.
"""

import threading

garlic_count = 0
potato_count = 0
pencil = threading.RLock()

def add_garlic():
    global garlic_count
    pencil.acquire()
    garlic_count += 1
    pencil.release()

def add_potato():
    global potato_count
    pencil.acquire()
    potato_count += 1
    add_garlic()
    pencil.release()

def shopper():
    for i in range(10_000):
        add_garlic()
        add_potato()

if __name__ == '__main__':
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print('We should buy', garlic_count, 'garlic.')
    print('We should buy', potato_count, 'potatoes.')
