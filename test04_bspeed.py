from collections import namedtuple
from math import sqrt

Point = namedtuple("Point", ["x", "y"])


def list_2_Points(lista: list) -> list[Point]:
    """Transform list of x,y values into a list of Points

    Args:
        lista: Array of points
            [(1,2),(2,7),...,(2,-6)]
    """
    newval = []
    for i in lista:
        #if not isinstance(i[0], int) or not isinstance(i[1], int):
        #    raise ValueError(f"x and y must be integers but you give ({i[0],i[1]})")
        p = Point(*i)
        newval.append(p)
    return newval


def distance(a: Point, b: Point) -> float:
    """Computes the euclidian distance  between two points"""
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def solution(p):
    if len(p) < 2 or len(p) > 2 * 10_000:
        raise ValueError(f"List length not allowed {len(p)}")
    assert all([len(i) == 2 for i in p])
    assert all([i <=1e7 and j <=1e7 for (i,j) in p])
    newpoints = list_2_Points(p)
    # iterating over all points by pairs
    k = 0
    currdis = []
    while len(newpoints) > 1:
        p1 = newpoints.pop()
        for p2 in newpoints:
            currdis.append(distance(p1, p2))
    return min(currdis)

print(solution([(1,2),(3,2)]))
