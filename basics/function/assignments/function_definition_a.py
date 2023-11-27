"""
* Assignment: Function Definition Define
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define function `say_hello`
    2. Function prints 'hello world' on screen
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `say_hello`
    2. Funkcja wypisuje 'hello world' na ekranie
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(say_hello), \
    'Object `say_hello` must be a function'

    >>> say_hello()
    hello world
"""


# Solution
def say_hello():
    print('hello world')
