Numeric Int
===========
* Represents integer
* Could be both signed and unsigned
* There is no maximal or minimal ``int`` value
* Default ``int`` size is 64 bit
* Python automatically extends ``int`` when need bigger number


Syntax
------
* Signed and Unsigned
* Use ``_`` for thousand separator

>>> data = 1
>>> data = +1
>>> data = -1

You can use ``_`` for easier read especially with big numbers:

>>> million = 1000000
>>> million = 1_000_000
>>>
>>> print(million)
1000000


Type Conversion
---------------
* Builtin function ``int()`` converts argument to ``int``
* It is not rounding
* Works with strings, if all characters could be converted to ``int``
* Supports only: ``+``, ``-`` and ``_`` (underscore)

Builtin function ``int()`` converts argument to ``int``:

>>> int(1)
1
>>>
>>> int(+1)
1
>>>
>>> int(-1)
-1

>>> int(1.337)
1
>>>
>>> int(+1.1337)
1
>>>
>>> int(-1.337)
-1

>>> int('1')
1
>>>
>>> int('+1')
1
>>>
>>> int('-1')
-1

>>> int('1_000_000')
1000000
>>>
>>> int('-1_000_000')
-1000000


Type Conversion Errors
----------------------
* Works with strings, if all characters could be converted to ``int``
* It is not validator or parser to extract all numbers from ``str``

Builtin function ``int()`` fails when in argument there are parameters
other than a digit, ``+`` or ``-`` sign and ``_``

>>> int('3.1337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '3.1337'

>>> int('+3.1337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '+3.1337'

>>> int('-3.1337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '-3.1337'

>>> int('3,1337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '3,1337'

>>> int('+3,1337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '+3,1337'

>>> int('-3,1337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '-3,1337'


Rounding
--------
* Builtin function ``int()`` does not round numbers - only converts to ``int``
* Use ``round()`` for numbers rounding

Builtin function ``int()`` does not round numbers:

>>> int(1.111)
1
>>>
>>> int(1.999)
1

Builtin function ``round()`` does that:

>>> round(1.111)
1
>>>
>>> round(1.999)
2


Use Case - 0x01
---------------
>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>> HOUR = 60 * MINUTE
>>> DAY = 24 * HOUR
>>>
>>>
>>> duration = 123456 * SECOND
>>>
>>> duration // DAY
1
>>> duration // HOUR
34
>>> duration // MINUTE
2057
>>> duration // SECOND
123456


Use Case - 0x02
---------------
>>> m = 1
>>> km = 1000 * m
>>> mi = 1652 * m
>>>
>>>
>>> distance = 123*mi
>>>
>>> distance // m
203196
>>> distance // km
203


Use Case - 0x03
---------------
>>> PLN = 1
>>> EUR = 4.71 * PLN  # 2023-03-19 17:00 GMT+1
>>> USD = 4.41 * PLN  # 2023-03-19 17:00 GMT+1
>>>
>>>
>>> price = 100*PLN
>>>
>>> round(price // EUR)
21
>>> round(price // USD)
22


Assignments
-----------
.. literalinclude:: assignments/type_int_a.py
    :caption: :download:`Solution <assignments/type_int_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_b.py
    :caption: :download:`Solution <assignments/type_int_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_c.py
    :caption: :download:`Solution <assignments/type_int_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_d.py
    :caption: :download:`Solution <assignments/type_int_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_e.py
    :caption: :download:`Solution <assignments/type_int_e.py>`
    :end-before: # Solution


Homework
--------
.. literalinclude:: assignments/type_int_f.py
    :caption: :download:`Solution <assignments/type_int_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_g.py
    :caption: :download:`Solution <assignments/type_int_g.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_h.py
    :caption: :download:`Solution <assignments/type_int_h.py>`
    :end-before: # Solution


.. todo:: assignments with sum(values)
.. todo:: assignments with isinstance() and type()
.. todo:: assignments with round()
