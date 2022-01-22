
"""
Python refactoring principles based on the Internet and my own opinions

Do's
- comprehensions > loops
- f-strings unless logging

- multi-assign and tuple unpacking
-- a, b = 1, 2     a, *b, c = stuff

- walrus
-- if account := get_account(...):

- zip, zip_longest
- itertools.chain('ab', 'cd'), itertools.chain.from_iterable(['ab', 'cd'])

- ternary
- generators
- any/all instead of loops
- minimize code in loops
- guard statement / short circuiting to simplify remove else's
- use decorators to replace repeated A-C in A>B>C
- use @dataclass
- extract / hoist repeated statements

Don't's
- use mutable default arguments: a: set = {1, 2, 3}

Refactors
- set of functions > Class    (member, class, static methods)
- object with 1 non-static non-init method > function
- code with lots of nesting
- use jmespath for nested json structures

"""


def zip_(*args):
    iters = [iter(i) for i in args]
    active = len(iters)
    if not active:
        return

    while True:
        vals = []
        for it in iters:
            try:
                vals.append(next(it))
            except StopIteration:
                return

        yield tuple(vals)


print(list(zip_(range(10), range(9))))
