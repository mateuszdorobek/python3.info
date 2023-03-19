Unpack Assignment
=================
* ``a = 1`` - Assignment
* ``a, b = 1, 2`` - Unpacking assignment
* ``a = b = 1`` - Chained assignment
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future

Assignment:

>>> a = 1

Unpacking assignment:

>>> a, b = 1, 2

Chained assignment:

>>> a = b = 1


Assignment
----------
* ``identifier = value``
* ``a = 1``
* Scalar Assignment

>>> a = 1
>>>
>>> print(f'{a=}')
a=1


Unpacking Assignment
--------------------
* ``sequence[identifier] = sequence[value]``
* ``a, b = 1, 2``
* Vector Assignment
* Sequence Assignment

>>> a, b = 1, 2
>>>
>>> print(f'{a=}, {b=}')
a=1, b=2

>>> a, b = 1, 2
>>> a, b, c = 1, 2, 3
>>> a, b, c, d = 1, 2, 3, 4
>>> a, b, c, d, e = 1, 2, 3, 4, 5


Chained Assignment
------------------
* ``a = b = 1``
* ``identifier1 = identifier2 = value``

>>> a = b = 1
>>>
>>> print(f'{a=}, {b=}')
a=1, b=1

>>> a = b = 1
>>> a = b = c = 1
>>> a = b = c = d = 1
>>> a = b = c = d = e = 1


Right-Side Brackets
-------------------
Scalar assignments:

>>> a = 1, 2
>>> a = (1, 2)
>>> a = [1, 2]
>>> a = {1, 2}

Unpacking assignments:

>>> a, b = 1, 2
>>> a, b = (1, 2)
>>> a, b = [1, 2]
>>> a, b = {1, 2}

Rationale:

>>> a, b = 1, 2
>>> a, b = (1, 2)


Left-Side Brackets
------------------
>>> (a) = (1)
>>>
>>> print(a)
1

>>> (a, b) = 1, 2
>>> (a, b) = (1, 2)

>>> (a, b, c) = (1, 2, 3)
>>> (a, b, c) = (1, 2, 3)
>>> (a, b, c) = [1, 2, 3]

>>> [a, b, c] = [1, 2, 3]
>>> [a, b, c] = (1, 2, 3)


Errors
------
>>> a, b, c = 1, 2, 3, 4
Traceback (most recent call last):
ValueError: too many values to unpack (expected 3)

>>> a, b, c = 1, 2
Traceback (most recent call last):
ValueError: not enough values to unpack (expected 3, got 2)

>>> {a, b, c} = {1, 2, 3}
Traceback (most recent call last):
SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?

>>> {a, b, c} = 1, 2, 3
Traceback (most recent call last):
SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?


Unpacking
---------
>>> data = [1, 2, 3]
>>> a, b, c = data
>>>
>>> print(f'{a=}, {b=}, {c=}')
a=1, b=2, c=3

>>> line = 'Mark,Watney,40'
>>> firstname, lastname, age = line.split(',')
>>>
>>> print(f'{firstname=}, {lastname=}, {age=}')
firstname='Mark', lastname='Watney', age='40'

>>> data = ['Mark', 'Watney', ('mwatney@nasa.gov', 'mwatney@gmail.com')]
>>> firstname, lastname, emails = data
>>>
>>> print(f'{firstname=}\n{lastname=}\n{emails=}')
firstname='Mark'
lastname='Watney'
emails=('mwatney@nasa.gov', 'mwatney@gmail.com')


Nested
------
>>> a, (b, c) = [1, (2, 3)]
>>>
>>> print(f'{a=}, {b=}, {c=}')
a=1, b=2, c=3

>>> data = ['Mark', 'Watney', ('mwatney@nasa.gov', 'mwatney@gmail.com')]
>>> firstname, lastname, (email_work, email_home) = data
>>>
>>> print(f'{firstname=}\n{lastname=}\n{email_work=}\n{email_home=}')
firstname='Mark'
lastname='Watney'
email_work='mwatney@nasa.gov'
email_home='mwatney@gmail.com'


Skipping Values
---------------
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future

>>> _ = 'Mark Watney'
>>>
>>> print(_)
Mark Watney

>>> line = 'Mark,Watney,40'
>>> firstname, lastname, _ = line.split(',')
>>>
>>> print(f'{firstname=}, {lastname=}')
firstname='Mark', lastname='Watney'

>>> line = 'Mark,Watney,40,185,75.5'
>>> firstname, lastname, _, _, _ = line.split(',')
>>>
>>> print(f'{firstname=}, {lastname=}')
firstname='Mark', lastname='Watney'


Use Case - 0x01
---------------
* Skip

>>> a, b, _ = 'red', 'green', 'blue'
>>> a, _, _ = 'red', 'green', 'blue'
>>> a, _, c = 'red', 'green', 'blue'
>>> _, b, _ = 'red', 'green', 'blue'
>>> _, _, c = 'red', 'green', 'blue'


Use Case - 0x02
---------------
* Passwd

>>> line = 'watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash'
>>> username, _, uid, _, _, _, _ = line.split(':')
>>>
>>> print(f'{username=}, {uid=}')
username='watney', uid='1000'


Use Case - 0x03
---------------
* Important

>>> _, important, _ = 1, 2, 3
>>>
>>> print(important)
2

>>> _, (important, _) = [1, (2, 3)]
>>>
>>> print(important)
2

>>> _, _, important = (True, [1, 2, 3, 4], 5)
>>>
>>> print(important)
5

>>> _, _,  important = (True, [1, 2, 3, 4], (5, True))
>>>
>>> print(important)
(5, True)
>>>
>>> _, _, (important, _) = (True, [1, 2, 3, 4], (5, True))
>>>
>>> print(important)
5

Python understands this as:

>>> _ = (True, [1, 2, 3, 4], (5, True))
>>>
>>> a,b,c = (object, object, object)
>>> a,b,(c,d) = (object, object, (object,object))


Recap
-----
* Scalar, unpacking assignment, chained assignment
* Both left and right expression side brackets are optional
* Unpacking nested sequences
* Skipping values is done by using ``_``

Scalar assignment:

>>> a = 1

Unpacking assignment:

>>> a, b = 1, 2

Chained assignment:

>>> a = b = 1

Unpacking nested:

>>> a, (b, c) = 1, (2, 3)

Skipping:

>>> _, (important, _) = 1, (2, 3)


Assignments
-----------
.. literalinclude:: assignments/sequence_unpack_a.py
    :caption: :download:`Solution <assignments/sequence_unpack_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_unpack_b.py
    :caption: :download:`Solution <assignments/sequence_unpack_b.py>`
    :end-before: # Solution
