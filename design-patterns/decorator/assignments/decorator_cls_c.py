"""
* Assignment: Decorator Class TypeCheck
* Complexity: medium
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Refactor decorator `decorator` to decorator `TypeCheck`
    2. Decorator checks types of all arguments (`*args` oraz `**kwargs`)
    3. Decorator checks return type
    4. When received type is not expected raise `TypeError` with:
        a. argument name
        b. actual type
        c. expected type
    5. Run doctests - all must succeed

Polish:
    1. Przerób dekorator `decorator` na klasę `TypeCheck`
    2. Dekorator sprawdza typy wszystkich argumentów (`*args` oraz `**kwargs`)
    3. Dekorator sprawdza typ zwracany
    4. Gdy otrzymany typ nie jest równy oczekiwanemu podnieś `TypeError` z:
        a. nazwa argumentu
        b. aktualny typ
        c. oczekiwany typ
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * https://docs.python.org/3/howto/annotations.html
    * `inspect.get_annotations()`
    * `function.__code__.co_varnames`
    * `dict(zip(...))`
    * `dict.items()`
    * `dict1 | dict2` - merging dicts

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(TypeCheck), \
    'TypeCheck should be a decorator class'

    >>> assert TypeCheck(lambda: ...), \
    'TypeCheck should take function as an argument'

    >>> assert isinstance(TypeCheck(lambda: ...), TypeCheck), \
    'TypeCheck() should return an object which is an instance of TypeCheck'

    >>> @TypeCheck
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

    >>> @TypeCheck
    ... def echo(a: str, b: int, c: float = 0.0) -> bool:
    ...     return str(a * b)
    >>>
    >>> echo('one', 1, 1.1)
    Traceback (most recent call last):
    TypeError: "return" is <class 'str'>, but <class 'bool'> was expected
"""

def typecheck(func):
    annotations = func.__annotations__

    def merge(args, kwargs) -> dict:
        return kwargs | dict(zip(annotations, args))

    def check(argname, argvalue):
        argtype = type(argvalue)
        expected = annotations[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, '
                            f'but {expected} was expected')

    def wrapper(*args, **kwargs):
        for argname, argvalue in merge(args, kwargs).items():
            check(argname, argvalue)
        result = func(*args, **kwargs)
        check('return', result)
        return result

    return wrapper


# Refactor typecheck into class
# type: type
class TypeCheck:
    ...


# Solution
class TypeCheck:
    def __init__(self, func):
        self.func = func
        self.annotations = func.__annotations__

    def merge(self, args, kwargs):
        return kwargs | dict(zip(self.annotations, args))

    def check(self, argname, argvalue):
        argtype = type(argvalue)
        expected = self.annotations[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, '
                            f'but {expected} was expected')

    def __call__(self, *args, **kwargs):
        for argname, argvalue in self.merge(args, kwargs).items():
            self.check(argname, argvalue)
        result = self.func(*args, **kwargs)
        self.check('return', result)
        return result
