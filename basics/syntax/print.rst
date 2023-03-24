Syntax Print
============


String
------
* Either quotes (") or apostrophes (') will work
* Pick one and be consistent
* Do not mix - ``str`` opening and closing characters must be the same
* More information in `String Define`

Either quotes (") or apostrophes (') will work. This topic will be covered
in depth while talking about string type.

>>> name = 'Mark'
>>> name = "Mark"

>>> name = "Mark'
Traceback (most recent call last):
SyntaxError: unterminated string literal (detected at line 1)

>>> name = 'Mark"
Traceback (most recent call last):
SyntaxError: unterminated string literal (detected at line 1)


String Interpolation
--------------------
* String interpolation will substitute variable
* More information in `String Literals`

>>> name = 'Mark'
>>>
>>> 'Hello {name}'
'Hello {name}'
>>>
>>> f'Hello {name}'
'Hello Mark'

Note, that adding ``f`` in front of the string will turn on the string
interpolation - variable substitution. Without it, string will be interpreted
as it is - with curly braces and variable name in it.


Print
-----
* Prints on the screen
* Print string
* Print variable
* Print formatted (interpolated) string
* More information in `Builtin Printing`

Print string:

>>> print('Hello World')
Hello World

Print variable:

>>> text = 'Hello World'
>>> print(text)
Hello World

Print interpolated string:

>>> name = 'Mark'
>>> print(f'Hello {name}')
Hello Mark


Newlines
--------
* Use ``\n`` for newline
* Do not add space after ``\n`` character

>>> print('Hello World')
Hello World

>>> print('Hello\nWorld')
Hello
World

>>> print('Hello\n World')
Hello
 World


Assignments
-----------
.. literalinclude:: assignments/syntax_print_a.py
    :caption: :download:`assignments/syntax_print_a.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_print_b.py
    :caption: :download:`assignments/syntax_print_b.py`
    :end-before: # Solution
