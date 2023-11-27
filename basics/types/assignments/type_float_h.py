"""
* Assignment: Type Float Gradient
* Type: homework
* Complexity: hard
* Lines of code: 7 lines
* Time: 8 min

English:
    1. At what altitude above sea level, pressure is equal
       to partial pressure of Oxygen
    2. Print result in meters rounding to two decimal places
    3. To calculate partial pressure use ratio
       (100% is 1013.25 hPa, 20.946% is how many hPa?)
    4. Calculated altitude is pressure at sea level minus
       oxygen partial pressure divided by gradient
    5. Mind the operator precedence
    6. Run doctests - all must succeed

Polish:
    1. Na jakiej wysokości nad poziomem morza panuje ciśnienie
       równe ciśnieniu parcjalnemu tlenu?
    2. Wypisz rezultat w metrach zaokrąglając do dwóch miejsc po przecinku
    3. Aby policzyć ciśnienie parcjalne skorzystaj z proporcji
       (100% to 1013.25 hPa, 20.946% to ile hPa?)
    4. Wyliczona wysokość to ciśnienie atmosferyczne na poziomie morza minus
       ciśnienie parcjalne tlenu podzielone przez gradient
    5. Zwróć uwagę na kolejność wykonywania działań
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * pressure gradient (decrease) = 11.3 Pa / 1 m
    * 1 hPa = 100 Pa
    * 1 kPa = 1000 Pa
    * 1 ata = 1013.25 hPa (ISA - International Standard Atmosphere)
    * Atmosphere gas composition:

        * Nitrogen 78.084%
        * Oxygen 20.946%
        * Argon 0.9340%
        * Carbon Dioxide 0.0407%
        * Others 0.001%

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert pO2 is not Ellipsis, \
    'Assign your result to variable `pO2`'
    >>> assert gradient is not Ellipsis, \
    'Assign your result to variable `gradient`'
    >>> assert altitude is not Ellipsis, \
    'Assign your result to variable `altitude`'
    >>> assert type(pO2) is float, \
    'Variable `pO2` has invalid type, should be float'
    >>> assert type(gradient) is float, \
    'Variable `gradient` has invalid type, should be float'
    >>> assert type(altitude) is float, \
    'Variable `altitude` has invalid type, should be float'

    >>> pO2
    21223.5345
    >>> gradient
    11.3
    >>> round(altitude/m, 2)
    7088.63
"""

PERCENT = 100
N2 = 78.084 / PERCENT
O2 = 20.946 / PERCENT
Ar = 0.9340 / PERCENT
CO2 = 0.0407 / PERCENT
Others = 0.001 / PERCENT

m = 1
Pa = 1
hPa = 100 * Pa
ata = 1013.25 * hPa
pO2 = O2 * ata

# 11.3 Pascals per meter
# type: float
gradient = ...

# Altitude is ata minus pO2 all that divided by gradient
# type: float
altitude = ...

# Solution
gradient = 11.3 * Pa / m
altitude = (ata - pO2) / gradient
