"""
Imagine at the end of a political conference, republicans and democrats are trying to
 leave the venue and ordering Uber rides at the same time. However, to make sure no fight breaks
 out in an Uber ride, the software developers at Uber come up with an algorithm whereby either an
  Uber ride can have all democrats or republicans or two Democrats and two Republicans. All other
  combinations can result in a fist-fight.

Your task as the Uber developer is to model the ride requestors as threads. Once an acceptable
combination of riders is possible, threads are allowed to proceed to ride. Each thread invokes
the method seated() when selected by the system for the next ride. When all the threads are seated,
any one of the four threads can invoke the method drive() to inform the driver to start the ride.
"""

# variables to count the party counts
# lock to manage access to the party counts
# barrier to implement requirement of 4 people per ride
from threading import Lock, Barrier, current_thread, Semaphore


class Solution:
    def __init__(self, ride_limit: int = 4):
        self.democrats_count = 0
        self.democrats_waiting = Semaphore(0)
        self.republicans_count = 0
        self.republicans_waiting = Semaphore(0)
        self.lock = Lock()
        self.barrier = Barrier(ride_limit)
        self.ride_count = 0

    def drive(self):
        self.ride_count += 1
        print(f'ride {self.ride_count} driving off', flush=True)

    def seated(self, party):
        print('\n{0} {1} seated'.format(party, current_thread().getName()), flush=True)

    def seat_demo(self):
        # case: 3 demos waiting > make 4
        # case: 2 or more republicans and 1 or more demos waiting
        # else: wait for more riders
        leader = False
        self.lock.acquire()
        if self.democrats_count == 4:
            leader = True
            self.democrats_count -= 4
            for _ in range(3):
                self.democrats_waiting.release()
        elif self.democrats_count == 2 and self.republicans_count >= 2:
            leader = True
            self.democrats_count -= 2
            self.republicans_count -=2
            self.democrats_waiting.release()
            self.republicans_waiting.release()
            self.republicans_waiting.release()
        else:
            # can't form full ride
            self.lock.release()
            self.democrats_waiting.acquire()

        self.seated('democrat')
        self.barrier.wait()  # halt thread until complete ride is found
        if leader:
            self.drive()
            self.lock.release()

    def seat_repub(self):
        leader = False
        if self.republicans_count == 4:
            for _ in range(3):
                self.republicans_waiting.release()
            leader = True
            self.republicans_count -= 4
        elif self.republicans_count == 2 and self.democrats_count >= 2:
            leader = True
            self.republicans_waiting.release()
            self.democrats_waiting.release()
            self.democrats_waiting.release()
            self.republicans_count -= 2
            self.democrats_count -= 2
        else:
            self.lock.release()
            self.republicans_waiting.acquire()

        self.seated('republican')
        self.barrier.wait()
        if leader:
            self.drive()
            self.lock.release()
