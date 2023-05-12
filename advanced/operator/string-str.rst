Operator String Str
===================
* Calling ``print(obj)`` calls ``str(obj)``
* Calling ``str(obj)`` calls ``obj.__str__()``
* Method ``obj.__str__()`` must return ``str``
* Intended for end-users of your class


Inherited
---------
Object without ``__str__()`` method overloaded prints their memory address:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>>
>>> print(mark)  # doctest: +ELLIPSIS
<__main__.User object at 0x...>
>>>
>>> str(mark)  # doctest: +ELLIPSIS
'<__main__.User object at 0x...>'
>>>
>>> mark.__str__()  # doctest: +ELLIPSIS
'<__main__.User object at 0x...>'


Overloaded
----------
Objects can verbose print if ``__str__()`` method is present:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __str__(self):
...         return f'Hello {self.firstname} {self.lastname}'
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>>
>>> print(mark)
Hello Mark Watney
>>>
>>> str(mark)
'Hello Mark Watney'
>>>
>>> mark.__str__()
'Hello Mark Watney'


Assignments
-----------
.. literalinclude:: assignments/operator_string_str_a.py
    :caption: :download:`Solution <assignments/operator_string_str_a.py>`
    :end-before: # Solution
