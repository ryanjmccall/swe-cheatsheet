import time
from threading import Condition, current_thread, Thread


class Barrier(object):
    def __init__(self, size):
        self.barrier_size = size
        self.reached_count = 0  # how many thread reached barrier
        self.released_count = self.barrier_size  # threads exited barrier
        self.cond = Condition()

    def arrived(self):
        self.cond.acquire()
        while self.reached_count == self.barrier_size:
            self.cond.wait()

        self.reached_count += 1
        if self.reached_count == self.barrier_size:
            self.released_count = self.barrier_size
        else:
            while self.reached_count < self.barrier_size:
                self.cond.wait()

        self.released_count -= 1
        if self.released_count == 0:
            self.reached_count = 0

        print("{0} released".format(current_thread().getName()), flush=True)
        self.cond.notify_all()
        self.cond.release()


def thread_process(sleep_for):
    time.sleep(sleep_for)
    print("{0} reached the barrier".format(current_thread().getName()), flush=True)
    barrier.arrived()

    time.sleep(sleep_for)
    print("{0} reached the barrier".format(current_thread().getName()))
    barrier.arrived()

    time.sleep(sleep_for)
    print("{0} reached the barrier".format(current_thread().getName()))
    barrier.arrived()


if __name__ == "__main__":
    barrier = Barrier(3)

    t1 = Thread(target=thread_process, args=(0,))
    t2 = Thread(target=thread_process, args=(0.5,))
    t3 = Thread(target=thread_process, args=(1.5,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
