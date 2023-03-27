Regex Syntax Flag
=================
* ``re.ASCII`` - perform ASCII-only matching instead of full Unicode matching
* ``re.IGNORECASE`` - case-insensitive search
* ``re.LOCALE`` - case-insensitive matching dependent on the current locale (deprecated)
* ``re.MULTILINE`` - match can start in one line, and end in another
* ``re.DOTALL`` - dot (``.``) matches also newline characters
* ``re.UNICODE`` - turns on unicode character support for ``\w``
* ``re.VERBOSE`` - ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``
* ``re.DEBUG`` - display debugging information during pattern compilation

The final piece of regex syntax that Python's regular expression engine offers
is a means of setting the flags. Usually the flags are set by passing them as
additional parameters when calling the ``re.compile()`` function, but sometimes
it's more convenient to set them as part of the regex itself. The syntax is
simply ``(?flags)`` where flags is one or more of the following:

* ``re.ASCII``
* ``re.IGNORECASE``
* ``re.LOCALE``
* ``re.MULTILINE``
* ``re.DOTALL``
* ``re.UNICODE``
* ``re.VERBOSE``
* ``re.DEBUG``

If the flags are set this way, they should be put at the start of the regex;
they match nothing, so their effect on the regex is only to set the flags.
The letters used for the flags are the same as the ones used by Perl's regex
engine, which is why s is used for re.DOTALL and x is used for re.VERBOSE
[#Summerfield2008]_.


SetUp
-----
>>> import re


ASCII
-----
* Short: ``a``
* Long: ``re.ASCII``
* Perform ASCII-only matching instead of full Unicode matching
* Works for ``\w``, ``\W``, ``\b``, ``\B``, ``\d``, ``\D``, ``\s`` and ``\S``
* ASCII only search is faster, but does not include unicode characters

>>> TEXT = 'cześć'  # 'hello' in Polish
>>> re.findall(r'\w', TEXT)
['c', 'z', 'e', 'ś', 'ć']
>>>
>>> re.findall(r'\w', TEXT, flags=re.ASCII)
['c', 'z', 'e']

Mind that range character class ``[a-z]`` is always ASCII:

>>> TEXT = 'cześć'  # 'hello' in Polish
>>>
>>> re.findall(r'[a-z]', TEXT)
['c', 'z', 'e']
>>>
>>> re.findall(r'[a-z]', TEXT, flags=re.ASCII)
['c', 'z', 'e']


IGNORECASE
----------
* Short: ``i``
* Long: ``re.IGNORECASE``
* Case-insensitive search
* Has Unicode support i.e. ``Ą`` and ``ą``


>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>>
>>> re.findall(r'mars', TEXT)
[]
>>>
>>> re.findall(r'mars', TEXT, flags=re.IGNORECASE)
['Mars']


LOCALE
------
* Short: ``L``
* Long: ``re.LOCALE``
* Case-insensitive matching dependent on the current locale
* Work for ``\w``, ``\W``, ``\b``, ``\B``
* Use of this flag is discouraged as the locale mechanism is very unreliable
* It only works with 8-bit locales

>>> import locale
>>>
>>> locale.getlocale()
('en_US', 'UTF-8')


MULTILINE
----------
* Short: ``m``
* Long: ``re.MULTILINE``
* Match can start in one line, and end in another
* Changes meaning of ``^``, now it is a start of a line
* Changes meaning of ``$``, now it is an end of line

>>> TEXT = 'hello\nworld'
>>>
>>> re.findall('^[a-z]', TEXT)
['h']
>>>
>>> re.findall('^[a-z]', TEXT, flags=re.MULTILINE)
['h', 'w']

>>> TEXT = """We choose to go to the moon.
... We choose to go to the moon in this decade and do the other things,
... not because they are easy,
... but because they are hard,
... because that goal will serve to organize and measure the best of our energies and skills,
... because that challenge is one that we are willing to accept,
... one we are unwilling to postpone,
... and one which we intend to win,
... and the others, too."""
>>>
>>>
>>> sentence = r'[A-Z][a-z, ]+\.'
>>> re.findall(sentence, TEXT)
['We choose to go to the moon.']
>>>
>>> sentence = r'[A-Z][a-z, \n]+\.'
>>> re.findall(sentence, TEXT)  # doctest: +NORMALIZE_WHITESPACE
['We choose to go to the moon.',
 'We choose to go to the moon in this decade and do the other things,\nnot because they are easy,\nbut because they are hard,\nbecause that goal will serve to organize and measure the best of our energies and skills,\nbecause that challenge is one that we are willing to accept,\none we are unwilling to postpone,\nand one which we intend to win,\nand the others, too.']


DOTALL
------
* Short: ``s``
* Long: ``re.DOTALL``
* Dot (``.``) matches also newline characters
* By default newlines are not matched by ``.``

>>> TEXT = 'hello\nworld'
>>>
>>> re.findall(r'.', TEXT)
['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
>>>
>>> re.findall(r'.', TEXT, flags=re.DOTALL)
['h', 'e', 'l', 'l', 'o', '\n', 'w', 'o', 'r', 'l', 'd']

Mind the ``\n`` character among results with ``re.DOTALL`` flag turned on.


UNICODE
-------
* Short: ``u``
* Long: ``re.UNICODE``
* On by default
* Turns on unicode character support
* Works for ``\w`` and ``\W``

>>> TEXT = 'cześć'  # in Polish language means hello
>>>
>>> re.findall(r'\w', TEXT)
['c', 'z', 'e', 'ś', 'ć']
>>>
>>> re.findall(r'\w', TEXT, flags=re.UNICODE)
['c', 'z', 'e', 'ś', 'ć']

Mind that range character class ``[a-z]`` is always ASCII:

>>> re.findall(r'[a-z]', TEXT)
['c', 'z', 'e']
>>>
>>> re.findall(r'[a-z]', TEXT, flags=re.UNICODE)
['c', 'z', 'e']


VERBOSE
-------
* Short: ``x``
* Long: ``re.VERBOSE``
* Ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``

>>> x = re.compile(r"\d+\.\d*")

>>> x = re.compile(r"\d(?#integral part)+\.(?#separator)\d*(?#fractional part)")

>>> x = re.compile(r"""
...     \d +  # integral part
...     \.    # separator
...     \d *  # fractional part
... """, flags=re.VERBOSE)


DEBUG
-----
* Long: ``re.DEBUG``
* Display debugging information during pattern compilation

>>> x = re.compile('^[a-z]+@nasa.gov$', flags=re.DEBUG)  # doctest: +NORMALIZE_WHITESPACE
AT AT_BEGINNING
MAX_REPEAT 1 MAXREPEAT
  IN
    RANGE (97, 122)
LITERAL 64
LITERAL 110
LITERAL 97
LITERAL 115
LITERAL 97
ANY None
LITERAL 103
LITERAL 111
LITERAL 118
AT AT_END
<BLANKLINE>
 0. INFO 4 0b0 10 MAXREPEAT (to 5)
 5: AT BEGINNING
 7. REPEAT_ONE 10 1 MAXREPEAT (to 18)
11.   IN 5 (to 17)
13.     RANGE 0x61 0x7a ('a'-'z')
16.     FAILURE
17:   SUCCESS
18: LITERAL 0x40 ('@')
20. LITERAL 0x6e ('n')
22. LITERAL 0x61 ('a')
24. LITERAL 0x73 ('s')
26. LITERAL 0x61 ('a')
28. ANY
29. LITERAL 0x67 ('g')
31. LITERAL 0x6f ('o')
33. LITERAL 0x76 ('v')
35. AT END
37. SUCCESS


References
----------
.. [#Summerfield2008] Summerfield, Mark. Programming in Python 3. Regular Expressions. Chapter: 12. Pages: 445-465. Year: 2008. Retrieved: 2021-04-11. Publisher: Addison-Wesley Professional. ISBN: 978-0-13-712929-4. URL: https://www.informit.com/articles/article.aspx?p=1278986
