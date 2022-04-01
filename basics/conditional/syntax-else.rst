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
>>> number = 3
>>>
>>> if number % 2 == 0:
...     print('even')
... else:
...     print('odd')
odd


Conditional Assignment
----------------------
>>> number = 3
>>>
>>> if number % 2 == 0:
...     status = 'even'
... else:
...     status = 'odd'
>>>
>>> print(status)
odd


Checking If Empty
-----------------
>>> name = input('What is your name?: ')  #input: '' (nothing)
>>>
>>> if name:
...     print(f'My name is... {name}')
... else:
...     print('Did you forget to type your name?')
Did you forget to type your name?


Use Case - 0x01
---------------
* Cosmonaut

>>> country = 'Russia'
>>>
>>> if country == 'USA':
...     job = 'astronaut'
... else:
...     job = 'cosmonaut'
>>>
>>> print(job)
cosmonaut


Use Case - 0x02
---------------
* Any

>>> data = [True, False, True]
>>>
>>> if any(data):
...     print('Yes')
... else:
...     print('No')
Yes


Use Case - 0x03
---------------
* All

>>> data = [True, False, True]
>>>
>>> if all(data):
...     print('Yes')
... else:
...     print('No')
No


Assignments
-----------
.. literalinclude:: assignments/conditional_else_a.py
    :caption: :download:`Solution <assignments/conditional_else_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/conditional_else_b.py
    :caption: :download:`Solution <assignments/conditional_else_b.py>`
    :end-before: # Solution
