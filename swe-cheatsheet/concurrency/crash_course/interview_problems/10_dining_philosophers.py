import random
import time
from threading import Semaphore, Thread

"""
Imagine you have five philosophers sitting on a roundtable. 
The philosopher's do only two kinds of activities. One: they contemplate,
 and two: they eat. However, they have only five forks between themselves to eat 
 their food with. Each philosopher requires both the fork to his left and the fork 
 to his right to eat his food.
 """


class Problem:
    def __init__(self, num=5):
        # this limit critically ensures that we don't get deadlock
        # in the case where n diners all grab their right fork
        self.diners_sem = Semaphore(num-1)
        self.forks = [Semaphore(1) for _ in range(num)]
        self.running = True

    def run(self, uid):
        while self.running:
            time.sleep(random.randint(800, 1200) / 1000)
            self.eat(uid)

    def eat(self, uid):
        self.diners_sem.acquire()

        left, right = uid, (uid + 1) % len(self.forks)
        self.forks[left].acquire()
        self.forks[right].acquire()

        print(f'{uid} eats with {left} {right}')

        self.forks[left].release()
        self.forks[right].release()

        self.diners_sem.release()


def main():
    num = 5
    problem = Problem(num)
    threads = [Thread(target=problem.run, args=(uid,)) for uid in range(num)]
    for t in threads:
        t.start()

    time.sleep(3)
    problem.running = False

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
