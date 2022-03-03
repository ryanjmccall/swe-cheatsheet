from multiprocessing import Pool
import os
import time


def init(main_id):
    print(f'process {os.getpid()} received task from process {main_id}')


def square(x):
    return x * x


def on_success(r):
    print(f'result {r}')


def on_error(err):
    print(f'error {err}')


if __name__ == '__main__':
    pid = os.getpid()
    pool = Pool(processes=1, initializer=init, initargs={pid}, maxtasksperchild=1)
    result = pool.apply_async(square, (9,), callback=on_success, error_callback=on_error)
    time.sleep(3)
    print(result.get(), result.ready(), result.successful())
