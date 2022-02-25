from threading import current_thread, Condition, Thread

flag = False
cond = Condition()


def child():
    global flag
    name = current_thread().getName()

    cond.acquire()
    if not flag:
        cond.wait()
        print(f'\n{name} woken up \n')

    cond.release()
    print(f'\n{name} exiting \n')


threads = [Thread(target=child, name=n)
           for n in ('t1', 't2', 't3')]
for t in threads:
    t.start()

cond.acquire()
cond.notify_all()
cond.release()

for t in threads:
    t.join()

print('exiting')
