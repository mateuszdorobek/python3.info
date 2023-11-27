"""
* Assignment: String Input Prompt
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Ask user to input text `NASA`
    2. Define `result: str` with text from user
    3. `MagicMock` will simulate inputting of `NASA` by user
    4. Use `input()` function as normal
    5. Run doctests - all must succeed

Polish:
    1. Poproś użytkownika o wprowadzenie tekstu `NASA`
    2. Zdefiniuj `result: str` z tekstem wprowadzonym od użytkownika
    3. `MagicMock` zasymuluje wpisanie `NASA` przez użytkownika
    4. Skorzytaj z funkcji `input()` tak jak normalnie
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'
    >>> assert input.call_count == 1, \
    'Call `input()` function'
    >>> assert 'NASA' in input.call_args.args[0], \
    'Ask user to input `NASA`'

    >>> result
    'NASA'
"""

from unittest.mock import MagicMock


# Simulate user input (for test automation)
input = MagicMock(side_effect=['NASA'])

# Ask user to type NASA
# type: str
result = ...

# Solution
result = input('Type NASA: ')
