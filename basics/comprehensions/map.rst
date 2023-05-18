Comprehension Map
=================


Example
-------
>>> [float(x) for x in range(0,5)]
[0.0, 1.0, 2.0, 3.0, 4.0]


Apply Function
--------------
>>> [pow(2,x) for x in range(0,5)]
[1, 2, 4, 8, 16]

>>> [pow(2,x) for x in range(0,5)]
[1, 2, 4, 8, 16]

>>> [pow(x,x) for x in range(0,5)]
[1, 1, 4, 27, 256]


Convert Data
------------
>>> DATA = [
...     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> [tuple(features) for *features,label in DATA[1:]]  # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9),
 (5.1, 3.5, 1.4, 0.2),
 (5.7, 2.8, 4.1, 1.3),
 (6.3, 2.9, 5.6, 1.8),
 (6.4, 3.2, 4.5, 1.5),
 (4.7, 3.2, 1.3, 0.2)]
>>>
>>> [tuple(X) for *X,y in DATA[1:]]  # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9),
 (5.1, 3.5, 1.4, 0.2),
 (5.7, 2.8, 4.1, 1.3),
 (6.3, 2.9, 5.6, 1.8),
 (6.4, 3.2, 4.5, 1.5),
 (4.7, 3.2, 1.3, 0.2)]


Map to String
-------------
>>> DATA = [1, 2, 3]
>>> str(DATA)
'[1, 2, 3]'

>>> [str(x) for x in DATA]
['1', '2', '3']

>>> data = [str(x) for x in DATA]
>>> ','.join(data)
'1,2,3'

>>> ','.join(str(x) for x in DATA)
'1,2,3'


Generate CSV
------------
>>> DATA = [1, 2, 3]
>>>
>>>
>>> ','.join(DATA)
Traceback (most recent call last):
TypeError: sequence item 0: expected str instance, int found

>>> DATA = [1, 2, 3]
>>>
>>>
>>> ','.join(str(x) for x in DATA)
'1,2,3'


Generate CSV Data
-----------------
>>> DATA = [
...     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>>
>>> result = [','.join(str(x) for x in row) for row in DATA]
>>> result = '\n'.join(result)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor
6.3,2.9,5.6,1.8,virginica
6.4,3.2,4.5,1.5,versicolor
4.7,3.2,1.3,0.2,setosa
7.0,3.2,4.7,1.4,versicolor


Parse CSV
---------
>>> DATA = '5.8,2.7,5.1,1.9\n5.1,3.5,1.4,0.2\n5.7,2.8,4.1,1.3'
>>>
>>> result = []
>>>
>>> for row in DATA.splitlines():
...     row = row.split(',')
...     result.append(row)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[['5.8', '2.7', '5.1', '1.9'],
 ['5.1', '3.5', '1.4', '0.2'],
 ['5.7', '2.8', '4.1', '1.3']]

>>> DATA = '5.8,2.7,5.1,1.9\n5.1,3.5,1.4,0.2\n5.7,2.8,4.1,1.3'
>>>
>>> [row.split(',') for row in DATA.splitlines()]  # doctest: +NORMALIZE_WHITESPACE
[['5.8', '2.7', '5.1', '1.9'],
 ['5.1', '3.5', '1.4', '0.2'],
 ['5.7', '2.8', '4.1', '1.3']]

>>> DATA = '5.8,2.7,5.1,1.9\n5.1,3.5,1.4,0.2\n5.7,2.8,4.1,1.3'
>>>
>>> [[float(x) for x in row.split(',')] for row in DATA.splitlines()]  # doctest: +NORMALIZE_WHITESPACE
[[5.8, 2.7, 5.1, 1.9],
 [5.1, 3.5, 1.4, 0.2],
 [5.7, 2.8, 4.1, 1.3]]

>>> DATA = '5.8,2.7,5.1,1.9,virginica\n5.1,3.5,1.4,0.2,setosa\n5.7,2.8,4.1,1.3,versicolor'
>>>
>>> def convert(x):
...     try:
...         return float(x)
...     except ValueError:
...         return x
>>>
>>> [[convert(x) for x in row.split(',')] for row in DATA.splitlines()]  # doctest: +NORMALIZE_WHITESPACE
[[5.8, 2.7, 5.1, 1.9, 'virginica'],
 [5.1, 3.5, 1.4, 0.2, 'setosa'],
 [5.7, 2.8, 4.1, 1.3, 'versicolor']]


Use Case - 0x01
---------------
* Raise number to the n-th power

>>> [pow(x,2) for x in range(0,5)]
[0, 1, 4, 9, 16]

>>> [x**2 for x in range(0,5)]
[0, 1, 4, 9, 16]

>>> [pow(2,x) for x in range(0,5)]
[1, 2, 4, 8, 16]

>>> [2**x for x in range(0,5)]
[1, 2, 4, 8, 16]


Use Case - 0x02
---------------
* Map list[dict]

>>> users = [
...     {'is_admin': True,  'name': 'Melissa Lewis'},
...     {'is_admin': True,  'name': 'Mark Watney'},
...     {'is_admin': False, 'name': 'Rick Martinez'},
...     {'is_admin': True,  'name': 'Alex Vogel'},
... ]
>>>
>>>
>>> admin = [{'firstname': user['name'].split()[0],
...           'lastname': user['name'].split()[1]}
...           for user in users
...           if user['is_admin']]
>>>
>>> print(admin)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Mark', 'lastname': 'Watney'},
 {'firstname': 'Alex', 'lastname': 'Vogel'}]


Use Case - 0x03
---------------
>>> users = [
...     {'is_admin': True,  'name': 'Melissa Lewis'},
...     {'is_admin': True,  'name': 'Mark Watney'},
...     {'is_admin': False, 'name': 'Rick Martinez'},
...     {'is_admin': True,  'name': 'Alex Vogel'},
... ]
>>>
>>>
>>> admins = [{'firstname': user['name'].split()[0].capitalize(),
...            'lastname': user['name'].split()[1][0]+'.'}
...            for user in users
...            if user['is_admin']]
>>>
>>> print(admins)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Melissa', 'lastname': 'L.'},
 {'firstname': 'Mark', 'lastname': 'W.'},
 {'firstname': 'Alex', 'lastname': 'V.'}]


Use Case - 0x04
---------------
* Assignment expression
* More information in `Assignment Expression`

>>> users = [
...     {'is_admin': True,  'name': 'Melissa Lewis'},
...     {'is_admin': True,  'name': 'Mark Watney'},
...     {'is_admin': False, 'name': 'Rick Martinez'},
...     {'is_admin': True,  'name': 'Alex Vogel'},
... ]
>>>
>>>
>>> admins = [{'firstname': fname, 'lastname': lname}
...            for user in users
...            if user['is_admin']
...            and (name := user['name'].split())
...            and (fname := name[0].capitalize())
...            and (lname := f'{name[1][0]}.')]
>>>
>>> print(admins)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Melissa', 'lastname': 'L.'},
 {'firstname': 'Mark', 'lastname': 'W.'},
 {'firstname': 'Alex', 'lastname': 'V.'}]


Use Case - 0x05
---------------
* Assignment expression
* More information in `Assignment Expression`

>>> users = [
...     {'is_admin': True,  'name': 'Melissa Lewis'},
...     {'is_admin': True,  'name': 'Mark Watney'},
...     {'is_admin': False, 'name': 'Rick Martinez'},
...     {'is_admin': True,  'name': 'Alex Vogel'},
... ]
>>>
>>>
>>> admins = [f'{fname} {lname[0]}.'
...           for user in users
...           if user['is_admin']
...           and (fullname := user['name'].split())
...           and (fname := fullname[0].capitalize())
...           and (lname := fullname[1].upper())]
>>>
>>> print(admins)
['Melissa L.', 'Mark W.', 'Alex V.']


.. todo:: Assignments
