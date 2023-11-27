"""
* Assignment: Type Float Velocity
* Type: class assignment
* Complexity: easy
* Lines of code: 9 lines
* Time: 3 min

English:
    1. Speed limit is 75 MPH
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Speed limit print in KPH (km/h)
    5. Run doctests - all must succeed

Polish:
    1. Ograniczenie prędkości wynosi 75 MPH
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Ograniczenie prędkości wypisz w KPH (km/h)
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert kph is not Ellipsis, \
    'Assign your result to variable `kph`'
    >>> assert mph is not Ellipsis, \
    'Assign your result to variable `mph`'
    >>> assert speed_limit_mph is not Ellipsis, \
    'Assign your result to variable `speed_limit_mph`'
    >>> assert speed_limit_kph is not Ellipsis, \
    'Assign your result to variable `speed_limit_kph`'
    >>> assert type(kph) is float, \
    'Variable `kph` has invalid type, should be float'
    >>> assert type(mph) is float, \
    'Variable `mph` has invalid type, should be float'
    >>> assert type(speed_limit_mph) is float, \
    'Variable `speed_limit_mph` has invalid type, should be float'
    >>> assert type(speed_limit_kph) is float, \
    'Variable `speed_limit_kph` has invalid type, should be float'

    >>> round(kph, 3)
    0.278
    >>> round(mph, 3)
    0.447
    >>> round(speed_limit_mph, 1)
    75.0
    >>> round(speed_limit_kph, 1)
    120.7
"""

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

m = 1
km = 1000 * m
mi = 1609.344 * m

# Miles per hour
# type: float
mph = ...

# Kilometers per hour
# type: float
kph = ...

# 75 miles per hour
# type: float
speed_limit = ...

# Speed limit in miles per hour
# type: float
speed_limit_mph = ...

# Speed limit in kilometers per hour
# type: float
speed_limit_kph = ...

# Solution
kph = km / HOUR
mph = mi / HOUR

speed_limit = 75 * mph

speed_limit_mph = speed_limit / mph
speed_limit_kph = speed_limit / kph
