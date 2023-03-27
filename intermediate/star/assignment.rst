Star Assignment
===============
* ``a, b, *c = 1, 2, 3, 4, 5``
* Used when there is arbitrary number of values to unpack
* Could be used from start, middle, end
* There can't be multiple star expressions in one assignment statement
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future

.. figure:: img/unpack-assignment,args,params.png


Example
-------
>>> def get_user_details(username):
...     return 'Mark', 'Watney', 'mwatney@nasa.gov', 'mwatney@esa.int', 'mwatney@polsa.gov.pl'
>>>
>>>
>>> firstname, lastname, *email = get_user_details('mwatney')
>>>
>>> firstname
'Mark'
>>>
>>> lastname
'Watney'
>>>
>>> email
['mwatney@nasa.gov', 'mwatney@esa.int', 'mwatney@polsa.gov.pl']


Arbitrary Number of Arguments
-----------------------------
Unpack values at the right side:

>>> a, b, *c = [1, 2, 3, 4, 5]
>>>
>>> print(f'{a=}, {b=}, {c=}')
a=1, b=2, c=[3, 4, 5]

Unpack values at the left side:

>>> *a, b, c = [1, 2, 3, 4, 5]
>>>
>>> print(f'{a=}, {b=}, {c=}')
a=[1, 2, 3], b=4, c=5

Unpack values from both sides at once:

>>> a, *b, c = [1, 2, 3, 4, 5]
>>>
>>> print(f'{a=}, {b=}, {c=}')
a=1, b=[2, 3, 4], c=5

Unpack from variable length:

>>> a, *b, c = [1, 2]
>>>
>>> print(f'{a=}, {b=}, {c=}')
a=1, b=[], c=2


Errors
------
Cannot unpack from both sides at once:

>>> *a, b, *c = [1, 2, 3, 4, 5]
Traceback (most recent call last):
SyntaxError: multiple starred expressions in assignment

Unpack requires values for required arguments:

>>> a, *b, c = [1]
Traceback (most recent call last):
ValueError: not enough values to unpack (expected at least 2, got 1)


Skipping Values
---------------
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future

>>> _ = 'Mark Watney'
>>>
>>> print(_)
Mark Watney

>>> line = 'Mark,Watney,mwatney@nasa.gov,mwatney@esa.int,mwatney@polsa.gov.pl'
>>> firstname, lastname, *_ = line.split(',')
>>>
>>> print(f'{firstname=}, {lastname=}')
firstname='Mark', lastname='Watney'

>>> line = '4.9,3.1,1.5,0.1,setosa'
>>> *_, label = line.split(',')
>>>
>>> print(f'{label=}')
label='setosa'

>>> line = 'watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash'
>>> username, _, uid, *_ = line.split(':')
>>>
>>> print(f'{username=}, {uid=}')
username='watney', uid='1000'


For Loop Unpacking
------------------
>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
... ]

>>> for row in DATA:
...     print(f'{row=}')
...
row=(5.8, 2.7, 5.1, 1.9, 'virginica')
row=(5.1, 3.5, 1.4, 0.2, 'setosa')
row=(5.7, 2.8, 4.1, 1.3, 'versicolor')

>>> for row in DATA:
...     values = row[0:4]
...     species = row[-1]
...     print(f'{values=}, {species=}')
...
values=(5.8, 2.7, 5.1, 1.9), species='virginica'
values=(5.1, 3.5, 1.4, 0.2), species='setosa'
values=(5.7, 2.8, 4.1, 1.3), species='versicolor'

>>> for row in DATA:
...     *values, species = row
...     print(f'{values=}, {species=}')
...
values=[5.8, 2.7, 5.1, 1.9], species='virginica'
values=[5.1, 3.5, 1.4, 0.2], species='setosa'
values=[5.7, 2.8, 4.1, 1.3], species='versicolor'

>>> for *values, species in DATA:
...     print(f'{values=}, {species=}')
...
values=[5.8, 2.7, 5.1, 1.9], species='virginica'
values=[5.1, 3.5, 1.4, 0.2], species='setosa'
values=[5.7, 2.8, 4.1, 1.3], species='versicolor'


Multi Dimensional
-----------------
>>> from pprint import pprint

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
... ]

>>> header = DATA[0]
>>> rows = DATA[1:]
>>>
>>> pprint(header)
('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')
>>>
>>> pprint(rows)
[(5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor')]

>>> header, *rows = DATA
>>>
>>> pprint(header)
('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')
>>>
>>> pprint(rows)
[(5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor')]


Merge
-----
>>> def echo(**a, **b):
...     return locals()
Traceback (most recent call last):
SyntaxError: arguments cannot follow var-keyword argument


Use Case - 0x01
---------------
>>> a, b, c = range(0, 3)
>>> a, b, c, d, e = range(0, 5)
>>> a, b, *c = range(0, 10)


Use Case - 0x01
---------------
>>> line = 'ares3,watney,lewis,vogel,johanssen'
>>> mission, *crew = line.split(',')
>>>
>>> print(f'{mission=}, {crew=}')
mission='ares3', crew=['watney', 'lewis', 'vogel', 'johanssen']


Use Case - 0x02
---------------
>>> first, *middle, last = [1, 2, 3, 4]
>>>
>>> print(f'{first=}, {middle=}, {last=}')
first=1, middle=[2, 3], last=4

>>> first, second, *others = [1, 2, 3, 4]
>>>
>>> print(f'{first=}, {second=}, {others=}')
first=1, second=2, others=[3, 4]


Use Case - 0x03
---------------
>>> first, second, *others = range(0,10)
>>>
>>> print(f'{first=}, {second=}, {others=}')
first=0, second=1, others=[2, 3, 4, 5, 6, 7, 8, 9]

>>> first, second, *_ = range(0,10)
>>>
>>> print(f'{first=}, {second=}')
first=0, second=1


Use Case - 0x04
---------------
* Python Version

>>> import sys
>>>
>>>
>>> major, minor, *_ = sys.version_info
>>>
>>> print(major, minor, sep='.')
3.11


Use Case - 0x05
---------------
* Iris 1D

>>> *values, species = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>>
>>> print(f'{values=}, {species=}')
values=[5.8, 2.7, 5.1, 1.9], species='virginica'


Use Case - 0x06
---------------
>>> *values, species = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>> avg = sum(values) / len(values)
>>>
>>> print(f'{avg=:.2f}, {species=}')
avg=3.88, species='virginica'


Use Case - 0x07
---------------
>>> line = '1969-07-21, 02:56:15, WARNING, Neil Armstrong first words on the Moon'
>>> d, t, lvl, *msg = line.split(', ')
>>>
>>> d
'1969-07-21'
>>> t
'02:56:15'
>>> lvl
'WARNING'
>>> msg
['Neil Armstrong first words on the Moon']


Use Case - 0x08
---------------
>>> line = 'watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash'
>>> username, password, uid, *others = line.split(':')
>>>
>>> username
'watney'
>>> password
'x'
>>> uid
'1000'
>>> others
['1000', 'Mark Watney', '/home/watney', '/bin/bash']


Use Case - 0x09
---------------
>>> line = 'watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash'
>>> username, _, uid, *_ = line.split(':')
>>>
>>> username
'watney'
>>> uid
'1000'


Use Case - 0x0A
---------------
>>> line = '4.9,3.1,1.5,0.1,setosa'
>>> *values, species = line.split(',')
>>> values
['4.9', '3.1', '1.5', '0.1']
>>> species
'setosa'


Use Case - 0x0B
---------------
>>> data = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>> *values, species = data
>>> values
[5.8, 2.7, 5.1, 1.9]
>>> species
'virginica'


Use Case - 0x0C
---------------
* Iris 2D

>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
... ]
>>>
>>>
>>> for *values, species in DATA:
...     avg = sum(values) / len(values)
...     print(f'{avg=:.2f} {species=}')
avg=3.88 species='virginica'
avg=2.55 species='setosa'
avg=3.48 species='versicolor'



Assignments
-----------
.. literalinclude:: assignments/star_assignment_a.py
    :caption: :download:`Solution <assignments/star_assignment_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/star_assignment_b.py
    :caption: :download:`Solution <assignments/star_assignment_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/star_assignment_c.py
    :caption: :download:`Solution <assignments/star_assignment_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/star_assignment_d.py
    :caption: :download:`Solution <assignments/star_assignment_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/star_assignment_e.py
    :caption: :download:`Solution <assignments/star_assignment_e.py>`
    :end-before: # Solution
