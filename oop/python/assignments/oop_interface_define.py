"""
* Assignment: OOP Interface Define
* Complexity: easy
* Lines of code: 13 lines
* Time: 8 min

English:
    1. Define interface `IrisInterface`
    2. Attributes: `sepal_length, sepal_width, petal_length, petal_width`
    3. Methods: `sum()`, `len()`, `mean()` in `IrisInterface`
    4. All methods and constructor must raise exception `NotImplementedError`
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj interfejs `IrisInterface`
    2. Attributes: `sepal_length, sepal_width, petal_length, petal_width`
    3. Metody: `sum()`, `len()`, `mean()` w `IrisInterface`
    4. Wszystkie metody oraz konstruktor muszą podnosić wyjątek `NotImplementedError`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert hasattr(IrisInterface, 'mean')
    >>> assert hasattr(IrisInterface, 'sum')
    >>> assert hasattr(IrisInterface, 'len')

    >>> from inspect import isfunction
    >>> assert isfunction(IrisInterface.mean)
    >>> assert isfunction(IrisInterface.sum)
    >>> assert isfunction(IrisInterface.len)

    >>> IrisInterface.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>,
     'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>,
     'petal_width': <class 'float'>}

    >>> iris = IrisInterface(5.8, 2.7, 5.1, 1.9)
    Traceback (most recent call last):
    NotImplementedError
"""


# Solution
class IrisInterface:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:

        raise NotImplementedError

    def mean(self) -> float:
        raise NotImplementedError

    def sum(self) -> float:
        raise NotImplementedError

    def len(self) -> int:
        raise NotImplementedError
