
ORD_0 = ord('0')


def convert_to_int(a: str):
    if not a or (a[0] == '-' and len(a) == 1):
        raise ValueError('bad input')

    neg = False
    if a[0] == '-':
        neg = True
        a = a[1:]

    total = 0
    factor = 1
    for c in reversed(a):
        total += (ord(c) - ORD_0) * factor
        factor *= 10

    return -total if neg else total


print(convert_to_int('-105'))
print(convert_to_int('12345'))
print(convert_to_int('0'))
