Regex Syntax Anchor
===================
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)
* ``^`` - start of line (changes meaning with ``re.MULTILINE``)
* ``$`` - end of line (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of text (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of text (doesn't change meaning with ``re.MULTILINE``)


SetUp
-----
>>> import re


Any Character
-------------
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)

Search for letters ``No`` followed by any character:

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>> re.findall(r'.st', TEXT)
['1st']

Search for uppercase letter followed by any three characters:

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>> re.findall(r'[A-Z]..', TEXT)
['Ema', 'Mar', 'Wat', 'Sat', 'Jan']

Example:

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>> re.findall(r'Jan 1..', TEXT)
['Jan 1st']


Start of Line
-------------
* ``^`` - start of a line
* Changes meaning with ``re.MULTILINE``

Search for a capital letter at the start of a line:

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>> re.findall(r'^[A-Z]', TEXT)
['E']

Search for a capital letter anywhere in text:

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>> re.findall(r'[A-Z]', TEXT)
['E', 'M', 'W', 'S', 'J', 'A', 'M']


End of Line
-----------
* ``$`` - end of line
* Changes meaning with ``re.MULTILINE``

Give me last characters in a line:

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>> re.findall(r'.$', TEXT)
['M']


Start of String
---------------
* ``\A`` - start of a text
* Doesn't change meaning with ``re.MULTILINE``

Search for a capital letter in text at the start of a line:

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>> re.findall(r'\A[A-Z]', TEXT)
['E']

Note, that the output is identical to Start of a Line ``^``. It will differ
when ``re.MULTILINE`` flag is present.

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>> re.findall(r'^[A-Z]', TEXT)
['E']


End of String
-------------
* ``\Z`` - end of a text
* Doesn't change meaning with ``re.MULTILINE``

Give me last character in a text:

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>> re.findall(r'.\Z', TEXT)
['M']

Note, that the output is identical to Start of a Line ``^``. It will differ
when ``re.MULTILINE`` flag is present.

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>> re.findall(r'.$', TEXT)
['M']


Use Case - 0x01
---------------
* ``abc.e`` - text `abc` then any character followed by letter `e`


Assignments
-----------
.. literalinclude:: assignments/re_syntax_anchor_a.py
    :caption: :download:`Solution <assignments/re_syntax_anchor_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_syntax_anchor_b.py
    :caption: :download:`Solution <assignments/re_syntax_anchor_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_syntax_anchor_c.py
    :caption: :download:`Solution <assignments/re_syntax_anchor_c.py>`
    :end-before: # Solution
