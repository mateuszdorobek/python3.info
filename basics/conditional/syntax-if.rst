Block If
========


Syntax
------
>>> # doctest: +SKIP
... if <condition>:
...     <do something>


SetUp
-----
Simulate user input (for test automation):

>>> from unittest.mock import MagicMock
>>> input = MagicMock(side_effect=['Mark Watney', ''])


Oneline Block
-------------
>>> if True:
...     print('First line of the true statement')
First line of the true statement


Multiline Blocks
----------------
>>> if True:
...     print('First line of the true statement')
...     print('Second line of the true statement')
...     print('Third line of the true statement')
First line of the true statement
Second line of the true statement
Third line of the true statement


Nested Blocks
-------------
>>> if True:
...     print('First line of the true statement')
...     print('Second line of the true statement')
...     if True:
...         print('First line of inner true statement')
First line of the true statement
Second line of the true statement
First line of inner true statement


Deeply Nested Blocks
--------------------
>>> if True:
...     print('a')
...     print('b')
...     if True:
...         print('c')
...         print('d')
...         if True:
...             print('e')
...             if True:
...                 print('f')
...     if True:
...         print('g')
...         print('h')
...     print('i')
...     print('j')
a
b
c
d
e
f
g
h
i
j


Value Check
-----------
>>> age = 42
>>>
>>> if age >= 18:
...     print('adult')
adult


Boundary Check
--------------
>>> age = 7
>>>
>>> if 0 <= age < 18:
...     print('Age is between 0 and 18')
Age is between 0 and 18

Is equivalent to:

>>> age = 7
>>>
>>> if 0 <= age and age < 18:
...     print('Age is between 0 and 18')
Age is between 0 and 18


Nested Boundary Check
---------------------
Checking if value is in range:

>>> a = 10
>>> b = 100
>>>
>>> if 0 <= a <= 50 < b:
...     print('Yes')
Yes


Checking If Empty
-----------------
>>> name = input('What is your name?: ')  #input: Mark Watney
>>>
>>> if name:
...     print(f'My name is... {name}')
My name is... Mark Watney

Note, that following code is very error prone:

>>> name = input('What is your name?: ')  #input:
>>>
>>> if name is None:
...     print('Name is empty')

This will never print "Name is empty" because if user will not type any data
just only hit the return key, variable name will hold an empty string not
a ``None`` value!

>>> name
''


Conditional Assignment
----------------------
* Define variable based on evaluation

>>> country = 'USA'
>>>
>>> if country == 'USA':
...     job = 'astronaut'
>>>
>>> print(job)
astronaut


Use Case - 0x01
---------------
* Even

>>> number = 4
>>>
>>> if number % 2 == 0:
...     print('even')
even


.. todo:: Assignments
