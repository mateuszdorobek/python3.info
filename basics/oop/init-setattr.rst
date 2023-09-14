OOP Init Setattr
================


>>> class User:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}


Constant Attributes
-------------------
>>> class User:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'

>>> mark = User()
>>> melissa = User()

>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> vars(melissa)
{'firstname': 'Mark', 'lastname': 'Watney'}


Variable Attributes
-------------------
>>> class User:
...     def __init__(self, a, b):
...         self.firstname = a
...         self.lastname = b

>>> mark = User('Mark', 'Watney')
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}

>>> mark = User(a='Mark', b='Watney')
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}


Better Names
------------
>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname

>>> mark = User('Mark', 'Watney')
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}

>>> mark = User(firstname='Mark', lastname='Watney')
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}


Combine Attributes
------------------
>>> class User:
...     def __init__(self, firstname, lastname):
...         self.name = f'{firstname} {lastname}'
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>> vars(mark)
{'name': 'Mark Watney'}

>>> print(mark.name)
Mark Watney
>>>
>>> print(mark.firstname)
Traceback (most recent call last):
AttributeError: 'User' object has no attribute 'firstname'
>>>
>>> print(mark.lastname)
Traceback (most recent call last):
AttributeError: 'User' object has no attribute 'lastname'


Use Case - 0x01
---------------
>>> class Point:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
>>>
>>>
>>> a = Point(10, 20)
>>> b = Point(10, y=20)
>>> c = Point(x=10, y=20)
>>> d = Point(y=20, x=10)


Use Case - 0x02
---------------
>>> class Point:
...     def __init__(self, x, y, z=0):
...         self.x = x
...         self.y = y
...         self.z = z

>>> a = Point(10, 20)
>>> b = Point(10, y=20)
>>> c = Point(x=10, y=20)
>>> d = Point(y=20, x=10)

>>> e = Point(10, 20, 30)
>>> f = Point(10, 20, z=30)
>>> g = Point(10, y=20, z=30)
>>> h = Point(10, z=30, y=20)
>>> i = Point(x=10, y=20, z=30)
>>> j = Point(x=10, z=30, y=20)
>>> k = Point(y=20, x=10, z=30)
>>> l = Point(y=20, z=30, x=10)
>>> m = Point(z=30, x=10, y=20)
>>> n = Point(z=30, y=20, x=10)


Use Case - 0x03
---------------
>>> class Iris:
...     def __init__(self, sepal_length, sepal_width,
...                  petal_length, petal_width, species):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species

>>> setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')

>>> virginica = Iris(
...     sepal_length=5.8,
...     sepal_width=2.7,
...     petal_length=5.1,
...     petal_width=1.9,
...     species='virginica')


Use Case - 0x04
---------------
* Dataclasses

Since Python 3.7: there is a ``@dataclass`` decorator, which automatically
generates ``__init__()`` arguments and fields. More information in
`OOP Dataclass`.

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str = 'Iris'
>>>
>>>
>>> virginica = Iris(
...     sepal_length=5.8,
...     sepal_width=2.7,
...     petal_length=5.1,
...     petal_width=1.9,
...     species='virginica')
>>>
>>> vars(virginica)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': 5.1,
 'petal_width': 1.9,
 'species': 'virginica'}


Use Case - 0x05
---------------
>>> from random import randint, seed
>>> seed(0)
>>>
>>>
>>> class Hero:
...     name: str
...     position: tuple[int,int]
...     health: int
...
...     def __init__(self, name, position_x, position_y):
...         self.name = name
...         self.position = (position_x, position_y)
...         self.health = randint(50,100)
>>>
>>>
>>> mark = Hero('Mark', position_x=10, position_y=20)
>>> vars(mark)
{'name': 'Mark', 'position': (10, 20), 'health': 74}

Use Case - 0x06
---------------
>>> from random import randint, seed
>>> seed(0)
>>>
>>>
>>> class Hero:
...     name: str
...     position: tuple[int,int]
...     health: int
...
...     def __init__(self, name, health_min=10, health_max=100):
...         self.name = name
...         self.position = (0, 0)
...         self.health = randint(health_min,health_max)
>>>
>>>
>>> mark = Hero('Mark', health_min=50)
>>> vars(mark)
{'name': 'Mark', 'position': (0, 0), 'health': 74}


Assignments
-----------
.. literalinclude:: assignments/oop_init_setattr_a.py
    :caption: :download:`Solution <assignments/oop_init_setattr_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_init_setattr_b.py
    :caption: :download:`Solution <assignments/oop_init_setattr_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_init_setattr_c.py
    :caption: :download:`Solution <assignments/oop_init_setattr_c.py>`
    :end-before: # Solution
