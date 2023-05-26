"""
* Assignment: Idioms Enumerate Impl
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Write own implementation of a built-in `enumerate()` function
    2. Define function `myenumerate` with parameters:
        a. parameter `iterable: list | tuple`
        b. parameter `start: int`
    3. Don't validate arguments and assume, that user will:
        a. always pass valid type of arguments
        b. iterable length will always be greater than 0
    4. Run doctests - all must succeed

Polish:
    1. Zaimplementuj własne rozwiązanie wbudowanej funkcji `enumerate()`
    2. Zdefiniuj funkcję `myenumerate` z parametrami:
        a. parametr `iterable: list | tuple`
        b. parametr `start: int`
    3. Nie waliduj argumentów i przyjmij, że użytkownik:
        a. zawsze poda argumenty poprawnych typów
        b. długość iterable będzie większa od 0
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * https://github.com/python/cpython/blob/main/Objects/enumobject.c

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(myenumerate)

    >>> months = ['January', 'February', 'March']
    >>> myenumerate(months)
    [(0, 'January'), (1, 'February'), (2, 'March')]

    >>> months = ['January', 'February', 'March']
    >>> myenumerate(months, start=1)
    [(1, 'January'), (2, 'February'), (3, 'March')]

    >>> months = ['January', 'February', 'March']
    >>> dict(myenumerate(months, start=1))
    {1: 'January', 2: 'February', 3: 'March'}
"""

# Define function `myrange` with parameters: `start`, `stop`, `step`
# Write own implementation of a built-in `range()` function
# type: Callable[[Iterable, int], list[tuple]]
def myenumerate(iterable, start=0):
    ...


# Solution
def myenumerate(iterable, start=0):
    current = start
    result = []

    for i in range(len(iterable)):
        row = (current, iterable[i])
        result.append(row)
        current += 1

    return result
