import multiprocessing
from multiprocessing import Process, Semaphore, Array


def child_func(child2parent, parent2child, arr):
    print(f'before {arr[0]}', flush=True)
    child2parent.release()
    parent2child.acquire()
    print(f'after {arr[0]}', flush=True)


def main():
    child2parent, parent2child = Semaphore(0), Semaphore(0)
    print(f'{multiprocessing.cpu_count()} CPUs')

    a = Array('i', range(6))
    print(f'parent sends array {id(a)}')

    p = Process(target=child_func, args=(child2parent, parent2child, a))
    p.start()
    child2parent.acquire()

    a[0] += 100
    print('parent changes shared value', flush=True)
    parent2child.release()
    p.join()


if __name__ == '__main__':
    main()
