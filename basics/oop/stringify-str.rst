OOP Stringify Str
=================
* Dedicated for end-user of your class
* Calling function ``print(obj)`` calls ``str(obj)``
* Calling function ``str(obj)`` calls ``obj.__str__()``
* Calling ``f'{obj}'`` calls ``obj.__str__()``
* Calling ``f'{obj!s}'`` calls ``obj.__str__()``
* Method ``obj.__str__()`` must return ``str``


Without Method
--------------
Object without ``__str__()`` method overloaded prints their memory address:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> mark = User('Mark', 'Watney')

>>> print(mark)  # doctest: +SKIP
<__main__.User object at 0x10aef7450>

>>> str(mark)  # doctest: +SKIP
'<__main__.User object at 0x10aef7450>'

>>> mark.__str__()  # doctest: +SKIP
'<__main__.User object at 0x10aef7450>'

>>> f'{mark}'  # doctest: +SKIP
'<__main__.User object at 0x10aef7450>'

>>> f'{mark!s}'  # doctest: +SKIP
'<__main__.User object at 0x10aef7450>'


Overloaded
----------
Objects can verbose print if ``__str__()`` method is present:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __str__(self):
...         return f'{self.firstname} {self.lastname}'
...
>>> mark = User('Mark', 'Watney')

>>> print(mark)
Mark Watney

>>> str(mark)
'Mark Watney'

>>> mark.__str__()
'Mark Watney'

>>> f'{mark}'
'Mark Watney'

>>> f'{mark!s}'
'Mark Watney'


Assignments
-----------
.. literalinclude:: assignments/oop_stringify_a.py
    :caption: :download:`Solution <assignments/oop_stringify_a.py>`
    :end-before: # Solution
