Match Pattern Walrus
====================

A `walrus pattern` looks like ``d := datetime(year=2020, month=m)``. It
matches only if its sub-pattern also matches. It binds whatever the
sub-pattern match does, and also binds the named variable to the entire
object.

SetUp
-----
>>> import re


Assignment Expression
---------------------
* A.K.A. Walrus Operator
* ``re.match()`` returns ``re.Match | None``

>>> email = 'mwatney@nasa.gov'
>>>
>>> result = re.match('[a-z]+@nasa.gov', email)
>>> print(result.group())
mwatney@nasa.gov

>>> email = 'mwatney@esa.int'  # invalid domain
>>>
>>> result = re.match('[a-z]+@nasa.gov', email)
>>> print(result.group())
Traceback (most recent call last):
AttributeError: 'NoneType' object has no attribute 'group'

>>> email = 'mwatney@esa.int'  # invalid domain
>>>
>>> result = re.match('[a-z]+@nasa.gov', email)
>>> if result:
...     print(result.group())
... else:
...     print('Invalid domain')
Invalid domain

>>> email = 'mwatney@esa.int'  # invalid domain
>>>
>>> if result := re.match('[a-z]+@nasa.gov', email):
...     print(result.group())
... else:
...     print('Invalid domain')
Invalid domain
