from threading import Thread, Event
import time


def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def printer():
    global shared
    while not exit_:
        prime_available.wait()
        print(shared, end=', ')
        shared = None
        prime_available.clear()

        prime_printed.set()


def finder():
    global shared
    p = 1
    while not exit_:
        while not is_prime(p):
            p += 1
            time.sleep(0.01)

        shared = p
        prime_available.set()
        prime_printed.wait()
        prime_printed.clear()
        p += 1


prime_available = Event()
prime_printed = Event()
shared = None
exit_ = False
t1 = Thread(target=printer)
t1.start()
t2 = Thread(target=finder)
t2.start()

time.sleep(3)

exit_ = True
prime_available.set()
prime_printed.set()

t1.join()
t2.join()

