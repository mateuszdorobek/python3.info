Match Pattern Capture
=====================

A `capture pattern` looks like x and is equivalent to an identical
assignment target: it always matches and binds the variable with the
given (simple) name.


class Request:
    def __init__(self, request: str):

      request = ['POST', '/user/', 'HTTP/2.0']

        match request.split():
            case ['POST',   path, 'HTTP/1.0']: self.post(path)
            case ['POST',   path, 'HTTP/1.1']: self.post(path)
            case ['POST',   path, 'HTTP/2.0']: self.post(path)

            case ['GET',    path, 'HTTP/2.0']: self.get(path)
            case ['PUT',    path, 'HTTP/2.0']: self.put(path)
            case ['DELETE', path, 'HTTP/2.0']: self.delete(path)



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
>>>
>>>
>>> Request('POST /user/ HTTP/2.0')
Processing POST request for /user/
>>>
>>> Request('GET /user/mwatney/ HTTP/2.0')
Processing GET request for /user/mwatney/
>>>
>>> Request('PUT /user/mwatney/ HTTP/2.0')
Processing PUT request for /user/mwatney/
>>>
>>> Request('DELETE /user/mwatney/ HTTP/2.0')
Processing DELETE request for /user/mwatney/


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
>>>
>>>
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
