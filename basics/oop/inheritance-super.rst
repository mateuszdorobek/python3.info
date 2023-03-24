OOP Inheritance Super
=====================
* ``super()`` Calls a method from superclass
* Order/location is important
* Raymond Hettinger - Super considered super! - PyCon 2015 [#Hettinger2015]_


Super With Methods
------------------
>>> class User:
...     def say_hello(self):
...         print(f'User says hello')

Defining method with the same name will overload one inherited from
superclass.

>>> class Admin(User):
...     def say_hello(self):
...         print(f'Admin says hello')
...
>>> mark = Admin()
>>> mark.say_hello()
Admin says hello

Order of ``super()`` is important:

>>> class Admin(User):
...     def say_hello(self):
...         super().say_hello()
...         print(f'Admin says hello')
>>>
>>>
>>> mark = Admin()
>>> mark.say_hello()
User says hello
Admin says hello

>>> class Admin(User):
...     def say_hello(self):
...         print(f'Admin says hello')
...         super().say_hello()
>>>
>>>
>>> mark = Admin()
>>> mark.say_hello()
Admin says hello
User says hello


Super With Attributes
---------------------
>>> class User:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.is_admin = False

Without ``super()``:

>>> class Admin(User):
...     def __init__(self):
...         self.is_admin = True
...
>>>
>>> mark = Admin()
>>> vars(mark)
{'is_admin': True}

With ``super()`` first:

>>> class Admin(User):
...     def __init__(self):
...         super().__init__()
...         self.is_admin = True
...
>>> mark = Admin()
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'is_admin': True}

With ``super()`` last (will override child's attributes):

>>> class Admin(User):
...     def __init__(self):
...         self.is_admin = True
...         super().__init__()
...
>>>
>>> mark = Admin()
>>> mark.is_admin
False


Super Init with Args
--------------------
>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.is_admin = False
>>>
>>>
>>> class Admin(User):
...     def __init__(self, firstname, lastname):
...         super().__init__(firstname, lastname)
...         self.is_admin = True
>>>
>>>
>>> mark = Admin('Mark', 'Watney')
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'is_admin': True}


References
----------
.. [#Hettinger2015] https://www.youtube.com/watch?v=EiOglTERPEo


Assignments
-----------
.. literalinclude:: assignments/oop_inheritance_super_a.py
    :caption: :download:`Solution <assignments/oop_inheritance_super_a.py>`
    :end-before: # Solution
