"""
* Assignment: Exception Assert Types
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Check value passed to a `add_numbers` function:
        a. assert that type of `a` or `b` is int or float
        b. if not, raise assertion error with message:
           'Parameter `a` must be int or float'
    2. Non-functional requirements:
        a. Write solution inside `add_numbers` function
        b. Mind the indentation level
        c. Use `assert` kyword
    3. Run doctests - all must succeed

Polish:
    1. Sprawdź poprawność wartości przekazanej do funckji `add_numbers`:
        a. zapewnij, że typ `a` oraz `b` jest int lub float
        b. jeżeli nie, podnieś błąd asercji z komunikatem:
           'Parameter `a` must be int or float'
    2. Wymagania niefunkcjonalne:
        a. Rozwiązanie zapisz wewnątrz funkcji `add_numbers`
        b. Zwróć uwagę na poziom wcięć
        c. Użyj słowa kluczowego `assert`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `assert`
    * `isinstance()`
    * `type()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> add_numbers(1, 0)
    1
    >>> add_numbers(0, 1)
    1
    >>> add_numbers(1.0, 0)
    1.0
    >>> add_numbers(0, 1.0)
    1.0
    >>> add_numbers('1', 0)
    Traceback (most recent call last):
    AssertionError: Parameter `a` must be int or float
    >>> add_numbers(0, '1')
    Traceback (most recent call last):
    AssertionError: Parameter `b` must be int or float
    >>> add_numbers([1], 0)
    Traceback (most recent call last):
    AssertionError: Parameter `a` must be int or float
    >>> add_numbers(0, [1])
    Traceback (most recent call last):
    AssertionError: Parameter `b` must be int or float
    >>> add_numbers(True, 0)
    Traceback (most recent call last):
    AssertionError: Parameter `a` must be int or float
    >>> add_numbers(0, False)
    Traceback (most recent call last):
    AssertionError: Parameter `b` must be int or float
"""

def add_numbers(a, b):
    return a + b


# Solution
def add_numbers(a, b):
    assert type(a) in (int, float), 'Parameter `a` must be int or float'
    assert type(b) in (int, float), 'Parameter `b` must be int or float'
    return a + b
