Match Wildcard
==============
* https://peps.python.org/pep-0622/#wildcard-pattern

The `wildcard pattern` is a single underscore: ``_``.  It always
matches, but does not capture any variable (which prevents
interference with other uses for ``_`` and allows for some
optimizations).

>>> user = 'Mark'
>>>
>>> match user:
...     case 'Mark':        print('Hello Mark')
...     case 'Melissa':     print('Hello Melissa')
...     case 'Rick':        print('Hello Rick')
...     case 'Alex':        print('Hello Alex')
...     case 'Beth':        print('Hello Beth')
...     case 'Chris':       print('Hello Chris')
...     case _:             raise PermissionError
...
Hello Mark


Use Case - 0x01
---------------
>>> def html_color(name):
...     match name:
...         case 'red':   return '#ff0000'
...         case 'green': return '#00ff00'
...         case 'blue':  return '#0000ff'
...         case _:       raise NotImplementedError('Unknown color')

>>> html_color('black')
Traceback (most recent call last):
NotImplementedError: Unknown color

>>> html_color('orange')
Traceback (most recent call last):
NotImplementedError: Unknown color


Use Case - 0x02
---------------
>>> weekday = 0
>>>
>>> match weekday:
...     case 1: print('poniedziałek')
...     case 2: print('wtorek')
...     case 3: print('środa')
...     case 4: print('poniedziałek')
...     case 5: print('wtorek')
...     case 6: print('środa')
...     case 7: print('środa')
...     case _: raise ValueError('Invalid weekday')  # wildcard pattern
...
Traceback (most recent call last):
ValueError: Invalid weekday
