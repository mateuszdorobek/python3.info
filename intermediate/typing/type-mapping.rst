Typing Mapping
==============
* Before Python 3.9 you need ``from typing import Dict``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y


Dict
----
Empty:

>>> data: dict = {}
>>> data: dict = dict()

Generic:

>>> data: dict = {'firstname': 'Mark', 'lastname': 'Watney'}

Strict:

>>> data: dict[str, str] = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> data: dict[str, str|int] = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>>
>>> data: dict[int, str] = {
...    0: 'setosa',
...    1: 'virginica',
...    2: 'versicolor'}
>>>
>>> data: dict[float, str] = {
...    5.8: 'Sepal length',
...    2.7: 'Sepal width',
...    5.1: 'Petal length',
...    1.9: 'Petal width'}
>>>
>>> data: dict[str, float] = {
...    'Sepal length': 5.8,
...    'Sepal width': 2.7,
...    'Petal length': 5.1,
...    'Petal width': 1.9}


Use Case - 0x01
---------------
>>> calendarium: dict[int, str] = {
...     1961: 'Yuri Gagarin fly to space',
...     1969: 'Neil Armstrong set foot on the Moon',
... }


Use Case - 0x02
---------------
>>> calendarium: dict[int, list[str]] = {
...     1961: ['Yuri Gagarin fly to space', 'Alan Shepard fly to space'],
...     1969: ['Neil Armstrong set foot on the Moon'],
... }


Further Reading
---------------
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


Assignments
-----------
.. literalinclude:: assignments/typing_mapping_a.py
    :caption: :download:`Solution <assignments/typing_mapping_a.py>`
    :end-before: # Solution
