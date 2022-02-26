from threading import Thread, Semaphore
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
    global shared_value
    while not exit_prog:
        sem_find.acquire()
        print(shared_value, end=' ')
        shared_value = None
        sem_print.release()


def finder():
    global shared_value
    p = 0
    while not exit_prog:
        p += 1
        while not is_prime(p):
            p += 1
            time.sleep(0.01)

        shared_value = p
        sem_find.release()
        sem_print.acquire()


sem_find = Semaphore(0)
sem_print = Semaphore(0)
shared_value = None
exit_prog = False

pThread = Thread(target=printer)
pThread.start()

fThread = Thread(target=finder)
fThread.start()

time.sleep(2)
exit_prog = True

pThread.join()
fThread.join()
