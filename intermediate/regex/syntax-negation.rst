Syntax Negation
===============
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

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'[0-9]', TEXT)
['3', '7', '2', '0', '3', '5', '1', '3', '7']

>>> re.findall(r'[^0-9]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['M', 'a', 'r', 'k', ' ', 'W', 'a', 't', 'n', 'e', 'y', ' ', 'o', 'f',
 ' ', 'A', 'r', 'e', 's', ' ', ' ', 'l', 'a', 'n', 'd', 'e', 'd', ' ',
 'o', 'n', ' ', 'M', 'a', 'r', 's', ' ', 'o', 'n', ':', ' ', 'N', 'o',
 'v', ' ', 't', 'h', ',', ' ', ' ', 'a', 't', ' ', ':', ' ', 'p', 'm']


Compare
-------
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'[A-Z]', TEXT)
['M', 'W', 'A', 'M', 'N']

>>> re.findall(r'^[A-Z]', TEXT)
['M']

>>> re.findall(r'[^A-Z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['a', 'r', 'k', ' ', 'a', 't', 'n', 'e', 'y', ' ', 'o', 'f', ' ', 'r',
 'e', 's', ' ', '3', ' ', 'l', 'a', 'n', 'd', 'e', 'd', ' ', 'o', 'n',
 ' ', 'a', 'r', 's', ' ', 'o', 'n', ':', ' ', 'o', 'v', ' ', '7', 't',
 'h', ',', ' ', '2', '0', '3', '5', ' ', 'a', 't', ' ', '1', ':', '3',
 '7', ' ', 'p', 'm']

>>> re.findall(r'^[^A-Z]', TEXT)
[]


Assignments
-----------
.. literalinclude:: assignments/re_syntax_negation_a.py
    :caption: :download:`Solution <assignments/re_syntax_negation_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_syntax_negation_b.py
    :caption: :download:`Solution <assignments/re_syntax_negation_b.py>`
    :end-before: # Solution
