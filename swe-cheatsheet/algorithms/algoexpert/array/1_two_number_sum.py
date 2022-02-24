def twoNumberSum(a, target):
    val_to_ind = {v: i for i, v in enumerate(a)}
    for i, v in enumerate(a):
        remain = target - v
        if remain in val_to_ind and i != val_to_ind[remain]:
            return [v, remain]

    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
