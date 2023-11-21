Typing Basic
============

Int
---
* Used to inform static type checker that the variable should be int

Declaration:

>>> data: int

>>> data: int = 1
>>> data: int = -1

Example:

>>> data: int
>>>
>>> data = 1        # ok
>>> data = -1       # ok
>>> data = 'hello'  # error


Float
-----
* Used to inform static type checker that the variable should be float

Declaration:

>>> data: float

>>> data: float = 0.0
>>> data: float = 1.23
>>> data: float = -1.23

Example:

>>> data: float
>>>
>>> data = 1.0        # ok
>>> data = -1.0       # ok
>>> data = 'hello'    # error


Str
---
* Used to inform static type checker that the variable should be str

Declaration:

>>> data: str

>>> data: str = ''
>>> data: str = 'hello'

Example:

>>> data: str
>>>
>>> data = 'Mark'           # ok
>>> data = 'Watney'         # ok
>>> data = 'Mark Watney'    # ok


Bool
----
* Used to inform static type checker that the variable should be bool

Declaration:

>>> data: bool

>>> data: bool = True
>>> data: bool = False

Example:

>>> data: bool
>>>
>>> data = True     # ok
>>> data = False    # ok
>>> data = None     # error


None
----
* Used to inform static type checker that the variable should be None

Declaration:

>>> data: None

>>> data: None = None

Example:

>>> data: None
>>>
>>> data = True     # error
>>> data = False    # error
>>> data = None     # ok


Errors
------
* Types are not Enforced
* This code will run without any problems
* Types are not required, and never will be
* Although ``mypy``, ``pyre-check`` or ``pytypes`` will throw error

>>> name: int = 'Mark Watney'


Use Case - 0x01
---------------
>>> firstname: str = 'Mark'
>>> lastname: str = 'Watney'
>>> age: int = 40
>>> adult: bool = True


Assignments
-----------
.. literalinclude:: assignments/typing_basic_a.py
    :caption: :download:`Solution <assignments/typing_basic_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/typing_basic_b.py
    :caption: :download:`Solution <assignments/typing_basic_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/typing_basic_c.py
    :caption: :download:`Solution <assignments/typing_basic_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/typing_basic_d.py
    :caption: :download:`Solution <assignments/typing_basic_d.py>`
    :end-before: # Solution
