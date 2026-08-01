#!/usr/bin/env python3
"""
Semaphore example (see README in this folder).

Uses `threading.Semaphore` to limit concurrent access to a shared
resource (charging stations). Demonstrates the simple concurrency
throttling pattern.
"""

import random
import threading
import time

charger = threading.Semaphore(1)

def cellphone():
    name = threading.current_thread().getName()
    with charger:
        print(name, 'is charging...')
        time.sleep(random.uniform(1,2))
        print(name, 'is DONE charging!')

if __name__ == '__main__':
    for phone in range(10):
        threading.Thread(target=cellphone, name='Phone-'+str(phone)).start()
