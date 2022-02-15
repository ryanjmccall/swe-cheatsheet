

class Rectangle(object):
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def area(self):
        if self.xmin > self.xmax:
            return 0
        if self.ymin > self.ymax:
            return 0
        return (self.xmax - self.xmin) * (self.ymax - self.ymin)


def rect_intersection(a: Rectangle, b: Rectangle) -> int:
    return Rectangle(xmin=max(a.xmin, b.xmin),
                     ymin=max(a.ymin, b.ymin),
                     xmax=min(a.xmax, b.xmax),
                     ymax=min(a.ymax, b.ymax))


def main():
    a = Rectangle(0, 0, 3, 2)
    b = Rectangle(1, 1, 3, 3)
    intersect = rect_intersection(a, b)
    print(intersect.area())


main()
