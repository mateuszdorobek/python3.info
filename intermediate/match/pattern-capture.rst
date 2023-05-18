Match Capture
=============
* https://peps.python.org/pep-0622/#capture-patterns

A `capture pattern` looks like x and is equivalent to an identical
assignment target: it always matches and binds the variable with the
given (simple) name.

A capture pattern serves as an assignment target for the matched expression.
Only a single name is allowed (a dotted name is a constant value pattern).
A capture pattern always succeeds.

>>> name = 'Mark'
>>>
>>> match name:
...     case '':
...         print('Hello stranger')
...     case firstname:
...         print(f'Hello {firstname}')
Hello Mark
