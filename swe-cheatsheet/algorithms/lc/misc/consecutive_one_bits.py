

def consecutive_ones(n: int):
    most = 0
    cur = 0
    mask = 1
    while n:
        if n & mask:
            cur += 1
        else:
            most = max(most, cur)
            cur = 0
        n >>= 1
    return max(most, cur)


print(consecutive_ones(n=242))
