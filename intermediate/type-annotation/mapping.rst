Type Annotation Mapping
=======================
* Before Python 3.9 you need ``from typing import Dict``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y


Dict
----
>>> data: dict = {}
>>> data: dict = dict()

>>> data: dict[int, str] = {
...    0: 'setosa',
...    1: 'virginica',
...    2: 'versicolor'}

>>> data: dict[float, str] = {
...    5.8: 'Sepal length',
...    2.7: 'Sepal width',
...    5.1: 'Petal length',
...    1.9: 'Petal width'}

>>> data: dict[str, float] = {
...    'Sepal length': 5.8,
...    'Sepal width': 2.7,
...    'Petal length': 5.1,
...    'Petal width': 1.9}


List of Dicts
-------------
>>> data: list[dict] = [
...     {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
...     {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
...     {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'}]

>>> data: list[dict[str, list[float] | str]] = [
...     {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
...     {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
...     {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'}]


Aliases
-------
>>> row = list[float]
>>> data: list[dict[str, row|str]] = [
...     {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
...     {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
...     {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'}]

>>> features = list[float]
>>> label = str
>>> row = dict[str, features|label]
>>> data: list[row] = [
...     {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
...     {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
...     {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'}]


Typed Dict
----------
Since Python 3.8: :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys

>>> from typing import TypedDict
>>>
>>>
>>> class Point(TypedDict):
...     x: int
...     y: int
>>>
>>>
>>> pt1: Point = {'x':1, 'y':2}
... # Ok
>>>
>>> pt2: Point = {'x':1, 'y':2, 'z':0}
... # Expected type 'Point', got 'Dict[str, int]' instead
>>>
>>> pt3: Point = {'x':1, 'z':0}
... # Expected type 'Point', got 'Dict[str, int]' instead
...
>>> pt4: Point = Point(x=1, y=2)
... # Ok
>>>
>>> pt5: Point = Point(x=1, z=2)
... # Unexpected argument
>>>
>>> pt6: Point = Point(x=1, y=2, z=0)
... # Unexpected argument
...
>>> pt6: Point = {}
>>> pt6['x'] = 10
... # Ok
>>>
>>> pt6['z'] = 20
... # TypeDict "Point" has no key 'z'


Further Reading
---------------
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`
