About Built-ins
===============


SetUp
-----
>>> import numpy as np


Pi number
---------
>>> np.pi
3.141592653589793


Euler number
------------
>>> np.e
2.718281828459045


Infinite
--------
Numpy built-in:

>>> np.inf
inf
>>>
>>> np.Infinity
inf
>>>
>>> np.Inf
inf
>>>
>>> np.PINF
inf
>>>
>>> np.NINF
-inf
>>>
>>> -np.inf
-inf
>>>
>>> -np.Inf
-inf
>>>
>>> -np.Infinity
-inf

Python built-in:

>>> float('Inf')
inf
>>>
>>> float('Infinity')
inf
>>>
>>> float('inf')
inf
>>>
>>> np.inf == float('inf')
True
>>>
>>> np.inf is float('inf')
False

Mathematical operations:

>>> np.inf + 1
inf
>>> np.inf + np.inf
inf
>>> np.inf - np.inf
nan
>>> np.inf - np.nan
nan
>>>
>>> np.inf * np.inf
inf
>>> np.inf / np.inf
nan
>>>
>>> 0 / np.inf
0.0
>>> np.inf / 0
Traceback (most recent call last):
ZeroDivisionError: float division by zero

Check for infinite values:

>>> a = np.array([1, 2, np.inf])
>>>
>>> np.isfinite(a)
array([ True,  True, False])
>>>
>>> np.isinf(a)
array([False, False,  True])


Not-a-Number
------------
* Special ``float`` value
* Propagates in calculations

A floating-point 'not a number' (NaN) value. Equivalent to the output of
``float('nan')``. Due to the requirements of the IEEE-754 standard,
``math.nan`` and ``float('nan')`` are not considered to equal to any other
numeric value, including themselves. To check whether a number is a ``NaN``,
use the ``isnan()`` function to test for ``NaNs`` instead of ``is`` or
``==``. Example [#pydocNaN]_:

Python Standard Library:

>>> import math
>>>
>>> math.nan == math.nan
False
>>> float('nan') == float('nan')
False
>>> math.isnan(math.nan)
True
>>> math.isnan(float('nan'))
True

Numpy built-in:

>>> np.NaN
nan
>>>
>>> np.NAN
nan
>>>
>>> np.nan
nan

Python built-in:

>>> float('nan')
nan
>>>
>>> np.nan is float('nan')
False
>>>
>>> np.nan == float('nan')
False
>>>
>>> np.nan is None
False
>>>
>>> np.nan == None
False

Boolean value of NaN:

>>> bool(None)
False
>>>
>>> bool(np.nan)
True

Mathematical operations:

>>> np.nan + 1
nan
>>> np.nan + np.nan
nan
>>> np.nan - np.nan
nan
>>> np.nan - np.inf
nan
>>>
>>> np.nan / np.nan
nan
>>> 0 / np.nan
nan
>>> np.nan / 0
Traceback (most recent call last):
ZeroDivisionError: float division by zero

Check for NaN values:

>>> a = np.array([1, 2, np.nan])
>>>
>>> np.isnan(a)
array([False, False,  True])

NaN Value:

>>> np.array([np.nan]).astype(int)
array([-9223372036854775808])


Isinf vs Isnan
--------------
>>> a = np.array([1, 2, np.inf])
>>>
>>> np.isnan(a)
array([False, False, False])

>>> a = np.array([1, 2, np.nan])
>>>
>>> np.isfinite(a)
array([ True,  True, False])
>>>
>>> np.isinf(a)
array([False, False, False])


References
----------
.. [#pydocNaN] https://docs.python.org/3/library/math.html#math.nan


.. todo:: Assignments
