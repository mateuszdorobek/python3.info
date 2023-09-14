OOP Method About
================
* ``name(self)`` - public method
* ``_name(self)`` - protected method (non-public by convention)
* ``__name(self)`` - private method (name mangling)
* ``__name__(self)`` - system method
* ``name_(self)`` - avoid name collision with built-ins


Recap
-----
* All functions are instances of a class ``function``
* All functions has attributes or methods such as ``__call__()``

>>> def add(a, b):
...     return a + b
...
>>>
>>> type(add)
<class 'function'>
>>>
>>> add.__call__(1, 2)
3


Function or Method
------------------
>>> class User:
...     def say_hello(self):
...         return 'hello'

>>> type(User.say_hello)
<class 'function'>

>>> mark = User()
>>> type(mark.say_hello)
<class 'method'>


Types
-----
Static method:

>>> class User:
...     def one():
...         print('one')

Dynamic method:

>>> class User:
...     def two(self):
...         print('two')

Static method:

>>> class User:
...     @staticmethod
...     def three():
...         print('three')

Class method:

>>> class User:
...     @classmethod
...     def four(cls):
...         print('four')


Example
-------
>>> class User:
...     def one():
...         print('one')
...
...     def two(self):
...         print('two')
...
...     @staticmethod
...     def three():
...         print('three')
...
...     @classmethod
...     def four(cls):
...         print('four')

>>> User.one()
one
>>>
>>> User.two()
Traceback (most recent call last):
TypeError: User.two() missing 1 required positional argument: 'self'
>>>
>>> User.three()
three
>>>
>>> User.four()
four

>>> mark = User()
>>>
>>> mark.one()
Traceback (most recent call last):
TypeError: User.one() takes 0 positional arguments but 1 was given
>>>
>>> mark.two()
two
>>>
>>> mark.three()
three
>>>
>>> mark.four()
four


Class Function
--------------
>>> class User:
...     def say_hello(self):
...         return 'hello'

Let's check the type of a ``User.say_hello``:

>>> type(User.say_hello)
<class 'function'>

Note, that ``say_hello()`` is a function not a method!!

What actually metod is? Is there a difference between method or a function?
Is method a function on an instance?

>>> vars(User)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
mappingproxy({'__module__': '__main__',
              'say_hello': <function User.say_hello at 0x...>,
              '__dict__': <attribute '__dict__' of 'User' objects>,
              '__weakref__': <attribute '__weakref__' of 'User' objects>,
              '__doc__': None})


Method
------
>>> class User:
...     def say_hello(self):
...         return 'hello'
>>>
>>> mark = User()

Let's check the type of a ``mark.say_hello``:

>>> type(mark.say_hello)
<class 'method'>

Note, that ``say_hello()`` is a method!!


Compare
-------
>>> class User:
...     def say_hello():
...         return 'hello'
>>>
>>>
>>> User.say_hello  # doctest: +ELLIPSIS
<function User.say_hello at 0x...>
>>>
>>> type(User.say_hello)
<class 'function'>
>>>
>>>
>>> mark = User()
>>>
>>> mark.say_hello  # doctest: +ELLIPSIS
<bound method User.say_hello of <__main__.User object at 0x...>>
>>>
>>> type(mark.say_hello)
<class 'method'>


>>> class User:
...     def say_hello(self):
...         return 'hello'
>>>
>>>
>>> User.say_hello  # doctest: +ELLIPSIS
<function User.say_hello at 0x...>
>>>
>>> type(User.say_hello)
<class 'function'>
>>>
>>>
>>> mark = User()
>>>
>>> type(mark.say_hello)
<class 'method'>
>>>
>>> mark.say_hello  # doctest: +ELLIPSIS
<bound method User.say_hello of <__main__.User object at 0x...>>


Use Case - 0x01
---------------
>>> name = 'Mark'
>>> name.upper()
'MARK'

Is equivalent to:

>>> str.upper('Mark')
'MARK'


Use Case - 0x02
---------------
>>> data = ['Mark', 'Watney', 'mwatney@nasa.gov']
>>> ','.join(data)
'Mark,Watney,mwatney@nasa.gov'

Is equivalent to:

>>> data = ['Mark', 'Watney', 'mwatney@nasa.gov']
>>> str.join(',', data)
'Mark,Watney,mwatney@nasa.gov'


Use Case - 0x03
---------------
>>> data = ['Mark', 'Watney', 'mwatney@nasa.gov']
>>> result = [x.upper() for x in data]
>>> list(result)
['MARK', 'WATNEY', 'MWATNEY@NASA.GOV']

Is equivalent to:

>>> data = ['Mark', 'Watney', 'mwatney@nasa.gov']
>>> result = map(str.upper, data)
>>> list(result)
['MARK', 'WATNEY', 'MWATNEY@NASA.GOV']


Use Case - 0x04
---------------
>>> class User:
...     def __init__(self, username):
...         self.username = username
...
...     def login(self):
...         print(f'User {self.username} logged-in')

Create users:

>>> users = [
...     User('mwatney'),
...     User('mlewis'),
...     User('rmartinez'),
... ]

Login all users:

>>> users = map(User.login, users)
>>> result = list(users)
User mwatney logged-in
User mlewis logged-in
User rmartinez logged-in
