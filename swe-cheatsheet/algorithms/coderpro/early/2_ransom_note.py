from collections import Counter, defaultdict


def can_construct_(note: str, magazine: str) -> bool:
    # put magazine in a counter and note in another counter
    # loop over note counter's entries assert counts are <= magazine's
    note_count = Counter(note)
    mag_count = Counter(magazine)
    for letter, n_count in note_count.items():
        if n_count > mag_count.get(letter, 0):
            return False

    return True


def can_construct(note: str, mag: str) -> bool:
    mag_count = Counter(mag)
    for s in note:
        if not mag_count[s]:
            return False

        mag_count[s] -= 1

    return True


print(can_construct('aa', 'aab'))
print(can_construct('abcc', 'aabbcc'))
