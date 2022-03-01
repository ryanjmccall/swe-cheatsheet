from multiprocessing import Process, Queue, current_process
import multiprocessing
import random


def child_process(q):
    count = 0
    while not q.empty():
        try:
            print(q.get(block=False, timeout=5))
            count += 1
        except:
            pass

    print("child process {0} processed {1} items from the queue".format(current_process().name, count), flush=True)


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    q = Queue()

    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))
    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q,))
    p2 = Process(target=child_process, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
