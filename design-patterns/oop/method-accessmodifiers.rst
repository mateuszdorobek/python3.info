OOP Method Access Modifiers
===========================
* Attributes and methods are always public
* No protected and private keywords
* Protecting is only by convention [#pydocprivatevar]_
* ``name(self)`` - public method
* ``_name(self)`` - protected method (non-public by convention)
* ``__name(self)`` - private method (name mangling)
* ``__name__(self)`` - system method
* ``name_(self)`` - avoid name collision


Protected Method
----------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     _firstname: str
...     _lastname: str
...
...     def _get_fullname(self):
...         return f'{self._firstname} {self._lastname}'
...
...     def get_publicname(self):
...         return f'{self._firstname} {self._lastname[0]}.'
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> mark._get_fullname()  # IDE should warn: "Access to a protected member _get_fullname of a class"
'Mark Watney'


Private Method
--------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self._firstname = firstname
...         self._lastname = lastname
...
...     def __get_fullname(self):
...         return f'{self._firstname} {self._lastname}'
...
...     def get_publicname(self):
...         return f'{self._firstname} {self._lastname[0]}.'
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>>
>>> mark.__get_fullname()
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__get_fullname'
>>>
>>> mark._Astronaut__get_fullname()  # IDE should warn: "Access to a protected member _Astronaut__get_fullname of a class"
'Mark Watney'


System Method
-------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self._firstname = firstname
...         self._lastname = lastname
...
...     def __str__(self):
...         return 'stringification'
...
...     def __repr__(self):
...         return 'representation'
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>>
>>> print(str(mark))
stringification
>>>
>>> print(repr(mark))
representation


Show Methods
------------
* ``dir()``

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self._firstname = firstname
...         self._lastname = lastname
...
...     def __get_fullname(self):
...         return f'{self._firstname} {self._lastname}'
...
...     def get_publicname(self):
...         return f'{self._firstname} {self._lastname[0]}.'
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>>
>>> print(dir(mark))  # doctest: +NORMALIZE_WHITESPACE
['_Astronaut__get_fullname', '__class__', '__delattr__', '__dict__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', '_firstname', '_lastname',
 'get_publicname']
>>>
>>> [method for method in dir(mark) if callable(getattr(mark, method))]  # doctest: +NORMALIZE_WHITESPACE
['_Astronaut__get_fullname', '__class__', '__delattr__', '__dir__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'get_publicname']
>>>
>>> public_methods = [method
...                   for method in dir(mark)
...                   if callable(getattr(mark, method))
...                   and not method.startswith('_')]
>>>
>>> protected_methods = [method
...                      for method in dir(mark)
...                      if callable(getattr(mark, method))
...                      and method.startswith('_')]
>>>
>>> private_methods = [method
...                    for method in dir(mark)
...                    if callable(getattr(mark, method))
...                    and method.startswith(f'_{mark.__class__.__name__}')]
>>>
>>> system_methods = [method
...                   for method in dir(mark)
...                   if callable(getattr(mark, method))
...                   and method.startswith(f'__')
...                   and method.endswith(f'__')]


References
----------
.. [#pydocprivatevar] https://docs.python.org/3/tutorial/classes.html#private-variables


Assignments
-----------
.. todo:: Assignments
