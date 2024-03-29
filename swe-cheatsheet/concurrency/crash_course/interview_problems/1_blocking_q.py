import time
from threading import Condition, Thread
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


def producer(bq: BlockingQueue):
    for _ in range(8):
        print('producer sent', _, flush=True)
        bq.enqueue(_)

    time.sleep(2)

    for _ in range(8):
        print('producer sent', _, flush=True)
        bq.enqueue(_)


def consumer(bq: BlockingQueue):
    time.sleep(1)

    for i in range(16):
        print('consumer got', bq.dequeue(), flush=True)


def main():
    q = BlockingQueue(limit=5)
    t1, t2 = Thread(target=producer, args=(q,)), Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
