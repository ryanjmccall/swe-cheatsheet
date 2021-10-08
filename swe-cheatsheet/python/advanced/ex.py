

def comprehension():
    iterable = range(10)
    print([x*x for x in iterable])
    print({x for x in iterable})
    print({str(x): x for x in iterable})
    print((x*x*x for x in iterable))
    print([x for x in iterable if x % 2])
    # multiple
    print([(x, y) for x in range(2) for y in range(3)])
    # nested
    print([[y for y in range(x)] for x in range(1, 5)])
    print()

# comprehension()


from functools import reduce


def hyper_vol(*lengths):
    print(type(lengths))
    print(type(*lengths))
    return reduce(lambda x, y: x * y, *lengths)


def hyper_vol_example():
    print(hyper_vol(range(1, 4)))
    print(hyper_vol([1, 2, 3]))

# hyper_vol_example()


def kwargs(**kwargs):
    print(kwargs)

# kwargs(a='1', b='2')


# Extended actual argument

t = tuple(range(1, 6))


def print_args(a1, a2, *args):
    print(a1, a2, args)


# print_args(*t)


# local function
# Scope resolution via LEGB rule. Lookup order:
# Local: Defined inside function / class
# Enclosed: Defined inside enclosing functions (nested function)
# Global: Defined at topmost level
# Built-in: Reserved names in Python built-in modules

def outer():
    def inner():
        return 'inner'

    return inner


# inner_func = outer()
# assert inner_func() == 'inner'


# closures

def closure(x: int):
    def inner(y: int):
        return x + y

    return inner


# inner_plus_3_func = closure(3)
# assert inner_plus_3_func(2) == 5
# print(inner_plus_3_func.__closure__)

# Decorators

def convert_upper(f):
    # print('convert_upper')

    def wrap(*args, **kwargs):
        print('wrap')
        x = f(*args, **kwargs)
        return x.upper()

    return wrap


@convert_upper
def my_name(name):
    print('my_name')
    return name


# print(my_name('ryanski'))


"""
Iterable protocol

Iterator: object when passed to next() fetches the next item
Iterable: object when passed into iter() returns an Iterator

"""


def iterable_ex():
    iterable = range(1)
    iterator = iter(iterable)
    print(next(iterator))
    try:
        next(iterator)
    except StopIteration:
        print('too much')


# iterable_ex()


"""
Generator is a function that returns an Iterator

If a function contains at least one yield statement it becomes a 
generator function

"""


def my_gen():
    yield 1
    yield 'hi'
    return 'plz stop'


# print([x for x in my_gen()])

# Context manager

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


# with File('demo.txt', 'w') as opened_file:
#     opened_file.write('Hola!')


# Class methods and static methods

class Foobar:
    CLASS_ATTR = 'peanut butter'

    def __init__(self, x):
        self.x = x

    @classmethod
    def get_attr(cls):
        return cls.CLASS_ATTR

    @classmethod
    def random(cls):
        return cls.get_attr()

    def get_x(self):
        return self.x

    @staticmethod
    def borf():
        return 1492


# bar = Foobar('x')
# assert bar.get_attr() == bar.random() == Foobar.get_attr()
# assert bar.get_x() == 'x'
# assert Foobar.borf() == 1492


class BaseClass(object):
    pass


class SubClass(BaseClass):
    pass


def inheritance():
    sub = SubClass()
    assert isinstance(sub, BaseClass)
    assert isinstance(sub, SubClass)
    assert issubclass(SubClass, BaseClass)
    assert not issubclass(BaseClass, SubClass)


# inheritance()


class Base1(object):
    pass


class Base2(object):
    pass


class Multiple(Base1, Base2):
    pass


assert Multiple.__bases__ == (Base1, Base2)
assert Multiple.__mro__ == (Multiple, Base1, Base2, object)


# Property decorator

class Example:

    def __init__(self):
        self._p = None  # _X means do not access

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, v):
        self._p = v


example = Example()
assert not example.p
example.p = 42
assert example.p == 42


# Operator overloading

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


# p1 = Point(2, 3)
# p2 = Point(-1, 2)
# print(p1 + p2)