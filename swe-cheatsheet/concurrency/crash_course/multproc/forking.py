import multiprocessing
from multiprocessing import Process


class Test:
    val = 777


def task():
    print(Test.val)


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')
    Test.val = 999

    # child process gets copy of all the resources of the parent
    # this could be open file, db connection that is in the parent!
    p = Process(target=task, name='p1')
    p.start()
    p.join()

