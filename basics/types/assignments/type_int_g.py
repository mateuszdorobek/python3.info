"""
* Assignment: Type Int Sub
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define average temperatures at surface of Moon [1]:
        a. day: 453 K
        b. night: 93 K
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj średnie temperatury powierzchni Księżyca [1]:
        a. dzień: 453 K
        b. noc: 93 K
    2. Uruchom doctesty - wszystkie muszą się powieść

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

    >>> assert lunar_day == 453, \
    'Invalid value for `lunar_day`, should be 453. Check you calculation'
    >>> assert lunar_night == 93, \
    'Invalid value for `lunar_night`, should be 93. Check you calculation'
"""

Kelvin = 1

# Lunar day: 453 Kelvins
# type: int
lunar_day = ...

# Lunar night: 93 Kelvins
# type: int
lunar_night = ...

# Solution
lunar_day = 453*Kelvin
lunar_night = 93*Kelvin
