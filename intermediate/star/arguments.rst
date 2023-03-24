Unpack Arguments
================
* Unpack and Arbitrary Number of Parameters and Arguments

.. figure:: img/unpack-assignment,args,params.png


Recap
-----
* Argument - Value or variable being passed to the function
* Positional arguments - value passed to function
* Positional arguments - order is important
* Positional arguments - must be at the left side
* Keyword arguments - value passed to function resolved by name
* Keyword arguments - order is not important
* Keyword arguments - must be on the right side
* Positional argument cannot follow keyword arguments

>>> def echo(a=None, b=None):
...     ...

>>> echo(1)          # positional argument
>>> echo(a=1)        # keyword argument
>>> echo(1, 2)       # positional arguments
>>> echo(2, 1)       # positional arguments
>>> echo(a=1, b=2)   # keyword arguments
>>> echo(b=2, a=1)   # keyword arguments, order doesn't matter
>>> echo(1, b=2)     # positional and keyword arguments

>>> echo(a=1, 2)
Traceback (most recent call last):
SyntaxError: positional argument follows keyword argument


Positional Arguments
--------------------
* ``*`` is used for positional arguments
* there is no convention, but you can use any name
* ``*`` unpacks from ``tuple``, ``list`` or ``set``

>>> def echo(a, b, c):
...     print(f'{a=}, {b=}, {c=}')

>>> echo(1, 2, 3)
a=1, b=2, c=3

>>> data = (1, 2, 3)
>>>
>>> echo(data[0], data[1], data[2])
a=1, b=2, c=3
>>>
>>> echo(*data)
a=1, b=2, c=3

>>> data = (1, 2, 3)
>>>
>>> echo(data)
Traceback (most recent call last):
TypeError: echo() missing 2 required positional arguments: 'b' and 'c'


Keyword Arguments
-----------------
* ``**`` is used for keyword arguments
* there is no convention, but you can use any name
* ``**`` unpacks from ``dict``

Keyword arguments passed directly:

>>> def echo(a, b, c):
...     print(f'{a=}, {b=}, {c=}')

>>> echo(a=1, b=2, c=3)
a=1, b=2, c=3

>>> data = {'a': 1, 'b': 2, 'c': 3}
>>>
>>> echo(a=data['a'], b=data['b'], c=data['c'])
a=1, b=2, c=3
>>>
>>> echo(**data)
a=1, b=2, c=3
>>>
>>> echo(*data.values())
a=1, b=2, c=3

>>> data = {'a': 1, 'b': 2, 'c': 3}
>>>
>>> echo(data)
Traceback (most recent call last):
TypeError: echo() missing 2 required positional arguments: 'b' and 'c'


Positional and Keyword Arguments
--------------------------------
>>> def echo(a, b, c, d):
...     print(f'{a=}, {b=}, {c=}, {d=}')

>>> echo(1, 2, c=3, d=4)
a=1, b=2, c=3, d=4

>>> data1 = (1, 2)
>>> data2 = {'c': 3, 'd': 4}
>>>
>>> echo(data1[0], data1[1], c=data2['c'], d=data2['d'])
a=1, b=2, c=3, d=4
>>>
>>> echo(*data1, **data2)
a=1, b=2, c=3, d=4

>>> data1 = (1, 2)
>>> data2 = {'c': 3}
>>>
>>> echo(*data1, **data2)
Traceback (most recent call last):
TypeError: echo() missing 1 required positional argument: 'd'

>>> data1 = (1, 2)
>>> data2 = {'c': 3, 'd': 4, 'a': 1}
>>>
>>> echo(*data1, **data2)
Traceback (most recent call last):
TypeError: echo() got multiple values for argument 'a'


Create One Object
-----------------
>>> class Iris:
...     def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species
...
...     def __repr__(self):
...         values = tuple(vars(self).values())
...         return f'Iris{values}'

Objects From Sequence:

>>> DATA = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>>
>>> result = Iris(*DATA)
>>> print(result)
Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

Objects From Mappings:

>>> DATA = {
...     'sepal_length': 5.8,
...     'sepal_width': 2.7,
...     'petal_length': 5.1,
...     'petal_width': 1.9,
...     'species': 'virginica',
... }
>>>
>>> result = Iris(**DATA)
>>> print(result)
Iris(5.8, 2.7, 5.1, 1.9, 'virginica')


Create Many Objects
-------------------
>>> from pprint import pprint
>>>
>>>
>>> class Iris:
...     def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species
...
...     def __repr__(self):
...         values = tuple(vars(self).values())
...         return f'Iris{values}'

Object from list of sequences:

>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>> result = [Iris(*row) for row in DATA]
>>>
>>> pprint(result)
[Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
 Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
 Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
 Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
 Iris(6.4, 3.2, 4.5, 1.5, 'versicolor'),
 Iris(4.7, 3.2, 1.3, 0.2, 'setosa')]

Objects from list of mappings:

>>> DATA = [
...     {"sepal_length":5.8,"sepal_width":2.7,"petal_length":5.1,"petal_width":1.9,"species":"virginica"},
...     {"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2,"species":"setosa"},
...     {"sepal_length":5.7,"sepal_width":2.8,"petal_length":4.1,"petal_width":1.3,"species":"versicolor"},
...     {"sepal_length":6.3,"sepal_width":2.9,"petal_length":5.6,"petal_width":1.8,"species":"virginica"},
...     {"sepal_length":6.4,"sepal_width":3.2,"petal_length":4.5,"petal_width":1.5,"species":"versicolor"},
...     {"sepal_length":4.7,"sepal_width":3.2,"petal_length":1.3,"petal_width":0.2,"species":"setosa"},
... ]
>>>
>>> result = [Iris(**row) for row in DATA]
>>>
>>> pprint(result)
[Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
 Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
 Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
 Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
 Iris(6.4, 3.2, 4.5, 1.5, 'versicolor'),
 Iris(4.7, 3.2, 1.3, 0.2, 'setosa')]

Objects from json:

>>> DATA = (
...     '[{"sepal_length":5.8,"sepal_width":2.7,"petal_length":5.1,"peta'
...     'l_width":1.9,"species":"virginica"},{"sepal_length":5.1,"sepal_'
...     'width":3.5,"petal_length":1.4,"petal_width":0.2,"species":"seto'
...     'sa"},{"sepal_length":5.7,"sepal_width":2.8,"petal_length":4.1,"'
...     'petal_width":1.3,"species":"versicolor"},{"sepal_length":6.3,"s'
...     'epal_width":2.9,"petal_length":5.6,"petal_width":1.8,"species":'
...     '"virginica"},{"sepal_length":6.4,"sepal_width":3.2,"petal_lengt'
...     'h":4.5,"petal_width":1.5,"species":"versicolor"},{"sepal_length'
...     '":4.7,"sepal_width":3.2,"petal_length":1.3,"petal_width":0.2,"s'
...     'pecies":"setosa"}]'
... )
>>>
>>> import json
>>> result = [Iris(**row) for row in json.loads(DATA)]
>>>
>>> pprint(result)
[Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
 Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
 Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
 Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
 Iris(6.4, 3.2, 4.5, 1.5, 'versicolor'),
 Iris(4.7, 3.2, 1.3, 0.2, 'setosa')]


Recap
-----
>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> def show(sl, sw, pl, pw, species):
...     avg = sum([sl,sw,pl,pw]) / len([sl,sw,pl,pw])
...     return species, avg, sl, sw, pl, pw
>>>
>>>
>>> for *values, species in DATA:
...     name, avg, *data = show(*values, species)
...     print(f'{avg=:.1f}, {values=}, {species=}')
avg=3.9, values=[5.8, 2.7, 5.1, 1.9], species='virginica'
avg=2.5, values=[5.1, 3.5, 1.4, 0.2], species='setosa'
avg=3.5, values=[5.7, 2.8, 4.1, 1.3], species='versicolor'
avg=4.1, values=[6.3, 2.9, 5.6, 1.8], species='virginica'
avg=3.9, values=[6.4, 3.2, 4.5, 1.5], species='versicolor'
avg=2.4, values=[4.7, 3.2, 1.3, 0.2], species='setosa'


Use Case - 0x01
---------------
Calling a function which has similar parameters. Passing configuration to the
function, which sets parameters from the config:

>>> def draw_line(x, y, color, type, width, markers):
...     ...

>>> draw_line(x=1, y=2, color='red', type='dashed', width='2px', markers='disc')
>>> draw_line(x=3, y=4, color='red', type='dashed', width='2px', markers='disc')
>>> draw_line(x=5, y=6, color='red', type='dashed', width='2px', markers='disc')

>>> style = {'color': 'red',
...          'type': 'dashed',
...          'width': '2px',
...          'markers': 'disc'}
>>>
>>> draw_line(x=1, y=2, **style)
>>> draw_line(x=3, y=4, **style)
>>> draw_line(x=5, y=6, **style)


Use Case - 0x02
---------------
>>> def print_coordinates(x, y, z):
...     print(f'{x=}, {y=}, {z=}')

Passing sequence to the function:

>>> point = [1, 2, 3]
>>>
>>> print_coordinates(point[0], point[1], point[2])
x=1, y=2, z=3
>>>
>>> print_coordinates(*point)
x=1, y=2, z=3

Passing mapping to the function:

>>> point = {'x': 1, 'y': 2, 'z': 3}
>>>
>>> print_coordinates(x=point['x'], y=point['y'], z=point['z'])
x=1, y=2, z=3
>>>
>>> print_coordinates(**point)
x=1, y=2, z=3
>>>
>>> print_coordinates(*point.values())
x=1, y=2, z=3

Passing sequence and mapping to the function:

>>> point2d = (1, 2)
>>> point3d = {'z': 3}
>>>
>>> print_coordinates(*point2d, **point3d)
x=1, y=2, z=3


Use Case - 0x03
---------------
>>> def database_connect(host, port, username, password, database):
...     ...

After reading config from file we have a dict:

>>> CONFIG = {
...     'host': 'example.com',
...     'port': 5432,
...     'username': 'myusername',
...     'password': 'mypassword',
...     'database': 'mydatabase'}

Database connection configuration read from config file:

>>> connection = database_connect(
...     host=CONFIG['host'],
...     port=CONFIG['port'],
...     username=CONFIG['username'],
...     password=CONFIG['password'],
...     database=CONFIG['database'])

Or:

>>> connection = database_connect(**CONFIG)


Use Case - 0x04
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Point:
...     x: int
...     y: int
...     z: int = 0
>>>
>>>
>>> MOVEMENT = [(0, 0),
...             (1, 0),
...             (2, 1, 1),
...             (3, 2),
...             (3, 3, -1),
...             (2, 3)]

>>> movement = [Point(x,y) for x,y in MOVEMENT]
Traceback (most recent call last):
ValueError: too many values to unpack (expected 2)

>>> movement = [Point(*coordinates) for coordinates in MOVEMENT]
>>>
>>> movement  # doctest: +NORMALIZE_WHITESPACE
[Point(x=0, y=0, z=0),
 Point(x=1, y=0, z=0),
 Point(x=2, y=1, z=1),
 Point(x=3, y=2, z=0),
 Point(x=3, y=3, z=-1),
 Point(x=2, y=3, z=0)]


Use Case - 0x04
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str
>>>
>>>
>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> result = [Iris(*row) for row in DATA]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9, species='virginica'),
 Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='setosa'),
 Iris(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3, species='versicolor'),
 Iris(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8, species='virginica'),
 Iris(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5, species='versicolor'),
 Iris(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2, species='setosa')]


Use Case - 0x05
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str
>>>
>>>
>>> DATA = [
...     {"sepal_length":5.8,"sepal_width":2.7,"petal_length":5.1,"petal_width":1.9,"species":"virginica"},
...     {"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2,"species":"setosa"},
...     {"sepal_length":5.7,"sepal_width":2.8,"petal_length":4.1,"petal_width":1.3,"species":"versicolor"},
...     {"sepal_length":6.3,"sepal_width":2.9,"petal_length":5.6,"petal_width":1.8,"species":"virginica"},
...     {"sepal_length":6.4,"sepal_width":3.2,"petal_length":4.5,"petal_width":1.5,"species":"versicolor"},
...     {"sepal_length":4.7,"sepal_width":3.2,"petal_length":1.3,"petal_width":0.2,"species":"setosa"}]
>>>
>>>
>>> result = [Iris(**row) for row in DATA]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9, species='virginica'),
 Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='setosa'),
 Iris(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3, species='versicolor'),
 Iris(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8, species='virginica'),
 Iris(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5, species='versicolor'),
 Iris(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2, species='setosa')]


Use Case - 0x06
---------------
Calling function with all variables from higher order function. ``locals()``
will return a ``dict`` with all the variables in local scope of the function:

>>> def template(template, **user_data):
...     print('Template:', template)
...     print('Data:', user_data)
>>>
>>>
>>> def controller(firstname, lastname, uid=0):
...     groups = ['admins', 'astronauts']
...     permission = ['all', 'everywhere']
...     return template('user_details.html', **locals())
>>>
>>>     # template('user_details.html',
>>>     #    firstname='Mark',
>>>     #    lastname='Watney',
>>>     #    uid=0,
>>>     #    groups=['admins', 'astronauts'],
>>>     #    permission=['all', 'everywhere'])
>>>
>>>
>>> controller('Mark', 'Watney')  # doctest: +NORMALIZE_WHITESPACE
Template: user_details.html
Data: {'firstname': 'Mark',
       'lastname': 'Watney',
       'uid': 0,
       'groups': ['admins', 'astronauts'],
       'permission': ['all', 'everywhere']}


Use Case - 0x07
---------------
* Definition of ``pandas.read_csv()`` function [#pandasreadcsv]_
* Proxy functions. One of the most common use of ``*args``, ``**kwargs``:

>>> def read_csv(filepath_or_buffer, /, *, sep=', ', delimiter=None,
...              header='infer', names=None, index_col=None, usecols=None,
...              squeeze=False, prefix=None, mangle_dupe_cols=True,
...              dtype=None, engine=None, converters=None, true_values=None,
...              false_values=None, skipinitialspace=False, skiprows=None,
...              nrows=None, na_values=None, keep_default_na=True,
...              na_filter=True, verbose=False, skip_blank_lines=True,
...              parse_dates=False, infer_datetime_format=False,
...              keep_date_col=False, date_parser=None, dayfirst=False,
...              iterator=False, chunksize=None, compression='infer',
...              thousands=None, decimal=b'.', lineterminator=None,
...              quotechar='"', quoting=0, escapechar=None, comment=None,
...              encoding=None, dialect=None, tupleize_cols=None,
...              error_bad_lines=True, warn_bad_lines=True, skipfooter=0,
...              doublequote=True, delim_whitespace=False, low_memory=True,
...              memory_map=False, float_precision=None): ...

Calling function with positional only arguments is insane. In Python
we don't do that, because we have keyword arguments.

>>> read_csv('myfile.csv', ';', None, 'infer', None, None, None, False, None,
...          True, None, None, None, None, None, False, None, None, None,
...          True, True, False, True, False, False, False, None, False,
...          False, None, 'infer', None, b',', None, '"', 0, None, None,
...          None, None, None, True, True, 0, True, False, True, False, None)
Traceback (most recent call last):
TypeError: read_csv() takes 1 positional argument but 49 were given

Keyword arguments with sensible defaults are your best friends. The number
of function parameters suddenly is not a problem:

>>> read_csv('myfile1.csv', delimiter=';', decimal=b',')
>>> read_csv('myfile2.csv', delimiter=';', decimal=b',')
>>> read_csv('myfile3.csv', delimiter=';', decimal=b',')
>>> read_csv('myfile4.csv', delimiter=';', decimal=b',')
>>> read_csv('myfile5.csv', delimiter=';', decimal=b',')

Proxy functions allows for changing defaults to the original function. One
simply define a function which has sensible defaults and call the original
function setting default values automatically:

>>> def mycsv(file, delimiter=';', decimal=b',', **kwargs):
...     return read_csv(file, delimiter=delimiter, decimal=decimal, **kwargs)

Thanks to using ``**kwargs`` there is no need to specify all the values
from the original function. The uncovered arguments will simply be put
in ``kwargs`` dictionary and passed to the original function:

>>> mycsv('myfile1.csv')
>>> mycsv('myfile2.csv')
>>> mycsv('myfile3.csv')
>>> mycsv('myfile4.csv')
>>> mycsv('myfile5.csv')

This allows for cleaner code. Each parameter will be passed to ``mycsv``
function. Then it will be checked if there is a different default value
already defined. If not, then parameter will be stored in ``kwargs`` and
passed to the original function:

>>> mycsv('myfile.csv', encoding='utf-8')
>>> mycsv('myfile.csv', encoding='utf-8', verbose=True)
>>> mycsv('myfile.csv', verbose=True, usecols=['Sepal Length', 'Species'])


Use Case - 0x08
---------------
Decorators are functions, which get reference to the decorated function as
it's argument, and has closure which gets original function arguments as
positional and keyword arguments:

>>> def mydecorator(func):
...     def wrapper(*args, **kwargs):
...         return func(*args, **kwargs)
...     return wrapper

Decorators could be used on any function, therefore we could not predict what
would be the name of the parameter passed to it:

>>> @mydecorator
... def add(a, b):
...     return a + b

>>> @mydecorator
... def echo(text):
...     return text

Moreover it depends on a user whether he/she chooses to run function
positionally, using keyword arguments or even both at the same time:

>>> add(1, 2)
3

>>> add(a=1, b=2)
3

>>> add(1, b=2)
3

>>> echo('hello')
'hello'


References
----------
.. [#pandasreadcsv] The pandas development team. API Reference Pandas.read_csv(). Year: 2021. Retrieved: 2021-12-05. URL: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html


Assignments
-----------
.. literalinclude:: assignments/star_arguments_a.py
    :caption: :download:`Solution <assignments/star_arguments_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/star_arguments_b.py
    :caption: :download:`Solution <assignments/star_arguments_b.py>`
    :end-before: # Solution
