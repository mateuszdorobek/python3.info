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

Chained unpacking assignment:

>>> a, b = c, d = 1, 2


Example
-------
>>> def get_user_details(username):
...     return 'Mark', 'Watney', 'mwatney@nasa.gov'
>>>
>>>
>>> firstname, lastname, email = get_user_details('mwatney')
>>>
>>> firstname
'Mark'
>>>
>>> lastname
'Watney'
>>>
>>> email
'mwatney@nasa.gov'


Assignment
----------
* Scalar Assignment
* ``identifier = object``
* ``a = 1``
* ``a = 1, 2``

>>> a = 1
>>>
>>> print(f'{a=}')
a=1

>>> a = 1, 2
>>>
>>> print(f'{a=}')
a=(1, 2)


Unpacking Assignment
--------------------
* ``iterable[identifier] = iterable[object]``
* ``a, b = 1, 2``
* ``a, b, c = 1, 2, 3``
* Sequence -> tuple, list
* Iterable -> tuple, list, set, frozenset, dict, ...
* Length at right and left side must be the same

>>> a, b = 1, 2
>>>
>>> print(f'{a=}, {b=}')
a=1, b=2

>>> a, = 1,
>>> a, b = 1, 2
>>> a, b, c = 1, 2, 3
>>> a, b, c, d = 1, 2, 3, 4
>>> a, b, c, d, e = 1, 2, 3, 4, 5

>>> a, b, c = 1, 2
Traceback (most recent call last):
ValueError: not enough values to unpack (expected 3, got 2)

>>> a, b, c = 1, 2, 3, 4
Traceback (most recent call last):
ValueError: too many values to unpack (expected 3)


Chained Assignment
------------------
* ``identifier1 = identifier2 = object``
* ``a = b = 1``
* ``a = b = c = 1``

>>> a = b = 1
>>>
>>> print(f'{a=}, {b=}')
a=1, b=1

>>> a = b = 1
>>> a = b = c = 1
>>> a = b = c = d = 1
>>> a = b = c = d = e = 1


Chained Unpacking Assignment
----------------------------
* ``iterable[identifier] = iterable[identifier] = iterable[object]``

>>> a, b = c, d = 1, 2
>>>
>>> print(f'{a=}, {b=}, {c=}, {d=}')
a=1, b=2, c=1, d=2

>>> a = b, c = 1, 2
>>>
>>> print(f'{a=}, {b=}, {c=}')
a=(1, 2), b=1, c=2


Brackets
--------
Brackets does not define tuple, commas do:

>>> a = 1, 2, 3
>>> b = (1, 2, 3)
>>>
>>> a == b
True

>>> a = (1, 2)
>>> type(a)
<class 'tuple'>
>>>
>>> a = 1, 2
>>> type(a)
<class 'tuple'>

>>> 1+2 * 3
7
>>>
>>> (1+2) * 3
9
>>>
>>> (1+2,) * 3
(3, 3, 3)

Right-Side Brackets:

>>> a, b, c = 1, 2, 3
>>> a, b, c = (1, 2, 3)
>>> a, b, c = [1, 2, 3]
>>> a, b, c = {1, 2, 3}

Left-Side Brackets:

>>> (a, b, c) = 1, 2, 3
>>> [a, b, c] = 1, 2, 3
>>> {a, b, c} = 1, 2, 3
Traceback (most recent call last):
SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?

Warning:

>>> (a) = 1
>>> (a,) = 1,

Errors:

>>> (a,) = 1
Traceback (most recent call last):
TypeError: cannot unpack non-iterable int object

>>> [a] = 1
Traceback (most recent call last):
TypeError: cannot unpack non-iterable int object


Swap
----
* Swap two variables

>>> a = 1
>>> b = 2
>>>
>>> a, b = b, a
>>>
>>> a
2
>>> b
1


Unpacking
---------
>>> def get_user():
...     return 'Mark', 'Watney', 'mwatney@nasa.gov'

>>> get_user()
('Mark', 'Watney', 'mwatney@nasa.gov')

>>> user = get_user()
>>>
>>> print(user)
('Mark', 'Watney', 'mwatney@nasa.gov')

>>> firstname, lastname, email = get_user()
>>>
>>> print(firstname)
Mark
>>>
>>> print(lastname)
Watney
>>>
>>> print(email)
mwatney@nasa.gov


Nested
------
>>> def get_user():
...     return 'Mark', 'Watney', ('mwatney@nasa.gov', 'mwatney@gmail.com')

>>> firstname, lastname, emails = get_user()
>>>
>>> print(emails)
('mwatney@nasa.gov', 'mwatney@gmail.com')

>>> firstname, lastname, (email_work, email_home) = get_user()
>>>
>>> print(email_work)
mwatney@nasa.gov
>>>
>>> print(email_home)
mwatney@gmail.com

>>> firstname, lastname, email_work, email_home = get_user()
Traceback (most recent call last):
ValueError: not enough values to unpack (expected 4, got 3)


Skipping Values
---------------
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future

>>> _ = 'Mark'
>>> print(_)
Mark

>>> def get_user():
...     return 'Mark', 'Watney', 'mwatney@nasa.gov'
>>>
>>>
>>> firstname, lastname, email = get_user()
>>> firstname, lastname, _ = get_user()
>>> firstname, _, _ = get_user()
>>> _, lastname, _ = get_user()
>>> _, _, email = get_user()


Copy Deep vs Reference
----------------------
>>> a = b = 1
>>> a
1
>>> b
1
>>>
>>> a = 2
>>> a
2
>>> b
1

>>> a = b = [1, 2]
>>>
>>> a
[1, 2]
>>> b
[1, 2]
>>>
>>> a.append(3)
>>>
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]


Use Case - 0x01
---------------
>>> a, b, c = range(0, 3)
>>> a, b, c, d, e = range(0, 5)
>>> a, b, c, d, e, f, g, h, i, j = range(0, 10)


Use Case - 0x02
---------------
>>> import sys
>>>
>>> major, minor, patch, *_ = sys.version_info
>>>
>>>
>>> print(major)
3
>>>
>>> print(minor)
11


Use Case - 0x03
---------------
* Line from ``/etc/passwd``

>>> line = 'watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash'
>>> username, _, uid, _, _, _, _ = line.split(':')
>>>
>>> print(f'{username=}, {uid=}')
username='watney', uid='1000'


Use Case - 0x04
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


Use Case - 0x05
---------------
>>> row = (5.8, 2.7, 5.1, 1.9, 'virginica')

>>> sl = row[0]
>>> sw = row[1]
>>> pl = row[2]
>>> pw = row[3]
>>> species = row[4]
>>>
>>> print(f'{sl=}, {sw=}, {pl=}, {pw=}, {species=}')
sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica'

>>> sl, sw, pl, pw, species = row
>>>
>>> print(f'{sl=}, {sw=}, {pl=}, {pw=}, {species=}')
sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica'


Use Case - 0x06
---------------
>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
... ]

>>> for row in DATA:
...     sl = row[0]
...     sw = row[1]
...     pl = row[2]
...     pw = row[3]
...     species = row[4]
...     print(f'{sl=}, {sw=}, {pl=}, {pw=}, {species=}')
sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica'
sl=5.1, sw=3.5, pl=1.4, pw=0.2, species='setosa'
sl=5.7, sw=2.8, pl=4.1, pw=1.3, species='versicolor'

>>> for sl, sw, pl, pw, species in DATA:
...     print(f'{sl=}, {sw=}, {pl=}, {pw=}, {species=}')
sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica'
sl=5.1, sw=3.5, pl=1.4, pw=0.2, species='setosa'
sl=5.7, sw=2.8, pl=4.1, pw=1.3, species='versicolor'


Recap
-----
* Four types of assignments: Scalar, Unpacking, Chained, Chained Unpacking Assignment
* For unpacking assignment, lengths at both sides must be the same
* Both left and right expression side brackets are optional
* Unpacking nested sequences
* Skipping values is done by using ``_``

Assignment:

>>> a = 1

Unpacking assignment:

>>> a, b = 1, 2

Chained assignment:

>>> a = b = 1

Chained unpacking assignment:

>>> a, b = c, d = 1, 2

Unpacking nested:

>>> a, (b, c) = 1, (2, 3)

Skipping:

>>> _, (important, _) = 1, (2, 3)


Assignments
-----------
.. literalinclude:: assignments/unpack_assignment_a.py
    :caption: :download:`Solution <assignments/unpack_assignment_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_assignment_b.py
    :caption: :download:`Solution <assignments/unpack_assignment_b.py>`
    :end-before: # Solution
