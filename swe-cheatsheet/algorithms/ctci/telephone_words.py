from collections import defaultdict
from typing import Dict, List, Iterator


NUM_TO_CHARS = {1: "abc", 2: "def", 3: "ghi", 4: "jkl", 5: "mno",
                6: "pqr", 7: "stu", 8: "vwx", 9: "y", 0: "z"}


WORDS = {"beg", "adi"}


def validChars(nums: List[int], idx: int,
               idxToWordChars: Dict[int, set]) -> Iterator[str]:
    allChars = NUM_TO_CHARS[nums[idx]]
    wordChars = idxToWordChars[idx]
    return filter(lambda c: c in wordChars, allChars)


def allWords(nums: List[int], validWords: set) -> List[str]:
    idxToChars = defaultdict(set)
    for w in iter(validWords):
        for i, c in enumerate(w):
            idxToChars[i].add(c)

    charArrays = [[c] for c in validChars(nums, 0, idxToChars)]
    for i in range(1, len(nums)):
        charArrays = [arr + [c]
                      for arr in charArrays
                      for c in validChars(nums, i, idxToChars)]

    words = ("".join(arr) for arr in charArrays)
    return list(filter(lambda x: x in validWords, words))


print(allWords([1, 2, 3], WORDS))
