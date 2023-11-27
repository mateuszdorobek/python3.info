"""
* Assignment: Conditional If Underage/Adult
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Ask user to input age
    2. Check whether user is adult (age equals or above 18)
    3. Run doctests - all must succeed

Polish:
    1. Poproś użytkownika o wprowadzenie wieku
    2. Sprawdź czy użytkownik jest pełnoletni (wiek równy lub powyżej 18)
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `int()`
    * `>=`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result in ('Adult', 'Young')
    True
"""

# Simulate user input (for test automation)
from unittest.mock import MagicMock
input = MagicMock(side_effect=['30'])


age = input('What is your age?: ')
ADULT = 18

# Whether 'Adult' or 'Young'
# type: str
result = ...

# Solution
if int(age) >= ADULT:
    result = 'Adult'
else:
    result = 'Young'
