"""
* Assignment: Type Int Add
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    2. Zero Celsius degrees is equal to 273.15 Kelvins
    3. For calculation use round number 273 (0°C = 273K)
    4. How many Kelvins has average temperatures at surface [1]:
        a. Mars highest: 20 °C
        b. Mars lowest: -153 °C
        c. Mars average: −63 °C
    5. Run doctests - all must succeed

Polish:
    1. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    2. Zero stopni Celsiusza to 273.15 Kelwiny
    3. W zadaniu przyjmij równe 273°C (0°C = 273K)
    4. Ile Kelwinów wynoszą średnie temperatury powierzchni [1]:
        a. Mars najwyższa: 20 °C
        b. Mars najniższa: -153 °C
        c. Mars średnia: −63 °C
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

    >>> assert mars_highest is not Ellipsis, \
    'Assign your result to variable `mars_highest`'
    >>> assert mars_lowest is not Ellipsis, \
    'Assign your result to variable `mars_lowest`'
    >>> assert mars_lowest is not Ellipsis, \
    'Assign your result to variable `mars_lowest`'
    >>> assert type(mars_highest) is int, \
    'Variable `mars_highest` has invalid type, should be int'
    >>> assert type(mars_lowest) is int, \
    'Variable `mars_lowest` has invalid type, should be int'
    >>> assert type(mars_lowest) is int, \
    'Variable `mars_average` has invalid type, should be int'

    >>> assert mars_highest == 293, \
    'Invalid value for `mars_highest`, should be 293. Check you calculation'
    >>> assert mars_lowest == 120, \
    'Invalid value for `mars_lowest`, should be 120. Check you calculation'
    >>> assert mars_average == 210, \
    'Invalid value for `mars_average`, should be 210. Check you calculation'

"""

Celsius = 1
Kelvin = 273

MARS_HIGHEST = 20*Celsius
MARS_LOWEST = -153*Celsius
MARS_AVERAGE = -63*Celsius


# Martian highest temperature: 20 Celsius in Kelvin
# type: int
mars_highest = ...

# Martian lowest temperature: -153 Celsius in Kelvin
# type: int
mars_lowest = ...

# Martian average temperature: -63 Celsius in Kelvin
# type: int
mars_average = ...

# Solution
mars_highest = MARS_HIGHEST + Kelvin
mars_lowest = MARS_LOWEST + Kelvin
mars_average = MARS_AVERAGE + Kelvin
