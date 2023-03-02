Syntax Qualifier
================
* Qualifier specifies what to find.
* ``a`` - Exact
* ``a|b`` - Alternative
* ``[abc]`` - Enumeration
* ``[a-z]`` - Range


SetUp
-----
>>> import re


Exact
-----
* ``a`` - Exact

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

Regular expressions allows to find exact matches:

>>> re.findall(r'a', TEXT)
['a', 'a', 'a', 'a', 'a']

Note, that regular expressions are case sensitive (unless ``re.IGNORECASE``
flag is present. More information in `Syntax Flags`):

>>> re.findall(r'A', TEXT)
['A']

Note, that regular expressions are used to search in text, therefore in case
of searching for a number it will return a strings with numbers in it:

>>> re.findall(r'1', TEXT)
['1']

Python ``re.findall()`` function will return empty list if none match was
found:

>>> re.findall(r'x', TEXT)
[]


Exact Alternate
---------------
* ``a|b`` - letter `a` or `b` (also works with expressions)

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

Alternative allows to search for two or more possible matches:

>>> re.findall(r'a|b', TEXT)
['a', 'a', 'a', 'a', 'a']

It can find more than two matches:

>>> re.findall(r'a|b|c|d', TEXT)
['a', 'a', 'a', 'd', 'd', 'a', 'a']
>>>
>>> re.findall(r'1|2|3', TEXT)
['3', '2', '3', '1', '3', '3']

It will work for both numbers, characters or any other object:

>>> re.findall(r'a|b|c|d|1|2|3', TEXT)
['a', 'a', '3', 'a', 'd', 'd', 'a', '2', '3', 'a', '1', '3', '3']

Examples:

>>> re.findall(r'a|e', TEXT)
['a', 'a', 'e', 'e', 'a', 'e', 'a', 'a']
>>>
>>> re.findall(r'a|e|i|o|u|y', TEXT)
['a', 'a', 'e', 'y', 'o', 'e', 'a', 'e', 'o', 'a', 'o', 'o', 'a']


Enumeration
-----------
* ``[abc]`` - letter `a` or `b` or `c`

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

Enumerations provide compact and more readable syntax for longer alternatives:

>>> re.findall(r'[abcd]', TEXT)
['a', 'a', 'a', 'd', 'd', 'a', 'a']
>>>
>>> re.findall(r'[123]', TEXT)
['3', '2', '3', '1', '3', '3']

It will work for both numbers, characters or any other object:

>>> re.findall(r'[abcd123]', TEXT)
['a', 'a', '3', 'a', 'd', 'd', 'a', '2', '3', 'a', '1', '3', '3']

Examples:

>>> re.findall(r'[a-z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['a', 'r', 'k', 'a', 't', 'n', 'e', 'y', 'o', 'f', 'r', 'e', 's', 'l',
 'a', 'n', 'd', 'e', 'd', 'o', 'n', 'a', 'r', 's', 'o', 'n', 'o', 'v',
 't', 'h', 'a', 't']
>>>
>>> re.findall(r'[az-]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['a', 'a', 'a', 'a', 'a']

>>> re.findall(r'[A-z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['M', 'a', 'r', 'k', 'W', 'a', 't', 'n', 'e', 'y', 'o', 'f', 'A', 'r',
 'e', 's', 'l', 'a', 'n', 'd', 'e', 'd', 'o', 'n', 'M', 'a', 'r', 's',
 'o', 'n', 'N', 'o', 'v', 't', 'h', 'a', 't']
>>>
>>> re.findall(r'[a-Z]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-Z at position 1
>>>
>>> re.findall(r'[z-a]', TEXT)
Traceback (most recent call last):
re.error: bad character range z-a at position 1

Use Cases:

>>> re.findall(r'[aeiouy]', TEXT)
['a', 'a', 'e', 'y', 'o', 'e', 'a', 'e', 'o', 'a', 'o', 'o', 'a']
>>>
>>> re.findall(r'a|e|i|o|u|y', TEXT)
['a', 'a', 'e', 'y', 'o', 'e', 'a', 'e', 'o', 'a', 'o', 'o', 'a']


Range
-----
* ``[a-z]`` - any lowercase ASCII letter from `a` to `z`
* ``[A-Z]`` - any uppercase ASCII letter from `A` to `Z`
* ``[0-9]`` - any digit from `0` to `9`
* ``[a-zA-Z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[A-z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[a-zA-Z0-9]`` - any ASCII letter from `a` to `z` or from `A` to `Z` or digit from `0` to `9`

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

Ranges provide even more readable and convenient way os specifying particular
characters to match. It is very useful to define ranges of numbers or letters
this way:

>>> re.findall(r'[a-z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['a', 'r', 'k', 'a', 't', 'n', 'e', 'y', 'o', 'f', 'r', 'e', 's', 'l',
 'a', 'n', 'd', 'e', 'd', 'o', 'n', 'a', 'r', 's', 'o', 'n', 'o', 'v',
 't', 'h', 'a', 't']
>>>
>>> re.findall(r'[A-Z]', TEXT)
['M', 'W', 'A', 'M', 'N']
>>>
>>> re.findall(r'[0-9]', TEXT)
['3', '7', '2', '0', '3', '5', '1', '3', '3', '7']

Note, that regular expressions are case sensitive (unless ``re.IGNORECASE``
flag is present. More information in `Syntax Flags`). You can also join
ranges to create even broader matches:

>>> re.findall(r'[a-zA-Z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['M', 'a', 'r', 'k', 'W', 'a', 't', 'n', 'e', 'y', 'o', 'f', 'A', 'r',
 'e', 's', 'l', 'a', 'n', 'd', 'e', 'd', 'o', 'n', 'M', 'a', 'r', 's',
 'o', 'n', 'N', 'o', 'v', 't', 'h', 'a', 't']
>>>
>>> re.findall(r'[a-zA-Z0-9]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['M', 'a', 'r', 'k', 'W', 'a', 't', 'n', 'e', 'y', 'o', 'f', 'A', 'r',
 'e', 's', '3', 'l', 'a', 'n', 'd', 'e', 'd', 'o', 'n', 'M', 'a', 'r',
 's', 'o', 'n', 'N', 'o', 'v', '7', 't', 'h', '2', '0', '3', '5', 'a',
 't', '1', '3', '3', '7']

Ranges are ordered in ASCII table order (more information in `Locale
Encoding`). Because uppercase letters are before lowercase letters (has
lower indexes), you can define range from ``Z-a``, but the opposite is not
true:

>>> re.findall(r'[Z-a]', TEXT)
['a', 'a', 'a', 'a', 'a']

>>> re.findall(r'[a-Z]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-Z at position 1

The last example can work in some other languages due to the different
implementation of the algorithm or PCRE standard. More information in `Syntax
Extensions`.

Mind that ranges not necessarily need to be from a-z. It could be any
alphabetic or numeric range:

>>> re.findall(r'[3-7]', TEXT)
['3', '7', '3', '5', '3', '3', '7']
>>>
>>> re.findall(r'[C-Y]', TEXT)
['M', 'W', 'M', 'N']
>>>
>>> re.findall(r'[3-7C-Y]', TEXT)
['M', 'W', '3', 'M', 'N', '7', '3', '5', '3', '3', '7']


Joining
-------
* ``[abc]|[123]`` - Enumeration alternative - letter `a`, `b` or `c` or digit `1`, `2` `3`
* ``[a-z]|[0-9]`` - Range alternative - any lowercase ASCII letter from `a` to `z` or digit from `0` to `9`

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

Alternative enumerations syntax is as follows:

>>> re.findall(r'[abc]|[123]', TEXT)
['a', 'a', '3', 'a', 'a', '2', '3', 'a', '1', '3', '3']

The effect is identical to:

>>> re.findall(r'[abc123]', TEXT)
['a', 'a', '3', 'a', 'a', '2', '3', 'a', '1', '3', '3']

You can define alternative ranges to find:

>>> re.findall(r'[A-Z]|[0-9]', TEXT)
['M', 'W', 'A', '3', 'M', 'N', '7', '2', '0', '3', '5', '1', '3', '3', '7']

The effect is identical to:

>>> re.findall(r'[A-Z0-9]', TEXT)
['M', 'W', 'A', '3', 'M', 'N', '7', '2', '0', '3', '5', '1', '3', '3', '7']


Examples
--------
* ``[d-m]`` - any lowercase letter from `d`  to `m`
* ``[3-7]`` - any digit from `3` to `7`
* ``[xz2]`` - `x` or `z` or `2`
* ``[d-mK-P3-8]`` - any lowercase letter from `d` to `m` or uppercase letter from `K` to `P` or digit from `3` to `8`
* ``x|z|2`` - `x` or `z` or `2`
* ``d|x`` - `d` or `x`
* ``[d-k]|[ABC]|[3-8]`` - any lowercase letter from `d` to `k` or uppercase `A`,`B` or `C` or digit from `3` to `8`


Use Case - 0x01
---------------
>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

Note, the `nd` in word `landed`:

>>> re.findall(r'st|nd|rd|th', TEXT)
['nd', 'th']

>>> re.findall(r'[st|nd|rd|th]', TEXT)
['r', 't', 'n', 'r', 's', 'n', 'd', 'd', 'n', 'r', 's', 'n', 't', 'h', 't']

>>> re.findall(r'[stndrdth]', TEXT)
['r', 't', 'n', 'r', 's', 'n', 'd', 'd', 'n', 'r', 's', 'n', 't', 'h', 't']


Use Case - 0x02
---------------
>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>>
>>>
>>> re.findall('A|B|C|M', TEXT)
['M', 'A', 'M']
>>>
>>> re.findall('^A|B|C|M', TEXT)
['M', 'M']
>>>
>>> re.findall('^A|^B|^C|^M', TEXT)
['M']
>>>
>>> re.findall('^(A|B|C|M)', TEXT)
['M']


Assignments
-----------
.. literalinclude:: assignments/re_syntax_qualifier_a.py
    :caption: :download:`Solution <assignments/re_syntax_qualifier_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_syntax_qualifier_b.py
    :caption: :download:`Solution <assignments/re_syntax_qualifier_b.py>`
    :end-before: # Solution
