"""
* Assignment: Numpy Algebra Euclidean 2D
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Given are two points `a: tuple[int, int]` and `b: tuple[int, int]`
    2. Coordinates are in cartesian system
    3. Points `a` and `b` are in two dimensional space
    4. Calculate distance between points using Euclidean algorithm
    5. Run doctests - all must succeed

Polish:
    1. Dane są dwa punkty `a: tuple[int, int]` i `b: tuple[int, int]`
    2. Koordynaty są w systemie kartezjańskim
    3. Punkty `a` i `b` są w dwuwymiarowej przestrzeni
    4. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result((0,0), (0,0)) is not Ellipsis, \
    'Assign result to function: `euclidean_distance`'

    >>> a = (1, 0)
    >>> b = (0, 1)
    >>> result(a, b)
    1.4142135623730951

    >>> result((0,0), (1,0))
    1.0

    >>> result((0,0), (1,1))
    1.4142135623730951

    >>> result((0,1), (1,1))
    1.0

    >>> result((0,10), (1,1))
    9.055385138137417
"""

from math import sqrt


# Calculate distance between points using Euclidean algorithm
# type: point = tuple[int,int]
# type: Callable[[point, point], point]
def result(a, b):
    ...


# Solution
def result(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    return sqrt((x2-x1)**2 + (y2-y1)**2)
