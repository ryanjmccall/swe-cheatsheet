import time
from threading import Thread, Semaphore


def task1():
    print('t1 acq')
    sem.acquire()


def task2():
    print('t2 release')
    sem.release()


sem = Semaphore(0)
thread2 = Thread(target=task2)
thread2.start()

time.sleep(2)

thread1 = Thread(target=task1)
thread1.start()

thread1.join()
thread2.join()
