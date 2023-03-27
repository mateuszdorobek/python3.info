Match Pattern Literal
=====================

A `literal pattern` is useful to filter constant values in a
structure. It looks like a Python literal (including some values like
``True``, ``False`` and ``None``). It only matches objects equal to
the literal, and never binds.


>>> weekday = 1
>>>
>>> match weekday:
...     case 1: print('Monday')
...     case 2: print('Tuesday')
...     case 3: print('Wednesday')
...     case 4: print('Thursday')
...     case 5: print('Friday')
...     case 6: print('Saturday')
...     case 7: print('Sunday')
Monday


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
* HTTP Status

>>> status = 404
>>>
>>> match status:
...     case 400:   reason = 'Bad request'
...     case 401:   reason = 'Unauthorized'
...     case 402:   reason = 'Payment Required'
...     case 402:   reason = 'Forbidden'
...     case 404:   reason = 'Not found'
...     case 418:   reason = "I'm a teapot"
>>>
>>>
>>> print(reason)
Not found


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
>>> count(1,2,3,4)
'Too many'
>>>
>>> count(1,2,3)
'Three'
>>>
>>> count(1,2)
'Two'
>>>
>>> count(1)
'One'
>>>
>>> count()
'Too few'


Use Case - 0x05
---------------
Simulate user input (for test automation):

>>> from unittest.mock import MagicMock
>>> input = MagicMock(side_effect=['French'])

Use Case:

>>> language = input('What is your language?: ')  #input: 'French'
>>>
>>> match language:
...     case 'English': response = 'Hello'
...     case 'German':  response = 'Guten Tag'
...     case 'Spanish': response = 'Hola'
...     case 'Polish':  response = 'Witaj'
...     case _:         response = "I don't speak this language"
>>>
>>>
>>> print(response)
I don't speak this language


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
...
...     while current < stop:
...         result.append(current)
...         current += step
...
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
...     case 'push':
...         print('pushing')
...     case 'pull':
...         print('pulling')
...     case _:
...         parser.error(f'{args.command!r} not yet implemented')
...
pushing


Assignments
-----------
.. literalinclude:: assignments/match_literal_a.py
    :caption: :download:`Solution <assignments/match_literal_a.py>`
    :end-before: # Solution
