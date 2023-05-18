OOP Inheritance About
=====================
* Used to avoid code duplication

.. glossary::

    parent
    superclass
    base class
        Class from other classes inherits

    child
    subclass
        Class which inherits from :term:`parent`

    inherit
    derive
        Class takes attributes and methods from parent.


One Child
---------
>>> class Parent:
...     pass
>>>
>>>
>>> class Child(Parent):
...     pass


Many Children
-------------
>>> class Account:
...     pass
>>>
>>>
>>> class User(Account):
...     pass
>>>
>>> class Admin(Account):
...     pass


Use Case - 0x01
---------------
>>> class Iris:
...     pass
>>>
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>> class Versicolor(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
