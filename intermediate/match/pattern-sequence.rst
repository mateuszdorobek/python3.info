Match Pattern Sequence
======================

A `sequence pattern` looks like ``[a, *rest, b]`` and is similar to a
list unpacking. An important difference is that the elements nested
within it can be any kind of patterns, not just names or sequences. It
matches only sequences of appropriate length, as long as all the
sub-patterns also match. It makes all the bindings of its sub-patterns.

>>> request = 'GET /index.html HTTP/2.0'
>>>
>>>
>>> match request.split():  # doctest: +SKIP
...     case ['GET', uri, 'HTTP/2.0']:     http20.get(uri)
...     case ['POST', uri, 'HTTP/2.0']:    http20.post(uri)
...     case ['PUT', uri, 'HTTP/2.0']:     http20.put(uri)
...     case ['DELETE', uri, 'HTTP/2.0']:  http20.delete(uri)


Use Case - 0x01
---------------
>>> request = 'GET /index.html HTTP/2.0'
>>>
>>>
>>> match request.split():  # doctest: +SKIP
...     case ['GET', uri, 'HTTP/1.0']:  http10.get(uri)
...     case ['GET', uri, 'HTTP/1.1']:  http11.get(uri)
...     case ['GET', uri, 'HTTP/2.0']:  http20.get(uri)


Use Case - 0x02
---------------
>>> request = 'GET /index.html HTTP/2.0'
>>>
>>>
>>> match request.split():  # doctest: +SKIP
...     case ['GET', uri, 'HTTP/1.1']:     http11.get(uri)
...     case ['GET', uri, 'HTTP/2.0']:     http20.get(uri)
...
...     case ['POST', uri, 'HTTP/1.1']:    http11.post(uri)
...     case ['POST', uri, 'HTTP/2.0']:    http20.post(uri)
...
...     case ['PUT', uri, 'HTTP/1.1']:     http11.put(uri)
...     case ['PUT', uri, 'HTTP/2.0']:     http20.put(uri)
...
...     case ['DELETE', uri, 'HTTP/1.1']:  http11.delete(uri)
...     case ['DELETE', uri, 'HTTP/2.0']:  http20.delete(uri)



Use Case - 0x03
---------------
>>> def range(*args):
...     match len(args):
...         case 3: start, stop, step = args
...         case 2: [start, stop], step = args, 1
...         case 1: start, [stop], step = 0, args, 1
...         case 0: raise TypeError('myrange expected at least 1 argument, got 0')
...         case _: raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')
...     ...


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
