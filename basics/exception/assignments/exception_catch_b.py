"""
* Assignment: Exception Catch Else
* Status: required
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Convert value passed to the `check` function as a `float`
    2. If conversion fails, raise `TypeError`
    3. If value is below AGE, raise `PermissionError`
    4. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    5. Run doctests - all must succeed

Polish:
    1. Przekonwertuj wartośc przekazaną do funckji `check` jako `float`
    2. Jeżeli konwersja się nie powiedzie, podnieś `TypeError`
    3. Jeżeli wartość jest poniżej AGE, podnieś `PermissionError`
    4. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> check(21)
    >>> check('one')
    Traceback (most recent call last):
    TypeError
    >>> check(1)
    Traceback (most recent call last):
    PermissionError
"""

ADULT = 18


def check(age):
    ...


# Solution
def check(age):
    try:
        age = float(age)
    except Exception:
        raise TypeError
    else:
        if age < ADULT:
            raise PermissionError
