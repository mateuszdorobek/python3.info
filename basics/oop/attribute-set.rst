OOP Attribute Set
=================


Syntax
------
>>> class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = Astronaut()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'


Attributes and Instances
------------------------
* Dynamic attributes

>>> class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = Astronaut()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>>
>>> melissa = Astronaut()
>>> melissa.firstname = 'Melissa'
>>> melissa.lastname = 'Lewis'
>>>
>>> rick = Astronaut()
>>> rick.firstname = 'Rick'
>>> rick.lastname = 'Martinez'


List
----
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str]
>>>
>>> mark = Astronaut()
>>> mark.missions = ['Ares1', 'Ares3']


Union
-----
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int | float
>>>
>>>
>>> mark = Astronaut()
>>> mark.age = 40
>>>
>>> melissa = Astronaut()
>>> melissa.age = 44.5


Optional
--------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int | None
>>>
>>>
>>> mark = Astronaut()
>>> mark.age = 40
>>>
>>> melissa = Astronaut()
>>> melissa.age = None


Example
-------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     agency: str
...     flown: bool
...     age: int | float
...     height: float | None
...     weight: float | None
...     missions: list[str] | None
...     friends: list['Astronaut'] | None
>>>
>>>
>>> mark = Astronaut()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>> mark.agency = 'NASA'
>>> mark.flown = True
>>> mark.age = 40
>>> mark.height = 185.5
>>> mark.weight = 75.5
>>> mark.missions = ['Ares1', 'Ares3']
>>> mark.friends = None


Use Case - 0x01
---------------
>>> class Point:
...     x: int
...     y: int
...     z: int

>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 0


Use Case - 0x02
---------------
>>> class Date:
...     year: int
...     month: int
...     day: int

First man in space:

>>> gagarin = Date()
>>> gagarin.year = 1961
>>> gagarin.month = 4
>>> gagarin.day = 12

First man on the Moon:

>>> armstrong = Date()
>>> armstrong.year = 1969
>>> armstrong.month = 7
>>> armstrong.day = 21


Use Case - 0x03
---------------
>>> class Laptop:
...     cpu: str
...     ram: str
...     ssd: str

>>> macbook = Laptop()
>>> macbook.cpu = '2.9 GHz 6-Core Intel Core i9'
>>> macbook.ram = '32 GB 2400 MHz DDR4'
>>> macbook.ssd = '1 TB APPLE SSD AP1024M'


Use Case - 0x04
---------------
>>> class Iris:
...     features: list[float]
...     label: str

>>> setosa = Iris()
>>> setosa.features = [5.1, 3.5, 1.4, 0.2]
>>> setosa.label = 'setosa'


Use Case - 0x05
---------------
>>> class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str

>>> flower = Iris()
>>> flower.sepal_length = 5.1
>>> flower.sepal_width = 3.5
>>> flower.petal_length = 1.4
>>> flower.petal_width = 0.2
>>> flower.species = 'setosa'


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_set_a.py
    :caption: :download:`Solution <assignments/oop_attribute_set_a.py>`
    :end-before: # Solution
