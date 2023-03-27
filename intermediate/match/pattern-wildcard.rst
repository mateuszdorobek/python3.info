Match Pattern Wildcard
======================

The `wildcard pattern` is a single underscore: ``_``.  It always
matches, but does not capture any variable (which prevents
interference with other uses for ``_`` and allows for some
optimizations).

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
