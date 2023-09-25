Match Sequence
==============
* https://peps.python.org/pep-0622/#sequence-patterns

A `sequence pattern` looks like ``[a, *rest, b]`` and is similar to a
list unpacking. An important difference is that the elements nested
within it can be any kind of patterns, not just names or sequences. It
matches only sequences of appropriate length, as long as all the
sub-patterns also match. It makes all the bindings of its sub-patterns.



>>> point = (1,2)
>>>
>>> match point:
...     case (x,y):     print(f'Point 2d: {x=}, {y=}')
...     case (x,y,z):   print(f'Point 3d: {x=}, {y=}, {z=}')
...
Point 2d: x=1, y=2

>>> point = (1,2,3)
>>>
>>> match point:
...     case (x,y):     print(f'Point 2d: {x=}, {y=}')
...     case (x,y,z):   print(f'Point 3d: {x=}, {y=}, {z=}')
...
Point 3d: x=1, y=2, z=3


Use Case - 0x01
---------------
SetUp:

>>> def handle_get(path): ...
>>> def handle_post(path): ...
>>> def handle_put(path): ...
>>> def handle_delete(path): ...

Usage:

>>> request = ['GET', '/index.html', 'HTTP/2.0']
>>>
>>> match request:
...     case ['GET', path, 'HTTP/2.0']:     handle_get(path)
...     case ['POST', path, 'HTTP/2.0']:    handle_post(path)
...     case ['PUT', path, 'HTTP/2.0']:     handle_put(path)
...     case ['DELETE', path, 'HTTP/2.0']:  handle_delete(path)


Use Case - 0x02
---------------
SetUp:

>>> def http10_get(path): ...
>>> def http11_get(path): ...
>>> def http20_get(path): ...
>>> def http30_get(path): ...

Usage:

>>> request = ['GET', '/index.html', 'HTTP/2.0']
>>>
>>> match request:  # doctest: +SKIP
...     case ['GET', path, 'HTTP/1.0']:  http10_get(path)
...     case ['GET', path, 'HTTP/1.1']:  http11_get(path)
...     case ['GET', path, 'HTTP/2.0']:  http20_get(path)
...     case ['GET', path, 'HTTP/3.0']:  http30_get(path)


Use Case - 0x03
---------------
SetUp:

>>> def handle_get(path): ...
>>> def handle_post(path): ...
>>> def handle_put(path): ...
>>> def handle_delete(path): ...

Usage:

>>> request = ['GET', '/index.html', 'HTTP/2.0']
>>>
>>> match request:
...     case ['GET', path, _]:     handle_get(path)
...     case ['POST', path, _]:    handle_post(path)
...     case ['PUT', path, _]:     handle_put(path)
...     case ['DELETE', path, _]:  handle_delete(path)


Use Case - 0x04
---------------
>>> request = 'GET /index.html HTTP/2.0'
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


Use Case - 0x05
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



Use Case - 0x01
---------------
>>> class Astronaut:
...     def move(self, *how):
...         match how:
...             case ['left', value]:   hero.move_left(value)
...             case ['right', value]:  hero.move_right(value)
...             case ['up', value]:     hero.move_up(value)
...             case ['down', value]:   hero.move_down(value)
...             case _: raise RuntimeError('Invalid move')
...
...     def move_left(self, value):
...         print(f'Moving left by {value}')
...
...     def move_right(self, value):
...         print(f'Moving right by {value}')
...
...     def move_up(self, value):
...         print(f'Moving up by {value}')
...
...     def move_down(self, value):
...         print(f'Moving down by {value}')

>>> hero = Astronaut()
>>>
>>> hero.move('left', 1)
Moving left by 1
>>>
>>> hero.move('right', 2)
Moving right by 2
>>>
>>> hero.move('up', 3)
Moving up by 3
>>>
>>> hero.move('down', 4)
Moving down by 4


Use Case - 0x02
---------------
>>> class Request:
...     def __init__(self, request: str):
...         match request.split():
...             case ['GET',    path, 'HTTP/2.0']: self.get(path)
...             case ['POST',   path, 'HTTP/2.0']: self.post(path)
...             case ['PUT',    path, 'HTTP/2.0']: self.put(path)
...             case ['DELETE', path, 'HTTP/2.0']: self.delete(path)
...
...     def get(self, path):
...         self.response = f'Processing GET request for {path}'
...
...     def post(self, path):
...         self.response = f'Processing POST request for {path}'
...
...     def put(self, path):
...         self.response = f'Processing PUT request for {path}'
...
...     def delete(self, path):
...         self.response = f'Processing DELETE request for {path}'
...
...     def __repr__(self):
...         return self.response

>>> Request('POST /user/ HTTP/2.0')
Processing POST request for /user/

>>> Request('GET /user/mwatney/ HTTP/2.0')
Processing GET request for /user/mwatney/

>>> Request('PUT /user/mwatney/ HTTP/2.0')
Processing PUT request for /user/mwatney/

>>> Request('DELETE /user/mwatney/ HTTP/2.0')
Processing DELETE request for /user/mwatney/


Use Case - 0x03
---------------
* HTTP Request

Test Setup:

>>> def handle_get(path): ...
>>> def handle_post(path): ...
>>> def handle_put(path): ...
>>> def handle_delete(path): ...

Use Case:

>>> request = 'GET /index.html HTTP/2.0'
>>>
>>> match request.split():
...     case ['GET', path, 'HTTP/2.0']:     handle_get(path)
...     case ['POST', path, 'HTTP/2.0']:    handle_post(path)
...     case ['PUT', path, 'HTTP/2.0']:     handle_put(path)
...     case ['DELETE', path, 'HTTP/2.0']:  handle_delete(path)


Assignments
-----------
.. literalinclude:: assignments/match_sequence_a.py
    :caption: :download:`Solution <assignments/match_sequence_a.py>`
    :end-before: # Solution
