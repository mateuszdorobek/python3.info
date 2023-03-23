"""
* Assignment: Mapping Switch Default
* Required: no
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Ask user to input single letter
    2. Convert to lowercase
    3. If letter is in `PL` then use conversion value as letter
    4. `MagicMock` will simulate inputting of a letter by user
    5. Use `input()` function as normal
    6. Run doctests - all must succeed

Polish:
    1. Poproś użytkownika o wprowadzenie jednej litery
    2. Przekonwertuj literę na małą
    3. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera
    4. `MagicMock` zasymuluje wpisanie litery przez użytkownika
    5. Skorzytaj z funkcji `input()` tak jak normalnie
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `input()`
    * `str.lower()`

Example:
    | Input | Output |
    |-------|--------|
    |   a   |    a   |
    |   A   |    a   |
    |   ą   |    a   |
    |   Ą   |    a   |
    |   b   |    b   |
    |   B   |    B   |
    |   c   |    c   |
    |   C   |    c   |
    |   ć   |    c   |
    |   Ć   |    c   |
    |  ...  |   ...  |

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> import string

    >>> assert letter is not Ellipsis, \
    'Ask user to input letter and assign it to: `letter`'

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> assert result not in PL.keys(), \
    'Result should not be in PL dict'

    >>> assert result in string.ascii_letters, \
    'Result should be an ASCII letter'
"""

from unittest.mock import MagicMock


# Simulate user input (for test automation)
input = MagicMock(side_effect=['Ł'])

PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

# String with letter from user
# type: str
letter = ...

# String with converted letter without PL diacritic chars
# type: str
result = ...

# Solution
letter = input('Type letter: ').lower()
result = PL.get(letter, letter)
