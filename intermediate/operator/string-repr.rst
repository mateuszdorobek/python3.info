Operator String Repr
====================
* Typing ``obj`` into REPL (console) calls ``repr(obj)``
* Calling ``repr(obj)`` calls ``obj.__repr__()``
* Method ``obj.__repr__()`` must return ``str``
* Intended for developers of your class
* Shows object representation
* Copy-paste for creating object with the same values
* Useful for debugging
* Printing ``list`` will call ``__repr__()`` method on each element


Inherited
---------
Object without ``__repr__()`` method overloaded prints their memory address:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>>
>>> mark  # doctest: +ELLIPSIS
<__main__.User object at 0x...>
>>>
>>> repr(mark)  # doctest: +ELLIPSIS
'<__main__.User object at 0x...>'
>>>
>>> mark.__repr__()  # doctest: +ELLIPSIS
'<__main__.User object at 0x...>'


Overloaded
----------
>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __repr__(self):
...         clsname = self.__class__.__name__
...         firstname = self.firstname
...         lastname = self.lastname
...         return f'{clsname}({firstname=}, {lastname=})'
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>>
>>> mark
User(firstname='Mark', lastname='Watney')
>>>
>>> repr(mark)
"User(firstname='Mark', lastname='Watney')"
>>>
>>> mark.__repr__()
"User(firstname='Mark', lastname='Watney')"


Nested
------
* Printing ``list`` will call ``__repr__()`` method on each element

>>> data = [1,2,3]
>>> print(data)
[1, 2, 3]

>>> class MyClass:
...     def __repr__(self): return 'repr'
...     def __str__(self): return 'str'
>>>
>>> data = [
...     MyClass(),
...     MyClass(),
...     MyClass(),
... ]
>>>
>>> print(data)
[repr, repr, repr]
>>> data
[repr, repr, repr]
>>> str(data)
'[repr, repr, repr]'
>>> repr(data)
'[repr, repr, repr]'


Printing ``list`` will call ``__repr__()`` method on each element:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __repr__(self):
...         return f'{self.firstname} {self.lastname}'
>>>
>>> admins = [
...     User('Mark', 'Watney'),
...     User('Melissa', 'Lewis'),
...     User('Rick', 'Martinez'),
... ]
>>>
>>> print(admins)
[Mark Watney, Melissa Lewis, Rick Martinez]


Assignments
-----------
.. literalinclude:: assignments/operator_string_repr_a.py
    :caption: :download:`Solution <assignments/operator_string_repr_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operator_string_repr_b.py
    :caption: :download:`Solution <assignments/operator_string_repr_b.py>`
    :end-before: # Solution


.. todo:: Assignment: Simple __repr__()
.. todo:: Assignment: Inheritance with __repr__()
