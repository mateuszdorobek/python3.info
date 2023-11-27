"""
* Assignment: Exception Catch Except
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Convert value passed to the `result` function as a `float`
    2. If conversion fails then print 'Invalid value'
    3. Non-functional requirements:
        a. Write solution inside `result` function
        b. Mind the indentation level
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj wartośc przekazaną do funckji `result` jako `float`
    2. Jeżeli konwersja się nie powiedzie to wypisz 'Invalid value'
    3. Wymagania niefunkcjonalne:
        a. Rozwiązanie zapisz wewnątrz funkcji `result`
        b. Zwróć uwagę na poziom wcięć
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `try`
    * `except`
    * `print()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result('1')
    >>> result('1.0')
    >>> result('1,0')
    Invalid value
"""


def result(value):
    ...


# Solution
def result(value):
    try:
        float(value)
    except ValueError:
        print('Invalid value')
