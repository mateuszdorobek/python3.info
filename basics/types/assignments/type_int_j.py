"""
* Assignment: Type Int Mul
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Calculate altitude in meters:
        a. Armstrong Limit: 19 km
        b. Stratosphere: 20 km
        c. USAF Space Line: 80 km
        d. IAF Space Line: 100 km
    2. Run doctests - all must succeed

Polish:
    1. Oblicz wysokości w metrach:
        a. Linia Armstronga: 19 km
        b. Stratosfera: 20 km
        c. Granica kosmosu wg. USAF: 80 km
        d. Granica kosmosu wg. IAF 100 km
    2. Uruchom doctesty - wszystkie muszą się powieść

References:
    * USAF - United States Air Force
    * IAF - International Astronautical Federation
    * Kármán line (100 km) - boundary between Earth's atmosphere and space
    * Armstrong limit (19 km) - altitude above which atmospheric pressure is
      sufficiently low that water boils at the temperature of the human body

Hints:
    * 1 km = 1000 m
    * Use // to get floor division as int

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert armstrong_limit is not Ellipsis, \
    'Assign your result to variable `armstrong_limit`'
    >>> assert stratosphere is not Ellipsis, \
    'Assign your result to variable `stratosphere`'
    >>> assert usaf_space is not Ellipsis, \
    'Assign your result to variable `usaf_space`'
    >>> assert iaf_space is not Ellipsis, \
    'Assign your result to variable `iaf_space`'
    >>> assert type(armstrong_limit) is int, \
    'Variable `armstrong_limit` has invalid type, should be int'
    >>> assert type(stratosphere) is int, \
    'Variable `stratosphere` has invalid type, should be int'
    >>> assert type(usaf_space) is int, \
    'Variable `usaf_space` has invalid type, should be int'
    >>> assert type(iaf_space) is int, \
    'Variable `iaf_space` has invalid type, should be int'

    >>> assert armstrong_limit == 19_000, \
    'Invalid value for `armstrong_limit`. Check you calculation'
    >>> assert stratosphere == 20_000, \
    'Invalid value for `stratosphere`. Check you calculation'
    >>> assert usaf_space == 80_000, \
    'Invalid value for `usaf_space`. Check you calculation'
    >>> assert iaf_space == 100_000, \
    'Invalid value for `iaf_space`. Check you calculation'
"""

m = 1
km = 1000 * m

ARMSTRONG_LIMIT = 19*km
STRATOSPHERE = 20*km
USAF_SPACE = 80*km
IAF_SPACE = 100*km


# Armstrong line: 19 kilometers in meters
# type: int
armstrong_limit = ...

# Stratosphere: 20 kilometers in meters
# type: int
stratosphere = ...

# USAF space line: 80 kilometers in meters
# type: int
usaf_space = ...

# IAF space line: 100 kilometers in meters
# type: int
iaf_space = ...

# Solution
armstrong_limit = ARMSTRONG_LIMIT // m
stratosphere = STRATOSPHERE // m
usaf_space = USAF_SPACE // m
iaf_space = IAF_SPACE // m
