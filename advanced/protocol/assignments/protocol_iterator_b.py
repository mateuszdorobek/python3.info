"""
* Assignment: Protocol Iterator Range
* Complexity: medium
* Lines of code: 9 lines
* Time: 8 min

English:
    1. Modify class `Range` to write own implementation
       of a built-in `range(start, stop, step)` function
    2. Assume, that user will never give only one argument;
       it will always be either two or three arguments
    3. Use Iterator protocol
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `Range` aby napisać własną implementację
       wbudowanej funkcji `range(start, stop, step)`
    2. Przyjmij, że użytkownik nigdy nie poda tylko jednego argumentu;
       zawsze będą to dwa lub trzy argumenty
    3. Użyj protokołu Iterator
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Range)

    >>> r = Range(0, 0, 0)
    >>> assert hasattr(r, '__iter__')
    >>> assert hasattr(r, '__next__')
    >>> assert ismethod(r.__iter__)
    >>> assert ismethod(r.__next__)

    >>> list(Range(0, 10, 2))
    [0, 2, 4, 6, 8]

    >>> list(Range(0, 5))
    [0, 1, 2, 3, 4]
"""
from dataclasses import dataclass


@dataclass
class Range:
    start: int = 0
    stop: int = None
    step: int = 1


# Solution
@dataclass
class Range:
    start: int
    stop: int
    step: int = 1
    _current: int = 0

    def __iter__(self):
        self._current = self.start
        return self

    def __next__(self):
        if self._current >= self.stop:
            raise StopIteration
        result = self._current
        self._current += self.step
        return result
