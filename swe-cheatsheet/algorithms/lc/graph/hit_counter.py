from collections import defaultdict


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min = 0
        self.limit = 300
        self.hits = [0] * self.limit

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        offset = timestamp - self.min
        if offset < self.limit:
            self.hits[offset] += 1
        else:
            from_end = offset - (self.limit - 1)
            self.hits = self.hits[from_end:] + [0] * from_end
            self.min += from_end

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        offset = timestamp - self.min
        return sum(self.hits[:offset])


def t():
    c = HitCounter()

    c.hit(1)
    c.hit(2)
    c.hit(3)

    print(c.getHits(4))

    c.hit(300)
    print(c.getHits(300))

    print(c.getHits(301))

    # 3 before 4
    # 3 before 300
    # 3: (2, 3, 300)


t()
