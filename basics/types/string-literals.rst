String Literals
===============

>>> text = 'hello'      # unicode
>>>
>>> text = u'hello'     # unicode
>>> text = b'hello'     # bytes
>>> text = f'hello'     # f-string
>>> text = r'hello'     # raw-string
>>>
>>> text = U'hello'     # unicode
>>> text = B'hello'     # bytes
>>> text = F'hello'     # f-string
>>> text = R'hello'     # raw-string


Escape Characters
-----------------
* ``\n`` - New line (ENTER)
* ``\t`` - Horizontal Tab (TAB)
* ``\'`` - Single quote ``'`` (escape in single quoted strings)
* ``\"`` - Double quote ``"`` (escape in double quoted strings)
* ``\\`` - Backslash ``\`` (to indicate, that this is not escape char)
* More information in `Builtin Printing`
* https://en.wikipedia.org/wiki/List_of_Unicode_characters


>>> print('Hello\World')
Hello\World

>>> print('Hello\nWorld')
Hello
World

>>> print('Hello\tWorld')  # doctest: +NORMALIZE_WHITESPACE
Hello	World


Unicode
-------
>>> print('\U0001F680')
🚀

>>> a = '\U0001F9D1'  # 🧑
>>> b = '\U0000200D'  # ''
>>> c = '\U0001F680'  # 🚀
>>>
>>> astronaut = a + b + c
>>> print(astronaut)
🧑‍🚀


Format String
-------------
* String interpolation (variable substitution)
* Since Python 3.6
* Used for ``str`` concatenation

>>> name = 'Mark'
>>>
>>> print('Hello {name}')
Hello {name}

>>> name = 'Mark'
>>> print(f'Hello {name}')
Hello Mark


Unicode Literal
---------------
* In Python 3 ``str`` is Unicode
* In Python 2 ``str`` is Bytes
* In Python 3 ``u'...'`` is only for compatibility with Python 2

>>> u'zażółć gęślą jaźń'
'zażółć gęślą jaźń'


Bytes Literal
-------------
* Used while reading from low level devices and drivers
* Used in sockets and HTTP connections
* ``bytes`` is a sequence of octets (integers between 0 and 255)
* ``bytes.decode()`` conversion to unicode ``str``
* ``str.encode()`` conversion to ``bytes``

>>> data = 'Moon'   # Unicode Literal
>>> data = u'Moon'  # Unicode Literal
>>> data = b'Moon'  # Bytes Literal

Encode string from unicode (UTF-8) string to bytes:

>>> data = 'cześć'
>>>
>>> data.encode()
b'cze\xc5\x9b\xc4\x87'

Decode string from bytes to unicode (UTF-8):

>>> data = b'cze\xc5\x9b\xc4\x87'
>>>
>>> data.decode()
'cześć'

Unicode (UTF-8) is a default encoding. You can also specify different
encodings to encode and decode data:

>>> data = 'cześć'
>>>
>>>
>>> data.encode('utf-8')
b'cze\xc5\x9b\xc4\x87'
>>>
>>> data.encode('iso-8859-2')
b'cze\xb6\xe6'
>>>
>>> data.encode('windows-1250')
b'cze\x9c\xe6'
>>>
>>> data.encode('cp1250')
b'cze\x9c\xe6'


Raw String
----------
* Escapes does not matters

>>> print('Print "\n" to get new line')
Print "
" to get new line

>>> print('Print "\\n" to get new line')
Print "\n" to get new line


Use Case - 0x01
---------------
Raw-string in Regular Expressions:

>>> '\\b[a-z]+\\b'
'\\b[a-z]+\\b'

>>> r'\b[a-z]+\b'
'\\b[a-z]+\\b'


Use Case - 0x02
---------------
Raw-string in escaping tab character:

>>> print('C:\watney\temporary.txt')  # doctest: +NORMALIZE_WHITESPACE
C:\watney	emporary.txt
>>>
>>> print(r'C:\watney\temporary.txt')
C:\watney\temporary.txt

Raw-string in escaping newline character:

>>> print('C:\nasa\myfile.txt')
C:
asa\myfile.txt
>>>
>>> print(r'C:\nasa\myfile.txt')
C:\nasa\myfile.txt

Raw-string in escaping newline and tab character:

>>> print('C:\nasa\temporary.txt')  # doctest: +NORMALIZE_WHITESPACE
C:
asa	emporary.txt
>>>
>>> print(r'C:\nasa\temporary.txt')
C:\nasa\temporary.txt


Use Case - 0x03
---------------
There are no problems with escapes in POSIX compliant paths:

>>> path = '/home/mwatney/myfile.txt'  # Linux
>>> path = '/User/mwatney/myfile.txt'  # macOS

In Windows you can find escape character in paths. In order to avoid problems
you can use slashes instead of backslashes:

>>> path = 'c:/Users/mwatney/myfile.txt'

This is not typical for this operating system, therefore hardly anyone does
that. Typically users will put paths using slashes, and that's ok, if you
are using escaped slashes or raw-strings:

>>> path = 'c:\\Users\\mwatney\\myfile.txt'
>>> path = r'c:\Users\mwatney\myfile.txt'

As soon as you forget about using either of them, the problem occurs:

>>> path = 'c:\Users\mwatney\myfile.txt'
Traceback (most recent call last):
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

Problem is with ``\Users``. After escape sequence ``\U...`` Python expects
hexadecimal Unicode codepoint, i.e. '\\U0001F680' which is a rocket 🚀
emoticon. In this example, Python finds letter ``s``, which is invalid
hexadecimal character and therefore raises an ``SyntaxError`` telling user
that there is an error with decoding bytes. The only valid hexadecimal
numbers are ``0123456789abcdefABCDEF`` and ``s`` isn't one of them.


Assignments
-----------
.. literalinclude:: assignments/type_strliterals_a.py
    :caption: :download:`Solution <assignments/type_strliterals_a.py>`
    :end-before: # Solution
