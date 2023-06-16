Functional Namespace
====================
* Functions provide namespaces
* Only code inside that namespace can access it's locals

In Python, a function is a namespace, which means that it is a container for
variables and other objects. The variables and objects defined within a
function are only accessible within that function's namespace, and cannot be
accessed from outside the function.

When a function is called, a new namespace is created for it. This namespace
contains all the local variables and objects defined within the function, as
well as any arguments passed to the function. The namespace is destroyed
when the function returns.

Here's an example of using a function as a namespace in Python:

>>> def my_function():
...     x = 10
...     y = 20
...     print(x + y)
>>>
>>> my_function()
30
>>> print(x)
Traceback (most recent call last):
NameError: name 'x' is not defined

In this example, the ``my_function()`` function defines two variables
(``x`` and ``y``) within its namespace. These variables are only accessible
within the function. When the function is called, it prints the sum of ``x``
and ``y``. When the function returns, the namespace is destroyed, and the
variables are no longer accessible.

If we try to access the ``x`` variable outside the function, we get a
``NameError`` because the variable is not defined in the global namespace.

Using functions as namespaces helps to keep code modular and organized.
It also helps to prevent naming conflicts between different parts of a program.


Variables Inside Function
-------------------------
* Variables inside function

>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'

Before call:

>>> firstname
Traceback (most recent call last):
NameError: name 'firstname' is not defined
>>>
>>> lastname
Traceback (most recent call last):
NameError: name 'lastname' is not defined

After call:

>>> run()
>>>
>>> firstname
Traceback (most recent call last):
NameError: name 'firstname' is not defined
>>>
>>> lastname
Traceback (most recent call last):
NameError: name 'lastname' is not defined


Functions Inside Function
-------------------------
* Functions inside function

>>> def run():
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')

>>> say_hello()
Traceback (most recent call last):
NameError: name 'say_hello' is not defined
>>>
>>> say_goodbye()
Traceback (most recent call last):
NameError: name 'say_goodbye' is not defined

>>> run()
>>>
>>> say_hello()
Traceback (most recent call last):
NameError: name 'say_hello' is not defined
>>>
>>> say_goodbye()
Traceback (most recent call last):
NameError: name 'say_goodbye' is not defined


Classes Inside Function
-----------------------
>>> def run():
...     class Admin:
...         pass
...
...     class Guest:
...         pass

>>> Admin()
Traceback (most recent call last):
NameError: name 'Admin' is not defined
>>>
>>> Guest()
Traceback (most recent call last):
NameError: name 'Guest' is not defined

>>> run()
>>>
>>> Admin()
Traceback (most recent call last):
NameError: name 'Admin' is not defined
>>>
>>> Guest()
Traceback (most recent call last):
NameError: name 'Guest' is not defined


Methods Inside Function
-----------------------
>>> def run():
...     class Admin:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     class Guest:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname

>>> Admin('Mark', 'Watney')
Traceback (most recent call last):
NameError: name 'Admin' is not defined
>>>
>>> Guest('Melissa', 'Lewis')
Traceback (most recent call last):
NameError: name 'Guest' is not defined

>>> run()
>>>
>>> Admin('Mark', 'Watney')
Traceback (most recent call last):
NameError: name 'Admin' is not defined
>>>
>>> Guest('Melissa', 'Lewis')
Traceback (most recent call last):
NameError: name 'Guest' is not defined


Instances Inside Function
-------------------------
>>> def run():
...     class Admin:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     class Guest:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     mark = Admin('Mark', 'Watney')
...     melissa = Guest('Melissa', 'Lewis')

>>> mark
Traceback (most recent call last):
NameError: name 'mark' is not defined
>>>
>>> melissa
Traceback (most recent call last):
NameError: name 'melissa' is not defined

>>> run()
>>>
>>> mark
Traceback (most recent call last):
NameError: name 'mark' is not defined
>>>
>>> melissa
Traceback (most recent call last):
NameError: name 'melissa' is not defined


All Together
------------
>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')
...
...     class Admin:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     class Guest:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     mark = Admin('Mark', 'Watney')
...     melissa = Guest('Melissa', 'Lewis')


Execute
-------
>>> def run():
...
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')
...
...     say_hello()
...     say_goodbye()
>>>
>>>
>>> result = run()
Hello
Goodbye
>>>
>>> print(result)
None


Return Results
--------------
>>> def run():
...
...     def get_hello():
...         return 'Hello'
...
...     def get_goodbye():
...         return 'Goodbye'
...
...     return get_hello()
>>>
>>>
>>> run()
'Hello'

>>> def run():
...
...     def get_hello():
...         return 'Hello'
...
...     def get_goodbye():
...         return 'Goodbye'
...
...     return get_hello(), get_goodbye()
>>>
>>>
>>> run()
('Hello', 'Goodbye')


Return Function
---------------
>>> def run():
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')
...
...     return say_hello
>>>
>>>
>>> hello = run()
>>> hello()
Hello

>>> def run():
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')
...
...     return say_hello, say_goodbye
>>>
>>>
>>> hello, goodbye = run()
>>>
>>> hello()
Hello
>>>
>>> goodbye()
Goodbye

>>> def run():
...     class Admin:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     return Admin('Mark', 'Watney')
>>>
>>>
>>> mark = run()
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}


Locals
------
>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')
...
...     class Admin:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     class Guest:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     mark = Admin('Mark', 'Watney')
...     melissa = Guest('Melissa', 'Lewis')
...
...     print(locals())

>>> run()   # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'say_hello': <function run.<locals>.say_hello at 0x...>,
 'say_goodbye': <function run.<locals>.say_goodbye at 0x...>,
 'Admin': <class '__main__.run.<locals>.Admin'>,
 'Guest': <class '__main__.run.<locals>.Guest'>,
 'mark': <__main__.run.<locals>.Admin object at 0x...>,
 'melissa': <__main__.run.<locals>.Guest object at 0x...>}
