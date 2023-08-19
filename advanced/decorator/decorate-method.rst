Decorate Method
===============
* ``mydecorator`` is a decorator name
* ``method`` is a method name
* ``self`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

SetUp:

>>> def mydecorator(method):
...     ...

Syntax:

>>> class MyClass:
...     @mydecorator
...     def mymethod(self, *args, **kwargs):
...         ...

Is equivalent to:

>>> class MyClass:
...     def mymethod(self, *args, **kwargs):
...         ...
>>>
>>>
>>> obj = MyClass()
>>> obj.mymethod = mydecorator(obj.mymethod)


Syntax
------
* ``mydecorator`` is a decorator name
* ``mymethod`` is a method name
* ``self`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

>>> def mydecorator(method):
...     def wrapper(self, *args, **kwargs):
...         return method(self, *args, **kwargs)
...     return wrapper
>>>
>>>
>>> class MyClass:
...     @mydecorator
...     def mymethod(self):
...         ...
>>>
>>>
>>> my = MyClass()
>>> my.mymethod()


Example
-------
>>> def run(method):
...     def wrapper(self, *args, **kwargs):
...         return method(self, *args, **kwargs)
...     return wrapper
>>>
>>>
>>> class User:
...     @run
...     def say_hello(self, name):
...         return f'My name... {name}'
>>>
>>>
>>> mark = User()
>>> mark.say_hello('José Jiménez')
'My name... José Jiménez'


Use Case - 0x01
---------------
* Is Allowed

>>> def if_allowed(method):
...     def wrapper(self, *args, **kwargs):
...         if self._is_allowed:
...             return method(self, *args, **kwargs)
...         else:
...             print('Sorry, Permission Denied')
...     return wrapper
>>>
>>>
>>> class MyClass:
...     def __init__(self):
...         self._is_allowed = True
...
...     @if_allowed
...     def do_something(self):
...         print('Doing...')
...
...     @if_allowed
...     def do_something_else(self):
...         print('Doing something else...')
>>>
>>>
>>> my = MyClass()
>>>
>>> my.do_something()
Doing...
>>> my.do_something_else()
Doing something else...
>>>
>>>
>>> my._is_allowed = False
>>>
>>> my.do_something()
Sorry, Permission Denied
>>> my.do_something_else()
Sorry, Permission Denied


Use Case - 0x02
---------------
* Paragraph

>>> def paragraph(method):
...     def wrapper(self, *args, **kwargs):
...         result = method(self, *args, **kwargs)
...         return f'<p>{result}</p>'
...     return wrapper
>>>
>>>
>>> class HTMLReport:
...     @paragraph
...     def first(self, *args, **kwargs):
...         return 'First'
...
...     @paragraph
...     def second(self, *args, **kwargs):
...         return 'Second'
>>>
>>>
>>> x = HTMLReport()
>>>
>>> x.first()
'<p>First</p>'
>>>
>>> x.second()
'<p>Second</p>'


Use Case - 0x03
---------------
>>> def login_required(obj):
...     def wrapper(instance, *args, **kwargs):
...         if not instance.is_authenticated:
...             raise PermissionError
...         return obj(instance, *args, **kwargs)
...     return wrapper
>>>
>>>
>>> class User:
...     def __init__(self, username, password):
...         self.username = username
...         self.password = password
...         self.is_authenticated = False
...
...     def login(self):
...         self.is_authenticated = True
...         print('User logged-in')
...
...     def logout(self):
...         self.is_authenticated = False
...         print('User logged-out')
...
...     @login_required
...     def change_password(self, new_password):
...         self.password = new_password

>>> mark = User('mwatney', 'Ares3')
>>> mark.password
'Ares3'

>>> mark.change_password('Nasa69')
Traceback (most recent call last):
PermissionError

>>> mark.login()
User logged-in
>>>
>>> mark.change_password('Nasa69')
>>> mark.password
'Nasa69'

>>> mark.logout()
User logged-out
>>> mark.change_password('Ares3')
Traceback (most recent call last):
PermissionError


Assignments
-----------
.. literalinclude:: assignments/decorator_method_a.py
    :caption: :download:`Solution <assignments/decorator_method_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_method_b.py
    :caption: :download:`Solution <assignments/decorator_method_b.py>`
    :end-before: # Solution
