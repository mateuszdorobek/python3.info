Idiom Switch
============


SetUp
-----
Let's take the following code and do the refactoring:

>>> print('Hello')
Hello


Iteration 1 - If/Else
---------------------
It all starts with single ``if/else`` statement

>>> language = 'Polish'
>>>
>>> if language == 'Polish':
...     result = 'Cześć'
... else:
...     result = 'Hello'
>>>
>>> print(result)
Cześć


Iteration 2 - Elif
------------------
It quickly grows into multiple ``elif``:

>>> language = 'Spanish'
>>>
>>> if language == 'Polish':
...     result = 'Cześć'
... elif language == 'English':
...     result = 'Hello'
... else:
...     result = 'Unknown language'
>>>
>>> print(result)
Unknown language

>>> language = 'Spanish'
>>>
>>> if language == 'Polish':
...     result = 'Cześć'
... elif language == 'English':
...     result = 'Hello'
... elif language == 'Spanish':
...     result = 'Hola'
... else:
...     result = 'Unknown language'
>>>
>>> print(result)
Hola

>>> language = 'Polish'
>>>
>>> if language == 'Polish':
...     result = 'Cześć'
... elif language == 'English':
...     result = 'Hello'
... elif language == 'German':
...     result = 'Guten Tag'
... elif language == 'Spanish':
...     result = 'Buenos Días'
... else:
...     result = 'Unknown language'
>>>
>>> print(result)
Cześć

>>> language = 'English'
>>>
>>> if language == 'Polish':
...     result = 'Cześć'
... elif language == 'English':
...     result = 'Hello'
... elif language == 'German':
...     result = 'Guten Tag'
... elif language == 'Spanish':
...     result = 'Buenos Días'
... elif language == 'Chinese':
...     result = '你好'
... elif language == 'French':
...     result = 'Bonjour'
... else:
...     result = 'Unknown language'
>>>
>>> print(result)
Hello


Iteration 3 - Switch / Pattern Matching
---------------------------------------
* In other languages you may find ``switch`` statement
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial

>>> language = 'English'
>>>
>>> match language:  # doctest: +SKIP
...     case 'Polish': result = 'Cześć'
...     case 'English': result = 'Hello'
...     case 'German': result = 'Guten Tag'
...     case 'Spanish': result = 'Hola'
...     case 'Chinese': result = '你好'
...     case 'French': result = 'Bonjour'
...     case _: result = 'Unknown language'
>>>
>>> print(result)
Hello

It's a bit cleaner, but essentially the same problem persists. Both
``switch/pattern matching`` and ``if/elif/else`` statements moves business
logic to the execution location, which makes it hard for future maintenance.


Iteration 4 - Imported Dict
---------------------------
Moving data to a custom i18n (internationalization) module.

Content of a `myapp.i18n` module:

>>> HELLO = {
...     'Polish': 'Cześć',
...     'English': 'Hello',
...     'German': 'Guten Tag',
...     'Spanish': 'Hola',
...     'Chinese': '你好',
...     'French':  'Bonjour',
... }

Then import this in the desired location:

>>> from myapp.i18n import HELLO  # doctest: +SKIP
>>>
>>>
>>> HELLO.get('Polish', 'Unknown language')
'Cześć'
>>>
>>> HELLO.get('Greek', 'Unknown language')
'Unknown language'

This is far better, but now the problem is, that at all times we need to put
fallback solution (Unknown language).


Iteration 5 - Imported Function
-------------------------------
Moving data to a custom i18n (internationalization) module and enclosing
this in a function.

Content of a `myapp.i18n` module:

>>> def hello(language):
...     return {
...         'Polish': 'Cześć',
...         'English': 'Hello',
...         'German': 'Guten Tag',
...         'Spanish': 'Hola',
...         'Chinese': '你好',
...         'French':  'Bonjour',
...     }.get(language, 'Unknown language')

Then import this in the desired location:

>>> from myapp.i18n import hello  # doctest: +SKIP
>>>
>>>
>>> hello(language='Polish')
'Cześć'
>>>
>>> hello(language='Greek')
'Unknown language'

This would be the best procedural solution. Language functions are stored in
one location, which is easy to maintain and extend. Function call is self
explanatory and keyword argument makes it even more explicit.


Iteration 6 - Polymorphism
--------------------------
However Python is an object oriented language and in this world we do
things slightly different. The ultimate OOP solution to this problem is
to use Polymorphism:

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Language(ABC):
...     @abstractmethod
...     def hello(self) -> str: ...
>>>
>>>
>>> class Polish(Language):
...     def hello(self):
...         return 'Cześć'
>>>
>>>
>>> class English(Language):
...     def hello(self):
...         return 'Hello'
>>>
>>>
>>> class Spanish(Language):
...     def hello(self):
...         return 'Hola'
>>>
>>>
>>> language = Polish()
>>> language.hello()
'Cześć'
>>>
>>> language = English()
>>> language.hello()
'Hello'


References
----------
.. [#patternmatching] Raymond Hettinger. Retrieved: 2021-03-07. URL: https://twitter.com/raymondh/status/1361780586570948609?s=20


Assignments
-----------
.. todo:: Assignments
