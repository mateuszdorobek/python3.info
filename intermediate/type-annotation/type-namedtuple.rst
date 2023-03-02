Type Annotation NamedTuple
==========================


SetUp
-----
>>> from typing import NamedTuple


Problem
-------
>>> def hello_astronaut(astronaut):
...     result = f'Hello {astronaut[0]} {astronaut[1]}'

>>> mark = ('Mark', 'Watney', 40)
>>> hello_astronaut(mark)

>>> iris = ('Iris', 'Setosa')
>>> hello_astronaut(iris)


Solution 1 - tuple
------------------
>>> def hello_astronaut(astronaut: tuple[str,str,int]):
...     result = f'Hello {astronaut[0]} {astronaut[1]}'

>>> mark = ('Mark', 'Watney', 40)
>>> hello_astronaut(mark) # ok

>>> iris = ('Iris', 'Setosa')
>>> hello_astronaut(iris)  # error (missing int)

>>> iris = ('Iris', 'Setosa', 1)
>>> hello_astronaut(iris)  # ok


Solution 2 - NamedTuple
-----------------------
>>> class Astronaut(NamedTuple):
...     firstname: str
...     lastname: str
...     age: int
>>>
>>>
>>> def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut[0]} {astronaut[1]}'

>>> mark = Astronaut('Mark', 'Watney', 40)
>>> hello_astronaut(mark) # ok

>>> mark = Astronaut(firstname='Mark', lastname='Watney', age=40)
>>> hello_astronaut(mark) # ok

>>> iris = ('Iris', 'Setosa', 1)
>>> hello_astronaut(iris)  # ok


Attributes
----------
Using ``NamedTuple`` we can also make ``hello_astronaut()`` function
more readable by using attributes ``astronaut.firstname`` and
``astronaut.lastname`` instead of indexes, such as: ``astronaut[0]``
and ``astronaut[1]``.

>>> def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut.firstname} {astronaut.lastname}'


IsInstance
----------
Note, that ``NamedTuple`` is still a tuple and you can compare both!

>>> class Astronaut(NamedTuple):
...     firstname: str
...     lastname: str

>>> a = ('Mark', 'Watney')
>>> b: Astronaut = ('Mark', 'Watney')
>>> c = Astronaut('Mark', 'Watney')
>>> d = Astronaut(firstname='Mark', lastname='Watney')

>>> isinstance(a, tuple)
True
>>>
>>> isinstance(b, tuple)
True
>>>
>>> isinstance(c, tuple)
True
>>>
>>> isinstance(d, tuple)
True

>>> type(a)
<class 'tuple'>
>>> type(b)
<class 'tuple'>
>>> type(c)
<class '__main__.Astronaut'>
>>> type(d)
<class '__main__.Astronaut'>

>>> Astronaut.mro()
[<class '__main__.Astronaut'>, <class 'tuple'>, <class 'object'>]

>>> a == b
True
>>> b == c
True
>>> c == d
True


Size
----
>>> from sys import getsizeof
>>>
>>> getsizeof(a)
56
>>> getsizeof(b)
56
>>> getsizeof(c)
56
>>> getsizeof(d)
56






NamedTuple
----------
SetUp:

>>> from typing import NamedTuple

Problem:

>>> def hello_astronaut(astronaut):
...     result = f'Hello {astronaut[0]} {astronaut[1]}'
>>>
>>>
>>> mark = ('Mark', 'Watney', 40)
>>> hello_astronaut(mark)
>>>
>>> iris = ('Iris', 'Setosa')
>>> hello_astronaut(iris)

Solution 1 - tuple:

>>> def hello_astronaut(astronaut: tuple[str,str,int]):
...     result = f'Hello {astronaut[0]} {astronaut[1]}'
>>>
>>>
>>> mark = ('Mark', 'Watney', 40)
>>> hello_astronaut(mark) # ok
>>>
>>> iris = ('Iris', 'Setosa')
>>> hello_astronaut(iris)  # error (missing int)
>>>
>>> iris = ('Iris', 'Setosa', 1)
>>> hello_astronaut(iris)  # ok

Solution 2 - NamedTuple:

>>> class Astronaut(NamedTuple):
...     firstname: str
...     lastname: str
...     age: int
>>>
>>>
>>> def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut[0]} {astronaut[1]}'
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', 40)
>>> hello_astronaut(mark) # ok
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney', age=40)
>>> hello_astronaut(mark) # ok
>>>
>>> iris = ('Iris', 'Setosa', 1)
>>> hello_astronaut(iris)  # ok

Using ``NamedTuple`` we can also make ``hello_astronaut()`` function
more readable by using attributes ``astronaut.firstname`` and
``astronaut.lastname`` instead of indexes, such as: ``astronaut[0]``
and ``astronaut[1]``.

>>> def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut.firstname} {astronaut.lastname}'

Note, that ``NamedTuple`` is still a tuple and you can compare both!

>>> class Astronaut(NamedTuple):
...     firstname: str
...     lastname: str

>>> a = ('Mark', 'Watney')
>>> b: Astronaut = ('Mark', 'Watney')
>>> c = Astronaut('Mark', 'Watney')
>>> d = Astronaut(firstname='Mark', lastname='Watney')

>>> isinstance(a, tuple)
True
>>>
>>> isinstance(b, tuple)
True
>>>
>>> isinstance(c, tuple)
True
>>>
>>> isinstance(d, tuple)
True

>>> type(a)
<class 'tuple'>
>>> type(b)
<class 'tuple'>
>>> type(c)
<class '__main__.Astronaut'>
>>> type(d)
<class '__main__.Astronaut'>

>>> Astronaut.mro()
[<class '__main__.Astronaut'>, <class 'tuple'>, <class 'object'>]

>>> a == b
True
>>> b == c
True
>>> c == d
True

>>> from sys import getsizeof
>>>
>>> getsizeof(a)
56
>>> getsizeof(b)
56
>>> getsizeof(c)
56
>>> getsizeof(d)
56





#%%

class Person(NamedTuple):
    firstname: str
    lastname: str


def say_hello(person: Person):
    print(f'Witaj {person.firstname} {person.lastname}')


osoba = Person(firstname='Mark', lastname='Watney')
say_hello(osoba)


#%%

class Point(TypedDict):
    x: int
    y: int
    z: int


point = Point(x=1, y=2, z=3)
point: Point = {'x':1, 'y':2, 'z':3}
point: Point = {'x':1, 'y':2, 'z':3.0}  # z jest float, a miał być int
point: Point = {'x':1, 'y':2}           # brakuje z


class Point(TypedDict):
    x: int
    y: int
    z: int | None

point: Point = {'x':1, 'y':2, 'z':None}


class Point(TypedDict):
    x: int
    y: int
    z: NotRequired[int]

point: Point = {'x':1, 'y':2, 'z':3}  # ok
point: Point = {'x':1, 'y':2, 'z':3.0}  # nie ok
point: Point = {'x':1, 'y':2, 'z':None}  # nie ok
point: Point = {'x':1, 'y':2}   # ok


class Point(TypedDict):
    x: Required[int]
    y: Required[int]
    z: NotRequired[int]



class GeographicCoordinate(NamedTuple):
    latitude: float
    longitude: float


locations: list[GeographicCoordinate] = [
    (25.91375, -60.15503),
    (-11.01983, -166.48477),
    (-11.01983, -166.48477)]

locations: list[GeographicCoordinate] = [
    GeographicCoordinate(25.91375, -60.15503),
    GeographicCoordinate(-11.01983, -166.48477),
    GeographicCoordinate(-11.01983, -166.48477)]

locations: list[GeographicCoordinate] = [
    GeographicCoordinate(latitude=25.91375, longitude=-60.15503),
    GeographicCoordinate(latitude=-11.01983, longitude=-166.48477),
    GeographicCoordinate(latitude=-11.01983, longitude=-166.48477)]


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


References
----------
.. [#pyDocTyping] https://docs.python.org/3/library/typing.html#module-contents
