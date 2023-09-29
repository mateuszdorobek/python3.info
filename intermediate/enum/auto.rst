Enum Auto
=========
* Automatically generated value
* ``auto()``

*auto* can be used in place of a value.  If used, the *Enum* machinery will
call an *Enum*'s :meth:`_generate_next_value_` to get an appropriate value.
For *Enum* and *IntEnum* that appropriate value will be the last value plus
one; for *Flag* and *IntFlag* it will be the first power-of-two greater
than the last value; for *StrEnum* it will be the lower-cased version of the
member's name.  Care must be taken if mixing *auto()* with manually specified
values.

*auto* instances are only resolved when at the top level of an assignment:

* ``FIRST = auto()`` will work (auto() is replaced with ``1``);

* ``SECOND = auto(), -2`` will work (auto is replaced with ``2``,
  so ``2, -2`` is used to create the ``SECOND`` enum member;

* ``THREE = [auto(), -3]`` will *not* work (``<auto instance>, -3``
  is used to create the ``THREE`` enum member)

``_generate_next_value_`` can be overridden to customize the values used by
*auto*.

.. note:: in 3.13 the default ``"generate_next_value_`` will always return
          the highest member value incremented by 1, and will fail if any
          member is an incompatible type.

>>> from enum import IntEnum, auto
>>>
>>> class Status(IntEnum):
...     TODO = auto()
...     IN_PROGRESS = auto()
...     IN_REVIEW = auto()
...     DONE = auto()
...     REJECTED = auto()
>>>
>>>
>>> Status.DONE.value
4

Let's add "In Test" status in the middle of an ``Enum``:

>>> class Status(IntEnum):
...     TODO = auto()
...     IN_PROGRESS = auto()
...     IN_TEST = auto()
...     IN_REVIEW = auto()
...     DONE = auto()
...     REJECTED = auto()
>>>
>>> Status.DONE.value
5

Let's change ``Status`` to ``StrEnum``

>>> from enum import StrEnum, auto
>>>
>>> class Status(StrEnum):
...     TODO = auto()
...     IN_PROGRESS = auto()
...     IN_TEST = auto()
...     IN_REVIEW = auto()
...     DONE = auto()
...     REJECTED = auto()
>>>
>>> Status.DONE.value
'done'
>>>
>>> Status.IN_PROGRESS.value
'in_progress'



SetUp
-----
>>> from enum import StrEnum, IntEnum, auto


StrEnum
-------
>>> class Color(StrEnum):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()

>>> Color.RED
<Color.RED: 'red'>


IntEnum
-------
>>> class Color(IntEnum):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()

>>> Color.RED
<Color.RED: 1>


Use Case - 0x01
---------------
>>> class Animal(StrEnum):
...     ANT = auto()
...     BEE = auto()
...     CAT = auto()
...     DOG = auto()
