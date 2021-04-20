"""
* Assignment: Function Return Numbers
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Define function `compute` without parameters
    2. Function should return sum of `1` and `2`
    3. Define `result` with result of function call
    X. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `compute` bez parametrów
    2. Funkcja powinna zwracać sumę `1` i `2`
    3. Zdefiniuj `result` z wynikiem wywołania funkcji
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> from inspect import isfunction
    >>> isfunction(compute)
    True
    >>> result
    3
"""


# Solution
def compute():
    return 1 + 2


result = compute()
