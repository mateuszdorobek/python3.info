String Define
=============
* ``str`` is a sequence of characters


Syntax
------
Empty string:

>>> data = ''

Define string:

>>> data = 'Mark Watney'

Multiline string:

>>> data =  'First line\nSecond line\nThird line'

>>> data = """First line
... Second line
... Third line"""

Longer strings (mind space at the end):

>>> data = text = (
...     'First part '
...     'Second part '
...     'Third part'
... )

>>> data = 'First part ' \
...        'Second part ' \
...        'Third part'


Quotes or Apostrophes
---------------------
* ``"`` and ``'`` works the same
* Choose one and keep consistency in code
* Python console prefers single quote (``'``) character
* It matters for ``doctest``, which compares two outputs character by character
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three
  double quote (``"""``) characters

Both ``"`` and ``'`` works the same

>>> a = 'It is Monty Python'
>>> b = "It is Monty Python"
>>>
>>> a == b
True

Python console prefers single quote (``'``) character:

>>> text = 'It is Monty Python'
>>> text
'It is Monty Python'
>>>
>>> text = "It is Monty Python"
>>> text
'It is Monty Python'

Why we have both?

>>> text = 'It\'s Monty Python'
>>> text
"It's Monty Python"
>>>
>>> text = "It's Monty Python"
>>> text
"It's Monty Python"

It's better to use double quotes, when text has apostrophes. This is also a
default the behavior of Python console, which prefers less escape characters:

>>> text = 'It\'s Monty Python'
>>> text
"It's Monty Python"

However HTML and XML uses double quotes to enclose attribute values,
hence it's better to use single quotes for the string:

>>> html = '<a href="https://python3.info">Python Book</a>'
>>> html
'<a href="https://python3.info">Python Book</a>'
>>>
>>> html = "<a href=\"https://python3.info\">Python Book</a>"
>>> html
'<a href="https://python3.info">Python Book</a>'

Errors:

>>> text = 'It's Monty Python'
Traceback (most recent call last):
SyntaxError: unterminated string literal (detected at line 1)

>>> html = "<a href="https://python3.info">Python Book</a>"
Traceback (most recent call last):
SyntaxError: invalid syntax

:pep:`257` -- Docstring Conventions: For multiline ``str`` always use three
double quote (``"""``) characters

>>> text = """It's \"Monty Python\""""
>>> text = '''It\'s "Monty Python"'''


Docstring
---------
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three
  double quote (``"""``) characters
* More information in `Function Doctest`

If assigned to variable, it serves as multiline ``str`` otherwise
it's a docstring:

>>> """We choose to go to the Moon!
... We choose to go to the Moon in this decade and do the other things,
... not because they are easy, but because they are hard;
... because that goal will serve to organize and measure the best of our
... energies and skills, because that challenge is one that we are willing
... to accept, one we are unwilling to postpone, and one we intend to win,
... and the others, too."""  # doctest: +SKIP

>>> text = """We choose to go to the Moon!
... We choose to go to the Moon in this decade and do the other things,
... not because they are easy, but because they are hard;
... because that goal will serve to organize and measure the best of our
... energies and skills, because that challenge is one that we are willing
... to accept, one we are unwilling to postpone, and one we intend to win,
... and the others, too."""


Type Conversion
---------------
Builtin function  ``str()`` converts argument to ``str``

>>> str('Moon')
'Moon'
>>>
>>> str(1969)
'1969'
>>>
>>> str(1.337)
'1.337'

Builtin function ``print()`` before printing on the screen
runs ``str()`` on its arguments:

>>> print(1969)
1969


Assignments
-----------
.. literalinclude:: assignments/type_strdefine_a.py
    :caption: :download:`Solution <assignments/type_strdefine_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_strdefine_b.py
    :caption: :download:`Solution <assignments/type_strdefine_b.py>`
    :end-before: # Solution

.. todo:: assignments with ord()
.. todo:: assignments with chr()
.. todo:: assignments with ascii()
