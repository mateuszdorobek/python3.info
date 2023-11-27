"""
* Assignment: Type Int Truediv
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Define variable in meters:
        a. Kármán Line Earth: 100_000 m
        b. Kármán Line Mars: 80_000 m
        c. Kármán Line Venus: 250_000 m
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne w metrach:
        a. Linia Kármána Ziemia: 100_000 m
        b. Linia Kármána Mars: 80_000 m
        c. Linia Kármána Wenus: 250_000 m
    2. Uruchom doctesty - wszystkie muszą się powieść

References:
    * Kármán line (100 km) - boundary between planets's atmosphere and space

Hints:
    * 1 km = 1000 m

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert karman_line_earth is not Ellipsis, \
    'Assign your result to variable `karman_line_earth`'
    >>> assert karman_line_mars is not Ellipsis, \
    'Assign your result to variable `karman_line_mars`'
    >>> assert karman_line_venus is not Ellipsis, \
    'Assign your result to variable `karman_line_venus`'
    >>> assert type(karman_line_earth) is int, \
    'Variable `karman_line_earth` has invalid type, should be int'
    >>> assert type(karman_line_mars) is int, \
    'Variable `karman_line_mars` has invalid type, should be int'
    >>> assert type(karman_line_venus) is int, \
    'Variable `karman_line_venus` has invalid type, should be int'

    >>> assert karman_line_earth == 100_000, \
    'Invalid value for `karman_line_earth`. Check you calculation'
    >>> assert karman_line_mars == 80_000, \
    'Invalid value for `karman_line_mars`. Check you calculation'
    >>> assert karman_line_venus == 250_000, \
    'Invalid value for `usaf_space`. Check you calculation'
"""

m = 1
km = 1000 * m

# Kármán Line Earth: 100_000 meters
# type: int
karman_line_earth = ...

# Kármán Line Mars: 80_000 meters
# type: int
karman_line_mars = ...

# Kármán Line Venus: 250_000 meters
# type: int
karman_line_venus = ...

# Solution
karman_line_earth = 100_000*m
karman_line_mars = 80_000*m
karman_line_venus = 250_000*m
