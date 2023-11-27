"""
* Assignment: Conditional Operator Modulo
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Read a number from user
    2. User will input `int` and will not try to input invalid data
    3. Define `result: bool` with parity check of input number
    4. Number is even, when divided modulo (`%`) by 2 reminder equal to 0
    5. Do not use `if` statement
    6. Run doctests - all must succeed

Polish:
    1. Wczytaj liczbę od użytkownika
    2. Użytkownika poda `int` i nie będzie próbował wprowadzać niepoprawnych danych
    3. Zdefiniuj `result: bool` z wynikiem sprawdzania parzystości liczby wprowadzonej
    4. Liczba jest parzysta, gdy dzielona modulo (`%`) przez 2 ma resztę równą 0
    5. Nie używaj instrukcji `if`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `int()`
    * `%`
    * `==`
    * `%` has different meaning for `int` and `str`
    * `%` on `str` is overloaded as a string formatting
    * `%` on `int` is overloaded as a modulo division

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is bool, \
    'Variable `result` has invalid type, should be bool'

    >>> result
    True
"""

from unittest.mock import MagicMock


# Simulate user input (for test automation)
input = MagicMock(side_effect=['4'])

number = input('What is your number?: ')

# Whether input number is even or odd (modulo divide)
# type: bool
result = ...

# Solution
result = int(number) % 2 == 0
