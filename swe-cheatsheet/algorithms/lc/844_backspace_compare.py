from functools import reduce


def backspaceCompare(a, b):
    def f(result: list, char: str):
        if char != '#':
            result.append(char)

        elif result:
            result.pop()

        return result

    # reduce(function, sequence, initial)
    return reduce(f, a, []) == reduce(f, b, [])


print(backspaceCompare("a#t", "b#t"))



