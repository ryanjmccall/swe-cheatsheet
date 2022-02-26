import time
from threading import Condition, Thread, current_thread


class TokenBucketFilterFactory:
    @staticmethod
    def makeTokenBucketFilter(capacity: int):
        f = MultithreadedTokenBucketFilter(capacity)
        f.initialize()  # start the Daemon outside the constructor
        return f


class MultithreadedTokenBucketFilter:
    ONE_SECOND = 1

    def __init__(self, max_tokens: int):
        self.max_tokens = max_tokens
        self.tokens = 0
        self.cond = Condition()

    def initialize(self):
        t = Thread(target=self.daemon_thread, daemon=True)
        t.start()

    def daemon_thread(self):
        while True:
            self.cond.acquire()
            if self.tokens < self.max_tokens:
                self.tokens += 1

            self.cond.notify()
            self.cond.release()
            time.sleep(self.ONE_SECOND)

    def get_token(self):
        self.cond.acquire()
        while not self.tokens:
            self.cond.wait()

        self.tokens -= 1

        self.cond.release()

        print("Granting " + current_thread().getName() + " token at " + str(time.time()))


def main():
    threads_list = []
    tbf = TokenBucketFilterFactory.makeTokenBucketFilter(10)
    for i in range(10):
        t = Thread(target=tbf.get_token, name=f't_{i}')
        threads_list.append(t)

    for t in threads_list:
        t.start()

    for t in threads_list:
        t.join()


if __name__ == "__main__":
    main()











