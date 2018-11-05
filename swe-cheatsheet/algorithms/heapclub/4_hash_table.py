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
        self.capacity = capacity
        self.size = 0
        self._keys = set()

        # storage format:
        # - list of buckets
        # - each bucket a list of entries
        # - each entry a key-value pair
        self.data = [[] for _ in range(capacity)]

    def _find(self, key) -> (List[list], list):
        """
        :param key: entry's key
        """
        idx = sumHashCode(key, self.capacity)
        entry = None
        bucket = self.data[idx]
        for e in bucket:
            if e[0] == key:
                entry = e
                break

        return bucket, entry

    def set(self, key, value: Any):
        bucket, entry = self._find(key)
        if entry:
            entry[1] = value
        else:
            bucket.append([key, value])
            self._keys.add(key)
            self.size += 1

    def get(self, key) -> Any:
        _, entry = self._find(key)
        if entry:
            return entry[1]

        raise KeyError(key)

    def containsKey(self, key) -> bool:
        return key in self._keys

    def remove(self, key) -> Any:
        bucket, entry = self._find(key)
        if entry:
            bucket.remove(entry)
            if not bucket:
                self._keys.remove(key)

            self.size -= 1
            return entry[1]

        raise KeyError(key)

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

