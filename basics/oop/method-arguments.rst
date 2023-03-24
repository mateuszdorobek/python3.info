OOP Method Arguments
====================
* Methods are functions in the class
* Prevents copy-paste code
* Improves readability
* Improves refactoring
* Decomposes bigger problem into smaller chunks
* At this moment:

    * At definition - ``self`` should always be a first parameter
    * At call - ``self`` is not passed as an argument (Python will do that)
    * Later you will learn more advanced things like static methods etc.

.. glossary::

    method
        Functions in the class which takes instance as first argument (``self``)


Method Parameters
-----------------
* At definition - ``self`` should always be a first parameter
* Later you will learn more advanced things like static methods etc.
* Parameter - Receiving variable used within the function
* Parameters could be required or optional (with default value)

Required parameter:

    * Necessary to call that function
    * Specified at leftmost side

Optional parameter:

    * Has default value
    * Optional to call that function
    * Default value will be overridden if specified at a call time
    * Specified at rightmost side

Without parameters:

>>> class Astronaut:
...     def say_hello(self):
...         print('My name... José Jiménez')

Methods with required parameter:

>>> class Astronaut:
...     def say_hello(self, firstname):
...         print(f'My name... {firstname}')

Method with optional parameter:

>>> class Astronaut:
...     def say_hello(self, firstname='unknown'):
...         print(f'My name... {firstname}')

Method with required and optional parameter:

>>> class Astronaut:
...     def say_hello(self, firstname, lastname='unknown'):
...         print(f'My name... {firstname} {lastname}')


Method Arguments
----------------
* At call - ``self`` is not passed as an argument (Python will do that)


>>> class Astronaut:
...     def say_hello(self):
...         print('My name... José Jiménez')
...
...
>>> jose = Astronaut()
>>> jose.say_hello()
My name... José Jiménez

Method with positional argument:

>>> class Astronaut:
...     def say_hello(self, name):
...         print(f'My name... {name}')
>>>
>>>
>>> jose = Astronaut()
>>>
>>> jose.say_hello('José Jiménez')
My name... José Jiménez
>>>
>>> jose.say_hello()
Traceback (most recent call last):
TypeError: Astronaut.say_hello() missing 1 required positional argument: 'name'

Method with keyword argument:

>>> class Astronaut:
...     def say_hello(self, firstname, lastname):
...         print(f'My name... {firstname} {lastname}')
>>>
>>>
>>> jose = Astronaut()
>>>
>>> jose.say_hello(firstname='José', lastname='Jiménez')
My name... José Jiménez
>>>
>>> jose.say_hello(lastname='Jiménez', firstname='José')
My name... José Jiménez
>>>
>>> jose.say_hello()
Traceback (most recent call last):
TypeError: Astronaut.say_hello() missing 2 required positional arguments: 'firstname' and 'lastname'


Assignments
-----------
.. literalinclude:: assignments/oop_method_a.py
    :caption: :download:`Solution <assignments/oop_method_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_method_b.py
    :caption: :download:`Solution <assignments/oop_method_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_method_c.py
    :caption: :download:`Solution <assignments/oop_method_c.py>`
    :end-before: # Solution
