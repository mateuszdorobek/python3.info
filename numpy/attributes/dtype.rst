Array Data Types
================
* Array can have only one data type (``dtype``)
* Type can be "non-primitive" - any class

.. figure:: img/array-dtype-sizes.png


SetUp
-----
>>> import numpy as np


Bits and Bytes
--------------
* Signed and unsigned
* Unsigned cannot be negative
* For negative signed numbers "Two's complement" is used

.. code-block:: text

    1       # unsigned

    +1      # signed
    -1      # signed

3 bit unsigned integers. Values: 8, minimal: 0, maximal: 8:

.. code-block:: text

    0       000
    1       001
    2       010
    3       011
    4       100
    5       101
    6       110
    7       111

3 bit signed integers. Values: 8, minimal: -4, maximal: 3:

.. code-block:: text

    +0      000
    +1      001
    +2      010
    +3      011
    −4      100
    −3      101
    −2      110
    −1      111

8 bit signed integers. Values: 256, minimal: -128, maximal: 127:

.. code-block:: text

    +0      00000000
    +1      00000001
    +2      00000010
    +126    01111110
    +127    01111111
    −128    10000000
    −127    10000001
    −126    10000010
    −2      11111110
    −1      11111111

32 bit unsigned int. Values: 2,147,483,647, minimal: 0, maximal: 2,147,483,647:

.. code-block:: text

    0       0000000000000000000000000000000000
    1       0000000000000000000000000000000001
    2       0000000000000000000000000000000010
    3       0000000000000000000000000000000011
    4       0000000000000000000000000000000100
    5       0000000000000000000000000000000101
    6       0000000000000000000000000000000110
    7       0000000000000000000000000000000111

Calculates a two's complement integer from the given input value's bits:

>>> def twos_complement(value: int, num_bits: int) -> int:
...     mask = 2 ** (num_bits - 1)
...     return -(value & mask) + (value & ~mask)

>>> np.binary_repr(0, 8)  # number 0 using 8-bit integer representation
'00000000'
>>>
>>> np.binary_repr(1, 8)  # number 1 using 8-bit integer representation
'00000001'
>>>
>>> np.binary_repr(2, 8)  # number 2 using 8-bit integer representation
'00000010'
>>>
>>> np.binary_repr(3, 8)  # number 3 using 8-bit integer representation
'00000011'
>>>
>>> np.binary_repr(-1, 8)  # number -1 using 8-bit integer representation
'11111111'
>>>
>>> np.binary_repr(-2, 8)  # number -2 using 8-bit integer representation
'11111110'
>>>
>>> np.binary_repr(-3, 8)  # number -3 using 8-bit integer representation
'11111101'


Comparison
----------
>>> data = 69
>>>
>>> np.binary_repr(data, 8)  # np.int8
'01000101'
>>>
>>> np.binary_repr(data, 16)  # np.int16
'0000000001000101'
>>>
>>> np.binary_repr(data, 32)  # np.int32
'00000000000000000000000001000101'
>>>
>>> np.binary_repr(data, 64)  # np.int64
'0000000000000000000000000000000000000000000000000000000001000101'


Signed int
----------
* Signed (positive and negative)
* ``np.int`` alias for ``np.int64``
* ``np.int0`` alias for ``np.int64`` - Integer used for indexing
* ``np.int8``
* ``np.int16``
* ``np.int32``
* ``np.int64``

.. csv-table:: Number of values is calculated with ``2 ** bytes``
    :header: "Type", "Bits", "Number of Values", "Minimal", "Maximal"

    "``np.int8``", "8", "256", "-128", "127"
    "``np.int16``", "16", "65,536", "-32,768", "32,767"
    "``np.int32``", "32", "4,294,967,296", "-2,147,483,648", "2,147,483,646"
    "``np.int64``", "64", "18,446,744,073,709,551,616", "-9,223,372,036,854,775,808", "9,223,372,036,854,775,807"

>>> a = np.array([1, 2, 3])
>>>
>>> type(a)
<class 'numpy.ndarray'>
>>>
>>> a.dtype
dtype('int64')

>>> a = np.array([[1., 2., 3.],
...               [4., 5., 6.]])
>>>
>>> a.astype(int)
array([[1, 2, 3],
       [4, 5, 6]])
>>>
>>> a.astype(np.int8)
array([[1, 2, 3],
       [4, 5, 6]], dtype=int8)
>>>
>>> a.astype(np.int64)
array([[1, 2, 3],
       [4, 5, 6]])


Unsigned int
------------
* Unsigned (non-negative only)
* ``np.uint0``
* ``np.uint8``
* ``np.uint16``
* ``np.uint32``
* ``np.uint64``

.. csv-table:: Number of values is calculated with ``2 ** bytes``
    :header: "Type", "Bits", "Number of Values", "Minimal", "Maximal"

    "``np.uint8``", "8", "256", "0", "255"
    "``np.uint16``", "16", "65,536", "0", "65,535"
    "``np.uint32``", "32", "4,294,967,296", "0", "4,294,967,295"
    "``np.uint64``", "64", "18,446,744,073,709,551,616", "0", "18,446,744,073,709,551,615"

>>> a = np.array([-1, 0, 1])
>>>
>>> type(a)
<class 'numpy.ndarray'>
>>>
>>> a.dtype
dtype('int64')

>>> a = np.array([-1, 0, 1])
>>>
>>> a.astype(int)
array([-1,  0,  1])
>>>
>>> a.astype(np.uint8)
array([255,   0,   1], dtype=uint8)
>>>
>>> a.astype(np.uint64)  # doctest: +NORMALIZE_WHITESPACE
array([18446744073709551615, 0, 1], dtype=uint64)


float
-----
* ``np.float``
* ``np.float16``
* ``np.float32``
* ``np.float64``
* ``np.float128``

.. csv-table:: Number of values is calculated with ``2 ** bytes``
    :header: "Type", "Bits", "Minimal", "Maximal"

    "``np.float16``", "16", "-65,504", "65,504"
    "``np.float32``", "32", "±0.000000×10−95", "±9.999999×1096"
    "``np.float64``", "64", "±0.000000000000000×10−383", "±9.999999999999999×10384"
    "``np.float128``", "64", "±0.000000000000000000000000000000000×10−6143", "±9.999999999999999999999999999999999×106144"

>>> a = np.array([1., 2., 3.])
>>>
>>> type(a)
<class 'numpy.ndarray'>
>>>
>>> a.dtype
dtype('float64')

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a.astype(float)
array([[1., 2., 3.],
       [4., 5., 6.]])
>>>
>>> a.astype(np.float16)
array([[1., 2., 3.],
       [4., 5., 6.]], dtype=float16)
>>>
>>> a.astype(np.float32)
array([[1., 2., 3.],
       [4., 5., 6.]], dtype=float32)
>>>
>>> a.astype(np.float64)
array([[1., 2., 3.],
       [4., 5., 6.]])
>>>
>>> a.astype(np.float128)
array([[1., 2., 3.],
       [4., 5., 6.]], dtype=float128)


complex
-------
* ``np.complex``
* ``np.complex64``
* ``np.complex128``
* ``np.complex256``

>>> a = np.array([1+2j])
>>>
>>> a.dtype
dtype('complex128')

>>> a = np.array([1.1+2.2j])
>>>
>>> a.dtype
dtype('complex128')


bool
----
>>> a = np.array([True, False, True])
>>>
>>> a.dtype
dtype('bool')

>>> a = np.array([1, 0, 1], bool)
>>>
>>> a.dtype
dtype('bool')
>>>
>>> a
array([ True, False,  True])


str
---
>>> np.array(['a', 'b', 'c'])
array(['a', 'b', 'c'], dtype='<U1')
>>>
>>> np.array(['one', 'two', 'three'])
array(['one', 'two', 'three'], dtype='<U5')


Comparison
----------
>>> a = np.array([[1, 2, 3],
...              [4, 5, 6],
...              [7, 8, 9]], dtype='int8')
>>> a.itemsize
1
>>> a.size
9
>>> a.nbytes
9

>>> b = np.array([[1, 2, 3],
...              [4, 5, 6],
...              [7, 8, 9]], dtype='int32')
>>> b.itemsize
4
>>> b.size
9
>>> b.nbytes
36

>>> c = np.array([[1, 2, 3],
...              [4, 5, 6],
...              [7, 8, 9]], dtype='int64')
>>> c.itemsize
8
>>> c.size
9
>>> c.nbytes
72


NBytes
------
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
...
>>> a.astype('int8').nbytes
9
>>>
>>> a.astype('int16').nbytes
18
>>>
>>> a.astype('int32').nbytes
36
>>>
>>> a.astype('int64').nbytes
72


Iinfo
-----
* For ``int``s only

>>> np.iinfo('int')
iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)
>>>
>>> np.iinfo('int8')
iinfo(min=-128, max=127, dtype=int8)
>>>
>>> np.iinfo('int16')
iinfo(min=-32768, max=32767, dtype=int16)
>>>
>>> np.iinfo('int32')
iinfo(min=-2147483648, max=2147483647, dtype=int32)
>>>
>>> np.iinfo('int64')
iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)
>>>
>>> np.iinfo('int0')
iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)


Finfo
-----
* For ``float``s only

>>> np.finfo('float16')
finfo(resolution=0.001, min=-6.55040e+04, max=6.55040e+04, dtype=float16)
>>>
>>> np.finfo('float32')
finfo(resolution=1e-06, min=-3.4028235e+38, max=3.4028235e+38, dtype=float32)
>>>
>>> np.finfo('float64')
finfo(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64)


Assignments
-----------
.. literalinclude:: assignments/numpy_dtype_a.py
    :caption: :download:`Solution <assignments/numpy_dtype_a.py>`
    :end-before: # Solution
