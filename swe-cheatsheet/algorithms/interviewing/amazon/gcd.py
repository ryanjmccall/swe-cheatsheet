from collections import defaultdict


def generalizedGCD(num, arr):
    divisor_count = defaultdict(int)
    for value in arr:
        for divisor in get_divisors(value):
            divisor_count[divisor] += 1

    return max(d for d, cnt in divisor_count.items() if cnt == num)


def get_divisors(value: int):
    for n in range(1, value + 1):
        if value % n == 0:
            yield n


def t():
    assert generalizedGCD(5, [2,3,4,5,6]) == 1
    assert generalizedGCD(5, [2,4,6,8,10]) == 2

    a = 5 != 5
    b = a >= 5
    b += 1
    b -= 1
    while a := 5:
        pass
    


t()
