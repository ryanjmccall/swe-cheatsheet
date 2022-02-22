def hasSingleCycle(array) -> bool:
    if not array:
        return False

    i, count = 0, 0
    for _ in array:
        if count and not i:
            return False

        count += 1
        i = next_index(i, array)

    return i == 0


def next_index(i, array) -> int:
    next_i = (i + array[i]) % len(array)
    return next_i if next_i >= 0 else next_i + len(array)


print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
