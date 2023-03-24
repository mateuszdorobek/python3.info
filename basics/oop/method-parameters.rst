OOP Method Parameters
=====================
* Methods are functions in the class
* Prevents copy-paste code
* Improves readability
* Improves refactoring
* Decomposes bigger problem into smaller chunks
* At definition - ``self`` should always be a first parameter
* At call - ``self`` is not passed as an argument (Python will do that)
* Later you will learn more advanced things like static methods etc.

Required parameter:

    * Necessary to call that function
    * Specified at leftmost side

Optional parameter:

    * Has default value
    * Optional to call that function
    * Default value will be overridden if specified at a call time
    * Specified at rightmost side

.. glossary::

    method
        Functions in the class which takes instance as first argument (``self``)


Without Parameters
------------------
>>> class User:
...     def login(self):
...         print(f'User logged-in')


Required Parameters
-----------------
* At definition - ``self`` should always be a first parameter
* Later you will learn more advanced things like static methods etc.
* Parameter - Receiving variable used within the function
* Parameters could be required or optional (with default value)

>>> class User:
...     def login(self, username, password):
...         print(f'User logged-in')


Optional Parameters
-------------------
>>> class User:
...     def login(self, username=None, password=None):
...         print(f'User logged-in')


Required and Optional Parameters
--------------------------------
>>> class User:
...     def login(self, username, password=None):
...         print(f'User logged-in')


Use Case - 0x01
---------------
>>> class User:
...     def login(self, username, password):
...         if username == 'mwatney' and password == 'nasa':
...             print('ok')
...         else:
...             raise PermissionError
...
>>>
>>>
>>> mark = User()
>>>
>>> mark.login()
Traceback (most recent call last):
TypeError: User.login() missing 2 required positional arguments: 'username' and 'password'
>>>
>>> mark.login('invalid', 'invalid')
Traceback (most recent call last):
PermissionError
>>>
>>> mark.login('mwatney', 'invalid')
Traceback (most recent call last):
PermissionError
>>>
>>> mark.login('invalid', 'nasa')
Traceback (most recent call last):
PermissionError
>>>
>>> mark.login('mwatney', 'nasa')
ok
>>>
>>> mark.login(username='mwatney', password='nasa')
ok


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
