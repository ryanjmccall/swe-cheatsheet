from threading import Barrier, Thread, current_thread, BrokenBarrierError
import random
import time


def foo():
    time.sleep(random.randint(0, 3))
    print("Currently {0} threads blocked on barrier".format(barrier.n_waiting))
    barrier.wait()
    print('got past barrier', flush=True)


def on_release():
    print("All threads released, reported by {0}".format(current_thread().getName()))


count = 5
barrier = Barrier(count, action=on_release)
threads = [Thread(target=foo) for _ in range(count - 1)]
for t in threads:
    t.start()

time.sleep(10)
try:
    barrier.abort()
except BrokenBarrierError as e:
    print('caught broken barrier error')
