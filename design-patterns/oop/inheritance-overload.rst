OOP Inheritance Overload
========================
* Child inherits all fields and methods from parent
* Used to avoid code duplication

.. glossary::

    overload
        When :term:`child` has method or attribute with the same name as
        :term:`parent`. In such case :term:`child` attribute will be used
        (will :term:`overload` :term:`parent`).


Overload Method
---------------
>>> class Person:
...     def say_hello(self):
...         print('Hello')
>>>
>>>
>>> class Astronaut(Person):
...     def say_hello(self):
...         print('Howdy')
>>>
>>>
>>> mark = Astronaut()
>>> mark.say_hello()
Howdy


Overload Init
-------------
>>> class Person:
...     def __init__(self):
...         print('Person init')
>>>
>>>
>>> class Astronaut(Person):
...     pass
>>>
>>>
>>> mark = Astronaut()
Person init

>>> class Person:
...     def __init__(self):
...         print('Person init')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut init')
>>>
>>>
>>> mark = Astronaut()
Astronaut init


Overload ClassVars
------------------
>>> class Person:
...     firstname = 'Mark'
...     lastname = 'Watney'
...     job = None
>>>
>>>
>>> class Astronaut(Person):
...     job = 'astronaut'
>>>
>>>
>>> mark = Astronaut()
>>>
>>> mark.firstname
'Mark'
>>> mark.lastname
'Watney'
>>> mark.job
'astronaut'


Overload Attribute
------------------
>>> class Person:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.job = None
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         self.job = 'astronaut'
>>>
>>>
>>> mark = Astronaut()
>>> vars(mark)
{'job': 'astronaut'}


Assignments
-----------
.. todo:: Assignments
