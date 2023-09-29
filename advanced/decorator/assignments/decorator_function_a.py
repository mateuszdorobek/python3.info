"""
* Assignment: Decorator Syntax About
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Create decorator `mydecorator`
    2. Decorator should have `wrapper` with `*args` and `**kwargs` parameters
    3. Wrapper should call original function with it's original parameters,
       and return its value
    4. Decorator should return `wrapper` function
    5. Run doctests - all must succeed

Polish:
    1. Stwórz dekorator `mydecorator`
    2. Dekorator powinien mieć `wrapper` z parametrami `*args` i `**kwargs`
    3. Wrapper powinien wywoływać oryginalną funkcję z jej oryginalnymi
       parametrami i zwracać jej wartość
    4. Decorator powinien zwracać funckję `wrapper`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(mydecorator), \
    'Create mydecorator() function'

    >>> assert isfunction(mydecorator(lambda: ...)), \
    'mydecorator() should take function as an argument'

    >>> @mydecorator
    ... def echo(text):
    ...     return text

    >>> echo('hello')
    'hello'
"""

# type: Callable[[Callable], Callable]
def mydecorator():
    pass

# Solution
def mydecorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
