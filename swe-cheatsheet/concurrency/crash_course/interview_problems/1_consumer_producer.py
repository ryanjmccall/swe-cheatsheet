# Title: blocking q, bounded buffer, consumer-producer
# Description: limited size buffer access by different producer consumer threads
# queue.Queue provides synchronized queue out of the box
# methods: pop(), append()
import time
from threading import Condition, current_thread, Thread
from collections import deque


class BlockingQueue:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.curr_size = 0
        self.cond = Condition()
        self.q = deque([])

    def dequeue(self):
        self.cond.acquire()
        while self.curr_size == 0:
            self.cond.wait()

        item = self.q.popleft()
        self.curr_size -= 1

        self.cond.notify_all()  # assures that the consumer thread also gets a chance to wake up
        self.cond.release()

        return item

    def enqueue(self, item):
        self.cond.acquire()
        while self.curr_size == self.max_size:
            self.cond.wait()

        self.q.append(item)
        self.curr_size += 1

        self.cond.notify_all()
        print(f'cur size {self.curr_size}', flush=True)
        self.cond.release()


def producer(q: BlockingQueue, val):
    while True:
        q.enqueue(val)
        val += 1
        time.sleep(0.1)


def consumer(q):
    while True:
        item = q.dequeue()
        print(f'{current_thread().getName()} consumed {item}')
        time.sleep(1)


def main():
    q = BlockingQueue(max_size=5)
    ts = [
        Thread(target=consumer, name='c1', args=(q,), daemon=True),
        Thread(target=consumer, name='c2', args=(q,), daemon=True),
        Thread(target=producer, name='p1', args=(q, 1), daemon=True),
        Thread(target=producer, name='p2', args=(q, 100), daemon=True)
    ]
    for t in ts:
        t.start()
    time.sleep(10)
    print('exit')


if __name__ == "__main__":
    main()
