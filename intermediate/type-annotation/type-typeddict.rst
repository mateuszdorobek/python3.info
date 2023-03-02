Type Annotation TypedDict
=========================
* Since Python 3.8:
* :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys


SetUp
-----
>>> from typing import TypedDict


Definition
----------
>>> class Astronaut(TypedDict):
...     firstname: str
...     lastname: str
...     age: int | float


Example
-------
>>> def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut["firstname"]} {astronaut["lastname"]}'

>>> mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>> hello_astronaut(mark)  # ok
>>>
>>> mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> hello_astronaut(mark)  # error: missing `age`  # doctest: +SKIP
>>>
>>> mark: Astronaut = {'firstname': 'Mark'}
>>> hello_astronaut(mark)  # error: missing `lastname` and `age`  # doctest: +SKIP
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney', age=40)
>>> hello_astronaut(mark)  # ok
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney')
>>> hello_astronaut(mark)  # error: missing `age`  # doctest: +SKIP
>>>
>>> mark = Astronaut(firstname='Mark')
>>> hello_astronaut(mark)  # error: missing `lastname`  # doctest: +SKIP
>>>
>>> iris = {'genus': 'Iris', 'species': 'Setosa'}
>>> hello_astronaut(iris)  # error: not an astronaut  # doctest: +SKIP




Typed Dict
----------
Since Python 3.8: :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys

>>> from typing import TypedDict


>>> class Astronaut(TypedDict):
...     firstname: str
...     lastname: str
...     age: int | float
...
...
>>> def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut["firstname"]} {astronaut["lastname"]}'
...
...
>>> mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>> hello_astronaut(mark)  # ok
>>>
>>> mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> hello_astronaut(mark)  # error: missing `age`  # doctest: +SKIP
>>>
>>> mark: Astronaut = {'firstname': 'Mark'}
>>> hello_astronaut(mark)  # error: missing `lastname` and `age`  # doctest: +SKIP
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney', age=40)
>>> hello_astronaut(mark)  # ok
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney')
>>> hello_astronaut(mark)  # error: missing `age`  # doctest: +SKIP
>>>
>>> mark = Astronaut(firstname='Mark')
>>> hello_astronaut(mark)  # error: missing `lastname`  # doctest: +SKIP
>>>
>>> iris = {'genus': 'Iris', 'species': 'Setosa'}
>>> hello_astronaut(iris)  # error: not an astronaut  # doctest: +SKIP


Future
------
* Since Python 3.11 :pep:`655` -- Marking individual TypedDict items as required or potentially-missing

>>> # doctest: +SKIP
... from typing import Required, NotRequired
...
...
... class Astronaut(TypedDict):
...     firstname: Required[str]
...     lastname: Required[str]
...     age: NotRequired[int|float]
...
...
... def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut["firstname"]} {astronaut["lastname"]}')
...
...
... mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
... hello_astronaut(mark)  # ok
...
... mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney'}
... hello_astronaut(mark)  # ok
...
... mark: Astronaut = {'firstname': 'Mark'}
... hello_astronaut(mark)  # error: missing `lastname`
...
... mark = Astronaut(firstname='Mark', lastname='Watney', age=40)
... hello_astronaut(mark)  # ok
...
... mark = Astronaut(firstname='Mark', lastname='Watney')
... hello_astronaut(mark)  # ok
...
... mark = Astronaut(firstname='Mark')
... hello_astronaut(mark)  # error: missing `lastname`
...
... iris = {'genus': 'Iris', 'species': 'Setosa'}
... hello_astronaut(iris)  # error: not an astronaut



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
