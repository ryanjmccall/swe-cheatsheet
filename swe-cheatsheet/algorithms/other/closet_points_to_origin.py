from heapq import nsmallest


def closest_points(points, k: int):
    return nsmallest(k, points, key=lambda p: _dist_to_origin(p))  # O(n) + O(k * log(n))

def closest_points_2(points, k):
    return sorted(points, key=lambda p: _dist_to_origin(p))[:k]  # O(n * log(n))


def _dist_to_origin(point) -> float:
    x, y = point
    return x * x + y * y


def test():
    points = [(9, 7), (1, 1), (3, 2), (-1, -1), (4, 1)]
    print(closest_points(points, k=3))
    print(closest_points_2(points, k=3))


test()
