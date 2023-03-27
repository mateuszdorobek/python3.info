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

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> re.findall(r'No.', TEXT)
['Nov']

Search for uppercase letter followed by any three characters:

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> re.findall(r'[A-Z]...', TEXT)
['Mark', 'Watn', 'Ares', 'Mars', 'Nov ']

Example:

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> re.findall(r'Nov 7..', TEXT)
['Nov 7th']


Start of Line
-------------
* ``^`` - start of a line
* Changes meaning with ``re.MULTILINE``

Search for a capital letter at the start of a line:

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> re.findall(r'^[A-Z]', TEXT)
['M']

Search for a capital letter anywhere in text:

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> re.findall(r'[A-Z]', TEXT)
['M', 'W', 'A', 'M', 'N']


End of Line
-----------
* ``$`` - end of line
* Changes meaning with ``re.MULTILINE``

Give me last characters in a line:

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> re.findall(r'.$', TEXT)
['7']


Start of String
---------------
* ``\A`` - start of a text
* Doesn't change meaning with ``re.MULTILINE``

Search for a capital letter in text at the start of a line:

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> re.findall(r'\A[A-Z]', TEXT)
['M']

Note, that the output is identical to Start of a Line ``^``. It will differ
when ``re.MULTILINE`` flag is present.

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> re.findall(r'^[A-Z]', TEXT)
['M']


End of String
-------------
* ``\Z`` - end of a text
* Doesn't change meaning with ``re.MULTILINE``

Give me last character in a text:

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> re.findall(r'.\Z', TEXT)
['7']

Note, that the output is identical to Start of a Line ``^``. It will differ
when ``re.MULTILINE`` flag is present.

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> re.findall(r'.$', TEXT)
['7']


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
