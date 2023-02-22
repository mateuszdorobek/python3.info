"""
* Assignment: RE Standards IsValidPesel
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Write implementation of `is_pesel_valid`:
       a. Pesel validation using regex is too complex
       b. Use simplified pattern: r'^\d{11}$'
       c. This pattern will allow to avoid 80% of accidental mistakes
    2. Run doctests - all must succeed

Polish:
    1. Napisz implementację `is_pesel_valid`
       a. Walidacja Pesel za pomocą regex jest zbyt skomplikowana
       b. Użyj uproszczonego wzorca: r'^\d{11}$'
       c. Ten wzorzec pozwoli na uniknięcie 80% przypadkowych błędów
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> is_pesel_valid('69072101234')
    True
    >>> is_pesel_valid('18220812345')
    True
"""

import re

PATTERN = r'^\d{11}$'


def is_pesel_valid(pesel: str) -> bool:
    ...


# Solution
def is_pesel_valid(pesel):
    if re.match(PATTERN, pesel):
        return True
    else:
        return False
