"""
* Assignment: Exception Custom Exception
* Required: no
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define custom exception `NegativeKelvinError`
    2. Check value `value` passed to a `result` function
    3. If `value` is lower than 0, raise `NegativeKelvinError`
    4. Non-functional requirements:
        a. Write solution inside `result` function
        b. Mind the indentation level
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj własny wyjątek `NegativeKelvinError`
    2. Sprawdź wartość `value` przekazaną do funckji `result`
    3. Jeżeli `value` jest mniejsze niż 0, podnieś `NegativeKelvinError`
    4. Wymagania niefunkcjonalne:
        a. Rozwiązanie zapisz wewnątrz funkcji `result`
        b. Zwróć uwagę na poziom wcięć
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `class`
    * `pass`
    * `raise`
    * `if`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> isclass(NegativeKelvinError)
    True
    >>> issubclass(NegativeKelvinError, Exception)
    True
    >>> result(1)
    >>> result(0)
    >>> result(-1)
    Traceback (most recent call last):
    exception_custom_a.NegativeKelvinError
"""


def result(value):
    ...


# Solution
class NegativeKelvinError(Exception):
    pass


def result(value):
    if value < 0:
        raise NegativeKelvinError
