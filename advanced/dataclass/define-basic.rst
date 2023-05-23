Dataclass Define Basic
======================


SetUp
-----
>>> from dataclasses import dataclass


Required Fields
---------------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str


Default Fields
--------------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     role: str = 'admin'


Lists
-----
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     groups: list[str]


Assignments
-----------
.. literalinclude:: assignments/dataclass_define_basic_a.py
    :caption: :download:`Solution <assignments/dataclass_define_basic_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/dataclass_define_basic_b.py
    :caption: :download:`Solution <assignments/dataclass_define_basic_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/dataclass_define_basic_c.py
    :caption: :download:`Solution <assignments/dataclass_define_basic_c.py>`
    :end-before: # Solution
