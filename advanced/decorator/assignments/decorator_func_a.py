"""
* Assignment: Decorator Function Check
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create decorator `check`
    2. Decorator calls function, only when `echo.disabled` is `False`
    3. Note that decorators overwrite reference and in `wrapper`
       you must check if `wrapper.disabled` is `False`
    4. Else raise an exception `PermissionError`
    5. Run doctests - all must succeed

Polish:
    1. Stwórz dekorator `check`
    2. Dekorator wywołuje funkcję, tylko gdy `echo.disabled` jest `False`
    3. Zwróć uwagę, że dekoratory nadpisują referencje i we `wrapper`
       musisz sprawdzić czy `wrapper.disabled` jest `False`
    4. W przeciwnym przypadku podnieś wyjątek `PermissionError`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(check), \
    'Create check() function'

    >>> assert isfunction(check(lambda: ...)), \
    'check() should take function as an argument'

    >>> @check
    ... def echo(text):
    ...     print(text)

    >>> assert isfunction(echo), \
    'Decorator check() should return a function'

    >>> echo.disabled = False
    >>> echo('hello')
    hello

    >>> echo.disabled = True
    >>> echo('hello')
    Traceback (most recent call last):
    PermissionError: Function is disabled

    >>> assert hasattr(echo, 'disabled')
"""


# type: Callable[[Callable], Callable]
def check(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


# Solution
def check(func):
    def wrapper(*args, **kwargs):
        if not wrapper.disabled:
            return func(*args, **kwargs)
        else:
            raise PermissionError('Function is disabled')

    return wrapper
