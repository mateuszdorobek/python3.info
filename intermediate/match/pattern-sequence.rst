Match Sequence
==============

A `sequence pattern` looks like ``[a, *rest, b]`` and is similar to a
list unpacking. An important difference is that the elements nested
within it can be any kind of patterns, not just names or sequences. It
matches only sequences of appropriate length, as long as all the
sub-patterns also match. It makes all the bindings of its sub-patterns.

SetUp:

>>> def handle_get(path): ...
>>> def handle_post(path): ...
>>> def handle_put(path): ...
>>> def handle_delete(path): ...

Usage:

>>> request = 'GET /index.html HTTP/2.0'
>>>
>>> request.split()
['GET', '/index.html', 'HTTP/2.0']
>>>
>>> match request.split():
...     case ['GET', path, 'HTTP/2.0']:     handle_get(path)
...     case ['POST', path, 'HTTP/2.0']:    handle_post(path)
...     case ['PUT', path, 'HTTP/2.0']:     handle_put(path)
...     case ['DELETE', path, 'HTTP/2.0']:  handle_delete(path)


Use Case - 0x01
---------------
>>> request = 'GET /index.html HTTP/2.0'
>>>
>>>
>>> match request.split():  # doctest: +SKIP
...     case ['GET', path, 'HTTP/1.0']:  http10.get(path)
...     case ['GET', path, 'HTTP/1.1']:  http11.get(path)
...     case ['GET', path, 'HTTP/2.0']:  http20.get(path)


Use Case - 0x02
---------------
>>> request = 'GET /index.html HTTP/2.0'
>>>
>>>
>>> match request.split():  # doctest: +SKIP
...     case ['GET', uri, 'HTTP/1.0']:     http10.get(uri)
...     case ['GET', uri, 'HTTP/1.1']:     http11.get(uri)
...     case ['GET', uri, 'HTTP/2.0']:     http20.get(uri)
...     case ['GET', uri, 'HTTP/3.0']:     http30.get(uri)
...
...     case ['POST', uri, 'HTTP/1.0']:    http10.post(uri)
...     case ['POST', uri, 'HTTP/1.1']:    http11.post(uri)
...     case ['POST', uri, 'HTTP/2.0']:    http20.post(uri)
...     case ['POST', uri, 'HTTP/3.0']:    http30.post(uri)
...
...     case ['PUT', uri, 'HTTP/1.0']:     http10.put(uri)
...     case ['PUT', uri, 'HTTP/1.1']:     http11.put(uri)
...     case ['PUT', uri, 'HTTP/2.0']:     http20.put(uri)
...     case ['PUT', uri, 'HTTP/3.0']:     http30.put(uri)
...
...     case ['DELETE', uri, 'HTTP/1.0']:  http10.delete(uri)
...     case ['DELETE', uri, 'HTTP/1.1']:  http11.delete(uri)
...     case ['DELETE', uri, 'HTTP/2.0']:  http20.delete(uri)
...     case ['DELETE', uri, 'HTTP/3.0']:  http30.delete(uri)


Use Case - 0x03
---------------
>>> def values(*data):
...     match data:
...         case [a, b, c]: pass
...         case [a, b]: c = 0
...         case [a]: b = 0; c = 0
...         case []: raise ValueError('Empty list')
...         case _: raise ValueError('Other error')
...     return a, b, c

>>> a, b, c = values(1, 2, 3)
>>>
>>> a
1
>>> b
2
>>> c
3

>>> a, b, c = values(1, 2)
>>>
>>> a
1
>>> b
2
>>> c
0

>>> a, b, c = values(1)
>>> a
1
>>> b
0
>>> c
0

>>> a, b, c = values()
Traceback (most recent call last):
ValueError: Empty list


Use Case - 0x04
---------------
>>> def range(*args):
...     match args:
...         case [start, stop, step]: pass
...         case [start, stop]: step = 1
...         case [stop]: start = 0; step = 1
...         case []: raise TypeError('myrange expected at least 1 argument, got 0')
...         case _: raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')


Use Case - 0x05
---------------
>>> def range(*args):
...     match args:
...         case [stop]:
...             start = 0
...             step = 1
...         case [start, stop]:
...             step = 1
...         case [start, stop, step]:
...             pass
...         case []:
...             msg = 'myrange expected at least 1 argument, got 0'
...             raise TypeError(msg)
...         case _:
...             msg = f'myrange expected at most 3 arguments, got {len(args)}'
...             raise TypeError(msg)


Assignments
-----------
.. literalinclude:: assignments/match_sequence_a.py
    :caption: :download:`Solution <assignments/match_sequence_a.py>`
    :end-before: # Solution
