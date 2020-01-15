

class Parent(object):
    x = 1


class ChildA(Parent):
    pass


class ChildB(Parent):
    pass


def test():
    p = Parent()
    a = ChildA()
    b = ChildB()
    print(p.x, a.x, b.x)

    a.x = 2
    print(p.x, a.x, b.x)

    p.x = 3
    print(p.x, a.x, b.x)

    Parent.x = 4
    print(p.x, a.x, b.x)

    Parent.x = 4
    b.x = 5
    print(p.x, a.x, b.x)


test()
