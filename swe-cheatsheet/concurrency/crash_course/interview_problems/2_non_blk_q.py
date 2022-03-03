import time
from collections import deque
from concurrent.futures import Future
from threading import RLock, current_thread, Thread
from typing import Any, Tuple


class NonBlockingQueue:
    def __init__(self, limit: int):
        self.q = deque([])
        self.waiting_enqueues = deque([])
        self.waiting_dequeues = deque([])
        self.limit = limit
        self.rlock = RLock()

    def enqueue(self, item) -> Future:
        enq_future = None
        with self.rlock:
            if len(self.q) < self.limit:
                self.q.append(item)
                if self.waiting_dequeues:
                    result = self.q.popleft()
                    get_future = self.waiting_dequeues.popleft()
                    get_future.set_result(result)
            else:
                enq_future = Future()
                self.waiting_enqueues.append(enq_future)

        return enq_future

    def dequeue(self) -> Tuple[Any, Future]:
        result, deq_future = None, None
        with self.rlock:
            if self.q:
                result = self.q.popleft()
                if self.waiting_enqueues:
                    put_future = self.waiting_enqueues.popleft()
                    put_future.set_result(True)  # signals to retry enqueue

            else:  # if empty
                deq_future = Future()
                self.waiting_dequeues.append(deq_future)

        return result, deq_future


def producer(q: NonBlockingQueue):
    item = 1
    while True:
        future = q.enqueue(item)
        if future:
            future.item = item
            future.deq = q
            future.add_done_callback(retry_enqueue)

        item += 1
        time.sleep(1)


def retry_enqueue(future):
    print(f'\nCallback invoked by thread {current_thread().getName()}')
    new_future = future.deq.enqueue(future.item)
    if new_future:
        new_future.item = future.item
        new_future.deq = future.deq
        new_future.add_done_callback(retry_enqueue)
    else:
        print("\n{0} successfully added on a retry".format(future.item))


def consumer(q: NonBlockingQueue):
    while True:
        item, future = q.dequeue()
        if item is None:
            future.add_done_callback(lambda f: f.result())
        else:
            print("\n{0} consumed item {1}".format(current_thread().getName(), item), flush=True)

        time.sleep(1)


if __name__ == "__main__":
    no_block_q = NonBlockingQueue(5)
    consumer = Thread(target=consumer, name='c', args=(no_block_q,), daemon=True)
    producer = Thread(target=producer, name='p', args=(no_block_q,), daemon=True)
    consumer.start()
    producer.start()
    time.sleep(10)
    print('exit')