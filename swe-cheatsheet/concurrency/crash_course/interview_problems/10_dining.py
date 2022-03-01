from threading import Thread
from threading import Semaphore
import random
import time


class DiningPhilosopherProblem:

    def __init__(self, diners: int):
        # this limit critically ensures that we don't get deadlock
        # in the case where n diners all grab their right fork
        self.diner_limit = Semaphore(diners - 1)
        self.forks = [Semaphore(1) for _ in range(diners)]
        self.running = True

    def dine(self, id):
        while self.running:
            self.contemplate()
            self.eat(id)

    def contemplate(self):
        sleep_for = random.randint(800, 1200) / 1000
        time.sleep(sleep_for)

    def eat(self, id):
        self.diner_limit.acquire()

        self.forks[id].acquire()
        right = (id + 1) % 5
        self.forks[(id + 1) % 5].acquire()

        print(f"{id} eats with {id} {right}")

        self.forks[id].release()
        self.forks[(id + 1) % 5].release()

        self.diner_limit.release()


def main():
    num = 5
    problem = DiningPhilosopherProblem(num)
    threads = [Thread(target=problem.dine, args=(uid,)) for uid in range(num)]
    for t in threads:
        t.start()

    time.sleep(3)
    problem.running = False

    for t in threads:
        t.join()



if __name__ == "__main__":
    main()
