import time
from threading import Thread, Semaphore, Condition
from typing import Callable


class AsyncExecutor:
    def __init__(self):
        pass

    def do_work(self, cb: Callable):
        time.sleep(1)  # simulated work
        cb()

    def exec_async(self, cb: Callable):
        Thread(target=self.do_work, args=(cb,)).start()


class SyncSemExecutor(AsyncExecutor):
    def __init__(self):
        super().__init__()
        self.sem = Semaphore(0)

    def do_work(self, cb: Callable):
        super().do_work(cb)
        self.sem.release()

    def exec(self, cb: Callable):
        super().exec_async(cb)
        self.sem.acquire()


class SyncCondExecutor(AsyncExecutor):
    def __init__(self):
        super().__init__()
        self.cond = Condition()
        self.is_complete = False

    def do_work(self, cb: Callable):
        super().do_work(cb)
        self.cond.acquire()
        self.is_complete = True
        self.cond.notify_all()
        self.cond.release()

    def exec(self, cb: Callable):
        super().exec_async(cb)
        self.cond.acquire()
        while not self.is_complete:
            self.cond.wait()
        self.cond.release()


def main():
    def foo():
        print('did work')

    # exc = SyncSemExecutor()
    # exc.exec(foo)
    # print('main advances')

    exc = SyncCondExecutor()
    exc.exec(foo)
    print('main advances pt2')


if __name__ == '__main__':
    main()




