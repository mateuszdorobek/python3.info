"""
* Assignment: Generator Function Range
* Complexity: medium
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Write own implementation of a built-in `range()` function
    2. Define function `myrange` with parameters:
        a. parameter `start: int`
        b. parameter `stop: int`
        c. parameter `step: int`
    3. Don't validate arguments and assume, that user will:
        a. always pass valid type of arguments
        b. never give only one argument
        c. arguments will be unsigned
    4. Do not use built-in function `range()`
    5. Run doctests - all must succeed

Polish:
    1. Zaimplementuj własne rozwiązanie wbudowanej funkcji `range()`
    2. Zdefiniuj funkcję `myrange` z parametrami:
        a. parameter `start: int`
        b. parameter `stop: int`
        c. parameter `step: int`
    3. Nie waliduj argumentów i przyjmij, że użytkownik:
        a. zawsze poda argumenty poprawnych typów
        b. nigdy nie poda tylko jednego argumentu
        c. argumenty będą nieujemne
    4. Nie używaj wbudowanej funkcji `range()`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * https://github.com/python/cpython/blob/main/Objects/rangeobject.c

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction, isgenerator, isgeneratorfunction
    >>> assert isfunction(myrange)
    >>> assert isgeneratorfunction(myrange)
    >>> assert isgenerator(myrange())

    >>> list(myrange(0, 10, 2))
    [0, 2, 4, 6, 8]

    >>> list(myrange(0, 5))
    [0, 1, 2, 3, 4]
"""

# Write own implementation of a built-in `range()` function
# Define function `myrange` with parameters: `start`, `stop`, `step`
# type: Callable[[int,int,int], list[int]]
def myrange():
    ...


# Solution
def myrange(start=0, stop=None, step=1):
    current = start
    while current < stop:
        yield current
        current += step
