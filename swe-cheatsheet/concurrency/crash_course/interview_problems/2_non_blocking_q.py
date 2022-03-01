import time
from collections import deque
from concurrent.futures import Future
from threading import RLock, current_thread, Thread


class NonBlockingQueue:
    def __init__(self, limit: int):
        self.limit = limit
        self.q = deque([])
        self.puts = deque([])
        self.gets = deque([])
        self.rlock = RLock()

    def enqueue(self, val):
        future = None
        with self.rlock:
            if len(self.q) == self.limit:
                future = Future()
                self.puts.append(future)
            else:
                self.q.append(val)
                if self.gets:
                    get_future = self.gets.popleft()
                    get_future.set_result(self.q.popleft())

        return future

    def dequeue(self):
        result, future = None, None
        with self.rlock:
            if self.q:
                result = self.q.popleft()
                if self.puts:
                    put_future = self.puts.popleft()
                    put_future.set_result(True)
            else:
                future = Future()
                self.gets.append(future)

        return result, future


def consumer_thread(q):
    while True:
        item, future = q.dequeue()
        if item is None:
            print('consumer received future')
        else:
            print("\n{0} consumed item {1}".format(current_thread().getName(), item), flush=True)
        time.sleep(1)


def producer_thread(q):
    item = 1
    while True:
        future = q.enqueue(item)
        if future:
            future.item = item
            future.q = q
            future.add_done_callback(retry_enqueue)

        item += 1
        time.sleep(.1)


def retry_enqueue(future):
    item = future.item
    q = future.q
    new_future = q.enqueue(item)
    if new_future:
        new_future.item = item
        new_future.q = q
        new_future.add_done_callback(retry_enqueue)
    else:
        print("\n{0} successfully added on a retry".format(item))


if __name__ == "__main__":
    no_block_q = NonBlockingQueue(5)

    consumerThread1 = Thread(target=consumer_thread, name="consumer", args=(no_block_q,), daemon=True)
    producerThread1 = Thread(target=producer_thread, name="producer", args=(no_block_q,), daemon=True)

    consumerThread1.start()
    producerThread1.start()

    time.sleep(15)
    print("\nMain thread exiting")