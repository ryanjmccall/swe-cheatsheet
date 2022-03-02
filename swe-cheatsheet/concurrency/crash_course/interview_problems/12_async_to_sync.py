# asked by netflix
from threading import Thread, Semaphore, Condition
import time


class AsyncExecutor:
    def work(self, callback):
        time.sleep(1)  # simulate work
        callback()

    def execute_async(self, callback):
        Thread(target=self.work, args=(callback,)).start()


class SyncExecutor(AsyncExecutor):
    def __init__(self):
        super().__init__()
        self.sem = Semaphore(0)

    def work(self, callback):
        super().work(callback)
        self.sem.release()

    def execute(self, callback):
        super().execute_async(callback)
        self.sem.acquire()


class SyncExecutor2(AsyncExecutor):
    def __init__(self):
        super().__init__()
        self.cv = Condition()
        self.complete = False

    def work(self, cb):
        super().work(cb)
        self.cv.acquire()
        self.cv.notify_all()
        self.complete = True
        self.cv.release()

    def execute(self, cb):
        super().execute_async(cb)
        self.cv.acquire()
        while not self.complete:
            self.cv.wait()
        self.cv.release()


def some_func():
    print('func executes')


def main():
    # ex = SyncExecutor()
    ex = SyncExecutor2()
    ex.execute(some_func)
    print('main exit')


main()
