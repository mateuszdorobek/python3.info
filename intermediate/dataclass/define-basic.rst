Dataclass Define Basic
======================


SetUp
-----
>>> from dataclasses import dataclass


Required Fields
---------------
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str


Default Fields
--------------
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: str = 'NASA'


Lists
-----
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str]


Assignments
-----------
.. literalinclude:: assignments/dataclass_define_basic_a.py
    :caption: :download:`Solution <assignments/dataclass_define_basic_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/dataclass_define_basic_b.py
    :caption: :download:`Solution <assignments/dataclass_define_basic_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/dataclass_define_basic_b.py
    :caption: :download:`Solution <assignments/dataclass_define_basic_b.py>`
    :end-before: # Solution
