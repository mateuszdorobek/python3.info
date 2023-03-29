Regex Syntax Negation
=====================
* Negation logically inverts qualifier
* ``[^...]`` - anything but ...


SetUp
-----
>>> import re


Syntax
------
* ``[^...]`` - anything but ...


Example
-------
* ``[^abc]`` - anything but letter `a` or `b` or `c`

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

>>> re.findall(r'[0-9]', TEXT)
['1', '2', '0', '0', '0', '1', '2', '0', '0']

>>> re.findall(r'[^0-9]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['E', 'm', 'a', 'i', 'l', ' ', 'f', 'r', 'o', 'm', ' ', 'M', 'a', 'r', 'k',
 ' ', 'W', 'a', 't', 'n', 'e', 'y', ' ', '<', 'm', 'w', 'a', 't', 'n', 'e',
 'y', '@', 'n', 'a', 's', 'a', '.', 'g', 'o', 'v', '>', ' ', 'r', 'e', 'c',
 'e', 'i', 'v', 'e', 'd', ' ', 'o', 'n', ':', ' ', 'S', 'a', 't', ',', ' ',
 'J', 'a', 'n', ' ', 's', 't', ',', ' ', ' ', 'a', 't', ' ', ':', ' ', 'A',
 'M']


Compare
-------
>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

>>> re.findall(r'[0-9]', TEXT)
['1', '2', '0', '0', '0', '1', '2', '0', '0']

>>> re.findall(r'^[0-9]', TEXT)
[]

>>> re.findall(r'[^0-9]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['E', 'm', 'a', 'i', 'l', ' ', 'f', 'r', 'o', 'm', ' ', 'M', 'a', 'r', 'k',
 ' ', 'W', 'a', 't', 'n', 'e', 'y', ' ', '<', 'm', 'w', 'a', 't', 'n', 'e',
 'y', '@', 'n', 'a', 's', 'a', '.', 'g', 'o', 'v', '>', ' ', 'r', 'e', 'c',
 'e', 'i', 'v', 'e', 'd', ' ', 'o', 'n', ':', ' ', 'S', 'a', 't', ',', ' ',
 'J', 'a', 'n', ' ', 's', 't', ',', ' ', ' ', 'a', 't', ' ', ':', ' ', 'A',
 'M']

>>> re.findall(r'^[^0-9]', TEXT)
['E']


Assignments
-----------
.. literalinclude:: assignments/re_syntax_negation_a.py
    :caption: :download:`Solution <assignments/re_syntax_negation_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_syntax_negation_b.py
    :caption: :download:`Solution <assignments/re_syntax_negation_b.py>`
    :end-before: # Solution
