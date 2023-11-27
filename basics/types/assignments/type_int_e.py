"""
* Assignment: Type Int Add
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Define average temperatures at surface of Mars [1]:
        a. highest: 20 °C
        b. lowest: -153 °C
        c. average: −63 °C
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj średnie temperatury powierzchni Marsa [1]:
        a. najwyższa: 20 °C
        b. najniższa: -153 °C
        c. średnia: −63 °C
    2. Uruchom doctesty - wszystkie muszą się powieść

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

    >>> assert mars_highest == 20, \
    'Invalid value for `mars_highest`, should be 20. Check you calculation'
    >>> assert mars_lowest == -153, \
    'Invalid value for `mars_lowest`, should be -153. Check you calculation'
    >>> assert mars_average == -63, \
    'Invalid value for `mars_average`, should be -63. Check you calculation'

"""

Celsius = 1

# Martian highest temperature: 20 Celsius
# type: int
mars_highest = ...

# Martian lowest temperature: -153 Celsius
# type: int
mars_lowest = ...

# Martian average temperature: -63 Celsius
# type: int
mars_average = ...

# Solution
mars_highest = 20*Celsius
mars_lowest = -153*Celsius
mars_average = -63*Celsius
