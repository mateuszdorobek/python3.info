Unpack Assignment Expression
============================


Important
---------
* Since Python 3.8: :pep:`572` -- Assignment Expressions
* Also known as "Walrus operator"
* Also known as "Named expression"

During discussion of this PEP, the operator became informally
known as "the walrus operator". The construct's formal name is
"Assignment Expressions" (as per the PEP title), but they may
also be referred to as "Named Expressions". The CPython reference
implementation uses that name internally). [#pep572]_

Guido van Rossum stepped down after accepting :pep:`572` -- Assignment Expressions:

.. figure:: img/unpack-assignmentexpr-bdfl.png


Syntax
------
Scalar:

.. code-block:: python

    (x := <VALUE>)

Comprehension:

.. code-block:: python

    result = [<RETURN>
              for <VARIABLE1> in <ITERABLE>
              if (<VARIABLE2> := <EXPR>)]

.. code-block:: python

    result = [<RETURN>
              for <VARIABLE1> in <ITERABLE>
              if (<VARIABLE2> := <EXPR>)
              and (<VARIABLE3> := <EXPR>)]

.. code-block:: python

    result = [<RETURN>
              for <VARIABLE1> in <ITERABLE>
              if (<VARIABLE2> := <EXPR>)
              and (<VARIABLE3> := <EXPR>)
              or (<VARIABLE4> := <EXPR>)]

Example
-------
* Defines and substitutes in one go

>>> x = 1
>>> print(x)
1

>>> print(x = 1)
Traceback (most recent call last):
TypeError: 'x' is an invalid keyword argument for print()

>>> print(x := 1)
1


What is not
-----------
* It's not substitution for equals

>>> x = 1
>>> print(x)
1

>>> x := 1
Traceback (most recent call last):
SyntaxError: invalid syntax


Processing Streams
------------------
* Processing steams in chunks:

>>> # doctest: +SKIP
... file = open('myfile.txt')
... chunk = file.read(100)
...
... while chunk:
...     print(chunk)
...     chunk = file.read(100)

>>> # doctest: +SKIP
... file = open('myfile.txt')
...
... while chunk := file.read(100):
...     print(chunk)


Checking Match
--------------
>>> import re
>>>
>>> DATA = 'mark.watney@nasa.gov'

Typically regular expressions requires to check if the value ``is not None``
before using it further:

>>> result = re.search(r'@nasa.gov', DATA)
>>>
>>> if result:
...     print(result)
<re.Match object; span=(11, 20), match='@nasa.gov'>

Assignment expressions allows to merge two independent lines into one
coherent statement:

>>> if result := re.search(r'@nasa.gov', DATA):
...     print(result)
<re.Match object; span=(11, 20), match='@nasa.gov'>


Comprehensions
--------------
Let's define data:

>>> DATA = ['Jan Twardowski',
...         'Melissa Lewis',
...         'Mark Watney']

Typical comprehension would require calling ``str.split()`` multiple times:

>>> result = [{'firstname': fullname.split()[0],
...            'lastname': fullname.split()[1]}
...           for fullname in DATA]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'Twardowski'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Mark', 'lastname': 'Watney'}]

Assignment expressions allows definition of a variable which can be used in
the comprehension. It is not only more clear and readable, but also saves
time and memory, especially if the function call would take a lot of
resources:

>>> result = [{'firstname': name[0], 'lastname': name[1]}
...           for fullname in DATA
...           if (name := fullname.split())]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'Twardowski'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Mark', 'lastname': 'Watney'}]


Assignment vs Assignment Expression
-----------------------------------
>>> (x := 1)
1
>>>
>>> print(x)
1

>>> x = 1, 2
>>>
>>> print(x)
(1, 2)

>>> (x := 1, 2)
(1, 2)
>>>
>>> print(x)
1

>>> result = (x := 1, 2)
>>>
>>> print(result)
(1, 2)

>>> x = 0
>>> x += 1
>>>
>>> print(x)
1

>>> x = 0
>>> x +:= 1
Traceback (most recent call last):
SyntaxError: invalid syntax

>>> data = {}
>>> data['commander'] = 'Mark Watney'
>>>
>>> data = {}
>>> data['commander'] := 'Mark Watney'
Traceback (most recent call last):
SyntaxError: cannot use assignment expressions with subscript


Use Case - 0x01
---------------
* Reusing Results

>>> def f(x):
...     return 1
>>>
>>>
>>> result = [f(x), f(x)+1, f(x)+2]
>>>
>>> result = [res := f(x), res+1, res+2]


Use Case - 0x02
---------------
>>> DATA = ['5.8,2.7,5.1,1.9,virginica',
...         '5.1,3.5,1.4,0.2,setosa',
...         '5.7,2.8,4.1,1.3,versicolor']
>>>
>>>
>>> result = [tuple(features + [species])
...           for row in DATA
...           if (line := row.split(','))
...           and (features := [float(x) for x in line[0:4]])
...           and (species := line[4])]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor')]


Use Case - 0x03
---------------
>>> DATA = [{'is_astronaut': True,  'name': 'JaN TwarDOwski'},
...         {'is_astronaut': True,  'name': 'Mark Jim WaTNey'},
...         {'is_astronaut': False, 'name': 'José Maria Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]

Comprehension:

>>> result = [{'firstname': person['name'].title().split()[0],
...            'lastname': person['name'].title().split()[-1]}
...           for person in DATA
...           if person['is_astronaut']]

Assignment expressions:

>>> result = [{'firstname': name[0],
...            'lastname': name[-1]}
...           for person in DATA
...           if person['is_astronaut']
...           and (name := person['name'].title().split())]

In both cases result is the same:

>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'Twardowski'},
 {'firstname': 'Mark', 'lastname': 'Watney'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'}]


Use Case - 0x04
---------------
>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>>
>>> astronauts = [{'firstname': fname, 'lastname': lname}
...                for person in DATA
...                if person['is_astronaut']
...                and (name := person['name'].split())
...                and (fname := name[0].capitalize())
...                and (lname := f'{name[1][0]}.')]
>>>
>>> print(astronauts)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'T.'},
 {'firstname': 'Mark', 'lastname': 'W.'},
 {'firstname': 'Melissa', 'lastname': 'L.'}]


Use Case - 0x05
---------------
>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>>
>>> astronauts = [f'{fname} {lname[0]}.'
...               for person in DATA
...               if person['is_astronaut']
...               and (fullname := person['name'].split())
...               and (fname := fullname[0].capitalize())
...               and (lname := fullname[1].upper())]
>>>
>>>
>>> print(astronauts)
['Jan T.', 'Mark W.', 'Melissa L.']


Use Case - 0x06
---------------
In the following example dataclasses are used to automatically
generate ``__init__()`` method based on the attributes:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
>>>
>>>
>>> class Versicolor(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>>
>>> DATA = [
...    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...    (5.8, 2.7, 5.1, 1.9, 'virginica'),
...    (5.1, 3.5, 1.4, 0.2, 'setosa'),
...    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...    (6.3, 2.9, 5.6, 1.8, 'virginica'),
...    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>>
>>> result = [iris(*values)
...           for *values, species in DATA[1:]
...           if (clsname := species.capitalize())
...           and (iris := globals()[clsname])]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2),
 Versicolor(sepal_length=7.0, sepal_width=3.2, petal_length=4.7, petal_width=1.4)]


Use Case - 0x07
---------------
>>> import re
>>>
>>>
>>> data = 'mark.watney@nasa.gov'
>>> pattern = r'([a-z]+)\.([a-z]+)@nasa.gov'

Procedural approach:

>>> match = re.match(pattern, data)
>>> result = match.groups() if match else None

Conditional statement requires to perform match twice in order to get results:

>>> result = re.match(pattern, data).groups() if re.match(pattern, data) else None

Assignment expressions allows to defile a variable and reuse it:

>>> result = x.groups() if (x := re.match(pattern, data)) else None

In all cases result is the same:

>>> print(result)
('mark', 'watney')


References
----------
.. [#pep572] Angelico, C. and Peters, T. and van Rossum, G. PEP 572 -- Assignment Expressions. Python Software Foundation. Year: 2018. Retrieved: 2020-12-04. Url: https://www.python.org/dev/peps/pep-0572/#abstract


Assignments
-----------
.. literalinclude:: assignments/unpack_assignmentexpr_a.py
    :caption: :download:`Solution <assignments/unpack_assignmentexpr_a.py>`
    :end-before: # Solution
