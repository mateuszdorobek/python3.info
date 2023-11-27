"""
* Assignment: Exception Assert Version
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Check value passed to a `result` function:
        a. Check if `version` is greater or equal to `REQUIRED_VERSION`
        b. If not, raise exception with message 'Python 3.10+ required'
    2. Non-functional requirements:
        a. Write solution inside `result` function
        b. Mind the indentation level
        c. Use `assert` kyword
    3. Run doctests - all must succeed

Polish:
    1. Sprawdź poprawność wartości przekazanej do funckji `result`:
        a. Sprawdź czy `version` jest większe lub równe `REQUIRED_VERSION`
        b. Jeżeli nie, podnieś wyjątek z komunikatem 'Python 3.10+ required'
    2. Wymagania niefunkcjonalne:
        a. Rozwiązanie zapisz wewnątrz funkcji `result`
        b. Zwróć uwagę na poziom wcięć
        c. Użyj słowa kluczowego `assert`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `assert`
    * `>=`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result( (3,9,0) )
    Traceback (most recent call last):
    AssertionError: Python 3.10+ required
    >>> result( (3,9,12) )
    Traceback (most recent call last):
    AssertionError: Python 3.10+ required
    >>> result( (3,10) )
    >>> result( (3,10,0) )
    >>> result( (3,10,1) )
    >>> result( (3,11) )
    >>> result( (3,12) )
"""

REQUIRED_VERSION = (3, 10)


def result(version):
    ...


# Solution
def result(version):
    assert version >= REQUIRED_VERSION, 'Python 3.10+ required'
