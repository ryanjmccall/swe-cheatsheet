import time
from threading import Lock
from threading import Thread
from threading import current_thread

sharedState = [1, 2, 3]
my_lock = Lock()


def foo():
    with my_lock:
        print("{0} has acquired the lock".format(current_thread().getName()))

        time.sleep(3)  #
        sharedState[0] = 777

        print("{0} about to release the lock".format(current_thread().getName()))

    print("{0} released the lock".format(current_thread().getName()))


def bar():
    print("{0} is attempting to acquire the lock".format(current_thread().getName()))

    with my_lock:
        print("{0} has acquired the lock".format(current_thread().getName()))

        print(sharedState[0])
        print("{0} about to release the lock".format(current_thread().getName()))

    print("{0} released the lock".format(current_thread().getName()))



if __name__ == "__main__":
    t = Thread(target=foo, name='t1')
    t.start()
    t2 = Thread(target=bar, name='t2')
    t2.start()
    t.join()
    t2.join()
