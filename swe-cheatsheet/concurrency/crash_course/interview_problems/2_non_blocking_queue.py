from threading import Thread, RLock, current_thread
from concurrent.futures import Future
import time
import random


class NonBlockingQueue:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.q = []
        self.q_waiting_puts = []
        self.q_waiting_gets = []
        self.lock = RLock()

    def dequeue(self):
        result, future = None, None
        with self.lock:
            if self.q:
                result = self.q.pop(0)
                if self.q_waiting_puts:
                    self.q_waiting_puts.pop(0).set_result(True)
            else:
                future = Future()
                self.q_waiting_gets.append(future)

        return result, future

    def enqueue(self, item):
        future = None
        with self.lock:
            size = len(self.q)
            if size == self.max_size:
                future = Future()
                self.q_waiting_puts.append(future)
            else:
                self.q.append(item)
                # resolve pending future for get request
                if self.q_waiting_gets:
                    future_get = self.q_waiting_gets.pop(0)
                    future_get.set_result(self.q.pop(0))

        return future


def retry_dequeue(future):
    item = future.result()
    print(f'\nretry_dequeue executed by thread {current_thread().getName()} and {item} consumed', flush=True)


def consumer_thread(q):
    while True:
        item, future = q.dequeue()
        if not item:
            future.add_done_callback(retry_dequeue)
        else:
            print("\n{0} consumed item {1}".format(current_thread().getName(), item), flush=True)

        # slow down the consumer
        time.sleep(1)


def retry_enqueue(future):
    print(f'\nCallback invoked by thread {current_thread().getName()}')
    item, q = future.item, future.q
    new_future = q.enqueue(item)
    if new_future:
        new_future.item = item
        new_future.q = q
        new_future.add_done_callback(retry_enqueue)
    else:
        print("\n{0} successfully added on a retry".format(item))


def producer_thread(q):
    item = 1
    while True:
        future = q.enqueue(item)
        if future:
            future.item = item
            future.q = q
            future.add_done_callback(retry_enqueue)

        item += 1
        time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    no_block_q = NonBlockingQueue(5)
    consumer = Thread(target=consumer_thread, name='c', args=(no_block_q,), daemon=True)
    producer = Thread(target=producer_thread, name='p', args=(no_block_q,), daemon=True)
    consumer.start()
    producer.start()
    time.sleep(10)
    print('exit')

