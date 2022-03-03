
"""
acquire_read_lock
release_read_lock
acquire_write_lock
release_write_lock

idea:
no writer to allow reader
reader allowed when other readers
writer allowed if no readers or writers

"""
import random
import time
from threading import Condition, current_thread, Thread


class ReadersWriteLock:
    def __init__(self):
        self.cond = Condition()
        self.write_ongoing = False
        self.readers = 0

    def acquire_read_lock(self):
        self.cond.acquire()
        while self.write_ongoing:
            self.cond.wait()

        self.readers += 1

        self.cond.release()

    def release_read_lock(self):
        self.cond.acquire()

        self.readers -= 1
        if self.readers == 0:
            self.cond.notify_all()

        self.cond.release()

    def acquire_write_lock(self):
        self.cond.acquire()
        while self.write_ongoing and self.readers > 0:
            self.cond.wait()

        self.write_ongoing = True

        self.cond.release()

    def release_write_lock(self):
        self.cond.acquire()

        self.write_ongoing = False
        self.cond.notify_all()

        self.cond.release()


def writer_thread(lock):
    while True:
        lock.acquire_write_lock()
        print("\n{0} writing at {1} and current readers = {2}".format(current_thread().getName(), time.time(),
                                                                      lock.readers), flush=True)
        write_for = random.randint(1, 5)
        time.sleep(write_for)
        print("\n{0} releasing at {1} and current readers = {2}".format(current_thread().getName(), time.time(),
                                                                        lock.readers),
              flush=True)
        lock.release_write_lock()
        time.sleep(1)


def reader_thread(lock):
    while 1:
        lock.acquire_read_lock()
        print("\n{0} reading at {1} and write in progress = {2}".format(current_thread().getName(), time.time(),
                                                                        lock.write_ongoing), flush=True)
        read_for = random.randint(1, 2)
        time.sleep(read_for)
        print("\n{0} releasing at {1} and write in progress = {2}".format(current_thread().getName(), time.time(),
                                                                          lock.write_ongoing), flush=True)
        lock.release_read_lock()
        time.sleep(1)


if __name__ == "__main__":
    lock = ReadersWriteLock()
    t1 = Thread(target=writer_thread, args=(lock, ), name='w1', daemon=True)
    t2 = Thread(target=writer_thread, args=(lock, ), name='w2', daemon=True)
    t1.start()

    readers = list()
    for i in range(0, 3):
        readers.append(Thread(target=reader_thread, args=(lock,), name="reader-{0}".format(i + 1), daemon=True))

    for reader in readers:
        reader.start()

    t2.start()

    time.sleep(15)