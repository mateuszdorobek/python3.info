"""
* Assignment: Generator Itertools Count
* Complexity: medium
* Lines of code: 3 lines
* Time: 3 min

English:
    1. `Label encoder` algorithm encodes labels (str) to numbers (int).
       Each unique label will assign autoincremented numbers.
       example: {'virginica': 0, 'setosa': 1, 'versicolor': 2}
    2. Modify code below and use `itertools.count()` instead of `i`
    3. Function resut must be `dict[str,int]`

Polish:
    1. Algorytm `label_encoder` koduje etykiety (str) do liczb (int).
       Kolejnym wystąpieniom unikalnych etykiet przyporządkowuje liczby.
       przykład: {'virginica': 0, 'setosa': 1, 'versicolor': 2}
    2. Zmodyfikuj kod poniżej i użyj `itertools.count()` zamiast `i`
    3. Wynik funkcji ma być `dict[str,int]`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction, isgeneratorfunction

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is dict, \
    'Result must be a dict'
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert all(type(element) is str for element in result), \
    'All elements in result must be a str'

    >>> result
    {'virginica': 0, 'setosa': 1, 'versicolor': 2}
"""
from itertools import count


DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


result = {}
i = 0

for *_, species in DATA[1:]:
    if species not in result:
        result[species] = i
        i += 1


# Solution
result = {}
i = count()

for *_, species in DATA[1:]:
    if species not in result:
        result[species] = next(i)
