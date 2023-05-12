Decorator Types
===============
* Decorator function
* Decorator method
* Decorator class


Decorator Function
------------------
* Decorator is a function which takes another object as an argument
* Doesn't matter, whether this object is a function, class or method

Definition:

>>> def mydecorator(obj):
...     ...

Usage:

>>> @mydecorator
... def say_hello():
...     return 'hello'

>>> @mydecorator
... class User:
...     def say_hello():
...         return 'hello'

>>> class User:
...     @mydecorator
...     def say_hello():
...         return 'hello'


Decorator Method
----------------
* Decorator is a method which takes instance and another object as an argument
* Doesn't matter, whether this object is a function, class or method

Definition:

>>> class MyClass:
...     @staticmethod
...     def mydecorator(obj):
...         ...

Usage:

>>> @MyClass.mydecorator
... def say_hello():
...     return 'hello'

>>> @MyClass.mydecorator
... class User:
...     def say_hello():
...         return 'hello'

>>> class User:
...     @MyClass.mydecorator
...     def say_hello():
...         return 'hello'


Decorator Class
---------------
* Decorator is a class which takes another object as an argument to ``__init__()`` method
* Doesn't matter, whether this object is a function, class or method

Definition:

>>> class MyDecorator:
...     def __init__(self, obj):
...         ...

Usage:

>>> @MyDecorator
... def say_hello():
...     return 'hello'

>>> @MyDecorator
... class User:
...     def say_hello():
...         return 'hello'

>>> class User:
...     @MyDecorator
...     def say_hello():
...         return 'hello'
