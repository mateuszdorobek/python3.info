OOP Method Self
===============

Calling method on an instance:

>>> text = str('hello')
>>> text.upper()
'HELLO'

Is equivalent to calling function on a class and passing instance
as a parameter:

>>> str.upper('hello')
'HELLO'


Method With Self
----------------
>>> class User:
...     def say_hello(self):
...         return 'hello'
...

>>> User.say_hello()
Traceback (most recent call last):
TypeError: User.say_hello() missing 1 required positional argument: 'self'

>>> mark = User()
>>> mark.say_hello()
'hello'


Method Without Self
-------------------
>>> class User:
...     def say_hello():
...         return 'hello'

>>> User.say_hello()
'hello'

>>> mark = User()
>>> mark.say_hello()
Traceback (most recent call last):
TypeError: User.say_hello() takes 0 positional arguments but 1 was given


Staticmethod
------------
>>> class User:
...     @staticmethod
...     def say_hello():
...         return 'hello'

>>> User.say_hello()
'hello'

>>> mark = User()
>>> mark.say_hello()
'hello'


Classmethod Without CLS
-----------------------
>>> class User:
...     @classmethod
...     def say_hello():
...         return 'hello'
...
>>>
>>> User.say_hello()
Traceback (most recent call last):
TypeError: User.say_hello() takes 0 positional arguments but 1 was given
>>>
>>> mark = User()
>>> mark.say_hello()
Traceback (most recent call last):
TypeError: User.say_hello() takes 0 positional arguments but 1 was given


Classmethod With CLS
--------------------
>>> class User:
...     @classmethod
...     def say_hello(cls):
...         return 'hello'

>>> User.say_hello()
'hello'

>>> mark = User()
>>> mark.say_hello()
'hello'


Use Case - 0x01
---------------
>>> data = ['mark', 'melissa', 'rick', 'alex']
>>> result = [x.upper() for x in data]
>>> list(result)
['MARK', 'MELISSA', 'RICK', 'ALEX']

>>> data = ['mark', 'melissa', 'rick', 'alex']
>>> result = [str.upper(x) for x in data]
>>> list(result)
['MARK', 'MELISSA', 'RICK', 'ALEX']

>>> data = ['mark', 'melissa', 'rick', 'alex']
>>> result = map(str.upper, data)
>>> list(result)
['MARK', 'MELISSA', 'RICK', 'ALEX']


Use Case - 0x02
---------------
>>> class User:
...     def __init__(self, username):
...         self.username = username
...
...     def login(self):
...         return f'User logged-in: {self.username}'
...
>>>
>>> users = [
...     User('mwatney'),
...     User('mlewis'),
...     User('rmartinez'),
... ]

>>> result = [u.login() for u in users]
>>> list(result)
['User logged-in: mwatney', 'User logged-in: mlewis', 'User logged-in: rmartinez']

>>> result = [User.login(u) for u in users]
>>> list(result)
['User logged-in: mwatney', 'User logged-in: mlewis', 'User logged-in: rmartinez']

>>> result = map(User.login, users)
>>> list(result)
['User logged-in: mwatney', 'User logged-in: mlewis', 'User logged-in: rmartinez']
