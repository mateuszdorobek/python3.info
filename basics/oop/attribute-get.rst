OOP Attribute Get
=================


Attribute Access
----------------
>>> class User:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = User()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>>
>>> print(f'Hello {mark.firstname} {mark.lastname}')
Hello Mark Watney


Accessing not Existing Attributes
---------------------------------
>>> class User:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = User()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>>
>>> print(mark.groups)
Traceback (most recent call last):
AttributeError: 'User' object has no attribute 'groups'


Get All Attributes and Values
-----------------------------
* ``vars(obj)`` - returns all fields in dict format

Define a class

>>> class User:
...     firstname: str
...     lastname: str
...     email: str
...     agency: str

Set all attributes:

>>> watney = User()
>>> watney.firstname = 'Mark'
>>> watney.lastname = 'Watney'
>>> watney.email = 'mwatney@nasa.gov'

Getting dynamic fields and values:

>>> vars(watney)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'email': 'mwatney@nasa.gov'}


Select Attributes
-----------------
>>> class User:
...     firstname: str
...     lastname: str
...     age: int
...     height: float
...     weight: float
>>>
>>>
>>> mark = User()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>> mark.age = 42
>>> mark.height = 178.0
>>> mark.weight = 75.5
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 42, 'height': 178.0, 'weight': 75.5}
>>>
>>> list(vars(mark).values())
['Mark', 'Watney', 42, 178.0, 75.5]
>>>
>>> [x for x in vars(mark).values() if type(x) is str]
['Mark', 'Watney']
>>>
>>> [x for x in vars(mark).values() if type(x) in (float, int)]
[42, 178.0, 75.5]
>>>
>>> {k:v for k,v in vars(mark).items()}
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 42, 'height': 178.0, 'weight': 75.5}
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
>>> class User:
...     firstname: str
...     lastname: str
...     mission: str
...     agency: str
>>>
>>>
>>> mark = User()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>> mark.email = 'mwatney@nasa.gov'
>>>
>>> melissa = User()
>>> melissa.firstname = 'Melissa'
>>> melissa.lastname = 'Lewis'
>>> melissa.email = 'mlewis@nasa.gov'
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'email': 'mwatney@nasa.gov'}
>>>
>>> vars(melissa)
{'firstname': 'Melissa', 'lastname': 'Lewis', 'email': 'mlewis@nasa.gov'}


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_get_a.py
    :caption: :download:`Solution <assignments/oop_attribute_get_a.py>`
    :end-before: # Solution
