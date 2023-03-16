OOP Methods and Attributes
==========================
* Methods are functions in the class
* First argument is always instance (``self``)
* While calling function you never pass ``self``
* Prevents copy-paste code
* Improves readability
* Improves refactoring
* Decomposes bigger problem into smaller chunks

Syntax:

>>> class MyClass:
...     def __init__(self):
...         self.myfield = 'some value'
...
...     def mymethod(self):
...         return self.myfield
>>>
>>>
>>> my = MyClass()
>>> my.mymethod()
'some value'


Methods Accessing Fields
------------------------
Methods Accessing Fields:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def say_hello(self):
...         return f'My name... {self.name}'
>>>
>>>
>>> jose = Astronaut('José Jiménez')
>>> jose.say_hello()
'My name... José Jiménez'

``self.name`` must be defined before accessing:

>>> class Astronaut:
...     def say_hello(self):
...         return f'My name... {self.name}'
>>>
>>>
>>> jose = Astronaut()
>>> jose.say_hello()
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'name'


Methods Calling Other Methods
-----------------------------
Methods Calling Other Methods:

>>> class Astronaut:
...     def get_name(self):
...         return 'José Jiménez'
...
...     def say_hello(self):
...         name = self.get_name()
...         return f'My name... {name}'
>>>
>>>
>>> jose = Astronaut()
>>> jose.say_hello()
'My name... José Jiménez'

Methods calling other methods:

>>> class Iris:
...     def __init__(self):
...         self.sepal_length = 5.1
...         self.sepal_width = 3.5
...         self.petal_length = 1.4
...         self.petal_width = 0.2
...
...     def sepal_area(self):
...         return self.sepal_length * self.sepal_width
...
...     def petal_area(self):
...         return self.petal_length * self.petal_width
...
...     def total_area(self):
...         return self.sepal_area() + self.petal_area()
>>>
>>>
>>> flower = Iris()
>>> flower.total_area()
18.13

Since Python 3.7 there is a ``@dataclass`` decorator, which automatically
generates ``__init__()`` method with arguments and set-up fields for you.
More information in `OOP Dataclass`.

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length = 5.1
...     sepal_width = 3.5
...     petal_length = 1.4
...     petal_width = 0.2
...     species: str = 'Iris'
...
...     def sepal_area(self):
...         return self.sepal_length * self.sepal_width
...
...     def petal_area(self):
...         return self.petal_length * self.petal_width
...
...     def total_area(self):
...         return self.sepal_area() + self.petal_area()
>>>
>>>
>>> flower = Iris()
>>> flower.total_area()
18.13


Examples
--------
>>> class Point:
...     def __init__(self, x, y, z):
...         self.x = x
...         self.y = y
...         self.z = z
...
...     def get_coordinates(self):
...         return self.x, self.y, self.z
...
...     def show(self):
...         return f'Point(x={self.x}, y={self.y}, z={self.z})'
>>>
>>>
>>> point = Point(x=1, y=2, z=3)
>>>
>>> vars(point)
{'x': 1, 'y': 2, 'z': 3}
>>>
>>> point.get_coordinates()
(1, 2, 3)
>>>
>>> point.show()
'Point(x=1, y=2, z=3)'


Use Case - 0x01
---------------
>>> class Counter:
...     current_value: int
...
...     def __init__(self):
...         self.current_value = 0
...
...     def increment(self):
...         self.current_value += 1
...
...     def decrement(self):
...         self.current_value -= 1
...         if self.current_value < 0:
...             raise ValueError('Cannot decrement below zero')
...
...     def show(self):
...         return self.current_value
>>>
>>>
>>> c = Counter()
>>>
>>> c.increment()
>>> c.increment()
>>> c.show()
2
>>>
>>> c.decrement()
>>> c.decrement()
>>> c.show()
0
>>>
>>> c.decrement()
Traceback (most recent call last):
ValueError: Cannot decrement below zero


Use Case - 0x02
---------------
>>> from typing import Literal
>>>
>>>
>>> class Car:
...     engine: Literal['on', 'off']
...
...     def __init__(self):
...         self.engine = 'off'
...
...     def engine_start(self):
...         self.engine = 'on'
...
...     def engine_stop(self):
...         self.engine = 'off'
...
...     def drive_to(self, location: str):
...         if self.engine != 'on':
...             raise RuntimeError('Engine must be turned on to drive')
...         else:
...             return f'Driving to {location}'
>>>
>>>
>>> maluch = Car()
>>>
>>> maluch.drive_to('Cologne, Germany')
Traceback (most recent call last):
RuntimeError: Engine must be turned on to drive
>>>
>>> maluch.engine
'off'
>>>
>>> maluch.engine_start()
>>> maluch.engine
'on'
>>>
>>> maluch.drive_to('Cologne, Germany')
'Driving to Cologne, Germany'
>>>
>>> maluch.engine_stop()
>>> maluch.engine
'off'


Use Case - 0x03
---------------
* Documentation: https://atlassian-python-api.readthedocs.io
* Source Code: https://github.com/atlassian-api/atlassian-python-api
* Examples: https://github.com/atlassian-api/atlassian-python-api/tree/master/examples

.. code-block:: console

    $ pip install atlassian-python-api

>>> # doctest: +SKIP
... from atlassian import Jira
...
... jira = Jira(
...     url='https://example.com:8080',
...     username='myusername',
...     password='mypassword')
...
... JQL = 'project = DEMO AND status IN ("To Do", "In Progress") ORDER BY issuekey'
...
... result = jira.jql(JQL)
... print(result)

>>> # doctest: +SKIP
... from atlassian import Confluence
...
... confluence = Confluence(
...     url='https://example.com:8090',
...     username='myusername',
...     password='mypassword')
...
... result = confluence.create_page(
...     space='DEMO',
...     title='This is the title',
...     body='This is the body. You can use <strong>HTML tags</strong>!')
...
... print(result)




Assignments
-----------
.. literalinclude:: assignments/oop_mthattr_a.py
    :caption: :download:`Solution <assignments/oop_mthattr_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_mthattr_b.py
    :caption: :download:`Solution <assignments/oop_mthattr_b.py>`
    :end-before: # Solution
