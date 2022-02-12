from typing import List


DIGITS = {str(x) for x in range(10)}


OPERATORS = {'+', '-', '/', '*'}


def calc(ops: List[str]) -> int:
    stk = []
    for op in ops:
        if op in DIGITS:
            stk.append(int(op))
        elif op in OPERATORS:
            prev = stk.pop()
            if op == '+':
                stk[-1] += prev
            elif op == '-':
                stk[-1] -= prev
            elif op == '*':
                stk[-1] *= prev
            else:
                stk[-1] /= prev
        else:
            raise ValueError('bad op ' + op)

    return stk[0]


print(calc(list('123+2*-')))
