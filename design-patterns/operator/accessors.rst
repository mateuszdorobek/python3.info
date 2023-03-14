Operator Accessors
==================
* ``obj(x)`` - call
* ``obj[x]`` - getitem
* ``obj[x]`` - missing
* ``obj[x] = 10`` - setitem
* ``del obj[x]`` - delitem


About
-----
.. csv-table:: Operator Overload
    :header: "Operator", "Method", "Remarks"
    :widths: 15, 45, 40

    "``obj(x)``",        "``obj.__call__(x)``"
    "``obj[x]``",        "``obj.__getitem__(x)``"
    "``obj[x]``",        "``obj.__missing__(x)``", "(when ``x`` is not in ``obj``)"
    "``obj[x] = 10``",   "``obj.__setitem__(x, 10)``"
    "``del obj[x]``",    "``obj.__delitem__(x)``"


Example
-------
>>> def echo(text):
...     return text
>>>
>>>
>>> echo('Mark Watney')
'Mark Watney'
>>>
>>> echo.__call__('Mark Watney')
'Mark Watney'


Use Case - 0x01
---------------
>>> data = dict()
>>>
>>> data['a'] = 10  # data.__setitem__('a', 10) -> None
>>> data['a']       # data.__getitem__('a') -> 10
10
>>>
>>> data['x']       # data.__getitem__('x') -> data.__missing__() -> KeyError: 'x'
Traceback (most recent call last):
KeyError: 'x'
>>>
>>> data()          # data.__call__() -> TypeError: 'dict' object is not callable
Traceback (most recent call last):
TypeError: 'dict' object is not callable


Use Case - 0x02
---------------
Recap information about slice:

>>> data = slice(1, 2, 3)
>>>
>>>
>>> data.start
1
>>>
>>> data.stop
2
>>>
>>> data.step
3

Let's define a class with getitem and it's instance:

>>> class MyClass:
...     def __getitem__(self, item):
...         print(type(item))
>>>
>>>
>>> my = MyClass()

>>> my[1]
<class 'int'>
>>>
>>> my[1.0]
<class 'float'>
>>>
>>> my[1:2]
<class 'slice'>
>>>
>>> my[1,2]
<class 'tuple'>
>>>
>>> my[[1,2]]
<class 'list'>
>>>

>>> my['1969-07-20':'1969-07-21']
<class 'slice'>
>>>
>>> my[['Evening','Morning']]
<class 'list'>
>>>
>>> my['1969-07-20':'1969-07-21', ['Evening','Morning']]
<class 'tuple'>


Use Case - 0x03
---------------
Getitem in ``numpy``:

>>> import numpy as np
>>>
>>>
>>> data = np.array([[1, 2, 3],
...                  [4, 5, 6],
...                  [7, 8, 9]])
>>>
>>> data[1][2]
6
>>>
>>> data[1,2]
6
>>>
>>> data[1:2]
array([[4, 5, 6]])
>>>
>>> data[1:2, 0]
array([4])
>>>
>>> data[1:2, 1:]
array([[5, 6]])

``data[1]``:

>>> data.__getitem__(1)
array([4, 5, 6])

``data[1,2]``:

>>> data.__getitem__((1,2))
6

``data[1:2]``:

>>> data.__getitem__(slice(1,2))
array([[4, 5, 6]])

``data[:, 2]``:

>>> data.__getitem__((slice(None,None,None), 2))
array([3, 6, 9])

Intuitive implementation of numpy ``array[row,col]`` accessor:

>>> class array(np.ndarray):
...     def __getitem__(key):
...         if isinstance(key, int):
...             return super().__getitem__(key)
...
...         if isinstance(key, tuple):
...             row = key[0]
...             col = key[1]
...             return super().__getitem__(row).__getitem__(col)
...
...         if isinstance(key, slice):
...             start = key[0] if key[0] else 0
...             stop = key[1] if key[0] else len(self)
...             step = key[2] if key[2] else 1
...             return ...


Use Case - 0x04
---------------
* Cache

>>> class Cache(dict):
...     def __init__(self, func):
...         self.func = func
...
...     def __call__(self, *args):
...         return self[args]
...
...     def __missing__(self, key):
...         self[key] = self.func(*key)
...         return self[key]
>>>
>>>
>>> @Cache
... def add(a, b):
...     return a + b
>>>
>>>
>>> _ = add(1,2)  # computed
>>> _ = add(1,2)  # fetched from cache
>>> _ = add(1,2)  # fetched from cache
>>> _ = add(1,2)  # fetched from cache
>>> _ = add(2,1)  # computed
>>> _ = add(2,1)  # fetched from cache
>>>
>>> add  # doctest: +NORMALIZE_WHITESPACE
{(1, 2): 3,
 (2, 1): 3}
