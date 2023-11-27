"""
* Assignment: Function Return Locals
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define function `result`
    2. Inside function define variable `a: int` with value 1
    3. Inside function define variable `b: int` with value 2
    4. Return `dict[str,int]` with variable names and its values,
       for example: {'a': 1, 'b': 2}
    5. Use `locals()`
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `result`
    2. Wewnątrz funkcji zdefiniuj zmienną `a: int` z wartością 1
    3. Wewnątrz funkcji zdefiniuj zmienną `b: int` z wartością 2
    4. Zwróć `dict[str,int]` z nazwami zmiennych i ich wartościami,
       przykład: {'a': 1, 'b': 2}
    5. Użyj `locals()`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert result is not Ellipsis, \
    'Write solution inside `result` function'
    >>> assert isfunction(result), \
    'Object `result` must be a function'

    >>> result()
    {'a': 1, 'b': 2}
"""


# Solution
def result():
    a = 1
    b = 2
    return locals()
