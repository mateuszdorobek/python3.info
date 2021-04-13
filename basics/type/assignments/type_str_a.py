"""
* Assignment: Type String Input
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Ask user to input text `NASA` (case sensitive)
    2. Define `result` with text from user

Polish:
    1. Poproś użytkownika o wprowadzenie tekstu `NASA` (wielkość liter ma znaczenie)
    2. Zdefiniuj `result` z tekstem wprowadzonym od użytkownika

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is str, 'Variable `result` has invalid type, should be str'

    >>> result
    'NASA'
"""

# Mock input() built-in function
from unittest.mock import MagicMock
input = MagicMock(return_value='NASA')

# Given
result = ...  # str: Type NASA

# Solution
result = input('Type NASA: ')
