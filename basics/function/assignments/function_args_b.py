"""
* Assignment: Function Arguments Divide
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define function `divide`
    2. Function takes two arguments
    3. Function returns result of the division of both arguments
    4. If division cannot be made, stop function and print:
       "Argument `b` cannot be zero"
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `divide`
    2. Funkcja przyjmuje dwa argumenty
    3. Funkcja zwraca wynik dzielenia dwóch argumentów
    4. Jeżeli nie można podzielić zakończ funkcję i wypisz:
       "Argument `b` cannot be zero"
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert divide is not Ellipsis, \
    'Write solution inside `divide` function'
    >>> assert isfunction(divide), \
    'Object `divide` must be a function'

    >>> divide(4, 0)
    Argument `b` cannot be zero

    >>> divide(4, 2)
    2.0
"""


# Solution
def divide(a, b):
    if b == 0:
        print('Argument `b` cannot be zero')
        return None
    return a / b
