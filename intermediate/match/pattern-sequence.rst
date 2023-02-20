Match Pattern Sequence
======================

A `sequence pattern` looks like ``[a, *rest, b]`` and is similar to a
list unpacking. An important difference is that the elements nested
within it can be any kind of patterns, not just names or sequences. It
matches only sequences of appropriate length, as long as all the
sub-patterns also match. It makes all the bindings of its sub-patterns.


Use Case - 0x03
---------------
* HTTP Request

Test Setup:

>>> def handle_get(path):
...     ...
...
>>> def handle_post(path):
...     ...
...
>>> def handle_put(path):
...     ...
...
>>> def handle_delete(path):
...     ...
...

Use Case:

>>> request = 'GET /index.html HTTP/2.0'
>>>
>>> match request.split():
...     case ['GET', path, 'HTTP/2.0']:     handle_get(path)
...     case ['POST', path, 'HTTP/2.0']:    handle_post(path)
...     case ['PUT', path, 'HTTP/2.0']:     handle_put(path)
...     case ['DELETE', path, 'HTTP/2.0']:  handle_delete(path)
