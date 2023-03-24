Numeric Float
=============
* Represents floating point number (vide IEEE-754)
* Could be both signed and unsigned
* Default ``float`` size is 64 bit
* Python automatically extends ``float`` when need bigger number

>>> data = 1.337
>>> data = +1.337
>>> data = -1.337

Floating-point numbers are not real numbers, so the result of ``1.0/3.0``
cannot be represented exactly without infinite precision. In the decimal
(base 10) number system, one-third is a repeating fraction, so it has an
infinite number of digits. Even simple non-repeating decimal numbers can
be a problem. One-tenth (0.1) is obviously non-repeating, so we can express
it exactly with a finite number of digits. As it turns out, since numbers
within computers are stored in binary (base 2) form, even one-tenth cannot
be represented exactly with floating-point numbers,

When should you use integers and when should you use floating-point numbers?
A good rule of thumb is this: use integers to count things and use
floating-point numbers for quantities obtained from a measuring device.
As examples, we can measure length with a ruler or a laser range finder;
we can measure volume with a graduated cylinder or a flow meter; we can
measure mass with a spring scale or triple-beam balance. In all of these
cases, the accuracy of the measured quantity is limited by the accuracy
of the measuring device and the competence of the person or system
performing the measurement. Environmental factors such as temperature
or air density can affect some measurements. In general, the degree
of inexactness of such measured quantities is far greater than that
of the floating-point values that represent them.

Despite their inexactness, floating-point numbers are used every day
throughout the world to solve sophisticated scientific and engineering
problems. The limitations of floating-point numbers are unavoidable since
values with infinite characteristics cannot be represented in a finite way.
Floating-point numbers provide a good trade-off of precision for practicality.

.. note:: Source [#Halterman2018]_


Without Zero Notation
---------------------
* ``.44`` - notation without leading zero
* ``69.`` - notation without trailing zero
* Used by ``numpy``

Leading zero:

>>> data = .44
>>> print(data)
0.44

Trailing zero:

>>> data = 69.
>>> print(data)
69.0


Engineering Notation
--------------------
* The exponential is a number divisible by 3
* Allows the numbers to explicitly match their corresponding SI prefixes
* The E (or e) should not be confused with the exponential ``e`` which holds
  a completely different significance

.. csv-table:: Engineering notation
    :header: "Name", "Symbol", "Base", "Value"

    "yotta", "Y", "1e24",  "1000000000000000000000000.0"
    "zetta", "Z", "1e21",  "1000000000000000000000.0"
    "exa",   "E", "1e18",  "1000000000000000000.0"
    "peta",  "P", "1e15",  "1000000000000000.0"
    "tera",  "T", "1e12",  "1000000000000.0"
    "giga",  "G", "1e9",   "1000000000.0"
    "mega",  "M", "1e6",   "1000000.0"
    "kilo",  "k", "1e3",   "1000.0"
    "",      "",  "1e0",   "1.0"
    "milli", "m", "1e−3",  "0.001.0"
    "micro", "μ", "1e−6",  "0.000001.0"
    "nano",  "n", "1e−9",  "0.000000001.0"
    "pico",  "p", "1e−12", "0.000000000001.0"
    "femto", "f", "1e−15", "0.000000000000001.0"
    "atto",  "a", "1e−18", "0.000000000000000001.0"
    "zepto", "z", "1e−21", "0.000000000000000000001.0"
    "yocto", "y", "1e−24", "0.000000000000000000000001.0"

>>> x = 1e6
>>> print(x)
1000000.0
>>>
>>> x = 1E6
>>> print(x)
1000000.0

>>> x = +1e6
>>> print(x)
1000000.0
>>>
>>> x = -1e6
>>> print(x)
-1000000.0

>>> x = 1e-3
>>> print(x)
0.001
>>>
>>> x = 1e-6
>>> print(x)
1e-06


Scientific notation
-------------------
* The E (or e) should not be confused with the exponential ``e`` which holds
  a completely different significance

>>> 1e1
10.0
>>>
>>> 1e2
100.0
>>>
>>> 1e3
1000.0

>>> 1e-3
0.001
>>>
>>> 1e-4
0.0001
>>>
>>> 1e-5
1e-05
>>>
>>> 1e-6
1e-06

>>> 1e3
1000.0
>>>
>>> -1e3
-1000.0
>>>
>>> 1e-3
0.001
>>>
>>> -1e-3
-0.001

>>> 1.337 * 1e3
1337.0
>>>
>>> 1.337 * 1e-3
0.001337


Type Casting
------------
Builtin function ``float()`` converts argument to ``float``

>>> float(1)
1.0
>>>
>>> float(+1)
1.0
>>>
>>> float(-1)
-1.0

>>> float(1.337)
1.337
>>>
>>> float(+1.337)
1.337
>>>
>>> float(-1.337)
-1.337

>>> float('1.337')
1.337
>>>
>>> float('+1.337')
1.337
>>>
>>> float('-1.337')
-1.337

>>> float('1,337')
Traceback (most recent call last):
ValueError: could not convert string to float: '1,337'

>>> float('+1,337')
Traceback (most recent call last):
ValueError: could not convert string to float: '+1,337'

>>> float('-1,337')
Traceback (most recent call last):
ValueError: could not convert string to float: '-1,337'


Round Number
------------
Rounding a number

>>> pi = 3.14159265359
>>>
>>>
>>> round(pi, 4)
3.1416
>>>
>>> round(pi, 2)
3.14
>>>
>>> round(pi)
3
>>>
>>> round(pi, 0)
3.0

Rounding a number in string formatting

>>> pi = 3.14159265359
>>>
>>>
>>> print(f'Pi number is {pi}')
Pi number is 3.14159265359
>>>
>>> print(f'Pi number is {pi:f}')
Pi number is 3.141593
>>>
>>> print(f'Pi number is {pi:.4f}')
Pi number is 3.1416
>>>
>>> print(f'Pi number is {pi:.2f}')
Pi number is 3.14
>>>
>>> print(f'Pi number is {pi:.0f}')
Pi number is 3

>>> round(10.5)
10
>>>
>>> round(10.51)
11


Type Checking
-------------
>>> x = 1.2
>>>
>>> type(x)
<class 'float'>
>>>
>>> x = 1.2
>>> type(x) is float
True
>>>
>>> type(x) in (int, float)
True

>>> x = 1.2
>>>
>>> isinstance(x, float)
True
>>>
>>> isinstance(x, (int,float))
True
>>>
>>> isinstance(x, int|float)  # since 3.10
True


Built-in Functions
------------------
Builtin function ``pow()`` raises number to the ``n-th`` power.
Note, that arithmetic operator ``**`` also raises number to the power:

>>> pow(10, 2)
100
>>>
>>> pow(2, -1)
0.5

>>> pow(1.337, 3)
2.389979753
>>>
>>> pow(4, 0.5)
2.0
>>>
>>> pow(2, 0.5)
1.4142135623730951

Builtin function ``pow()`` can be used to calculate roots of a number:

>>> pow(4, 1/2)
2.0
>>>
>>> pow(2, 1/2)
1.4142135623730951
>>>
>>> pow(27, 1/3)
3.0

>>> pow(4, -1/2)
0.5
>>>
>>> pow(2, -1/2)
0.7071067811865476
>>>
>>> pow(27, -1/3)
0.33333333333333337

>>> pow(-2, -1)
-0.5
>>>
>>> pow(-4, -1)
-0.25

Builtin function ``pow()`` can return ``complex`` numbers.
Note that Python has special ``complex()`` numeric type.

>>> pow(-2, -1/2)
(4.329780281177467e-17-0.7071067811865476j)
>>>
>>> pow(-2, 1/2)
(8.659560562354934e-17+1.4142135623730951j)
>>>
>>> pow(-4, -1/2)
(3.061616997868383e-17-0.5j)
>>>
>>> pow(-4, 1/2)
(1.2246467991473532e-16+2j)

Absolute value

>>> abs(1)
1
>>>
>>> abs(1.337)
1.337

>>> abs(-1)
1
>>>
>>> abs(-1.337)
1.337


References
----------
.. [#Halterman2018] Halterman, R.L. Fundamentals of Python Programming. Publisher: Southern Adventist University. Year: 2018.


Assignments
-----------
.. literalinclude:: assignments/type_float_a.py
    :caption: :download:`Solution <assignments/type_float_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_b.py
    :caption: :download:`Solution <assignments/type_float_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_c.py
    :caption: :download:`Solution <assignments/type_float_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_d.py
    :caption: :download:`Solution <assignments/type_float_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_e.py
    :caption: :download:`Solution <assignments/type_float_e.py>`
    :end-before: # Solution


Homework
--------
.. literalinclude:: assignments/type_float_f.py
    :caption: :download:`Solution <assignments/type_float_f.py>`
    :end-before: # Solution

.. figure:: img/spacesuits.png

    EMU and Orlan

.. literalinclude:: assignments/type_float_g.py
    :caption: :download:`Solution <assignments/type_float_g.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_h.py
    :caption: :download:`Solution <assignments/type_float_h.py>`
    :end-before: # Solution

.. todo:: assignments with average calculation mean(iris)
.. todo:: assignments with currency conversion
.. todo:: assignments with temperature conversion
.. todo:: assignments with isinstance() and type()
.. todo:: assignments with round()
.. todo:: assignments with pow()
.. todo:: assignments with abs()
