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

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> astro  # doctest: +ELLIPSIS
<__main__.Astronaut object at 0x...>
>>>
>>> repr(astro)  # doctest: +ELLIPSIS
'<__main__.Astronaut object at 0x...>'
>>>
>>> astro.__repr__()  # doctest: +ELLIPSIS
'<__main__.Astronaut object at 0x...>'


Overloaded
----------
>>> class Astronaut:
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
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> astro
Astronaut(firstname='Mark', lastname='Watney')
>>>
>>> repr(astro)
"Astronaut(firstname='Mark', lastname='Watney')"
>>>
>>> astro.__repr__()
"Astronaut(firstname='Mark', lastname='Watney')"


Nested
------
* Printing ``list`` will call ``__repr__()`` method on each element

>>> data = [1,2,3]
>>> print(data)
[1, 2, 3]

Printing ``list`` will call ``__repr__()`` method on each element:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> crew = [Astronaut('Mark Watney'),
...         Astronaut('Melissa Lewis'),
...         Astronaut('Rick Martinez')]
>>>
>>> print(crew)  # doctest: +ELLIPSIS
[<__main__.Astronaut object at 0x...>, <__main__.Astronaut object at 0x...>, <__main__.Astronaut object at 0x...>]

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def __repr__(self):
...         return f'{self.name}'
>>>
>>> crew = [Astronaut('Mark Watney'),
...         Astronaut('Melissa Lewis'),
...         Astronaut('Rick Martinez')]
>>>
>>> print(crew)
[Mark Watney, Melissa Lewis, Rick Martinez]


Assignments
-----------
.. literalinclude:: assignments/operator_string_repr_a.py
    :caption: :download:`Solution <assignments/operator_string_repr_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operator_string_repr_b.py
    :caption: :download:`Solution <assignments/operator_string_repr_b.py>`
    :end-before: # Solution

.. todo:: dorobić zadanie z dziedziczeniem REPR
