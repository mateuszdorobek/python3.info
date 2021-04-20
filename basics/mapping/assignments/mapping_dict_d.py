"""
* Assignment: Mapping Dict Translate
* Status: optional
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Ask user to input single letter
    2. Convert to lowercase
    3. If letter is in `PL` then use conversion value as letter
    4. `MagicMock` will simulate inputting of a letter by user
    5. Use `input()` function as normal
    X. Run doctests - all must succeed

Polish:
    1. Poproś użytkownika o wprowadzenie jednej litery
    2. Przekonwertuj literę na małą
    3. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera
    4. `MagicMock` zasymuluje wpisanie litery przez użytkownika
    5. Skorzytaj z funkcji `input()` tak jak normalnie
    X. Uruchom doctesty - wszystkie muszą się powieść

Example:
    | Input | Output |
    |-------|--------|
    |   A   |    a   |
    |   x   |    x   |
    |   ś   |    s   |
    |   Ź   |    z   |

Tests:
    >>> type(result)
    <class 'str'>
    >>> result not in PL.keys()
    True
    >>> import string
    >>> result in string.ascii_letters
    True
"""

# `MagicMock` will simulate inputting of a letter by user
from unittest.mock import MagicMock
input = MagicMock(return_value='ł')


PL = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ż': 'z',
    'ź': 'z',
}

letter = ...  # str: with letter from user
result = ...  # str: with converted letter without PL diacritic chars


# Solution
letter = input('Type letter: ').strip().lower()
result = PL.get(letter, letter)

