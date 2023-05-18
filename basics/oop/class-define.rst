OOP Class Define
================
* Object Oriented Paradigm
* Model world as objects that interacts with each other
* Classes are templates for objects
* ``PascalCase`` name convention
* Never print in a class

.. glossary::

    class
        Templates for objects.


Classes
-------
* Classes are templates for objects

Classes should have capitalized name:

>>> class User:
...     pass


Class Names
-----------
* ``PascalCase`` name convention

Multi-word class names should use ``PascalCase``:

>>> class SuperUser:
...     pass


Good Practices
--------------
* Never print in a class
* All classes in one file - when classes are short
* One class per file - when classes are long

You can mix classes and functions in one file:

>>> def say_hello():
...     pass
>>>
>>>
>>> class User:
...     pass


Use Case - 0x01
---------------
>>> class Guest:
...     pass
>>>
>>>
>>> class User:
...     pass
>>>
>>>
>>> class Admin:
...     pass


Assignments
-----------
.. literalinclude:: assignments/oop_class_define_a.py
    :caption: :download:`Solution <assignments/oop_class_define_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_class_define_b.py
    :caption: :download:`Solution <assignments/oop_class_define_b.py>`
    :end-before: # Solution
