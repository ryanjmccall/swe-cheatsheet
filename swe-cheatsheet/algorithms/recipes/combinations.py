def combos_recur_gen(arr: list, carry=()):
    for i, v in enumerate(arr):
        yield carry + (v,)
        yield from combos_recur_gen(arr[i + 1:], carry + (v,))


def t():
    print('\n'.join(''.join(c) for c in combos_recur_gen(arr=list('1234'))))


t()
