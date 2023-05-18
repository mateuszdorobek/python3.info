Function Arguments
==================
* Argument - value/variable/reference being passed to the function
* Positional argument - value passed to function - order is important
* Keyword argument - value passed to function resolved by name - order is not important

Function definition with parameters:

.. code-block:: python

    myfunction(<arguments>)

>>> add(1, 2)  # doctest: +SKIP
>>> add(a=1, b=2)  # doctest: +SKIP
>>> add(1, b=2)  # doctest: +SKIP

.. glossary::

    argument
        Value/variable/reference being passed to the function

    positional argument
        Value passed to function - order is important

    keyword argument
        Value passed to function resolved by name - order is not important


Positional Arguments
--------------------
* Order of positional arguments has significance

Let's define a function:

>>> def echo(a, b):
...     return f'{a=}, {b=}'

Positional arguments are resolved by order. This mean, that the first
argument will be assigned to the first parameter, and the second argument
to the second parameter and so on:

>>> echo(1, 2)
'a=1, b=2'

The order of positional parameters is important:

>>> echo(2, 1)
'a=2, b=1'


Keyword Arguments
-----------------
* Order of keyword arguments has no significance

Let's define a function:

>>> def echo(a, b):
...     return f'{a=}, {b=}'

Keyword arguments are resolved by name instead of the position. This mean, that
the argument with particular name will be assigned to the corresponding parameter
with the same name in function signature.

>>> echo(a=1, b=2)
'a=1, b=2'

The order of keyword parameters is not important, because values are assigned by
name, not a position:

>>> echo(b=2, a=1)
'a=1, b=2'


Positional and Keyword Arguments
--------------------------------
* Positional arguments must be at the left side
* Keyword arguments must be at the right side

>>> def echo(a, b):
...     return f'{a=}, {b=}'

All positional arguments must be on the left side, and all the required arguments
must be on the right side:

>>> echo(1, b=2)
'a=1, b=2'

Passing positional argument which follows keyword argument will yield a
``SyntaxError``:

>>> echo(a=1, 2)
Traceback (most recent call last):
SyntaxError: positional argument follows keyword argument

Positional argument are resolved first. Defining keyword argument which follows
positional argument with the same name will yield a ``TypeError``:

>>> echo(1, a=2)
Traceback (most recent call last):
TypeError: echo() got multiple values for argument 'a'


Errors
------
>>> def echo(a, b, c, d, e):
...     return f'{a=}, {b=}, {c=}, {d=}, {e=}'
>>>
>>>
>>> echo(1, 2, 3)
Traceback (most recent call last):
TypeError: echo() missing 2 required positional arguments: 'd' and 'e'
>>>
>>> echo(1, 2, 3, d=4)
Traceback (most recent call last):
TypeError: echo() missing 1 required positional argument: 'e'
>>>
>>> echo(1, 2, 3, d=4, 5)
Traceback (most recent call last):
SyntaxError: positional argument follows keyword argument
>>>
>>> echo(1, 2, 4, 5, c=3)
Traceback (most recent call last):
TypeError: echo() got multiple values for argument 'c'
>>>
>>> echo(1, 2, 3, d=4, e=5)
'a=1, b=2, c=3, d=4, e=5'


Use Case - 0x01
---------------
>>> def say_hello(text='say what?'):
...      return text
>>>
>>>
>>> say_hello('hello')
'hello'
>>>
>>> say_hello(text='hello world')
'hello world'
>>>
>>> say_hello()
'say what?'


Use Case - 0x02
---------------
>>> def connect(*args, **kwargs):
...     ...

>>> connect('myusername', 'mypassword')

>>> connect('myusername', 'mypassword', 'example.com', 443, False, 1, True)

>>> connect(host='example.com', username='myusername', password='mypassword')

>>> connect(
...     host='example.com',
...     username='myusername',
...     password='mypassword',
...     port=443,
...     ssl=True,
...     persistent=True)


Use Case - 0x03
---------------
>>> def read_csv(*args, **kwargs):
...     pass

>>> read_csv('iris.csv')

>>> read_csv('iris.csv', encoding='utf-8')

>>> read_csv('iris.csv', encoding='utf-8', parse_dates=['born'])

>>> read_csv('iris.csv', skiprows=3, delimiter=';')

>>> read_csv('iris.csv',
...     encoding='utf-8',
...     skiprows=3,
...     delimiter=';',
...     usecols=['sepal_length', 'species'],
...     parse_dates=['born'])


Assignments
-----------
.. literalinclude:: assignments/function_args_a.py
    :caption: :download:`Solution <assignments/function_args_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_b.py
    :caption: :download:`Solution <assignments/function_args_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_c.py
    :caption: :download:`Solution <assignments/function_args_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_d.py
    :caption: :download:`Solution <assignments/function_args_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_e.py
    :caption: :download:`Solution <assignments/function_args_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_f.py
    :caption: :download:`Solution <assignments/function_args_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_g.py
    :caption: :download:`Solution <assignments/function_args_g.py>`
    :end-before: # Solution
