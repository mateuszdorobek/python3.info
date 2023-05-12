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
>>> class Account:
...     def say_hello(self):
...         print('Hello Account')
>>>
>>>
>>> class User(Account):
...     def say_hello(self):
...         print('Hello User')
>>>
>>>
>>> mark = User()
>>> mark.say_hello()
Hello User


Overload Init
-------------
>>> class Account:
...     def __init__(self):
...         print('Init Account')
>>>
>>>
>>> class User(Account):
...     pass
>>>
>>>
>>> mark = User()
Init Account

>>> class Account:
...     def __init__(self):
...         print('Init Account')
>>>
>>>
>>> class User(Account):
...     def __init__(self):
...         print('Init User')
>>>
>>>
>>> mark = User()
Init User


Overload ClassVars
------------------
>>> class Account:
...     firstname = 'Mark'
...     lastname = 'Watney'
...     group = None
>>>
>>>
>>> class User(Account):
...     group = 'admins'
>>>
>>>
>>> mark = User()
>>>
>>> mark.firstname
'Mark'
>>> mark.lastname
'Watney'
>>> mark.group
'admins'


Overload Attribute
------------------
>>> class Account:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.group = None
>>>
>>>
>>> class User(Account):
...     def __init__(self):
...         self.group = 'admins'
>>>
>>>
>>> mark = User()
>>> vars(mark)
{'group': 'admins'}


Assignments
-----------
.. todo:: Assignments
