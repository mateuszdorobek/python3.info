"""
* Assignment: Decorator Syntax Disable
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Modify decorator `disable`
    2. Decorator raises `PermissionError` and does not execute function
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj dekorator `disable`
    2. Dekorator podnosi `PermissionError` i nie wywołuje funkcji
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(disable), \
    'Create disable() function'

    >>> assert isfunction(disable(lambda: ...)), \
    'disable() should take function as an argument'

    >>> @disable
    ... def echo(text):
    ...     print(text)

    >>> echo('hello')
    Traceback (most recent call last):
    PermissionError: Function is disabled
"""


# type: Callable[[Callable], Callable]
def disable(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


# Solution
def disable(func):
    def wrapper(*args, **kwargs):
        raise PermissionError('Function is disabled')

    return wrapper
