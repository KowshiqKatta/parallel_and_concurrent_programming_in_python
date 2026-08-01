#!/usr/bin/env python3
"""
Starvation example (see README in this folder).

Shows how some threads may be perpetually denied access to resources
when contention and scheduling bias exist. This example launches many
threads competing for the same locks and reports per-thread counts.
"""

import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 5000

def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    sushi_eaten = 0
    while sushi_count > 0: # eat sushi until it's all gone
        with first_chopstick:
            with second_chopstick:
                if sushi_count > 0:
                    sushi_count -= 1
                    sushi_eaten += 1
                    print(name, 'took a piece! Sushi remaining:', sushi_count)
    print(name, 'took', sushi_eaten, 'pieces')

if __name__ == '__main__':
    for thread in range(50):
        threading.Thread(target=philosopher, args=('Barron', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=('Olivia', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=('Steve', chopstick_a, chopstick_b)).start()
