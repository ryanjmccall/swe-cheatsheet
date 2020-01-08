
class Repeater:
    def __init__(self, val):
        self.val = val

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.val


def test():
    repeater = Repeater('Hi')
    for i in repeater:
        print(i)

    """
    repeater = Repeater('hi')
    itr = repeater.__iter__()
    while True:
        print(itr.__next__())
    """

def test_two():
    itr = iter(Repeater('fun'))
    for _ in range(4):
        print(next(itr))


# test()
# test_two()

# Itr and next in same class
class BoundedRepeater:
    def __init__(self, val, limit: int):
        self.val = val
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.val


def for_loop():
    itr = iter(BoundedRepeater('hi', 3))
    while True:
        try:
            yield next(itr)
        except StopIteration:
            break


def test_3():
    print(' '.join(BoundedRepeater(val='yeah!', limit=7)))
    print(' '.join(for_loop()))

test_3()

