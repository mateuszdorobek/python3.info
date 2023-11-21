Performance Collections
=======================

* https://docs.python.org/3/library/collections.html

It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multi-sets in other languages.

This module implements specialized container data types providing alternatives to Python's general purpose built-in containers, dict, list, set, and tuple.

.. csv-table:: ``collections`` module containers
    :header: : "Name", "Description"

    ``namedtuple``    , "factory function for creating tuple subclasses with named fields"
    ``deque``         , "list-like container with fast appends and pops on either end"
    ``ChainMap``      , "dict-like class for creating a single view of multiple mappings"
    ``Counter``       , "dict subclass for counting hashable objects"
    ``OrderedDict``   , "dict subclass that remembers the order entries were added"
    ``defaultdict``   , "dict subclass that calls a factory function to supply missing values"
    ``UserDict``      , "wrapper around dictionary objects for easier dict subclassing"
    ``UserList``      , "wrapper around list objects for easier list subclassing"
    ``UserString``    , "wrapper around string objects for easier string subclassing"


``OrderedDict``
---------------
>>> jose = {'firstname': 'José', 'lastname': 'Jiménez', 'agency': 'NASA'}
>>>
>>> print(jose)
{'firstname': 'José', 'lastname': 'Jiménez', 'agency': 'NASA'}
>>>
>>> print(jose['firstname'], jose['lastname'], jose['agency'])
José Jiménez NASA

>>> from collections import OrderedDict
>>>
>>> jose = OrderedDict(firstname='José', lastname='Jiménez', agency='NASA')
>>> print(jose)
OrderedDict({'firstname': 'José', 'lastname': 'Jiménez', 'agency': 'NASA'})
>>>
>>> dict(jose)
{'firstname': 'José', 'lastname': 'Jiménez', 'agency': 'NASA'}


``namedtuple``
--------------
>>> from collections import namedtuple
>>>
>>>
>>> Point = namedtuple('Point', ('x', 'y'))
>>>
>>> p1 = Point(x=50, y=120)
>>> p2 = Point(50, 120)
>>>
>>> print(p1)
Point(x=50, y=120)
>>>
>>> print(p1.x)
50
>>>
>>> print(p1.y)
120
>>>
>>> print(p2)
Point(x=50, y=120)

>>> from collections import namedtuple
>>>
>>>
>>> Astronaut = namedtuple('Astronaut', ['firstname', 'lastname', 'agency'])
>>> jose = Astronaut(firstname='José', lastname='Jiménez', agency='NASA')
>>>
>>> print(jose)
Astronaut(firstname='José', lastname='Jiménez', agency='NASA')
>>>
>>> print(jose.firstname, jose.lastname, jose.agency)
José Jiménez NASA


Counter
-------
>>> from random import randint, seed
>>> seed(0)
>>>
>>>
>>> random_numbers = [randint(0, 10) for a in range(0, 50)]
>>> counter = dict()
>>>
>>> for number in random_numbers:
...     if number in counter:
...         counter[number] += 1
...     else:
...         counter[number] = 1
>>>
>>> counter.items()
dict_items([(6, 5), (0, 4), (4, 6), (8, 7), (7, 5), (5, 4), (9, 5), (3, 2), (2, 3), (1, 5), (10, 4)])

>>> from collections import Counter
>>> from random import randint, seed
>>> seed(0)
>>>
>>>
>>> random_numbers = [randint(0, 10) for a in range(0, 50)]
>>> counter = Counter(random_numbers)
>>>
>>> counter.most_common(5)
[(8, 7), (4, 6), (6, 5), (7, 5), (9, 5)]


DefaultDict
-----------
>>> colors = ['red', 'green', 'red', 'blue']
>>>
>>> result = dict()
>>>
>>> for color in colors:
...     if color not in result:
...         result[color] = 1
...     else:
...         result[color] += 1
>>>
>>> print(result)
{'red': 2, 'green': 1, 'blue': 1}

>>> from collections import defaultdict
>>>
>>>
>>> colors = ['red', 'green', 'red', 'blue']
>>>
>>> result = defaultdict(int)
>>>
>>> for color in colors:
...     result[color] += 1
>>>
>>>
>>> print(result)
defaultdict(<class 'int'>, {'red': 2, 'green': 1, 'blue': 1})


UserString
----------
>>> from collections import UserString
>>>
>>>
>>> class str(UserString):
...     def __add__(self, other):
...         return f'{self} {other}'
>>>
>>>
>>> result = str('José') + 42
>>> print(result)
José 42

>>> from collections import UserString
>>>
>>>
>>> class str(UserString):
...     def __add__(self, other):
...         return f'{self} {other}'
>>>
>>>
>>> class Point:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...
...     def __str__(self):
...         return f'({self.x}, {self.y})'
>>>
>>>
>>> p = Point(x=10, y=20)
>>>
>>> out = str('José') + p
>>> print(out)
José (10, 20)


.. todo:: Assignments
