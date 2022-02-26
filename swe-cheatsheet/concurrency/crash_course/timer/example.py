from threading import Timer, current_thread
import time


def say_hi():
    print(f'{current_thread().getName()} says hi')


t = Timer(1, say_hi)
t.start()
# time.sleep(1)

print(f'{current_thread().getName()} exiting')
