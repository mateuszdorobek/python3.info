OOP Stringify Repr
==================
* Calling function ``repr(obj)`` calls ``obj.__repr__()``
* Method ``obj.__repr__()`` must return ``str``
* Dedicated for developers
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
...
...
>>> mark = User('Mark', 'Watney')

>>> mark  # doctest: +SKIP
<__main__.User object at 0x10aef7450>

>>> repr(mark)  # doctest: +SKIP
'<__main__.User object at 0x10aef7450>'

>>> mark.__repr__()  # doctest: +SKIP
'<__main__.User object at 0x10aef7450>'

>>> f'{mark!r}'  # doctest: +SKIP
'<__main__.User object at 0x10aef7450>'


Overloaded
----------
>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __repr__(self):
...         firstname = self.firstname
...         lastname = self.lastname
...         return f'User({firstname=}, {lastname=})'
...
...
>>> mark = User('Mark', 'Watney')

>>> mark
User(firstname='Mark', lastname='Watney')

>>> repr(mark)
"User(firstname='Mark', lastname='Watney')"

>>> mark.__repr__()
"User(firstname='Mark', lastname='Watney')"

>>> f'{mark!r}'
"User(firstname='Mark', lastname='Watney')"


Assignments
-----------
.. literalinclude:: assignments/oop_stringify_b.py
    :caption: :download:`Solution <assignments/oop_stringify_b.py>`
    :end-before: # Solution
