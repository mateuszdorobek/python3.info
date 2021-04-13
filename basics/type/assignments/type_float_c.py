"""
* Assignment: Type Float Volume
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Bottle volume is 20 Fl Oz
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Compare result with "Tests" section (see below)

Polish:
    1. Objętość butelki wynosi 20 Fl Oz
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert volume is not Ellipsis, 'Assignment solution must be in `volume` instead of ... (Ellipsis)'
    >>> assert volume_floz is not Ellipsis, 'Assignment solution must be in `volume_floz` instead of ... (Ellipsis)'
    >>> assert volume_l is not Ellipsis, 'Assignment solution must be in `volume_l` instead of ... (Ellipsis)'
    >>> assert type(volume) is float, 'Variable `volume` has invalid type, should be float'
    >>> assert type(volume_floz) is float, 'Variable `volume_floz` has invalid type, should be float'
    >>> assert type(volume_l) is float, 'Variable `volume_l` has invalid type, should be float'

    >>> volume_floz
    20.0
    >>> volume_l
    0.5914688
"""

# Given
liter = 1
floz = 0.02957344 * liter

volume = ...  # float: 20 Fl Oz
volume_floz = ...  # float: volume in fluid ounces
volume_l = ...  # float: volume in liters

# Solution
volume = 20 * floz
volume_floz = volume / floz
volume_l = volume / liter
