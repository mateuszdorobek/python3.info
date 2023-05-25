Typing Nested
=============
* Before Python 3.9 you need ``from typing import List, Tuple, Set, Frozenset``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections

>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
... ]
>>>
>>> x = DATA[0][-1]
>>> x  # doctest: +SKIP
>>> # IDE don't know what type is species
>>> # and cannot give hints for autocompletion

>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
... ]
>>>
>>> x: str = DATA[0][-1]
>>> x  # doctest: +SKIP
>>> # IDE knows exactly what type is species
>>> # and what methods hint for autocompletion


List of Lists
-------------
Declaration:

>>> data: list
>>> data: list[list]
>>> data: list[list[int]]

Example:

>>> data: list = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]]

>>> data: list[list] = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]]

>>> data: list[list[int]] = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]]


List of Tuples
--------------
Declaration:

>>> data: list
>>> data: list[tuple]
>>> data: list[tuple[float, float, float, float, str]]

Example:

>>> data: list = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica'),
... ]

>>> data: list[tuple] = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica'),
... ]

>>> data: list[tuple[float, float, float, float, str]] = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica'),
... ]


List of Dicts
-------------
>>> data: list[dict] = [
...     {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
...     {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
...     {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
... ]

>>> data: list[dict[str, list[float] | str]] = [
...     {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
...     {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
...     {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
... ]


Aliases
-------
Declaration:

>>> row = tuple[int, int, int]
>>> data: list[row]

Example:

>>> Iris = tuple[float, float, float, float, str]
>>>
>>> data: list[Iris] = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica'),
... ]

>>> features = list[float]
>>> label = str
>>>
>>> data: list[dict[str, features|label]] = [
...     {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
...     {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
...     {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
... ]


Unions
------
Declaration:

>>> a = tuple[str, str, str]
>>> b = tuple[int, int, int]
>>> c = tuple[float, float, float]
>>>
>>> data: list[a | b | c]

>>> header = tuple[str, str, str]
>>> row = tuple[int, int, int]
>>>
>>> data: tuple[header,row,...]

Example:

>>> Header = tuple[str, str, str, str, str]
>>> Row = tuple[float, float, float, float, str]
>>>
>>> DATA: tuple[Header,Row,...] = (
...     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
... )


Use Case - 0x01
---------------
>>> GeographicCoordinate = tuple[float, float]
>>>
>>> locations: list[GeographicCoordinate] = [
...     (25.91375, -60.15503),
...     (-11.01983, -166.48477),
...     (-11.01983, -166.48477),
... ]


Use Case - 0x02
---------------
>>> data: list[list|tuple|set] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> data: list[list[int] | tuple[int, ...] | set[int]] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> row = list[int] | tuple[int, ...] | set[int]
>>>
>>> data: list[row] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]



Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


References
----------
.. [#pyDocTyping] https://docs.python.org/3/library/typing.html#module-contents


Assignments
-----------
.. literalinclude:: assignments/typing_nested_a.py
    :caption: :download:`Solution <assignments/typing_nested_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/typing_nested_b.py
    :caption: :download:`Solution <assignments/typing_nested_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/typing_nested_c.py
    :caption: :download:`Solution <assignments/typing_nested_c.py>`
    :end-before: # Solution
