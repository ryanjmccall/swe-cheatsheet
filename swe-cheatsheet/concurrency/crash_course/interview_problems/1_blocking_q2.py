import time
from threading import Condition, Thread
from collections import deque
from typing import Any


class BlockingQueue:
    def __init__(self, limit: int):
        if limit > 10e6:
            raise ValueError('limit cannot exceed 1M')

        self.limit = limit
        self.cond = Condition()
        self.deq = deque([])

    def enqueue(self, item: Any):
        with self.cond:
            while len(self.deq) == self.limit:
                self.cond.wait()

            self.deq.append(item)

            self.cond.notify_all()

    def dequeue(self) -> Any:
        with self.cond:
            while not self.deq:
                self.cond.wait()

            item = self.deq.popleft()

            self.cond.notify_all()

        return item


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

