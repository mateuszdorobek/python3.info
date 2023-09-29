"""
* Assignment: Idiom Zip Impl
* Complexity: medium
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Write own implementation of a built-in `zip()` function
    2. Define function `myzip` with parameters:
        a. parameter `a: list | tuple`
        b. parameter `b: list | tuple`
        c. parameter `strict: bool`
    3. Don't validate arguments and assume, that user will:
        a. always pass valid type of arguments
        b. iterable length will always be greater than 0
        c. user can only pass two iterables: `a`, `b`
    4. Do not use built-in function `zip()`
    5. Run doctests - all must succeed

Polish:
    1. Zaimplementuj własne rozwiązanie wbudowanej funkcji `zip()`
    2. Zdefiniuj funkcję `myzip` z parametrami:
        a. parametr `a: list | tuple`
        b. parametr `b: list | tuple`
        c. parametr `strict: bool`
    3. Nie waliduj argumentów i przyjmij, że użytkownik:
        a. zawsze poda argumenty poprawnych typów
        b. długość iterable będzie większa od 0
        c. użytkownik może podać tylko dwie iterable: `a`, `b`
    4. Nie używaj wbudowanej funkcji `zip()`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction
    >>> assert isfunction(myzip)

    >>> list(myzip(['a', 'b', 'c'], [1, 2, 3]))
    [('a', 1), ('b', 2), ('c', 3)]

    >>> dict(myzip(['a', 'b', 'c'], [1, 2, 3]))
    {'a': 1, 'b': 2, 'c': 3}

    >>> dict(myzip(['a', 'b', 'c'], [1, 2, 3, 4]))
    {'a': 1, 'b': 2, 'c': 3}

    >>> dict(myzip(['a', 'b', 'c'], [1, 2, 3], strict=True))
    {'a': 1, 'b': 2, 'c': 3}

    >>> dict(myzip(['a', 'b', 'c'], [1, 2, 3, 4], strict=True))
    Traceback (most recent call last):
    ValueError: zip() argument 2 is longer than argument 1
"""

# Write own implementation of a built-in `zip()` function
# Define function `myrange` with parameters: `a`, `b`, `strict`
# type: Callable[[Iterable, Iterable, bool], list[tuple]]
def myzip(a, b, strict=False):
    ...


# Solution
def myzip(a, b, strict=False):
    times = min([len(a), len(b)])
    result = []

    if strict and len(a) != len(b):
        raise ValueError('zip() argument 2 is longer than argument 1')

    for i in range(times):
        row = (a[i], b[i])
        result.append(row)

    return result
