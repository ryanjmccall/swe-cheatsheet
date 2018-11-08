from typing import Any, List


def strHashCode(key: str, size: int) -> int:
    # convert each char to Unicode code point and sum
    return sum(map(lambda x: ord(x), key)) % size


def intHashCode(key: int, size: int) -> int:
    return key % size


class HashTable:
    def __init__(self, capacity: int=1000):
        self._cap = capacity
        self.size = 0
        self._keys = set()

        # list of buckets, each a list of entries, each a key-value pair
        self._buckets = [[] for _ in range(capacity)]

    def _find(self, k) -> (List[list], int):
        """
        :param k: entry's key
        :returns key's bucket and index of matching entry or -1 if no match
        """
        h = intHashCode(k, self._cap)
        bucket = self._buckets[h]
        for i, e in enumerate(bucket):
            if e[0] == k:
                return bucket, i

        return bucket, -1

    def put(self, key, value: Any):
        bucket, idx = self._find(key)
        if idx == -1:
            bucket.append([key, value])
            self._keys.add(key)
            self.size += 1
        else:
            bucket[idx][1] = value

    def get(self, key) -> Any:
        bucket, idx = self._find(key)
        if idx == -1:
            raise KeyError(key)

        return bucket[idx][1]

    def remove(self, key) -> Any:
        bucket, idx = self._find(key)
        if idx == -1:
            raise KeyError(key)

        entry = bucket.pop(idx)
        self.size -= 1
        self._keys.remove(key)
        return entry[1]

    def contains_key(self, key) -> bool:
        return key in self._keys

    def count(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def keys(self):
        for k in iter(self._keys):
            yield k

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.remove(key)

    def __str__(self):
        return ", ".join(k + ":" + str(self.get(k)) for k in self._keys)


def run():
    t = HashTable(capacity=3)
    for i in range(20):
        t.put(i, i)
        print(t.get(i))
        print(t.contains_key(i))

    print(list(t.keys()))

    for i in range(10):
        t.remove(i)
        print(t.contains_key(i))

    print(list(t.keys()))


if __name__ == "__main__":
    run()
