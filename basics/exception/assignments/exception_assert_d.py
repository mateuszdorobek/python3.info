"""
* Assignment: Exception Assert Set
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Check value passed to a `check` function:
        a. assert that `data: set` contains numbers: 1, 2 and 3
        b. if not, raise assertion error
    2. Non-functional requirements:
        a. Write solution inside `check` function
        b. Mind the indentation level
        c. Use `assert` kyword
    3. Run doctests - all must succeed

Polish:
    1. Sprawdź poprawność wartości przekazanej do funckji `check`:
        a. zapewnij, że `data: set` ma liczby: 1, 2 i 3
        b. jeżeli nie, podnieś błąd asercji
    2. Wymagania niefunkcjonalne:
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
        c. Użyj słowa kluczowego `assert`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `assert`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> check({1, 2, 3, 4, 5})
    Traceback (most recent call last):
    AssertionError
    >>> check({1, 2, 3, 4})
    Traceback (most recent call last):
    AssertionError
    >>> check({1, 2, 3})
    >>> check({1, 3, 2})
    >>> check({2, 1, 3})
    >>> check({2, 3, 1})
    >>> check({3, 1, 2})
    >>> check({3, 2, 1})
    >>> check({1, 2})
    Traceback (most recent call last):
    AssertionError
    >>> check({1, 3})
    Traceback (most recent call last):
    AssertionError
    >>> check({2, 1})
    Traceback (most recent call last):
    AssertionError
    >>> check({2, 3})
    Traceback (most recent call last):
    AssertionError
    >>> check({3, 1})
    Traceback (most recent call last):
    AssertionError
    >>> check({3, 2})
    Traceback (most recent call last):
    AssertionError
    >>> check({1})
    Traceback (most recent call last):
    AssertionError
    >>> check({2})
    Traceback (most recent call last):
    AssertionError
    >>> check({3})
    Traceback (most recent call last):
    AssertionError
"""

def check(data):
    ...


# Solution
def check(data):
    assert data == {1, 2, 3}
