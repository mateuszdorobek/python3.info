"""
* Assignment: Type Int Sub
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    2. Zero Kelvin (absolute) is equal to -273.15 Celsius degrees
    3. For calculation use round number -273 (0K = -273°C)
    4. How many Celsius degrees has average temperatures at surface [1]:
        a. Lunar day: 453 K
        b. Lunar night: 93 K
    5. Run doctests - all must succeed

Polish:
    1. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    2. Zero Kelwina (bezwzględne) to -273.15 stopni Celsiusza
    3. W zadaniu przyjmij równe -273°C (0K = -273°C)
    4. Ile stopni Celsiusza wynoszą średnie temperatury powierzchni [1]:
        a. Księżyca w dzień: 453 K
        b. Księżyca w nocy: 93 K
    5. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * Use only +273 and -273

References:
    [1] Centro de Astrobiología (CSIC-INTA).
        Rover Environmental Monitoring Station, Mars Science Laboratory (NASA).
        Year: 2019.
        Retrieved: 2019-08-06.
        URL: http://cab.inta-csic.es/rems/marsweather.html

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert lunar_day is not Ellipsis, \
    'Assign your result to variable `lunar_day`'
    >>> assert lunar_night is not Ellipsis, \
    'Assign your result to variable `lunar_night`'
    >>> assert type(lunar_day) is int, \
    'Variable `lunar_day` has invalid type, should be int'
    >>> assert type(lunar_night) is int, \
    'Variable `lunar_night` has invalid type, should be int'

    >>> assert lunar_day == 180, \
    'Invalid value for `lunar_day`, should be 180. Check you calculation'
    >>> assert lunar_night == -180, \
    'Invalid value for `lunar_night`, should be -180. Check you calculation'
"""

Celsius = 273
Kelvin = 1

LUNAR_DAY = 453*Kelvin
LUNAR_NIGHT = 93*Kelvin

# Lunar day: 453 Kelvin in Celsius
# type: int
lunar_day = ...

# Lunar night: 93 Kelvin in Celsius
# type: int
lunar_night = ...

# Solution
lunar_day = LUNAR_DAY - Celsius
lunar_night = LUNAR_NIGHT - Celsius
