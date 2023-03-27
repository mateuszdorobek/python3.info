Unpack Parameters
=================
* More information in `Unpack Assignment`
* More information in `Unpack Parameters`
* More information in `Unpack Arguments`


.. figure:: img/unpack-assignment,args,params.png


Syntax
------
>>> def myfunction(*args):
...     pass

>>> def myfunction(**kwargs):
...     pass

>>> def myfunction(*args, **kwargs):
...     pass


Recap
-----
* Parameter - Receiving variable used within the function
* Required parameters - Parameter which is necessary to call function
* Optional parameters - Parameter which is optional and has default value (if not specified at call time)
* Optional parameter - also known as: parameter with default value

Required parameters:

>>> def echo(a, b):
...     pass

Optional parameters:

>>> def echo(a=1, b=2):
...     pass

Required and optional parameters:

>>> def echo(a, b=2):
...     pass

Required parameters must be the leftmost:

>>> def echo(a=1, b):
...     pass
Traceback (most recent call last):
SyntaxError: non-default argument follows default argument


Positional Parameters
---------------------
* ``*`` is used for positional parameters
* ``args`` is a convention, but you can use any name
* ``*args`` unpacks to ``tuple``

>>> def echo(*args):
...     print(f'{args=}')
>>>
>>>
>>> echo()
args=()
>>>
>>> echo(1)
args=(1,)
>>>
>>> echo(2, 3)
args=(2, 3)
>>>
>>> echo(1, 2, 3, 4, 5)
args=(1, 2, 3, 4, 5)


Keyword Parameters
------------------
* ``**`` is used for keyword parameters
* ``kwargs`` is a convention, but you can use any name
* ``**kwargs`` unpacks to ``dict``

>>> def echo(**kwargs):
...     print(f'{kwargs=}')
>>>
>>>
>>> echo()
kwargs={}
>>>
>>> echo(a=1)
kwargs={'a': 1}
>>>
>>> echo(a=1, b=2)
kwargs={'a': 1, 'b': 2}
>>>
>>> echo(a=1, b=2, c=3, d=4, e=5)
kwargs={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


Positional and Keyword Parameters
---------------------------------
* ``*`` is used for positional parameters
* ``**`` is used for keyword parameters
* ``*args`` unpacks to ``tuple``
* ``**kwargs`` unpacks to ``dict``

>>> def echo(*args, **kwargs):
...     print(f'{args=}, {kwargs=}')
>>>
>>>
>>> echo()
args=(), kwargs={}
>>>
>>> echo(1, 2, 3)
args=(1, 2, 3), kwargs={}
>>>
>>> echo(d=4, e=5, f=6)
args=(), kwargs={'d': 4, 'e': 5, 'f': 6}
>>>
>>> echo(1, 2, 3, d=4, e=5, f=6)
args=(1, 2, 3), kwargs={'d': 4, 'e': 5, 'f': 6}


Parameters with Args, Kwargs
----------------------------
>>> def echo(a, b, c=None, *args):
...     print(f'{a=}, {b=}, {c=}, {args=}')
>>>
>>>
>>> echo(1, 2)
a=1, b=2, c=None, args=()
>>>
>>> echo(1, 2, 3)
a=1, b=2, c=3, args=()
>>>
>>> echo(1, 2, 3, 4)
a=1, b=2, c=3, args=(4,)
>>>
>>> echo(1, 2, 3, 4, 5, 6)
a=1, b=2, c=3, args=(4, 5, 6)

>>> def echo(a, b, c=None, **kwargs):
...     print(f'{a=}, {b=}, {c=}, {kwargs=}')
>>>
>>>
>>> echo(1, 2)
a=1, b=2, c=None, kwargs={}
>>>
>>> echo(1, 2, 3)
a=1, b=2, c=3, kwargs={}
>>>
>>> echo(1, 2, 3, d=7, e=8, f=9)
a=1, b=2, c=3, kwargs={'d': 7, 'e': 8, 'f': 9}
>>>
>>> echo(1, 2, a=7)
Traceback (most recent call last):
TypeError: echo() got multiple values for argument 'a'

>>> def echo(a, b, c=None, *args, **kwargs):
...     print(f'{a=}, {b=}, {c=}, {args=}, {kwargs=}')
>>>
>>>
>>> echo(1, 2)
a=1, b=2, c=None, args=(), kwargs={}
>>>
>>> echo(1, 2, 3, 4, 5, 6)
a=1, b=2, c=3, args=(4, 5, 6), kwargs={}
>>>
>>> echo(1, 2, 3, d=7, e=8, f=9)
a=1, b=2, c=3, args=(), kwargs={'d': 7, 'e': 8, 'f': 9}
>>>
>>> echo(1, 2, 3, 4, 5, 6, d=7, e=8, f=9)
a=1, b=2, c=3, args=(4, 5, 6), kwargs={'d': 7, 'e': 8, 'f': 9}


Merge
-----
>>> def echo(a,b,c,d,e):
...     return locals()
...
...
>>> data1 = {'a':1, 'b':2, 'c':3}
>>> data2 = {'d':4, 'e':5}
>>>
>>> echo(**data1, **data2)
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Merging dicts before Python 3.9:

>>> {**data1, **data2}
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Merging dicts since Python 3.9:

>>> data1 | data2
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}




Use Case - 0x01
---------------
>>> def add(*values):
...     total = 0
...     for value in values:
...         total += value
...     return total
>>>
>>>
>>> add()
0
>>>
>>> add(1)
1
>>>
>>> add(1, 4)
5
>>>
>>> add(3, 1)
4
>>>
>>> add(1, 2, 3, 4)
10


Use Case - 0x02
---------------
>>> def celsius_to_kelvin(*degrees):
...     return [x+273.15 for x in degrees]
>>>
>>>
>>> celsius_to_kelvin(1)
[274.15]
>>>
>>> celsius_to_kelvin(1, 2, 3, 4, 5)
[274.15, 275.15, 276.15, 277.15, 278.15]


Use Case - 0x03
---------------
>>> def html_list(*fruits):
...     print('<ul>')
...     for fruit in fruits:
...         print(f'<li>{fruit}</li>')
...     print('</ul>')
>>>
>>>
>>> html_list('apple', 'banana', 'orange')
<ul>
<li>apple</li>
<li>banana</li>
<li>orange</li>
</ul>


Use Case - 0x04
---------------
Intuitive definition of ``print`` function:

>>> print('hello')
hello
>>>
>>> print('hello', 'world')
hello world
>>>
>>> print('hello', 'new', 'world')
hello new world

>>> def print(*values, sep=' ', end='\n'):
...     return sep.join(values) + end



Assignments
-----------
.. literalinclude:: assignments/star_parameters_a.py
    :caption: :download:`Solution <assignments/star_parameters_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/star_parameters_b.py
    :caption: :download:`Solution <assignments/star_parameters_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/star_parameters_c.py
    :caption: :download:`Solution <assignments/star_parameters_c.py>`
    :end-before: # Solution
