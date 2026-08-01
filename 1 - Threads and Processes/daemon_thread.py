#!/usr/bin/env python3
"""
Daemon thread example (see README in this folder).

Demonstrates a background (daemon) thread that runs while the
main thread executes; the daemon thread is terminated automatically
when the main program exits.
"""

import threading
import time

def kitchen_cleaner():
    while True:
        print('Olivia cleaned the kitchen.')
        time.sleep(1)

if __name__ == '__main__':
    olivia = threading.Thread(target=kitchen_cleaner)
    olivia.daemon = True
    olivia.start()

    print('Barron is cooking...')
    time.sleep(0.6)
    print('Barron is cooking...')
    time.sleep(0.6)
    print('Barron is cooking...')
    time.sleep(0.6)
    print('Barron is done!')
