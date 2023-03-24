OOP Init Define
===============
* ``__init__()`` - initializer method
* It's a first method run after object is initiated
* All classes has default ``__init__()``

.. glossary::

    constructor
        Method called at object instantiation used to create object.
        Constructor is called on not fully initialized object and hence
        do not have access to object methods. Constructor should return
        ``None``.

    initializer
        Method called at object instantiation used to fill empty object
        with values. Initializer is called upon object initialization
        and hence can modify object and use its methods. Initializer
        should return ``None``.


Without Arguments
-----------------
Initializer method without arguments:

>>> class User:
...     def __init__(self):
...         print('Hello')
>>>
>>>
>>> mark = User()
Hello


Required Parameters
-------------------
>>> class User:
...     def __init__(self, firstname, lastname):
...         print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> mark = User()
Traceback (most recent call last):
TypeError: User.__init__() missing 2 required positional arguments: 'firstname' and 'lastname'

>>> class User:
...     def __init__(self, firstname, lastname):
...         print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> mark = User('Mark', 'Watney')
Hello Mark Watney
>>>
>>> mark = User(firstname='Mark', lastname='Watney')
Hello Mark Watney


Optional Parameters
-------------------
>>> class User:
...     def __init__(self, firstname=None, lastname=None):
...         print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> mark = User('Mark', 'Watney')
Hello Mark Watney
>>>
>>> mark = User('Mark')
Hello Mark None
>>>
>>> mark = User()
Hello None None


Assignments
-----------
.. literalinclude:: assignments/oop_init_define_a.py
    :caption: :download:`Solution <assignments/oop_init_define_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_init_define_b.py
    :caption: :download:`Solution <assignments/oop_init_define_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_init_define_c.py
    :caption: :download:`Solution <assignments/oop_init_define_b.py>`
    :end-before: # Solution
