def combos_recur_gen(left: list, right: list):
    for i, v in enumerate(right):
        yield left + [v]
        yield from combos_recur_gen(left + [v], right[i + 1:])


def t():
    print('\n'.join(''.join(c) for c in combos_recur_gen(left=[], right=list('1234'))))


t()
