def sortedSquaredArray(array):
    res = []
    i = 0
    for i, v in enumerate(array):
        if v < 0:
            array[i] = -array[i]
        else:
            break

    left = i - 1
    while left > 0 and i < len(array):
        if array[left] < array[i]:
            res.append(array[left] * array[left])
            left -= 1
        else:
            res.append(array[i] * array[i])
            i += 1

    while left > 0:
        res.append(array[left] * array[left])
        left -= 1

    while i < len(array):
        res.append(array[i] * array[i])
        i += 1

    return res


print(sortedSquaredArray([-2, -1]))
