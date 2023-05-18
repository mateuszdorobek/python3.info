Boolean Disjunction
===================
* ``or``

.. code-block:: text

    1 | 1 -> 1
    1 | 0 -> 1
    0 | 1 -> 1
    0 | 0 -> 0


Syntax
------
>>> True or True
True

>>> True or False
True

>>> False or True
True

>>> False or False
False


Example
-------
>>> name = 'Mark Watney'
>>>
>>> name == 'Mark Watney' or name == 'Melissa Lewis'
True

Because:

>>> name = 'Mark Watney'
>>>
>>> name == 'Mark Watney'
True
>>> name == 'Melissa Lewis'
False

Rule:

>>> True or False
True


Control Flow
------------
>>> name = 'Watney'
>>>
>>> if name == 'Watney' or name == 'Lewis':
...     print('Hello Mark')
... else:
...     print('Access denied')
Hello Mark


.. todo:: Assignments
