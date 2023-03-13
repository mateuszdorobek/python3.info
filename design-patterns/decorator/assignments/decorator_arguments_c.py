"""
* Assignment: Decorator Arguments TypeCheck
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Create decorator function `typecheck`
    2. Decorator checks return type only if `check_return` is `True`
    3. Run doctests - all must succeed

Polish:
    1. Stwórz dekorator funkcję `typecheck`
    2. Dekorator sprawdza typ zwracany tylko gdy `check_return` jest `True`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * https://docs.python.org/3/howto/annotations.html
    * `inspect.get_annotations()`
    * `function.__code__.co_varnames`
    * `dict(zip(...))`
    * `dict.items()`
    * `dict1 | dict2` - merging dicts

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction, isclass

    >>> assert isfunction(typecheck), \
    'Create typecheck() function'

    >>> assert isfunction(typecheck(True)), \
    'typecheck() should take one positional arguments'

    >>> assert isfunction(typecheck(check_return=True)), \
    'typecheck() should take one keyword arguments: check_return'

    >>> assert isfunction(typecheck(check_return=True)(lambda: ...)), \
    'typecheck() should return decorator which can take a function'

    >>> @typecheck(check_return=True)
    ... def echo(a: str, b: int, c: float = 0.0) -> bool:
    ...     return bool(a * b)

    >>> echo('one', 1)
    True
    >>> echo('one', 1, 1.1)
    True
    >>> echo('one', b=1)
    True
    >>> echo('one', 1, c=1.1)
    True
    >>> echo('one', b=1, c=1.1)
    True
    >>> echo(a='one', b=1, c=1.1)
    True
    >>> echo(c=1.1, b=1, a='one')
    True
    >>> echo(b=1, c=1.1, a='one')
    True
    >>> echo('one', c=1.1, b=1)
    True
    >>> echo(1, 1)
    Traceback (most recent call last):
    TypeError: "a" is <class 'int'>, but <class 'str'> was expected
    >>> echo('one', 'two')
    Traceback (most recent call last):
    TypeError: "b" is <class 'str'>, but <class 'int'> was expected
    >>> echo('one', 1, 'two')
    Traceback (most recent call last):
    TypeError: "c" is <class 'str'>, but <class 'float'> was expected
    >>> echo(b='one', a='two')
    Traceback (most recent call last):
    TypeError: "b" is <class 'str'>, but <class 'int'> was expected
    >>> echo('one', c=1.1, b=1.1)
    Traceback (most recent call last):
    TypeError: "b" is <class 'float'>, but <class 'int'> was expected

    >>> @typecheck(check_return=True)
    ... def echo(a: str, b: int, c: float = 0.0) -> bool:
    ...     return str(a * b)
    >>>
    >>> echo('one', 1, 1.1)
    Traceback (most recent call last):
    TypeError: "return" is <class 'str'>, but <class 'bool'> was expected

    >>> @typecheck(check_return=False)
    ... def echo(a: str, b: int, c: float = 0.0) -> bool:
    ...     return str(a * b)
    >>>
    >>> echo('one', 1, 1.1)
    'one'
"""

# type: Callable[[Callable], Callable]
def decorator(func):
    def validate(argname, argval):
        argtype = type(argval)
        expected = func.__annotations__[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, '
                            f'but {expected} was expected')

    def wrapper(*args, **kwargs):
        arguments = kwargs | dict(zip(func.__annotations__.keys(), args))
        [validate(k, v) for k, v in arguments.items()]
        result = func(*args, **kwargs)
        validate('return', result)
        return result

    return wrapper


# Solution
def typecheck(check_return: bool = True):
    def decorator(func):
        def validate(argname, argval):
            argtype = type(argval)
            expected = func.__annotations__[argname]
            if argtype is not expected:
                raise TypeError(f'"{argname}" is {argtype}, '
                                f'but {expected} was expected')

        def wrapper(*args, **kwargs):
            arguments = kwargs | dict(zip(func.__annotations__.keys(), args))
            [validate(k, v) for k, v in arguments.items()]
            result = func(*args, **kwargs)
            if check_return:
                validate('return', result)
            return result

        return wrapper

    return decorator
