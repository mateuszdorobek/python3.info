Type Annotation Deprecated
==========================

The redundant types are deprecated as of Python 3.9 but no deprecation
warnings will be issued by the interpreter. It is expected that type
checkers will flag the deprecated types when the checked program targets
Python 3.9 or newer. [#pyDocTyping]_

The deprecated types will be removed from the typing module in the first
Python version released 5 years after the release of Python 3.9.0. See
details in PEP 585—Type Hinting Generics In Standard Collections.
[#pyDocTyping]_


Optional
--------
* Since Python 3.10 you can write ``int | None``
* ``Optional[int] == Union[int, None] == int | None``

>>> from typing import Optional
>>>
>>> data: Optional[int] = 1337
>>> data: Optional[int] = None

>>> from typing import Optional
>>>
>>>
>>> def find(text: str, substr: str) -> Optional[int]:
...     position = text.find(substr)
...     if position == -1:
...         return None
...     else:
...         return position
>>>
>>>
>>> find('Python', 'x')
>>> find('Python', 'o')
4


Union
-----
* Since Python 3.10 you can write ``int | float``
* ``Union[int, str] == Union[str, int]``

>>> from typing import Union
>>>
>>> number: Union[int, float] = 1337
>>> number: Union[int, float] = 1.337

>>> from typing import Union
>>>
>>>
>>> def add(a: Union[int,float], b: Union[int,float]) -> Union[int,float]:
...     return a + b


List
----
* Since Python 3.9 you can write ``list[int]``

>>> from typing import List
>>>
>>>
>>> data: List[int] = [1, 2, 3, 4]
>>> data: List[float] = [5.8, 2.7, 5.1, 1.9]
>>> data: List[str] = ['a', 'b', 'c', 'd']


Tuple
-----
* Since Python 3.9 you can write ``tuple[int, ...]``

>>> from typing import Tuple
>>>
>>>
>>> data: Tuple[int, int, int] = (1, 2, 3)
>>> data: Tuple[str, str, str] = ('setosa', 'virginica', 'versicolor')
>>> data: Tuple[str, int, float] = ('a', 2, 3.3)
>>> data: Tuple[int, ...] = (1, 2, 3)
>>> data: Tuple[str, ...] = ('setosa', 'virginica', 'versicolor')


Set
---
* Since Python 3.9 you can write ``set[int]``

>>> from typing import Set
>>>
>>>
>>> data: Set[int] = {1, 2, 3}
>>> data: Set[float] = {0.0, 1.1, 2.2}
>>> data: Set[str] = {'a', 'b', 'c'}


FrozenSet
---------
* Since Python 3.9 you can write ``frozenset[int]``

>>> from typing import FrozenSet
>>>
>>>
>>> data: FrozenSet[int] = {1, 2, 3}
>>> data: FrozenSet[float] = {0.0, 1.1, 2.2}
>>> data: FrozenSet[str] = {'a', 'b', 'c'}


List[tuple]
-----------
* Since Python 3.9 you can write ``list[tuple]``

>>> from typing import List, Tuple

>>> data: List[tuple] = [
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...    (7.6, 3.0, 6.6, 2.1, 'virginica')]

>>> data: List[Tuple[float, float, float, float, str]] = [
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...    (7.6, 3.0, 6.6, 2.1, 'virginica')]

>>> GeographicCoordinate = Tuple[float, float]
>>> locations: List[GeographicCoordinate] = [
...    (25.91375, -60.15503),
...    (-11.01983, -166.48477),
...    (-11.01983, -166.48477)]

>>> Iris = Tuple[float, float, float, float, str]
>>> data: List[Iris] = [
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...    (7.6, 3.0, 6.6, 2.1, 'virginica')]


List[list]
----------
* Since Python 3.9 you can write ``list[list]``

>>> from typing import List

>>> data: List[list] = [
...    [1, 2, 3],
...    [4, 5, 6],
...    [7, 8, 9]]

>>> data: List[List[int]] = [
...    [1, 2, 3],
...    [4, 5, 6],
...    [7, 8, 9]]


Nested
------
* Since Python 3.9 you can write ``list[list|tuple|set]``

>>> from typing import Union, List, Tuple, Set

>>> data: List[Union[list, tuple, set]] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> data: List[Union[List[int], Tuple[int, int, int], Set[int]]] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> Row = Union[List[int],
...             Tuple[int, int, int],
...             Set[int]]
...
>>> data: List[Row] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]


Dict
----
* Since Python 3.9 you can write ``dict[str,str]``

>>> from typing import Dict
>>>
>>>
>>> data: Dict[int, str] = {
...    0: 'setosa',
...    1: 'virginica',
...    2: 'versicolor'}
