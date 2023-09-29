"""
* Assignment: Idiom Reduce Impl
* Complexity: medium
* Lines of code: 4 lines
* Time: 13 min

English:
    1. Write own implementation of a built-in `reduce()` function
    2. Define function `myreduce` with parameters:
        a. parameter `function: Callable`
        b. parameter `iterable: list | tuple`
    3. Don't validate arguments and assume, that user will:
        a. always pass valid type of arguments
        b. iterable length will always be greater than 0
    4. Do not use: map, filter, zip, enumerate, all, any, reduce
    5. Run doctests - all must succeed

Polish:
    1. Zaimplementuj własne rozwiązanie wbudowanej funkcji `reduce()`
    2. Zdefiniuj funkcję `myreduce` z parametrami:
        a. parameter `function: Callable`
        b. parameter `iterable: list | tuple`
    3. Nie waliduj argumentów i przyjmij, że użytkownik:
        a. zawsze poda argumenty poprawnych typów
        b. długość iterable będzie większa od 0
    4. Nie używaj: map, filter, zip, enumerate, all, any, reduce
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction
    >>> from operator import add, mul
    >>> assert isfunction(myreduce)

    >>> myreduce(add, [1, 2, 3, 4, 5])
    15

    >>> myreduce(mul, [1, 2, 3, 4, 5])
    120
"""

# Write own implementation of a built-in `reduce()` function
# Define function `myrange` with parameters: `function`, `iterable`
# type: Callable[[Callable, Iterable], Any]
def myreduce(function, iterable):
    ...


# Solution
def myreduce(function, iterable):
    result = iterable[0]

    for current in iterable[1:]:
        result = function(result, current)

    return result
