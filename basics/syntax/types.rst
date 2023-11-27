Syntax Types
============
* ``int`` - Integer number
* ``float`` - Floating point number
* ``bool`` - Boolean value
* ``str`` - Character string
* ``None`` - Empty value (null)
* ``list`` - Ordered sequence of objects (can be modified)
* ``tuple`` - Ordered sequence of objects (cannot be modified)
* ``set`` - Unordered sequence of objects (can be modified)
* ``dict`` - Key-value data structure
* ``type()`` - Returns exact type of an argument
* ``isinstance()`` - Allows for checking if value is expected type

This concept is only briefly described here. More information will be in
upcoming chapters.


Basic types
-----------
>>> data = 1                 # int
>>> data = 1.2               # float
>>> data = True              # bool
>>> data = False             # bool
>>> data = None              # NoneType
>>> data = 'abc'             # str


Sequences
---------
>>> data = [1, 2, 3]         # list
>>> data = (1, 2, 3)         # tuple
>>> data = {1, 2, 3}         # set


Mappings
--------
>>> data = {'a': 1, 'b': 2}  # dict


Type Checking
-------------
* ``type()`` - Returns type of an argument
* ``isinstance()`` - Allows for checking if value is expected type
* To check if type is what you expected use ``type()`` or ``isinstance()``
* Later you will learn the difference

>>> x = 1
>>> type(x)
<class 'int'>

>>> x = 1
>>> type(x) is int
True

>>> x = 1
>>> isinstance(x, int)
True


Use Case - 0x01
---------------
>>> name = 'Mark Watney'
>>> age = 42
>>> height = 178.0
>>> is_astronaut = True
>>> friends = None


Assignments
-----------
.. literalinclude:: assignments/syntax_types_a.py
    :caption: :download:`assignments/syntax_types_a.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_types_b.py
    :caption: :download:`assignments/syntax_types_b.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_types_c.py
    :caption: :download:`assignments/syntax_types_c.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_types_d.py
    :caption: :download:`assignments/syntax_types_d.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_assignment_e.py
    :caption: :download:`assignments/syntax_assignment_e.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_assignment_f.py
    :caption: :download:`assignments/syntax_assignment_f.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_assignment_g.py
    :caption: :download:`assignments/syntax_assignment_g.py`
    :end-before: # Solution
