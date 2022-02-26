
"""
Imagine you have a bucket that gets filled with tokens at the rate of 1 token per second.
The bucket can hold a maximum of N tokens. Implement a thread-safe class that lets threads get a
token when one is available. If no token is available, then the token-requesting threads should block.

The class should expose an API called get_token() that various threads can call to get a token.
"""
import time
from threading import Lock, current_thread, Thread


class TokenBucketFilter:
    def __init__(self, max_tokens: int):
        self.max_tokens = max_tokens
        self.last_request_time = time.time()
        self.tokens = 0
        self.lock = Lock()

    def get_token(self):
        with self.lock:
            self.tokens += int(time.time() - self.last_request_time)
            if self.tokens > self.max_tokens:
                self.tokens = self.max_tokens

            if self.tokens == 0:
                time.sleep(1)
            else:
                self.tokens -= 1
            self.last_request_time = time.time()
            print("Granting {0} token at {1} ".format(current_thread().getName(), int(time.time())))


if __name__ == '__main__':
    f = TokenBucketFilter(1)
    ts = [Thread(target=f.get_token) for _ in range(10)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
