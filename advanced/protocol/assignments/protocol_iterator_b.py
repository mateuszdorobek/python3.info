"""
* Assignment: Protocol Iterator Range
* Complexity: medium
* Lines of code: 14 lines
* Time: 8 min

English:
    1. Define class `Range` with parameters: `start`, `stop`, `step`
    2. Write own implementation of a built-in `range(start, stop, step)` function
    3. Assume, that user will never giv only one argument; always it will be either two or three arguments
    4. Use Iterator protocol
    5. All tests must pass
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Range` z parametrami: `start`, `stop`, `step`
    2. Zaimplementuj własne rozwiązanie wbudowanej funkcji `range(start, stop, step)`
    3. Przyjmij, że użytkownik nigdy nie poda tylko jednego argumentu; zawsze będą to dwa lub trzy argumenty
    4. Użyj protokołu Iterator
    5. Wszystkie testy muszą przejść
    6. Uruchom doctesty - wszystkie muszą się powieść

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


# Solution
class Range:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self._iter_index = self.start
        return self

    def __next__(self):
        if self._iter_index >= self.stop:
            raise StopIteration
        result = self._iter_index
        self._iter_index += self.step
        return result
