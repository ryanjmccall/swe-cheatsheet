from threading import Condition, Thread
import time


flag = False

cond = Condition()


def child():
    cond.acquire()

    if not flag:
        cond.wait(timeout=0.5)
    if not flag:
        print('child thread timed out waiting for notify')

    cond.release()


thread = Thread(target=child)
thread.start()

time.sleep(3)
thread.join()

