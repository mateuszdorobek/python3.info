"""
* Assignment: Type Float Volume
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Bottle volume is 20 Fl Oz
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Run doctests - all must succeed

Polish:
    1. Objętość butelki wynosi 20 Fl Oz
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert volume is not Ellipsis, \
    'Assign your result to variable `volume`'
    >>> assert volume_floz is not Ellipsis, \
    'Assign your result to variable `volume_floz`'
    >>> assert volume_l is not Ellipsis, \
    'Assign your result to variable `volume_l`'
    >>> assert type(volume) is float, \
    'Variable `volume` has invalid type, should be float'
    >>> assert type(volume_floz) is float, \
    'Variable `volume_floz` has invalid type, should be float'
    >>> assert type(volume_l) is float, \
    'Variable `volume_l` has invalid type, should be float'

    >>> volume_floz
    20.0
    >>> volume_l
    0.5914688
"""

liter = 1
floz = 0.02957344 * liter

# 20 Fl Oz
# type: float
volume = ...

# Volume in fluid ounces
# type: float
volume_floz = ...

# Volume in liters
# type: float
volume_l = ...

# Solution
volume = 20 * floz
volume_floz = volume / floz
volume_l = volume / liter
