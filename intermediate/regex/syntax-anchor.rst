Syntax Anchor
=============
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)
* ``^`` - start of line (changes meaning with ``re.MULTILINE``)
* ``$`` - end of line (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of text (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of text (doesn't change meaning with ``re.MULTILINE``)


Any Character
-------------
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

Search for letters ``No`` followed by any character:

>>> re.findall(r'No.', TEXT)
['Nov']

Search for uppercase letter followed by any three characters:

>>> re.findall(r'[A-Z]...', TEXT)
['Mark', 'Watn', 'Ares', 'Mars', 'Nov ']

Example:

>>> re.findall(r'1:37 ..', TEXT)
['1:37 pm']
>>>
>>> re.findall(r'Nov 7..', TEXT)
['Nov 7th']


Start of Line
-------------
* ``^`` - start of a line
* Changes meaning with ``re.MULTILINE``

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

Search for a capital letter in text at the start of a line:

>>> re.findall(r'^[A-Z]', TEXT)
['M']

Search for a capital letter anywhere in text:

>>> re.findall(r'[A-Z]', TEXT)
['M', 'W', 'A', 'M', 'N']


End of Line
-----------
* ``$`` - end of line
* Changes meaning with ``re.MULTILINE``

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

Give me last two characters in a text:

>>> re.findall(r'..$', TEXT)
['pm']


Start of String
---------------
* ``\A`` - start of a text
* Doesn't change meaning with ``re.MULTILINE``

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

Search for a capital letter in text at the start of a line:

>>> re.findall(r'\A[A-Z]', TEXT)
['M']

Note, that the output is identical to Start of a Line ``^``. It will differ
when ``re.MULTILINE`` flag is present.

>>> re.findall(r'^[A-Z]', TEXT)
['M']


End of String
-------------
* ``\Z`` - end of a text
* Doesn't change meaning with ``re.MULTILINE``

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

Give me last two characters in a text:

>>> re.findall(r'..\Z', TEXT)
['pm']

Note, that the output is identical to Start of a Line ``^``. It will differ
when ``re.MULTILINE`` flag is present.

>>> re.findall(r'..$', TEXT)
['pm']


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
