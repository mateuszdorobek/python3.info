"""
* Assignment: Exception Raise Many
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. Validate value passed to a `result` function
    2. If `value` is:
        a. other type than `int` or `float` raise `TypeError`
        b. less than zero, raise `ValueError`
        c. below `ADULT`, raise `PermissionError`
    3. Non-functional requirements:
        a. Write solution inside `result` function
        b. Mind the indentation level
    4. Run doctests - all must succeed

Polish:
    1. Sprawdź poprawność wartości przekazanej do funckji `result`
    2. Jeżeli `age` jest:
        a. innego typu niż `int` lub `float`, podnieś wyjątek `TypeError`
        b. mniejsze niż zero, podnieś wyjątek `ValueError`
        c. mniejsze niż `ADULT`, podnieś wyjątek `PermissionError`
    3. Wymagania niefunkcjonalne:
        a. Rozwiązanie zapisz wewnątrz funkcji `result`
        b. Zwróć uwagę na poziom wcięć
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `not in`
    * `raise`
    * `if`
    * `isinstance()`
    * `type()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result(18)
    >>> result(17.9999)
    Traceback (most recent call last):
    PermissionError
    >>> result(-1)
    Traceback (most recent call last):
    ValueError
    >>> result('one')
    Traceback (most recent call last):
    TypeError
    >>> result(True)
    Traceback (most recent call last):
    TypeError
"""

ADULT = 18


def result(age):
    ...


# Solution
def result(age):
    if type(age) not in (int, float):
        raise TypeError

    if age < 0:
        raise ValueError

    if age < ADULT:
        raise PermissionError
