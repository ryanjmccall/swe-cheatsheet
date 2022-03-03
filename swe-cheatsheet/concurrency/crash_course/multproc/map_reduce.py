

from multiprocessing import Pool
import os


def init(main_id):
    print(f'process {os.getpid()} received task from parent {main_id}')


def square(x):
    return x * x


def on_success(r):
    print(f'result {r}')


def on_error(err):
    print(f'error {err}')


def map_async(pool):
    pool.map_async(square, tuple(range(1, 11)), chunksize=2, callback=on_success,
                   error_callback=on_error)


if __name__ == '__main__':
    pid = os.getpid()
    pool = Pool(processes=5, initializer=init, initargs={pid}, maxtasksperchild=50)
    res = pool.map(square, tuple(range(1, 11)), chunksize=2)  # chunksize => work / proc
    print(res)
    pool.close()
    pool.join()

    # other methods in pool
    # imap, imap_unordered => blocking calls that return iterators (no callbacks)

    # starmap, starmap_async
    # allow multiple subtask arguments

    # Python mapreduce doesn't handle failures
    # - implement try in the task execution method
    # - collect failed task and resubmit them for execution
