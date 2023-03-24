Logic Bool
==========
* ``True`` - Positive value
* ``False`` - Negative value
* First letter capitalized, other are lower cased
* Builtin function ``bool()`` converts argument to ``bool``


Syntax
------
* First letter capitalized, other are lower cased

>>> data = True
>>> data = False

>>> data = true
Traceback (most recent call last):
NameError: name 'true' is not defined

>>> data = TRUE
Traceback (most recent call last):
NameError: name 'TRUE' is not defined


Type Casting
------------
* Builtin function ``bool()`` converts argument to ``bool``

>>> bool(True)
True
>>>
>>> bool(False)
False
>>>
>>> bool(1)
True
>>>
>>> bool(0)
False

>>> bool(1)
True
>>>
>>> bool(2)
True
>>>
>>> bool(3)
True
>>>
>>> bool(-1)
True
>>>
>>> bool(-2)
True
>>>
>>> bool(-3)
True
>>>
>>> bool(1.0)
True
>>>
>>> bool('Mark Watney')
True


Negative values
---------------
>>> bool(0)
False
>>>
>>> bool(0.0)
False
>>>
>>> bool(0+0j)
False
>>>
>>> bool(0.0+0.0j)
False
>>>
>>> bool(False)
False
>>>
>>> bool(None)
False
>>>
>>> bool('')
False
>>>
>>> bool(())
False
>>>
>>> bool([])
False
>>>
>>> bool({})
False

>>> bool(int())
False
>>>
>>> bool(float())
False
>>>
>>> bool(complex())
False
>>>
>>> bool(bool())
False
>>>
>>> bool(str())
False
>>>
>>> bool(tuple())
False
>>>
>>> bool(list())
False
>>>
>>> bool(dict())
False
>>>
>>> bool(set())
False


Comparison
----------
* ``x < y`` - Less than
* ``x <= y`` - Less or equal
* ``x > y`` - Greater than
* ``x >= y`` - Greater or equal
* ``==`` - Equals
* ``!=`` - Not Equals

>>> 10 < 2
False
>>>
>>> 10 <= 2
False
>>>
>>> 10 > 2
True
>>>
>>> 10 >= 2
True
>>>
>>> 10 == 2
False
>>>
>>> 10 != 2
True

>>> x = 1
>>> y = 2
>>>
>>>
>>> x == 1
True
>>>
>>> y == 2
True
>>>
>>> x == y
False
>>>
>>> x != y
True


Negation
--------
.. code-block:: text

    ~1 -> 0
    ~0 -> 1

>>> not True
False

>>> not False
True


Conjunction
-----------
Definition:

.. code-block:: text

    1 & 1 -> 1
    1 & 0 -> 0
    0 & 1 -> 0
    0 & 0 -> 0

Example:

>>> True and True
True
>>>
>>> True and False
False
>>>
>>> False and True
False
>>>
>>> False and False
False


Use Case - 0x01
---------------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> firstname == 'Mark' and lastname == 'Watney'
True
>>>
>>> firstname == 'Mark'
True
>>>
>>> lastname == 'Watney'
True
>>>
>>> True and True
True


Use Case - 0x02
---------------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> firstname == 'Mark' and lastname == 'Lewi'
False
>>>
>>> firstname == 'Mark'
True
>>>
>>> lastname == 'Lewi'
False
>>>
>>> True and False
False


Disjunction
-----------
Definition:

.. code-block:: text

    1 | 1 -> 1
    1 | 0 -> 1
    0 | 1 -> 1
    0 | 0 -> 0

Example:

>>> True or True
True
>>>
>>> True or False
True
>>>
>>> False or True
True
>>>
>>> False or False
False


Use Case - 0x01
---------------
>>> name = 'Mark Watney'
>>>
>>> name == 'Mark Watney' or name == 'Melissa Lewis'
True


Use Case - 0x02
---------------
>>> name = 'Mark Watney'
>>>
>>>
>>> name == 'Mark Watney'
True
>>>
>>> name == 'Melissa Lewis'
False
>>>
>>> True or False
True


Boolean Algebra
---------------
Example:

>>> True and True or False
True
>>>
>>> False and False or True
True

>>> (True and True) or False
True
>>>
>>> True and (True or False)
True

>>> True and False or False
False
>>>
>>> True and (False or False)
False


Use Case - 0x01
---------------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> (firstname == 'Mark' and lastname == 'Watney') \
...     or (firstname == 'Melissa' and lastname == 'Lewis') \
...     or (firstname == 'Rick' and lastname == 'Martinez')
True


Use Case - 0x02
---------------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> firstname == 'Mark' and lastname == 'Watney'
True
>>>
>>> firstname == 'Melissa' and lastname == 'Lewis'
False
>>>
>>> firstname == 'Rick' and lastname == 'Martinez'
False
>>>
>>> True or False or False
True


Built-in Functions
------------------
* ``type()`` - Checks type of an object
* ``isinstance(a, x)`` - If ``a`` is instance of ``x``
* ``isinstance(a, (x,y))`` - If ``a`` is instance of ``x`` or ``y``

>>> type(True)
<class 'bool'>
>>>
>>> type(False)
<class 'bool'>

>>> isinstance(1, bool)
False
>>>
>>> isinstance(1, int)
True
>>>
>>> isinstance(1, float)
False

>>> isinstance(1.23, bool)
False
>>>
>>> isinstance(1.23, int)
False
>>>
>>> isinstance(1.23, float)
True

>>> isinstance(True, bool)
True
>>>
>>> isinstance(True, int)
True
>>>
>>> isinstance(True, float)
False
>>>
>>> isinstance(False, bool)
True
>>>
>>> isinstance(False, int)
True
>>>
>>> isinstance(False, float)
False


Assignments
-----------
.. literalinclude:: assignments/type_bool_a.py
    :caption: :download:`Solution <assignments/type_bool_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_bool_b.py
    :caption: :download:`Solution <assignments/type_bool_b.py>`
    :end-before: # Solution

.. todo:: assignments with all() and any()
.. todo:: assignments with isinstance() and type()
