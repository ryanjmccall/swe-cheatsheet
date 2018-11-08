from typing import Any, List, Union


KEY_TYPES = (str, int)


def sumHashCode(key: Union[str, int], size: int) -> int:
    assert isinstance(key, KEY_TYPES), ("key type: %s not found in %s" %
                                        (type(key), KEY_TYPES))
    # convert each char to Unicode code point and sum
    return (sum(map(lambda x: ord(x) , key)) % size
            if isinstance(key, str)
            else key % size)


class HashTable:
    def __init__(self, capacity: int=1000):
        self._cap = capacity
        self.size = 0
        self._keys = set()

        # storage format:
        # - list of buckets
        # - each bucket a list of entries
        # - each entry a key-value pair
        self._data = [[] for _ in range(capacity)]

    def _find(self, key) -> (List[list], int):
        """
        :param key: entry's key
        :returns corresponding bucket and index of matching entry or -1 is not
        present
        """
        idx = sumHashCode(key, self._cap)
        bucket = self._data[idx]
        for i, e in enumerate(bucket):
            if e[0] == key:
                return bucket, i

        return bucket, -1

    def set(self, key, value: Any):
        bucket, bucketIdx = self._find(key)
        if bucketIdx == -1:
            bucket.append([key, value])
            self._keys.add(key)
            self.size += 1
        else:
            bucket[bucketIdx][1] = value

    def get(self, key) -> Any:
        bucket, bucketIdx = self._find(key)
        if bucketIdx == -1:
            raise KeyError(key)

        return bucket[bucketIdx][1]

    def remove(self, key) -> Any:
        bucket, bucketIdx = self._find(key)
        if bucketIdx == -1:
            raise KeyError(key)

        entry = bucket.pop(bucketIdx)
        self.size -= 1
        self._keys.remove(key)

        return entry[1]

    def containsKey(self, key) -> bool:
        return key in self._keys

    def keys(self):
        for k in iter(self._keys):
            yield k

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.remove(key)

    def __str__(self):
        return ", ".join(k + ":" + str(self.get(k)) for k in self._keys)


def run():
    t = HashTable(capacity=3)
    for i in range(20):
        t.set(i, i)
        print(t.get(i))
        print(t.containsKey(i))

    print(list(t.keys()))

    for i in range(10):
        t.remove(i)
        print(t.containsKey(i))

    print(list(t.keys()))


if __name__ == "__main__":
    run()
