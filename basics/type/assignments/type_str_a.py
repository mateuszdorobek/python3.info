"""
* Assignment: Type String Input
* Status: required
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Ask user to input text `NASA`
    2. Define `result` with text from user
    3. `MagicMock` will simulate inputing of `NASA` by user
    4. Use `input()` function as normal

Polish:
    1. Poproś użytkownika o wprowadzenie tekstu `NASA`
    2. Zdefiniuj `result` z tekstem wprowadzonym od użytkownika
    3. `MagicMock` zasymuluje wpisanie `NASA` przez użytkownika
    4. Skorzytaj z funkcji `input()` tak jak normalnie

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is str, 'Variable `result` has invalid type, should be str'
    >>> assert input.call_count == 1, 'Call `input()` function'
    >>> assert 'NASA' in input.call_args.args[0], 'Ask user to input `NASA`'

    >>> result
    'NASA'
"""

# Mock input() built-in function
from unittest.mock import MagicMock
input = MagicMock(return_value='NASA')

# Given
result = input('Type NASA: ')  # str: Type NASA
