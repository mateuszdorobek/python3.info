Block Else
==========
* Unconditional Alternative
* Optional
* Executed when condition is not met


Syntax
------
>>> # doctest: +SKIP
... if <condition>:
...     <do something>
... else:
...     <do something>


SetUp
-----
Simulate user input (for test automation)

>>> from unittest.mock import MagicMock
>>> input = MagicMock(side_effect=[''])


Oneline Block
-------------
>>> if True:
...     print('True statement')
... else:
...     print('Else statement')
True statement


Multiline Block
---------------
>>> if True:
...     print('True statement, first line')
...     print('True statement, second line')
... else:
...     print('Else statement, first line')
...     print('Else statement, second line')
True statement, first line
True statement, second line


Nested Blocks
-------------
>>> if True:
...     print('Outer block, true statement, first line')
...     print('Outer block, true statement, second line')
...
...     if True:
...         print('Inner block, true statement, first line')
...         print('Inner block, true statement, second line')
...     else:
...         print('Inner block, else statement, fist line')
...         print('Inner block, else statement, second line')
...
... else:
...     print('Outer block, else statement, first line')
...     print('Outer block, else statement, second line')
Outer block, true statement, first line
Outer block, true statement, second line
Inner block, true statement, first line
Inner block, true statement, second line


Value Check
-----------
>>> age = 40
>>>
>>> if age >= 18:
...     print('adult')
... else:
...     print('minor')
...
adult

Note, that in Poland you are an adult when above 18 years old.


Conditional Assignment
----------------------
>>> age = 40
>>>
>>> if age >= 18:
...     adult = True
... else:
...     adult = False
>>>
>>> print(adult)
True

Note, that in Poland you are an adult when above 18 years old.


Checking If Empty
-----------------
>>> age = input('What is your age?: ')  #input: '' (nothing)
>>>
>>> if not age:
...     print('Did you enter your age correctly?')
...
Did you enter your age correctly?


Membership
----------
>>> admins = ['mwatney', 'mlewis', 'rmartinez']
>>> login = 'avogel'

>>> if login in admins:
...     is_admin = True
... else:
...     is_admin = False


Use Case - 0x01
---------------
>>> number = 5
>>>
>>> if number % 2 == 0:
...     print('even')
... else:
...     print('odd')
odd


Use Case - 0x01
---------------
>>> country = 'USA'
>>>
>>> if country == 'USA':
...     job = 'astronaut'
... else:
...     job = 'cosmonaut'
>>>
>>> print(job)
astronaut


Use Case - 0x02
---------------
>>> data = [True, False, True]
>>>
>>> if any(data):
...     print('Yes')
... else:
...     print('No')
...
Yes


Use Case - 0x03
---------------
>>> data = [True, False, True]
>>>
>>> if all(data):
...     print('Yes')
... else:
...     print('No')
...
No


Assignments
-----------
.. literalinclude:: assignments/conditional_else_a.py
    :caption: :download:`Solution <assignments/conditional_else_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/conditional_else_b.py
    :caption: :download:`Solution <assignments/conditional_else_b.py>`
    :end-before: # Solution
