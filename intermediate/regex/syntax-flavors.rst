Regex Syntax Flavors
====================
* In other programming languages
* PCRE - Perl Compatible Regular Expressions

.. figure:: img/regex-xkcd-standards.png

    How Standards Proliferate. XKCD Standards [#xkcd927]_


SetUp
-----
>>> import re


Future
------
* Since Python 3.11
* Atomic grouping ``((?>...))`` and possessive quantifiers (``*+``, ``++``, ``?+``, ``{m,n}+``) are now supported in regular expressions.
* https://www.regular-expressions.info/atomic.html
* https://github.com/python/cpython/issues/34627


Enclosing
---------
* In Python we use raw-string (``r'...'``)
* In JavaScript we use ``/pattern/flags`` or ``new RegExp(pattern, flags)``

Python:

>>> string = 'hello'
>>> string = "hello"
>>> regex = r'[a-z]+'
>>> regex = r"[a-z]+"

JavaScript:

.. code-block:: javascript

    string = "hello"
    regex = /[a-z]+/
    regex = new RegExp('[a-z]+)


Flags
-----
* In Python we use raw-string (``r'...'``)
* In JavaScript we use ``/pattern/flags`` or ``new RegExp(pattern, flags)``

Python:

>>> # doctest: +SKIP
... re.findall(r'[a-z]+', TEXT, flags=re.I)
... re.findall(r'[a-z]+', TEXT, flags=re.IGNORECASE)

.. code-block:: javascript

    /[a-z]+/i
    new RegExp("[a-z]", 'i')


Named Ranges
------------
* ``[:allnum:]`` - Alphabetic and numeric character ``[a-zA-Z0-9]``
* ``[:alpha:]`` - Alphabetic character ``[a-zA-Z]``
* ``[:alnum:]`` - Alphabetic and numeric character ``[a-zA-Z0-9]``
* ``[:alpha:]`` - Alphabetic character ``[a-zA-Z]``
* ``[:blank:]`` - Space or tab
* ``[:cntrl:]`` - Control character
* ``[:digit:]`` - Digit
* ``[:graph:]`` - Non-blank character (excludes spaces, control characters, and similar)
* ``[:lower:]`` - Lowercase alphabetical character
* ``[:print:]`` - Like [:graph:], but includes the space character
* ``[:punct:]`` - Punctuation character
* ``[:space:]`` - Whitespace character (``[:blank:]``, newline, carriage return, etc.)
* ``[:upper:]`` - Uppercase alphabetical
* ``[:xdigit:]`` - Digit allowed in a hexadecimal number (i.e., 0-9a-fA-F)
* ``[:word:]`` - A character in one of the following Unicode general categories Letter, Mark, Number, Connector_Punctuation
* ``[:ascii:]`` - A character in the ASCII character set

In Python those Named Ranges does not work. String ``[:alpha:]`` will be
interpreted literally as either: ``:`` or ``a`` or ``l`` or ``p`` or ``h``
or ``a``.

>>> import re
>>> TEXT = 'hello world'
>>>
>>>
>>> re.findall(r'[:allnum:]', TEXT)
['l', 'l', 'l']
>>>
>>> re.findall(r'[:alpha:]', TEXT)
['h', 'l', 'l', 'l']


Range
-----
* ``[a-Z]`` == ``[a-zA-Z]``
* ``[a-9]`` == ``[a-zA-Z0-9]``
* Works in other languages, but not in Python

>>> import re
>>> TEXT = 'hello world'
>>>
>>>
>>> re.findall(r'[a-Z]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-Z at position 1
>>>
>>> re.findall(r'[a-9]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-9 at position 1


Group Backreference
-------------------
* ``$1`` - grep, egrep, Jetbrains IDE
* ``\1``
* ``\g<1>`` - Python
* ``\g<name>`` - Python

In JavaScript name groups don't have ``?P`` but only ``?``:

.. code-block:: python

    '(?P<name>\d+)'

.. code-block:: javascript

    '(?<name>\d+)'


>>> HTML = '<span>Hello World</span>'
>>> re.findall(r'<(?P<tag>.+)>(?:.+)</(?P=tag)>', HTML)
['span']

>>> ARES = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>>
>>> year = r'(?P<year>\d{4})'
>>> month = r'(?P<month>[A-Z][a-z]+)'
>>> day = r'(?P<day>\d{1,2})'
>>> date = f'{month} {day}(?:st|nd|rd|th), {year}'
>>>
>>> re.search(date, ARES).groupdict()
{'month': 'Nov', 'day': '7', 'year': '2035'}
>>>
>>> re.sub(date, '\g<year> \g<month> \g<day>', ARES)
'Mark Watney of Ares 3 landed on Mars on: 2035 Nov 7 at 13:37'
>>>
>>> re.sub(date, '\g<3> \g<1> \g<2>', ARES)
'Mark Watney of Ares 3 landed on Mars on: 2035 Nov 7 at 13:37'


References
----------
.. [#xkcd927] Munroe, R. How Standards Proliferate. Year: 2022. Retrieved: 2022-04-27. URL: https://xkcd.com/927/
