Syntax Assignment Expression
============================
* Since Python 3.8: :pep:`572` -- Assignment Expressions
* Also known as "Walrus operator"
* Also known as "Named expression"

Python's assignment expression is a feature introduced in Python 3.8. It
allows you to assign a value to a variable as part of a larger expression.
The syntax for the assignment expression is as follows:

>>> variable := expression  # doctest: +SKIP

The expression is evaluated and the result is assigned to the variable on
the left-hand side of the ``:=`` operator. The variable can then be used in
the rest of the expression.

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


Value of the Expression
-----------------------
* First defines identifier with value
* Then returns the value from the identifier
* Both operations in the same line

>>> x = 1
>>> x
1

>>> result = (x = 1)
Traceback (most recent call last):
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

>>> x = 1
>>> print(x)
1

>>> print(x = 1)
Traceback (most recent call last):
TypeError: 'x' is an invalid keyword argument for print()

>>> print(x := 1)
1


Assign in the Expression
------------------------
>>> if x = 1:
...     print('yes')
... else:
...     print('no')
Traceback (most recent call last):
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

>>> if x := 1:
...     print('yes')
... else:
...     print('no')
yes


Assignment and Evaluation
-------------------------
Assignment Expression assigns and immediately evaluates expression:

>>> if x := 1:
...     print('yes')
... else:
...     print('no')
yes
>>>
>>> x
1

>>> if x := 0:
...     print('ok')
... else:
...     print('no')
no
>>>
>>> x
0


What Assignment Expression is?
------------------------------
>>> if x := 1:
...     print('yes')
... else:
...     print('no')
yes

Is equivalent to:

>>> x = 1
>>> if x:
...     print('yes')
... else:
...     print('no')
yes


What Assignment Expression is not?
----------------------------------
* It's not substitution for equals

>>> x = 1

>>> x := 1
Traceback (most recent call last):
SyntaxError: invalid syntax


Checking Match
--------------
SetUp:

>>> import re

In order to find `username` in email address we need to define
regular expression pattern:

>>> pattern = r'([a-z]+)@nasa.gov'

Let's search for `username` in email address:

>>> email = 'mwatney@nasa.gov'
>>>
>>> result = re.search(pattern, email)
>>> username = result.group(1)
>>>
>>> print(username)
mwatney

This works well when username is valid and is indeed in email.
What if, the username is invalid:

>>> email = 'mwatney69@nasa.gov'
>>>
>>> result = re.search(pattern, email)
>>> username = result.group(1)
Traceback (most recent call last):
AttributeError: 'NoneType' object has no attribute 'group'

This is because ``re.search()`` returns an optional value
``re.Match | None``. Therefore, regular expression matches
requires to check if the value ``is not None`` before using it further:

>>> email = 'mwatney69@nasa.gov'
>>>
>>> result = re.search(pattern, email)
>>> if result:
...     username = result.group(1)
...     print(username)

Assignment expressions allows to merge two independent lines into one
coherent statement to unpack and process an optional:

>>> email = 'mwatney69@nasa.gov'
>>>
>>> if result := re.search(pattern, email):
...     username = result.group(1)
...     print(username)


Processing Streams
------------------
* Processing steams in chunks

Imagine we have a temperature sensor, and this sensor stream values.
We have a process which receives values from string and appends them
to the file. Let's simulate the process by adding temperature
measurements to the file:

>>> with open('/tmp/myfile.txt', mode='w') as file:
...     _ = file.write('21.1,21.1,21.2,21.2,21.3,22.4,')

Note, that all values have fixed length of 4 bytes plus comma (5th byte).
We cannot open and read whole file to the memory, like we normally do.
This file may be huge, much larger than RAM in our computer.

We will process file reading 5 bytes of data (one measurement) at a time:

>>> file = open('/tmp/myfile.txt')
>>>
>>> value = file.read(5).removesuffix(',')
>>> while value:
...     print(f'Processing... {value}')
...     value = file.read(5).removesuffix(',')
Processing... 21.1
Processing... 21.1
Processing... 21.2
Processing... 21.2
Processing... 21.3
Processing... 22.4

As you can see we have two places where we define number of bytes,
read and cleanup data. First ``file.read()`` is needed to enter the loop.
Second ``file.read()`` is needed to process the file further until the end.
Using assignment expression we can write code which is far better:

>>> file = open('/tmp/myfile.txt')
>>>
>>> while value := file.read(5).removesuffix(","):
...     print(f'Processing... {value}')
Processing... 21.1
Processing... 21.1
Processing... 21.2
Processing... 21.2
Processing... 21.3
Processing... 22.4

Imagine if this is not a 5 bytes of data, but a chunk of data for processing
(for example a ten megabytes at once). This construct make more sense then.

Always remember to close the file at the end:

>>> file.close()


Variables in comprehensions
---------------------------
>>> DATA = {
...     'mission': 'Ares 3',
...     'launch': '2035-06-29',
...     'landing': '2035-11-07',
...     'destination': 'Mars',
...     'location': 'Acidalia Planitia',
...     'crew': [{'name': 'Melissa Lewis', 'email': 'mlewis@nasa.gov'},
...              {'name': 'Rick Martinez', 'email': 'rmartinez@nasa.gov'},
...              {'name': 'Alex Vogel', 'email': 'avogel@esa.int'},
...              {'name': 'Pan Twardowski', 'email': 'ptwardowski@polsa.gov.pl'},
...              {'name': 'Chris Beck', 'email': 'cbeck@nasa.gov'},
...              {'name': 'Beth Johanssen', 'email': 'bjohanssen@nasa.gov'},
...              {'name': 'Mark Watney', 'email': 'mwatney@nasa.gov'},
...              {'name': 'Ivan Ivanovich', 'email': 'iivanovich@roscosmos.ru'}]}
>>>
>>>
>>> DOMAINS = ('esa.int', 'nasa.gov')

>>> result = [astronaut['email']
...           for astronaut in DATA['crew']
...           if astronaut['email'].endswith(DOMAINS)]
>>> result  # doctest: +NORMALIZE_WHITESPACE
['mlewis@nasa.gov',
 'rmartinez@nasa.gov',
 'avogel@esa.int',
 'cbeck@nasa.gov',
 'bjohanssen@nasa.gov',
 'mwatney@nasa.gov']

>>> result = [email
...           for astronaut in DATA['crew']
...           if (email := astronaut['email'])
...           and email.endswith(DOMAINS)]
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
['mlewis@nasa.gov',
 'rmartinez@nasa.gov',
 'avogel@esa.int',
 'cbeck@nasa.gov',
 'bjohanssen@nasa.gov',
 'mwatney@nasa.gov']


Comprehensions
--------------
Let's define data:

>>> DATA = [
...     'Mark Watney',
...     'Melissa Lewis',
...     'Rick Martinez',
... ]

Typical comprehension would require calling ``str.split()`` multiple times:

>>> result = [{'firstname': fullname.split()[0],
...            'lastname': fullname.split()[1]}
...           for fullname in DATA]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Mark', 'lastname': 'Watney'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Rick', 'lastname': 'Martinez'}]

Assignment expressions allows definition of a variable which can be used in
the comprehension. It is not only more clear and readable, but also saves
time and memory, especially if the function call would take a lot of
resources:

>>> result = [{'firstname': name[0], 'lastname': name[1]}
...           for fullname in DATA
...           if (name := fullname.split())]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Mark', 'lastname': 'Watney'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Rick', 'lastname': 'Martinez'}]

You can define multiple assignment expressions if needed.

>>> result = [{'firstname': name[0], 'lastname': name[1]}
...           for fullname in DATA
...           if (name := fullname.split())
...           and (firstname := name[0])
...           and (lastname := name[1])]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Mark', 'lastname': 'Watney'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Rick', 'lastname': 'Martinez'}]


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

>>> def run(x):
...     return 1
>>>
>>>
>>> result = [run(x), run(x)+1, run(x)+2]
>>>
>>> result = [res := run(x), res+1, res+2]


Use Case - 0x02
---------------
>>> from pprint import pprint

We want to convert:

>>> DATA = """5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor"""

Into:

>>> pprint(result)  # doctest: +SKIP
[(5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor')]

Using loop:

>>> result = []
>>> for line in DATA.splitlines():
...     records = line.split(',')
...     features = tuple(map(float, records[0:4]))
...     species = (records[-1],)
...     result.append(features + species)

Using comprehension:

>>> result = [tuple(map(float, line.split(',')[0:4])) + (line.split(',')[-1],)
...           for line in DATA.splitlines()]

Using comprehension with assignment expression:

>>> result = [tuple(map(float, records[0:4])) + (records[-1],)
...           for line in DATA.splitlines()
...           if (records := line.split(','))]

Using comprehension with multiple assignment expression:

>>> result = [tuple(features) + (species,)
...           for line in DATA.splitlines()
...           if (records := line.split(','))
...           and (features := map(float, records[0:4]))
...           and (species := records[-1])]


Use Case - 0x03
---------------
>>> DATA = """5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor"""

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... result = []
... for line in DATA.splitlines():
...     *values, species = line.split(',')
...     values = map(float,values)
...     row = tuple(values) + (species,)
...     result.append(row)
3.18 µs ± 394 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... result = [tuple(values) + (species,)
...           for line in DATA.splitlines()
...           if (row := line.split(','))
...           and (values := map(float, row[:-1]))
...           and (species := row[-1])]
2.97 µs ± 386 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... result = (tuple(values) + (species,)
...           for line in DATA.splitlines()
...           if (row := line.split(','))
...           and (values := map(float, row[:-1]))
...           and (species := row[-1]))
577 ns ± 53.3 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Note, that the generator expression will not return values, but create
an object which execution will get values. This is the reason why this
solution is such drastically fast.


Use Case - 0x04
---------------
>>> DATA = """5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor"""

>>> result = [tuple(values) + (species,)
...           for line in DATA.splitlines()
...           if (row := line.split(','))
...           and (values := map(float, row[:-1]))
...           and (species := row[-1])]
>>>
>>> result   # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor')]

>>> result = (tuple(values) + (species,)
...           for line in DATA.splitlines()
...           if (row := line.split(','))
...           and (values := map(float, row[:-1]))
...           and (species := row[-1]))
>>>
>>> result  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>
>>>
>>> next(result)
(5.8, 2.7, 5.1, 1.9, 'virginica')
>>>
>>> next(result)
(5.1, 3.5, 1.4, 0.2, 'setosa')
>>>
>>> next(result)
(5.7, 2.8, 4.1, 1.3, 'versicolor')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration


Use Case - 0x05
---------------
>>> users = [
...     {'is_admin': False, 'name': 'Mark Watney'},
...     {'is_admin': True,  'name': 'Melissa Lewis'},
...     {'is_admin': False, 'name': 'Rick Martinez'},
...     {'is_admin': False, 'name': 'Alex Vogel'},
...     {'is_admin': True,  'name': 'Beth Johanssen'},
...     {'is_admin': False, 'name': 'Chris Beck'},
... ]

Comprehension:

>>> result = [{'firstname': user['name'].title().split()[0],
...            'lastname': user['name'].title().split()[1]}
...           for user in users
...           if user['is_admin']]

One assignment expression:

>>> result = [{'firstname': name[0],
...            'lastname': name[1]}
...           for user in users
...           if user['is_admin']
...           and (name := user['name'].title().split())]

Many assignment expressions:

>>> result = [{'firstname': firstname,
...            'lastname': lastname}
...           for user in users
...           if user['is_admin']
...           and (name := user['name'].title().split())
...           and (firstname := name[0])
...           and (lastname := name[1])]

In all cases result is the same:

>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Beth', 'lastname': 'Johanssen'}]


Use Case - 0x07
---------------
In the following example dataclasses are used to automatically
generate ``__init__()`` method based on the attributes:

>>> from dataclasses import dataclass
>>> from pprint import pprint
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
...    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
...    (5.8, 2.7, 5.1, 1.9, 'virginica'),
...    (5.1, 3.5, 1.4, 0.2, 'setosa'),
...    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...    (6.3, 2.9, 5.6, 1.8, 'virginica'),
...    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
... ]
>>>
>>>
>>> result = [iris(*values)
...           for *values, species in DATA[1:]
...           if (clsname := species.capitalize())
...           and (iris := globals()[clsname])]
>>>
>>> pprint(result, width=120)
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2),
 Versicolor(sepal_length=7.0, sepal_width=3.2, petal_length=4.7, petal_width=1.4)]


Use Case - 0x09
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


Use Case - 0x0A
---------------
>>> #doctest: +SKIP
... from ninja import Router
... from django.contrib.auth import authenticate, login
... from backend.auth.schemas import LoginRequest SessionIdResponse
... from backend.common.schemas import ResponseUnauthorized
...
... router = Router()
...
...
... @router.api_operation(
...     methods=['POST'],
...     path='session/',
...     response={
...         200: SessionIdResponse,
...         401: ResponseUnauthorized},
...     summary='Authenticate using Cookies and SessionID')
... def session(request, data: LoginRequest):
...     username = data.username
...     password = data.password
...     if user := authenticate(request, username=username, password=password):
...         login(request, user)
...         return 200, {'sessionid': request.session.session_key}
...     else:
...         return 401, {'details': 'Invalid credentials'}


References
----------
.. [#pep572] Angelico, C. and Peters, T. and van Rossum, G. PEP 572 -- Assignment Expressions. Python Software Foundation. Year: 2018. Retrieved: 2020-12-04. Url: https://www.python.org/dev/peps/pep-0572/#abstract


Assignments
-----------
.. literalinclude:: assignments/syntax_assignmentexpr_a.py
    :caption: :download:`Solution <assignments/syntax_assignmentexpr_a.py>`
    :end-before: # Solution
