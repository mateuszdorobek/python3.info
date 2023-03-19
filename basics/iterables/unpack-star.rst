Unpack Star
===========
* ``a, b, *c = 1, 2, 3, 4, 5``
* Used when there is arbitrary number of values to unpack
* Could be used from start, middle, end
* There can't be multiple star expressions in one assignment statement
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future

.. figure:: img/unpack-assignment,args,params.png


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

>>> line = 'Mark,Watney,40,185,75.5'
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


Assignments
-----------
.. literalinclude:: assignments/sequence_star_a.py
    :caption: :download:`Solution <assignments/sequence_star_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_star_b.py
    :caption: :download:`Solution <assignments/sequence_star_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_star_c.py
    :caption: :download:`Solution <assignments/sequence_star_c.py>`
    :end-before: # Solution
