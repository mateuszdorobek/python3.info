"""
* Assignment: FuncProg Callable Define
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define function `check` without any parameter
    2. Function `check` must return `wrapper: Callable`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `check` bez żadnego parametru
    2. Funkcja `check` ma zwracać `wrapper: Callable`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(check)
    >>> assert isfunction(wrapper)
    >>> assert isfunction(check())

    >>> wrapper()
    'hello from wrapper'

    >>> check()()
    'hello from wrapper'
"""


def wrapper():
    return 'hello from wrapper'


# Without any parameter
# Returns wrapper function
# type: Callable[[Callable], Callable]
def check():
    ...


# Solution
def check():
    return wrapper
