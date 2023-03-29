Regex Syntax Qualifier
======================
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

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

Regular expressions allows to find exact matches:

>>> re.findall(r'a', TEXT)
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

Note, that regular expressions are case sensitive (unless ``re.IGNORECASE``
flag is present. More information in `Syntax Flags`):

>>> re.findall(r'A', TEXT)
['A']

Note, that regular expressions are used to search in text, therefore in case
of searching for a number it will return a strings with numbers in it:

>>> re.findall(r'1', TEXT)
['1', '1']

Python ``re.findall()`` function will return empty list if none match was
found:

>>> re.findall(r'x', TEXT)
[]


Exact Alternate
---------------
* ``a|b`` - letter `a` or `b` (also works with expressions)

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

Alternative allows to search for two or more possible matches:

>>> re.findall(r'a|b', TEXT)
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

It can find more than two matches:

>>> re.findall(r'a|b|c|d', TEXT)
['a', 'a', 'a', 'a', 'a', 'a', 'c', 'd', 'a', 'a', 'a']
>>>
>>> re.findall(r'1|2|3', TEXT)
['1', '2', '1', '2']

It will work for both numbers, characters or any other object:

>>> re.findall(r'a|b|c|d|1|2|3', TEXT)
['a', 'a', 'a', 'a', 'a', 'a', 'c', 'd', 'a', 'a', '1', '2', 'a', '1', '2']

Examples:

>>> re.findall(r'a|e', TEXT)
['a', 'a', 'a', 'e', 'a', 'e', 'a', 'a', 'e', 'e', 'e', 'a', 'a', 'a']
>>>
>>> re.findall(r'a|e|i|o|u|y', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['a', 'i', 'o', 'a', 'a', 'e', 'y', 'a', 'e', 'y', 'a', 'a', 'o', 'e',
 'e', 'i', 'e', 'o', 'a', 'a', 'a']



Enumeration
-----------
* ``[abc]`` - letter `a` or `b` or `c`

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

Enumerations provide compact and more readable syntax for longer alternatives:

>>> re.findall(r'[abcd]', TEXT)
['a', 'a', 'a', 'a', 'a', 'a', 'c', 'd', 'a', 'a', 'a']
>>>
>>> re.findall(r'[123]', TEXT)
['1', '2', '1', '2']

It will work for both numbers, characters or any other object:

>>> re.findall(r'[abcd123]', TEXT)
['a', 'a', 'a', 'a', 'a', 'a', 'c', 'd', 'a', 'a', '1', '2', 'a', '1', '2']

Examples:

>>> re.findall(r'[a-z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['m', 'a', 'i', 'l', 'f', 'r', 'o', 'm', 'a', 'r', 'k', 'a', 't', 'n', 'e',
 'y', 'm', 'w', 'a', 't', 'n', 'e', 'y', 'n', 'a', 's', 'a', 'g', 'o', 'v',
 'r', 'e', 'c', 'e', 'i', 'v', 'e', 'd', 'o', 'n', 'a', 't', 'a', 'n', 's',
 't', 'a', 't']
>>>
>>> re.findall(r'[az-]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

>>> re.findall(r'[A-z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['E', 'm', 'a', 'i', 'l', 'f', 'r', 'o', 'm', 'M', 'a', 'r', 'k', 'W', 'a',
 't', 'n', 'e', 'y', 'm', 'w', 'a', 't', 'n', 'e', 'y', 'n', 'a', 's', 'a',
 'g', 'o', 'v', 'r', 'e', 'c', 'e', 'i', 'v', 'e', 'd', 'o', 'n', 'S', 'a',
 't', 'J', 'a', 'n', 's', 't', 'a', 't', 'A', 'M']
>>>
>>> re.findall(r'[a-Z]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-Z at position 1
>>>
>>> re.findall(r'[z-a]', TEXT)
Traceback (most recent call last):
re.error: bad character range z-a at position 1

Use Cases:

>>> re.findall(r'[aeiouy]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['a', 'i', 'o', 'a', 'a', 'e', 'y', 'a', 'e', 'y', 'a', 'a', 'o', 'e',
 'e', 'i', 'e', 'o', 'a', 'a', 'a']
>>>
>>> re.findall(r'a|e|i|o|u|y', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['a', 'i', 'o', 'a', 'a', 'e', 'y', 'a', 'e', 'y', 'a', 'a', 'o', 'e',
 'e', 'i', 'e', 'o', 'a', 'a', 'a']


Range
-----
* ``[a-z]`` - any lowercase ASCII letter from `a` to `z`
* ``[A-Z]`` - any uppercase ASCII letter from `A` to `Z`
* ``[0-9]`` - any digit from `0` to `9`
* ``[a-zA-Z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[A-z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[a-zA-Z0-9]`` - any ASCII letter from `a` to `z` or from `A` to `Z` or digit from `0` to `9`

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

Ranges provide even more readable and convenient way os specifying particular
characters to match. It is very useful to define ranges of numbers or letters
this way:

>>> re.findall(r'[a-z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['m', 'a', 'i', 'l', 'f', 'r', 'o', 'm', 'a', 'r', 'k', 'a', 't', 'n', 'e',
 'y', 'm', 'w', 'a', 't', 'n', 'e', 'y', 'n', 'a', 's', 'a', 'g', 'o', 'v',
 'r', 'e', 'c', 'e', 'i', 'v', 'e', 'd', 'o', 'n', 'a', 't', 'a', 'n', 's',
 't', 'a', 't']
>>>
>>> re.findall(r'[A-Z]', TEXT)
['E', 'M', 'W', 'S', 'J', 'A', 'M']
>>>
>>> re.findall(r'[0-9]', TEXT)
['1', '2', '0', '0', '0', '1', '2', '0', '0']

Note, that regular expressions are case sensitive (unless ``re.IGNORECASE``
flag is present. More information in `Syntax Flags`). You can also join
ranges to create even broader matches:

>>> re.findall(r'[a-zA-Z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['E', 'm', 'a', 'i', 'l', 'f', 'r', 'o', 'm', 'M', 'a', 'r', 'k', 'W', 'a',
 't', 'n', 'e', 'y', 'm', 'w', 'a', 't', 'n', 'e', 'y', 'n', 'a', 's', 'a',
 'g', 'o', 'v', 'r', 'e', 'c', 'e', 'i', 'v', 'e', 'd', 'o', 'n', 'S', 'a',
 't', 'J', 'a', 'n', 's', 't', 'a', 't', 'A', 'M']
>>>
>>> re.findall(r'[a-zA-Z0-9]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['E', 'm', 'a', 'i', 'l', 'f', 'r', 'o', 'm', 'M', 'a', 'r', 'k', 'W', 'a',
 't', 'n', 'e', 'y', 'm', 'w', 'a', 't', 'n', 'e', 'y', 'n', 'a', 's', 'a',
 'g', 'o', 'v', 'r', 'e', 'c', 'e', 'i', 'v', 'e', 'd', 'o', 'n', 'S', 'a',
 't', 'J', 'a', 'n', '1', 's', 't', '2', '0', '0', '0', 'a', 't', '1', '2',
 '0', '0', 'A', 'M']

Ranges are ordered in ASCII table order (more information in `Locale
Encoding`). Because uppercase letters are before lowercase letters (has
lower indexes), you can define range from ``Z-a``, but the opposite is not
true:

>>> re.findall(r'[Z-a]', TEXT)
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

>>> re.findall(r'[a-Z]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-Z at position 1

The last example can work in some other languages due to the different
implementation of the algorithm or PCRE standard. More information in `Syntax
Extensions`.

Mind that ranges not necessarily need to be from a-z. It could be any
alphabetic or numeric range:

>>> re.findall(r'[2-7]', TEXT)
['2', '2']
>>>
>>> re.findall(r'[C-Y]', TEXT)
['E', 'M', 'W', 'S', 'J', 'M']
>>>
>>> re.findall(r'[3-7C-Y]', TEXT)
['E', 'M', 'W', 'S', 'J', 'M']


Joining
-------
* ``[abc]|[123]`` - Enumeration alternative - letter `a`, `b` or `c` or digit `1`, `2` `3`
* ``[a-z]|[0-9]`` - Range alternative - any lowercase ASCII letter from `a` to `z` or digit from `0` to `9`

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

Alternative enumerations syntax is as follows:

>>> re.findall(r'[abc]|[123]', TEXT)
['a', 'a', 'a', 'a', 'a', 'a', 'c', 'a', 'a', '1', '2', 'a', '1', '2']

The effect is identical to:

>>> re.findall(r'[abc123]', TEXT)
['a', 'a', 'a', 'a', 'a', 'a', 'c', 'a', 'a', '1', '2', 'a', '1', '2']

You can define alternative ranges to find:

>>> re.findall(r'[A-Z]|[0-9]', TEXT)
['E', 'M', 'W', 'S', 'J', '1', '2', '0', '0', '0', '1', '2', '0', '0', 'A', 'M']

The effect is identical to:

>>> re.findall(r'[A-Z0-9]', TEXT)
['E', 'M', 'W', 'S', 'J', '1', '2', '0', '0', '0', '1', '2', '0', '0', 'A', 'M']


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
>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

Note, the `nd` in word `landed`:

>>> re.findall(r'st|nd|rd|th', TEXT)
['st']

>>> re.findall(r'[st|nd|rd|th]', TEXT)
['r', 'r', 't', 'n', 't', 'n', 'n', 's', 'r', 'd', 'n', 't', 'n', 's', 't', 't']

>>> re.findall(r'[stndrdth]', TEXT)
['r', 'r', 't', 'n', 't', 'n', 'n', 's', 'r', 'd', 'n', 't', 'n', 's', 't', 't']


Use Case - 0x02
---------------
>>> import re
>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'
>>>
>>>
>>> re.findall('A|B|C|M', TEXT)
['M', 'A', 'M']
>>>
>>> re.findall('^A|B|C|M', TEXT)
['M', 'M']
>>>
>>> re.findall('^A|^B|^C|^M', TEXT)
[]
>>>
>>> re.findall('^(A|B|C|M)', TEXT)
[]


Assignments
-----------
.. literalinclude:: assignments/re_syntax_qualifier_a.py
    :caption: :download:`Solution <assignments/re_syntax_qualifier_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_syntax_qualifier_b.py
    :caption: :download:`Solution <assignments/re_syntax_qualifier_b.py>`
    :end-before: # Solution
