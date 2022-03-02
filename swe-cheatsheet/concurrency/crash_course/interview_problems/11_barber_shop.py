"""
barbershop has a waiting room with n chairs and there's 1 barber chair where you receive the haircut
no customer > barber sleeps
all chairs filled > customer leaves
barber busy chairs available > customer sits
barber sleeping > customer wakes up
"""

import time
from threading import Lock, Semaphore, Thread


class BarberShop:
    def __init__(self):
        self.total_chairs = 3
        self.haircuts_given = 0

        self.lock = Lock()  # to guard access of multiple customer threads to customer count
        self.waiting_customers = 0

        # bidirectional communication between customers and the barber
        self.awaiting_customer_arrive = Semaphore(0)
        self.awaiting_barber_ready = Semaphore(0)
        self.awaiting_barber_finish_cut = Semaphore(0)
        self.awaiting_customer_leave = Semaphore(0)

    def customer_arrive(self):
        with self.lock:
            if self.waiting_customers == self.total_chairs:
                print('customer walks out due to busyness')
                return

            self.waiting_customers += 1

        self.awaiting_customer_arrive.release()
        self.awaiting_barber_ready.acquire()

        self.awaiting_barber_finish_cut.acquire()
        self.awaiting_customer_leave.release()

        with self.lock:
            self.waiting_customers -= 1

    def barber(self):
        while True:
            self.awaiting_customer_arrive.acquire()  # go to sleep
            self.awaiting_barber_ready.release()

            time.sleep(0.05)
            self.haircuts_given += 1
            print(f'barber finishes cut, count={self.haircuts_given}')

            self.awaiting_barber_finish_cut.release()
            self.awaiting_customer_leave.acquire()


def main():
    shop = BarberShop()
    barber = Thread(target=shop.barber, daemon=True)
    barber.start()

    customers = [Thread(target=shop.customer_arrive) for _ in range(10)]
    customers2 = [Thread(target=shop.customer_arrive) for _ in range(5)]
    for t in customers:
        t.start()

    time.sleep(0.5)

    for t in customers2:
        t.start()

    for t in customers + customers2:
        t.join()


if __name__ == "__main__":
    main()
