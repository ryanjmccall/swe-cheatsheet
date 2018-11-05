# 1
def xor(n: int) -> int:
    """
    n % 4 = remainder
    0 > n
    1 > 1
    2 > n + 1
    3 > 0

    :param n:
    :return:
    """
    mod = n % 4
    if not mod:
        return n
    elif mod == 1:
        return 1
    elif mod == 2:
        return n + 1
    else:
        return 0

# 2

# 3
def isPowerOfTwo(x: int) -> bool:
    """
    4 -> (100)
    3 -> (011)
    4 & 3 -> 0
    """
    return x and not (x & (x - 1))

print(4 & 3)


# 4


# 5


# 6


# 7 swap two numbers
def swap(a, b):
    a ^= b
    b ^= a
    a ^= b

