Regex RE Compile
================
* ``re.compile()``
* Used when pattern is reused (especially in the loop)


Syntax
------
>>> # doctest: +SKIP
... re.compile(<pattern>, <text>)


Example
-------
>>> import re
>>>
>>> fullname = re.compile(r'(?P<firstname>\w+) (?P<lastname>\w+)')


No Compile
----------
Compiles at every loop iteration, and then matches:

>>> import re
>>>
>>>
>>> DATA = [
...     'mark.watney@nasa.gov',
...     'Mark.Watney@nasa.gov',
...     '+mark.watney@nasa.gov',
...     'mark.watney+@nasa.gov',
...     'mark.watney+newsletter@nasa.gov',
...     'mark.watney@.gov',
...     '@nasa.gov',
...     'mark.watney@nasa.g',
... ]
>>>
>>>
>>> valid_email = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'
>>>
>>> for email in DATA:
...     if re.match(valid_email, email):
...         print('valid  ', email)
...     else:
...         print('invalid', email)
valid   mark.watney@nasa.gov
valid   Mark.Watney@nasa.gov
invalid +mark.watney@nasa.gov
valid   mark.watney+@nasa.gov
valid   mark.watney+newsletter@nasa.gov
invalid mark.watney@.gov
invalid @nasa.gov
invalid mark.watney@nasa.g


Compile
-------
Compiling before loop, hence matching only inside:

>>> import re
>>>
>>>
>>> DATA = [
...     'mark.watney@nasa.gov',
...     'Mark.Watney@nasa.gov',
...     '+mark.watney@nasa.gov',
...     'mark.watney+@nasa.gov',
...     'mark.watney+newsletter@nasa.gov',
...     'mark.watney@.gov',
...     '@nasa.gov',
...     'mark.watney@nasa.g',
... ]
>>>
>>>
>>> valid_email = re.compile(r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$')
>>>
>>> for email in DATA:
...     if valid_email.match(email):
...         print('valid  ', email)
...     else:
...         print('invalid', email)
valid   mark.watney@nasa.gov
valid   Mark.Watney@nasa.gov
invalid +mark.watney@nasa.gov
valid   mark.watney+@nasa.gov
valid   mark.watney+newsletter@nasa.gov
invalid mark.watney@.gov
invalid @nasa.gov
invalid mark.watney@nasa.g
