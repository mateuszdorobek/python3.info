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


Types
-----
Dynamic method:

>>> class MyClass:
...     def mymethod(self):
...         pass

Static method:

>>> class MyClass:
...     def mymethod():
...         pass

Static method:

>>> class MyClass:
...     @staticmethod
...     def mymethod():
...         pass

Class method:

>>> class MyClass:
...     @classmethod
...     def mymethod(cls):
...         pass
