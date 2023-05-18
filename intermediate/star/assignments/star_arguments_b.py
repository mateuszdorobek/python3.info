"""
* Assignment: Unpack Arguments Range
* Complexity: medium
* Lines of code: 25 lines
* Time: 13 min

English:
    1. Write own implementation of a built-in function `range()`,
       example usage: `myrange(0, 10)` or `myrange(0, 10, 2)`
    2. Note, that function does not take any keyword arguments
    3. How to implement passing only stop argument, i.e. `myrange(10)`?
    4. Run doctests - all must succeed

Polish:
    1. Zaimplementuj własne rozwiązanie wbudowanej funkcji `range()`,
       przykład użycia: `myrange(0, 10)` lub `myrange(0, 10, 2)`
    2. Zauważ, że funkcja nie przyjmuje żanych argumentów nazwanych (keyword)
    3. Jak zaimplementować możliwość podawania tylko końca, tj. `myrange(10)`?
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * https://github.com/python/cpython/blob/main/Objects/rangeobject.c#LC75
    * `raise TypeError('error message')`
    * use `*args` and `**kwargs`
    * `if len(args) == ...`
    * `match len(args)`

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


# Write own implementation of a built-in function `range()`
# example: myrange(0, 10, 2), myrange(0, 10)
# note: function does not take keyword arguments
# type: Callable[[int,int,int], list[int]]
def myrange():
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

    match len(args):
        case 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        case 2:
            start = args[0]
            stop = args[1]
            step = 1
        case 1:
            start = 0
            stop = args[0]
            step = 1
        case 0:
            raise TypeError('myrange expected at least 1 argument, got 0')
        case _:
            n = len(args)
            raise TypeError(f'myrange expected at most 3 arguments, got {n}')


    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result


## Alternative solution
# match len(args):
#     case 3: start, stop, step = args
#     case 2: (start, stop), step = args, 1
#     case 1: start, stop, step = 0, args, 1
#     case 0: raise TypeError('myrange expected at least 1 argument, got 0')
#     case _: raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')
