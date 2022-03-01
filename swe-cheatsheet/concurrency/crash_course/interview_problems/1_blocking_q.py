from threading import Condition
from collections import deque


class BlockingQueue:
    def __init__(self, limit: int):
        self.limit = limit
        self.size = 0
        self.cond = Condition()
        self.q = deque([])

    def enqueue(self, val):
        self.cond.acquire()
        while self.size == self.limit:
            self.cond.wait()

        # critical section
        self.q.append(val)
        self.size += 1
        # /critical

        self.cond.notify_all()
        self.cond.release()


    def dequeue(self):
        self.cond.acquire()
        while not self.q:
            self.cond.wait()

        # critical
        res = self.q.popleft()
        self.size -= 1
        # /critical

        self.cond.notify_all()
        self.cond.release()
        return res
