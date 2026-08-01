#!/usr/bin/env python3
"""
Thread lifecycle example (see README in this folder).

Shows a `Thread` subclass, starting the thread, checking `is_alive()`,
and using `join()` to wait for completion — common patterns for
coordinating worker threads.
"""

import threading
import time

class ChefOlivia(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        print('Olivia started & waiting for sausage to thaw...')
        time.sleep(3)
        print('Olivia is done cutting sausage.')

# main thread
if __name__ == '__main__':
    print("Barron started & requesting Olivia's help.")
    olivia = ChefOlivia()
    print('  Olivia alive?:', olivia.is_alive())

    print('Barron tells Olivia to start.')
    olivia.start()
    print('  Olivia alive?:', olivia.is_alive())

    print('Barron continues cooking soup.')
    time.sleep(0.5)
    print('  Olivia alive?:', olivia.is_alive())

    print('Barron patiently waits for Olivia to finish and join...')
    olivia.join()
    print('  Olivia alive?:', olivia.is_alive())

    print('Barron and Olivia are both done!')
