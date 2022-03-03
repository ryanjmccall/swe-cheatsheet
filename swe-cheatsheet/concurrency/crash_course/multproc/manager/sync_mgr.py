from multiprocessing.managers import SyncManager
from multiprocessing import Process
import multiprocessing

# port number on which the manager runs and another can
# connect at
port_num = 55555


def process1_task(lstProxy):
    lstProxy[0] = 1
    print("process 1 sees list as " + str(lstProxy))
    nested_list = list({})
    lstProxy.append(nested_list)

    nested_list.append(99)
    nested_list.append(98)
    nested_list.append(97)
    print("Child process sees lstProxy as: " + str(lstProxy))
    lstProxy[3] = nested_list
    print("Child process sees lstProxy as: " + str(lstProxy))


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    manager = SyncManager(address=('127.0.0.1', port_num))
    manager.start()
    lst = manager.list([0, 0, 0])

    # create first process
    p1 = Process(target=process1_task, args=(lst,))
    p1.start()
    p1.join()
