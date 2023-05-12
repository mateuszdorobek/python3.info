OOP Attribute Get
=================


Attribute Access
----------------
>>> class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = Astronaut()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>>
>>> print(f'Hello {mark.firstname} {mark.lastname}')
Hello Mark Watney


Accessing not Existing Attributes
---------------------------------
>>> class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = Astronaut()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>>
>>> print(mark.missions)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'missions'


Get All Attributes and Values
-----------------------------
* ``vars(obj)`` - returns all fields in dict format

Define a class

>>> class Astronaut:
...     firstname: str
...     lastname: str
...     mission: str
...     agency: str

Set all attributes:

>>> watney = Astronaut()
>>> watney.firstname = 'Mark'
>>> watney.lastname = 'Watney'
>>> watney.mission = 'Ares 3'
>>> watney.agency = 'NASA'

Getting dynamic fields and values:

>>> vars(watney)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'mission': 'Ares 3',
 'agency': 'NASA'}


Select Attributes
-----------------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     height: float
...     weight: float
>>>
>>>
>>> mark = Astronaut()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>> mark.age = 44
>>> mark.height = 185.5
>>> mark.weight = 75.5
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 44, 'height': 185.5, 'weight': 75.5}
>>>
>>> list(vars(mark).values())
['Mark', 'Watney', 44, 185.5, 75.5]
>>>
>>> [x for x in vars(mark).values() if type(x) is str]
['Mark', 'Watney']
>>>
>>> [x for x in vars(mark).values() if type(x) in (float, int)]
[44, 185.5, 75.5]
>>>
>>> {k:v for k,v in vars(mark).items()}
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 44, 'height': 185.5, 'weight': 75.5}
>>>
>>> {k:v for k,v in vars(mark).items() if k in ['firstname', 'lastname']}
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> {k:v for k,v in vars(mark).items() if type(v) is str}
{'firstname': 'Mark', 'lastname': 'Watney'}


Use Case - 0x01
---------------
>>> class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str
>>>
>>>
>>> flower = Iris()
>>> flower.sepal_length = 5.1
>>> flower.sepal_width = 3.5
>>> flower.petal_length = 1.4
>>> flower.petal_width = 0.2
>>> flower.species = 'setosa'
>>>
>>> vars(flower)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.1,
 'sepal_width': 3.5,
 'petal_length': 1.4,
 'petal_width': 0.2,
 'species': 'setosa'}


Use Case - 0x02
---------------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     mission: str
...     agency: str
>>>
>>>
>>> mark = Astronaut()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>> mark.mission = 'Ares 3'
>>> mark.agency = 'NASA'
>>>
>>> melissa = Astronaut()
>>> melissa.firstname = 'Melissa'
>>> melissa.lastname = 'Lewis'
>>> melissa.mission = 'Ares 3'
>>> melissa.agency = 'NASA'
>>>
>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'mission': 'Ares 3',
 'agency': 'NASA'}
>>>
>>> vars(melissa)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Melissa',
 'lastname': 'Lewis',
 'mission': 'Ares 3',
 'agency': 'NASA'}


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_get_a.py
    :caption: :download:`Solution <assignments/oop_attribute_get_a.py>`
    :end-before: # Solution
