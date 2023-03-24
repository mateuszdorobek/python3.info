"""
* Assignment: Exception Custom Exception
* Required: no
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define custom exception `IsDead`
    2. Check value `health` passed to a `hero` function
    3. If `health` is lower than 0, raise `IsDead`
    4. Non-functional requirements:
        a. Write solution inside `hero` function
        b. Mind the indentation level
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj własny wyjątek `IsDead`
    2. Sprawdź wartość `health` przekazaną do funckji `hero`
    3. Jeżeli `health` jest mniejsza niż 0, podnieś `IsDead`
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

    >>> isclass(IsDead)
    True
    >>> issubclass(IsDead, Exception)
    True
    >>> hero(1)
    >>> hero(0)
    >>> hero(-1)
    Traceback (most recent call last):
    exception_custom_b.IsDead
"""


def hero(health):
    ...


# Solution
class IsDead(Exception):
    pass


def hero(health):
    if health < 0:
        raise IsDead
