#!/usr/bin/env python3
"""
Read-write lock example (see README in this folder).

This example uses the third-party `readerwriterlock` package to
demonstrate a reader-writer lock where many readers can access the
resource concurrently while writers obtain exclusive access.

Note: `readerwriterlock` is not part of the standard library. See the
README for instructions to install the dependency or use the safe
pure-Python demo provided in this folder.
"""

import threading
try:
    from readerwriterlock import rwlock
except Exception:
    rwlock = None

WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today = 0

if rwlock is not None:
    marker = rwlock.RWLockFair()

    def calendar_reader(id_number):
        global today
        read_marker = marker.gen_rlock()
        name = 'Reader-' + str(id_number)
        while today < len(WEEKDAYS)-1:
            read_marker.acquire()
            print(name, 'sees that today is', WEEKDAYS[today], '-read count:', read_marker.c_rw_lock.v_read_count)
            read_marker.release()

    def calendar_writer(id_number):
        global today
        write_marker = marker.gen_wlock()
        name = 'Writer-' + str(id_number)
        while today < len(WEEKDAYS)-1:
            write_marker.acquire()
            today = (today + 1) % 7
            print(name, 'updated date to ', WEEKDAYS[today])
            write_marker.release()

    if __name__ == '__main__':
        # create ten reader threads
        for i in range(10):
            threading.Thread(target=calendar_reader, args=(i,)).start()
        # ...but only two writer threads
        for i in range(2):
            threading.Thread(target=calendar_writer, args=(i,)).start()
else:
    if __name__ == '__main__':
        print('readerwriterlock package not found. See README.md for a pure-Python alternative in this folder.')
