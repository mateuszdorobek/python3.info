Match Pattern Literal
=====================

A `literal pattern` is useful to filter constant values in a
structure. It looks like a Python literal (including some values like
``True``, ``False`` and ``None``). It only matches objects equal to
the literal, and never binds.

>>> def weekday(number):
...     match number:
...         case 1: print('Monday')
...         case 2: print('Tuesday')
...         case 3: print('Wednesday')
...         case 4: print('Thursday')
...         case 5: print('Friday')
...         case 6: print('Saturday')
...         case 7: print('Sunday')

>>> weekday(1)
Monday
>>>
>>> weekday(2)
Tuesday
>>>
>>> weekday(7)
Sunday


Use Case - 0x01
---------------
>>> def html_color(name):
...     match name:
...         case 'red':   return '#ff0000'
...         case 'green': return '#00ff00'
...         case 'blue':  return '#0000ff'
>>>
>>>
>>> html_color('red')
'#ff0000'
>>>
>>> html_color('green')
'#00ff00'
>>>
>>> html_color('blue')
'#0000ff'


Use Case - 0x02
---------------
>>> def status(result):
...     match result:
...         case True:  return 'success'
...         case False: return 'error'
...         case None:  return 'in-progress'
>>>
>>>
>>> status(True)
'success'
>>>
>>> status(False)
'error'
>>>
>>> status(None)
'in-progress'


Use Case - 0x03
---------------
>>> def http_status(status_code):
...     match status_code:
...         case 400:   return 'Bad request'
...         case 401:   return 'Unauthorized'
...         case 402:   return 'Payment Required'
...         case 403:   return 'Forbidden'
...         case 404:   return 'Not found'
...         case 418:   return "I'm a teapot"

>>> http_status(400)
'Bad request'
>>>
>>> http_status(403)
'Forbidden'
>>>
>>> http_status(404)
'Not found'


Use Case - 0x04
---------------
>>> def count(*args):
...     match len(args):
...         case 3: return 'Three'
...         case 2: return 'Two'
...         case 1: return 'One'
...         case 0: return 'Too few'
...         case _: return 'Too many'
>>>
>>>
>>> count(1, 2, 3, 4)
'Too many'
>>>
>>> count(1, 2, 3)
'Three'
>>>
>>> count(1, 2)
'Two'
>>>
>>> count(1)
'One'
>>>
>>> count()
'Too few'


Use Case - 0x05
---------------
>>> def say_hello(language):
...     match language:
...         case 'English': return 'Hello'
...         case 'German':  return 'Guten Tag'
...         case 'Spanish': return 'Hola'
...         case 'Polish':  return 'Witaj'
...         case _:         return "I don't speak this language"

>>> say_hello('English')
'Hello'
>>>
>>> say_hello('Polish')
'Witaj'
>>>
>>> say_hello('French')
"I don't speak this language"


Use Case - 0x06
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
...         case _:
...             raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')
...
...     current = start
...     result = []
...     while current < stop:
...         result.append(current)
...         current += step
...     return result


Use Case - 0x07
---------------
>>> def myrange(*args, **kwargs):
...     match len(args):
...         case 3:
...             start, stop, step = args
...         case 2:
...             start, stop = args
...             step = 1
...         case 1:
...             start = 0
...             stop = args[0]
...             step = 1
...         case 0:
...             raise TypeError('myrange expected at least 1 argument, got 0')
...         case _:
...             raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')
...     ...


Use Case - 0x08
---------------
>>> def myrange(*args, **kwargs):
...     match len(args):
...         case 3: start, stop, step = args
...         case 2: [start, stop], step = args, 1
...         case 1: start, [stop], step = 0, args, 1
...         case 0: raise TypeError('myrange expected at least 1 argument, got 0')
...         case _: raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')
...     ...


Use Case - 0x09
---------------
>>> import argparse
>>>
>>> parser = argparse.ArgumentParser()
>>> _ = parser.add_argument('command', choices=['push', 'pull', 'commit'])
>>> args = parser.parse_args(['push'])
>>>
>>> match args.command:
...     case 'push': print('Pushing...')
...     case 'pull': print('Pulling...')
...     case _:      parser.error(f'{args.command!r} not yet implemented')
...
Pushing...


Assignments
-----------
.. literalinclude:: assignments/match_literal_a.py
    :caption: :download:`Solution <assignments/match_literal_a.py>`
    :end-before: # Solution
