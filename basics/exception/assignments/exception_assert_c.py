"""
* Assignment: Exception Assert Len
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Check value passed to a `check` function:
        a. assert that argument `data` has length of 3
        b. if not, raise assertion error
    2. Non-functional requirements:
        a. Write solution inside `check` function
        b. Mind the indentation level
        c. Use `assert` kyword
    3. Run doctests - all must succeed

Polish:
    1. Sprawdź poprawność wartości przekazanej do funckji `check`:
        a. zapewnij, że argument `data` ma długość 3
        b. jeżeli nie, podnieś błąd asercji
    2. Wymagania niefunkcjonalne:
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
        c. Użyj słowa kluczowego `assert`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `assert`
    * `len()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> check([1, 2, 3, 4, 5])
    Traceback (most recent call last):
    AssertionError
    >>> check([1, 2, 3, 4])
    Traceback (most recent call last):
    AssertionError
    >>> check([1, 2, 3])
    >>> check([1, 2])
    Traceback (most recent call last):
    AssertionError
    >>> check([1])
    Traceback (most recent call last):
    AssertionError
    >>> check([])
    Traceback (most recent call last):
    AssertionError
"""

def check(data):
    ...


# Solution
def check(data):
    assert len(data) == 3
