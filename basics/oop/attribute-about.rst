OOP Attribute About
===================
* Attributes are also known as "Properties" or "Fields"
* Attributes store information for instances
* Access field values using dot (``.``) notation

.. glossary::

    field
        Variable inside the class.
        Can be used as a synonym of :term:`property` or :term:`attribute`.

    property
        Variable inside the class.
        Can be used as a synonym of :term:`field` or :term:`attribute`.

    state
        Current values of all variables in a class. Changes during
        lifetime of an object. Represents current state of an object.

    attribute
        Variable inside the class.
        Can be used as a synonym of :term:`field` or :term:`property`.
        In Python, methods also can be described as attributes,
        but justification for that is a bit more complex which will
        be introduced later in a book.

    namespace
        Container for storing related data


About
-----
An example "Glass with Water" can illustrate the distinction of properties
and state attributes:

Properties:

*  color
*  width
*  height
*  radius
*  capacity
*  net mass (without water)

Fields:

* volume  (how much water is currently in the glass)
* gross mass = net mass + water mass (water mass depends on its volume used))

.. figure:: img/oop-classes-glass.jpg

    Source: [#glassimg]_

Class example with distinction of properties and field attributes.

>>> class Glass:
...
...     # Properties
...     color: str
...     width: float
...     height: float
...     radius: float
...     capacity: float
...     net_mass: float  # without water
...
...     # Fields
...     volume: float  # how much water is currently in the glass
...     gross_mass: float  # mass depends on its volume used (glass+water)



What are attributes?
--------------------
* Scalars creates values
* Identifiers and values creates variables
* Values with relations creates structures
* Structures with identifiers creates data
* Data with context and relations creates information

Scalars creates values:

>>> 'Mark'  # doctest: +SKIP
>>> 'Watney'  # doctest: +SKIP
>>> '1969-07-21'  # doctest: +SKIP

Identifiers and values creates variables:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>> birthday = '1969-07-21'

Related values creates structures:

>>> user = ['Mark', 'Watney', '1969-07-21']

Structures with identifiers creates data:

>>> user = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'birthday': '1969-07-21',
... }

Data with context creates classes:

>>> class User:
...     firstname: str
...     lastname: str
...     birthday: str
>>>
>>> user = User()
>>> user.firstname = 'Mark'
>>> user.lastname = 'Watney'
>>> user.birthday = '1969-07-21'

Classes with relations creates information:

>>> class Date:
...     year: int
...     month: int
...     day: int
>>>
>>> class User:
...     firstname: str
...     lastname: str
...     birthday: Date
>>>
>>>
>>> birthday = Date()
>>> birthday.year = 1969
>>> birthday.month = 7
>>> birthday.day = 21
>>>
>>> user = User()
>>> user.firstname = 'Mark'
>>> user.lastname = 'Watney'
>>> user.birthday = birthday


State
-----
>>> class User:
...     firstname: str
...     lastname: str
...     birthday: str

>>> user = User()
>>> vars(user)
{}

>>> user.firstname = 'Mark'
>>> user.lastname = 'Watney'
>>> user.birthday = '1969-07-21'
>>> vars(user)
{'firstname': 'Mark', 'lastname': 'Watney', 'birthday': '1969-07-21'}

>>> user.firstname = 'Melissa'
>>> user.lastname = 'Lewis'
>>> user.birthday = '1961-04-12'
>>> vars(user)
{'firstname': 'Melissa', 'lastname': 'Lewis', 'birthday': '1961-04-12'}


Namespace
---------
* Class creates space, in which names has meaning

Unrelated variables:

>>> firstname: str
>>> lastname: str

Related variables:

>>> user_firstname: str
>>> user_lastname: str

Class creates common space for names (namespace):

>>> class User:
...     firstname: str
...     lastname: str


References
----------
.. [#glassimg] https://media.istockphoto.com/vectors/glasses-set-for-water-glasses-full-empty-halffilled-with-water-vector-vector-id905957960?k=6&m=905957960&s=612x612&w=0&h=DE0uCDCehEA_eDHzHW38jvhl3pYjNuoqXZ_6ZzHbz0M=


.. todo:: Assignments





>>> mark = User()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>>
>>> melissa = User()
>>> melissa.firstname = 'Melissa'
>>> melissa.lastname = 'Lewis'
>>>
>>> vars(melissa)
{'firstname': 'Melissa', 'lastname': 'Lewis'}

>>> class User:
...     firstname: str
...     lastname: str
...     age: int
...
>>>
>>> mark = User()
>>> mark.firstname
Traceback (most recent call last):
AttributeError: 'User' object has no attribute 'firstname'

>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>> mark.email = 'mwatney@nasa.gov'
