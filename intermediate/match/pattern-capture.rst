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
...     case 'Mark':    print('Hello Mark')     # Literal pattern
...     case 'Melissa': print('Hello Melissa')  # Literal pattern
...     case name:      print(f'Hello {name}')  # Capture pattern
...
Hello Mark


Use Case - 0x01
---------------
>>> def myrange(*args, **kwargs):
...     if kwargs:
...         raise TypeError('myrange() takes no keyword arguments')
...
...     match len(args):
...         case 3:
...             start = args[0]
...             stop = args[1]
...             step = args[2]
...         case 2:
...             start = args[0]
...             stop = args[1]
...             step = 1
...         case 1:
...             start = 0
...             stop = args[0]
...             step = 1
...         case 0:
...             raise TypeError('myrange expected at least 1 argument, got 0')
...         case other:
...             raise TypeError(f'myrange expected at most 3 arguments, got {other}')
...
...     current = start
...     result = []
...
...     while current < stop:
...         result.append(current)
...         current += step
...
...     return result
