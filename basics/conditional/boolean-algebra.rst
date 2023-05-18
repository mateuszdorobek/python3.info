Boolean Algebra
===============


>>> True and True or False
True
>>>
>>> False and False or True
True

>>> (True and True) or False
True
>>>
>>> True and (True or False)
True

>>> True and False or False
False
>>>
>>> True and (False or False)
False

>>> True or False and True
True
>>>
>>> False or True and False
False
>>>
>>> False or True and True
True
>>>
>>> (False or True) and True
True
>>> (False or True) and False
False
>>>
>>> True and True or False and True
True
>>> True and (True or False) and True
True
>>>
>>> True or False and True or False
True
>>> (True or False) and (True or False)
True
>>> True or False and True or True
True
>>> (True or False) and (True or True)
True


Precedence
----------
* First ``and``s are evaluated together
* Then ``or``s


Optimization
------------
* Python won't evaluate the rest of an expression if already knows an answer

Python won't evaluate the rest of an expression if already knows an answer.
In the following example you may see, that expression on the right side
is not checked at all! Mind also, that variable ``x`` was never defined!

>>> False and x > 1
False
>>>
>>> x
Traceback (most recent call last):
NameError: name 'x' is not defined

Python will see ``False and ...``. ``False`` and something will always
return ``False`` so Python does performance optimization and won't even
check the other argument. In this case, it would fail with ``NameError``
if it does.


Example
-------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> (firstname == 'Mark' and lastname == 'Watney') \
...     or (firstname == 'Melissa' and lastname == 'Lewis') \
...     or (firstname == 'Rick' and lastname == 'Martinez')
True

Because:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> firstname == 'Mark' and lastname == 'Watney'
True
>>>
>>> firstname == 'Melissa' and lastname == 'Lewis'
False
>>>
>>> firstname == 'Rick' and lastname == 'Martinez'
False

Rule:

>>> True or False or False
True


Control Flow
------------
* Use parenthesis for explicit order

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> if (firstname == 'Mark' and lastname == 'Watney') \
...         or (firstname == 'Melissa' and lastname == 'Lewis') \
...         or (firstname == 'Rick' and lastname == 'Martinez'):
...
...     print('Hello user')
... else:
...     print('Access denied')
Hello user


Good Practices
--------------
>>> # doctest: +SKIP
... for line in file:
...     if line and (not line.startswith('#') or not line.isspace()):
...         ...

>>> # doctest: +SKIP
... for line in file:
...     if len(line) == 0:
...         continue
...
...     if line.startswith('#'):
...         continue
...
...     if line.isspace():
...         continue


.. todo:: Assignments
