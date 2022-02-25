"""
Idiomatic use of wait()

acquire lock
while(condition_to_test is not satisfied):
    wait

# condition is true, perform work
release lock

Idiomatic use of notify()

acquire lock
set condition_to_test to true/satisfied
notify
release lock
"""
import time
from threading import Condition, Lock, Thread


# Printer/Consumer thread
def printer_thread():
    global prime_holder
    global found_prime

    while not exit_prog:

        # Wait for work
        cond_var.acquire()
        while not found_prime and not exit_prog:
            cond_var.wait()
        cond_var.release()

        if not exit_prog:
            print(prime_holder)
            prime_holder = None

            # Wake producer
            cond_var.acquire()
            found_prime = False  # modify shared var
            cond_var.notify()
            cond_var.release()


# Finder Producer thread
def finder_thread():
    global prime_holder
    global found_prime
    i = 1
    while not exit_prog:
        while not is_prime(i):
            i += 1
            time.sleep(0.01)

        prime_holder = i

        # notify consumer
        cond_var.acquire()
        found_prime = True
        cond_var.notify()
        cond_var.release()

        # wait for consumer reply
        cond_var.acquire()
        while found_prime and not exit_prog:
            cond_var.wait()
        cond_var.release()

        i += 1


def is_prime(num):
    if num == 2 or num == 3:
        return True
    div = 2
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


cond_var = Condition(Lock())
found_prime = False
prime_holder = None
exit_prog = False


printer = Thread(target=printer_thread)
printer.start()

finder = Thread(target=finder_thread)
finder.start()

time.sleep(3)

exit_prog = True

cond_var.acquire()
cond_var.notifyAll()
cond_var.release()

printer.join()
finder.join()




