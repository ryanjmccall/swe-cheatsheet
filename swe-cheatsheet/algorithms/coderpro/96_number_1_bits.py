


def num_1bits(n: int) -> int:
    bits = 0
    while n:
        if n & 1:
            bits += 1
        n >>= 1

    return bits


print(num_1bits(23))


