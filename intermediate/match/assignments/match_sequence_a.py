"""
* Assignment: Idioms Match Range
* Complexity: medium
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Write own implementation of a built-in function `range()`
    2. Note, that function does not take any keyword arguments
    3. How to implement passing only stop argument
       `myrange(start=0, stop=???, step=1)`?
    4. Use `match args`
    5. Run doctests - all must succeed

Polish:
    1. Zaimplementuj własne rozwiązanie wbudowanej funkcji `range()`
    2. Zauważ, że funkcja nie przyjmuje żanych argumentów nazwanych (keyword)
    3. Jak zaimplementować możliwość podawania tylko końca
       `myrange(start=0, stop=???, step=1)`?
    4. Użyj `match args`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * https://github.com/python/cpython/blob/main/Objects/rangeobject.c#LC75
    * `raise TypeError('error message')`
    * use `*args` and `**kwargs`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(myrange)

    >>> myrange(0, 10, 2)
    [0, 2, 4, 6, 8]

    >>> myrange(0, 5)
    [0, 1, 2, 3, 4]

    >>> myrange(5)
    [0, 1, 2, 3, 4]

    >>> myrange()
    Traceback (most recent call last):
    TypeError: myrange expected at least 1 argument, got 0

    >>> myrange(1,2,3,4)
    Traceback (most recent call last):
    TypeError: myrange expected at most 3 arguments, got 4

    >>> myrange(stop=2)
    Traceback (most recent call last):
    TypeError: myrange() takes no keyword arguments

    >>> myrange(start=1, stop=2)
    Traceback (most recent call last):
    TypeError: myrange() takes no keyword arguments

    >>> myrange(start=1, stop=2, step=2)
    Traceback (most recent call last):
    TypeError: myrange() takes no keyword arguments
"""


# myrange(start=0, stop=???, step=1)
# note, function does not take keyword arguments
# type: Callable[[int,int,int], list[int]]
def myrange(*args, **kwargs):
    if kwargs:
        raise TypeError('myrange() takes no keyword arguments')

    start = ...
    stop = ...
    step = ...

    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result


# Solution
def myrange(*args, **kwargs):
    if kwargs:
        raise TypeError('myrange() takes no keyword arguments')

    match args:
        case [start, stop, step]: pass
        case [start, stop]: step = 1
        case [stop]: start = 0; step = 1
        case []: raise TypeError('myrange expected at least 1 argument, got 0')
        case _: raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')

    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result
