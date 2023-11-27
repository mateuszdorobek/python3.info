"""
* Assignment: Type Float Altitude
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Plane altitude is 10.000 ft
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Result round to one decimal place
    5. Run doctests - all must succeed

Polish:
    1. Wysokość lotu samolotem wynosi 10 000 ft
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Wynik zaokrąglij do jednego miejsca po przecinku
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert altitude is not Ellipsis, \
    'Assign your result to variable `altitude`'
    >>> assert altitude_m is not Ellipsis, \
    'Assign your result to variable `altitude_m`'
    >>> assert altitude_ft is not Ellipsis, \
    'Assign your result to variable `altitude_ft`'
    >>> assert type(altitude) is float, \
    'Variable `altitude` has invalid type, should be float'
    >>> assert type(altitude_m) is float, \
    'Variable `altitude_m` has invalid type, should be float'
    >>> assert type(altitude_ft) is float, \
    'Variable `altitude_ft` has invalid type, should be float'

    >>> altitude
    3048.0
    >>> altitude_m
    3048.0
    >>> altitude_ft
    10000.0
"""

m = 1
ft = 0.3048 * m

# 10_000 ft
# type: float
altitude = ...

# Altitude in meters
# type: float
altitude_m = ...

# Altitude in feet
# type: float
altitude_ft = ...

# Solution
altitude = 10_000 * ft
altitude_m = altitude / m
altitude_ft = altitude / ft
