Typing NamedTuple
=================


SetUp
-----
>>> from typing import NamedTuple


Tuple
-----
Problem:

>>> def hello(user):
...     print(f'Hello {user[0]} {user[1]}')
>>>
>>>
>>> mark = ('Mark', 'Watney')
>>> hello(mark)
Hello Mark Watney
>>>
>>> mark = ['Mark', 'Watney']
>>> hello(mark)
Hello Mark Watney
>>>
>>> mark = {'Mark', 'Watney'}
>>> hello(mark)
Traceback (most recent call last):
TypeError: 'set' object is not subscriptable

Solution:

>>> def hello(user: tuple):
...     print(f'Hello {user[0]} {user[1]}')
>>>
>>>
>>> mark = ('Mark', 'Watney')
>>> hello(mark)
Hello Mark Watney
>>>
>>> mark = {'Mark', 'Watney'}
>>> hello(mark)  # Expected type 'tuple', got 'set[str]' instead
Traceback (most recent call last):
TypeError: 'set' object is not subscriptable


Tuple[str,str]
--------------
Problem:

>>> def hello(user: tuple):
...     print(f'Hello {user[0]} {user[1]}')
>>>
>>>
>>> mark = ('Mark', 'Watney')
>>> hello(mark)
Hello Mark Watney
>>>
>>> mark = ('Mark', 'Watney', 'mwatney@nasa.gov')
>>> hello(mark)
Hello Mark Watney
>>>
>>> mark = ('Mark',)
>>> hello(mark)
Traceback (most recent call last):
IndexError: tuple index out of range

Solution:

>>> def hello(user: tuple[str,str]):
...     print(f'Hello {user[0]} {user[1]}')
>>>
>>>
>>> mark = ('Mark', 'Watney')
>>> hello(mark)
Hello Mark Watney
>>>
>>> mark = ('Mark', 'Watney', 'mwatney@nasa.gov')
>>> hello(mark)  # Expected type 'tuple[str, str]', got 'tuple[str, str, str]' instead
Hello Mark Watney
>>>
>>> mark = ('Mark',)
>>> hello(mark)  # Expected type 'tuple[str, str]', got 'tuple[str]' instead
Traceback (most recent call last):
IndexError: tuple index out of range


NamedTuple
----------
>>> class User(NamedTuple):
...     firstname: str
...     lastname: str
>>>
>>>
>>> def hello(user: User):
...     print(f'Hello {user[0]} {user[1]}')
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>> hello(mark)
Hello Mark Watney
>>>
>>> mark = User(firstname='Mark', lastname='Watney')
>>> hello(mark)
Hello Mark Watney

Using ``NamedTuple`` we can also make ``hello()`` function more readable
by using named attributes ``user.firstname`` and ``user.lastname`` instead
of indexes, such as: ``user[0]`` and ``user[1]``:

>>> class User(NamedTuple):
...     firstname: str
...     lastname: str
>>>
>>>
>>> def hello(user: User):
...     print(f'Hello {user.firstname} {user.lastname}')
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>> hello(mark)
Hello Mark Watney
>>>
>>> mark = User(firstname='Mark', lastname='Watney')
>>> hello(mark)
Hello Mark Watney

Note, that this is a regular class so you can also use methods in it:

>>> class User(NamedTuple):
...     firstname: str
...     lastname: str
...
...     def hello(self):
...         print(f'Hello {self.firstname} {self.lastname}')
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>> mark.hello()
Hello Mark Watney
>>>
>>> mark = User(firstname='Mark', lastname='Watney')
>>> mark.hello()
Hello Mark Watney


Default
-------
>>> class Point(NamedTuple):
...     x: int
...     y: int
>>>
>>>
>>> pt = Point()
Traceback (most recent call last):
TypeError: Point.__new__() missing 2 required positional arguments: 'x' and 'y'

>>> class Point(NamedTuple):
...     x: int = 0
...     y: int = 0
>>>
>>>
>>> pt = Point()
>>> pt
Point(x=0, y=0)


Extensibility
-------------
>>> class Point(NamedTuple):
...     x: int
...     y: int
...     z: int = 0

>>> pt = Point(1, 2)
>>> pt
Point(x=1, y=2, z=0)

>>> pt = Point(1, 2, 3)
>>> pt
Point(x=1, y=2, z=3)


Contract
--------
Problem:

>>> def get_user(uid):
...     return (1, 'Mark', 'Watney', 40, 185.5, 75.0, True, False, None)
>>>
>>>
>>> mark = get_user(1000)
>>>
>>> mark[1]
'Mark'
>>>
>>> mark[2]
'Watney'
>>>
>>> mark[6]
True

Tuple annotation:

>>> def get_user(uid: int) -> tuple[int,str,str,int,float,float,bool,bool,bool|None]:
...     return (1, 'Mark', 'Watney', 40, 185.5, 75.0, True, False, None)
>>>
>>>
>>> mark = get_user(1000)
>>>
>>> mark[1]
'Mark'
>>>
>>> mark[2]
'Watney'
>>>
>>> mark[6]
True

NamedTuple annotation:

>>> class User(NamedTuple):
...     id: int
...     firstname: str
...     lastname: str
...     age: int
...     height: int | float
...     weight: int | float
...     is_astronaut: bool
...     is_assigned: bool
...     mission: str | None
>>>
>>>
>>> def get_user(uid: int) -> User:
...     return User(1, 'Mark', 'Watney', 40, 185.5, 75.0, True, False, None)
>>>
>>>
>>> mark = get_user(1000)
>>>
>>> mark.firstname
'Mark'
>>>
>>> mark.lastname
'Watney'
>>>
>>> mark.is_astronaut
True
>>>
>>> mark[1]
'Mark'
>>>
>>> mark[2]
'Watney'
>>>
>>> mark[6]
True

Moreover returning values are much more readable:

>>> def get_user(uid: int) -> User:
...     return User(
...         id=1,
...         firstname='Mark',
...         lastname='Watney',
...         age=40,
...         height=185.5,
...         weight=75.0,
...         is_astronaut=True,
...         is_assigned=False,
...         mission=None)


Iteration
---------
>>> class User(NamedTuple):
...     firstname: str
...     lastname: str
>>>
>>> mark = User(firstname='Mark', lastname='Watney')

>>> mark[0]
'Mark'
>>>
>>> mark[1]
'Watney'

>>> for field in mark:
...     print(field)
...
Mark
Watney


IsInstance
----------
Note, that ``NamedTuple`` is still a tuple and you can compare both!

>>> class User(NamedTuple):
...     firstname: str
...     lastname: str
>>>
>>> mark = User(firstname='Mark', lastname='Watney')

>>> isinstance(mark, tuple)
True

>>> type(mark)
<class '__main__.User'>

>>> User.mro()
[<class '__main__.User'>, <class 'tuple'>, <class 'object'>]


Equality
--------
>>> class User(NamedTuple):
...     firstname: str
...     lastname: str
>>>
>>>
>>> a = ('Mark', 'Watney')
>>> b = User('Mark', 'Watney')
>>> c = User(firstname='Mark', lastname='Watney')

Equality:

>>> a == b
True
>>>
>>> a == c
True
>>>
>>> b == c
True

Identity:

>>> a is b
False
>>>
>>> a is c
False
>>>
>>> b is c
False


Size
----
>>> from sys import getsizeof
>>>
>>>
>>> class User(NamedTuple):
...     firstname: str
...     lastname: str
>>>
>>>
>>> a = ('Mark', 'Watney')
>>> b = User('Mark', 'Watney')
>>> c = User(firstname='Mark', lastname='Watney')

>>> getsizeof(a)
56
>>>
>>> getsizeof(b)
56
>>>
>>> getsizeof(c)
56


Use Case - 0x01
---------------
>>> class Point(NamedTuple):
...     x: int = 0
...     y: int = 0
>>>
>>>
>>> class Position:
...     position: Point
...
...     def __init__(self, initial_position: Point = Point()):
...         self.position = initial_position
...
...     def set_position(self, position: Point) -> None:
...         self.position = position
...
...     def get_position(self) -> Point:
...         return self.position
>>>
>>>
>>> current = Position()
>>>
>>> current.get_position()
Point(x=0, y=0)
>>>
>>> current.set_position(Point(1, 2))
>>>
>>> current.get_position()
Point(x=1, y=2)


Use Case - 0x02
---------------
>>> class GeographicCoordinate(NamedTuple):
...     latitude: float
...     longitude: float
>>>
>>>
>>> locations: list[tuple[float,float]] = [
...     (25.91375, -60.15503),
...     (-11.01983, -166.48477),
...     (-11.01983, -166.48477)]
>>>
>>> locations: list[GeographicCoordinate] = [
...     GeographicCoordinate(25.91375, -60.15503),
...     GeographicCoordinate(-11.01983, -166.48477),
...     GeographicCoordinate(-11.01983, -166.48477)]
>>>
>>> locations: list[GeographicCoordinate] = [
...     GeographicCoordinate(latitude=25.91375, longitude=-60.15503),
...     GeographicCoordinate(latitude=-11.01983, longitude=-166.48477),
...     GeographicCoordinate(latitude=-11.01983, longitude=-166.48477)]


Use Case - 0x03
---------------
>>> from itertools import starmap
>>> from pprint import pprint
>>>
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica'),
...     (4.9, 3.0, 1.4, 0.2, 'setosa'),
...     (4.9, 2.5, 4.5, 1.7, 'virginica'),
...     (7.1, 3.0, 5.9, 2.1, 'virginica'),
...     (4.6, 3.4, 1.4, 0.3, 'setosa'),
...     (5.4, 3.9, 1.7, 0.4, 'setosa'),
...     (5.7, 2.8, 4.5, 1.3, 'versicolor'),
...     (5.0, 3.6, 1.4, 0.3, 'setosa'),
...     (5.5, 2.3, 4.0, 1.3, 'versicolor'),
...     (6.5, 3.0, 5.8, 2.2, 'virginica'),
...     (6.5, 2.8, 4.6, 1.5, 'versicolor'),
...     (6.3, 3.3, 6.0, 2.5, 'virginica'),
...     (6.9, 3.1, 4.9, 1.5, 'versicolor'),
...     (4.6, 3.1, 1.5, 0.2, 'setosa'),
... ]

>>> class Iris(NamedTuple):
...     sl: float
...     sw: float
...     pl: float
...     pw: float
...     species: str

>>> result = starmap(Iris, DATA[1:])
>>> data = list(result)

>>> pprint(data)
[Iris(sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica'),
 Iris(sl=5.1, sw=3.5, pl=1.4, pw=0.2, species='setosa'),
 Iris(sl=5.7, sw=2.8, pl=4.1, pw=1.3, species='versicolor'),
 Iris(sl=6.3, sw=2.9, pl=5.6, pw=1.8, species='virginica'),
 Iris(sl=6.4, sw=3.2, pl=4.5, pw=1.5, species='versicolor'),
 Iris(sl=4.7, sw=3.2, pl=1.3, pw=0.2, species='setosa'),
 Iris(sl=7.0, sw=3.2, pl=4.7, pw=1.4, species='versicolor'),
 Iris(sl=7.6, sw=3.0, pl=6.6, pw=2.1, species='virginica'),
 Iris(sl=4.9, sw=3.0, pl=1.4, pw=0.2, species='setosa'),
 Iris(sl=4.9, sw=2.5, pl=4.5, pw=1.7, species='virginica'),
 Iris(sl=7.1, sw=3.0, pl=5.9, pw=2.1, species='virginica'),
 Iris(sl=4.6, sw=3.4, pl=1.4, pw=0.3, species='setosa'),
 Iris(sl=5.4, sw=3.9, pl=1.7, pw=0.4, species='setosa'),
 Iris(sl=5.7, sw=2.8, pl=4.5, pw=1.3, species='versicolor'),
 Iris(sl=5.0, sw=3.6, pl=1.4, pw=0.3, species='setosa'),
 Iris(sl=5.5, sw=2.3, pl=4.0, pw=1.3, species='versicolor'),
 Iris(sl=6.5, sw=3.0, pl=5.8, pw=2.2, species='virginica'),
 Iris(sl=6.5, sw=2.8, pl=4.6, pw=1.5, species='versicolor'),
 Iris(sl=6.3, sw=3.3, pl=6.0, pw=2.5, species='virginica'),
 Iris(sl=6.9, sw=3.1, pl=4.9, pw=1.5, species='versicolor'),
 Iris(sl=4.6, sw=3.1, pl=1.5, pw=0.2, species='setosa')]

>>> data[0]
Iris(sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica')
>>>
>>> data[0].sl
5.8
>>> data[0].species
'virginica'
>>>
>>> tuple(data[0])
(5.8, 2.7, 5.1, 1.9, 'virginica')


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


References
----------
.. [#pyDocTyping] https://docs.python.org/3/library/typing.html#module-contents
