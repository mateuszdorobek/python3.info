Boolean Operator
================


Equals
------
* ``==`` - ``eq`` (equals)

Comparing ``str``:

>>> 'Monty Python' == 'Python'
False
>>> 'Python' == 'Python'
True
>>> 'python' == 'Python'
False

Comparing ``tuple``:

>>> (1, 2) == (1, 2)
True
>>> (1, 2) == (2, 1)
False

Comparing ``list``:

>>> [1, 2] == [1, 2]
True
>>> [1, 2] == [2, 1]
False

Comparing ``set``:

>>> {1, 2} == {1, 2}
True
>>> {1, 2} == {2, 1}
True

Comparing types and values:

>>> (1,2) == [1,2]
False
>>> (1,2) == {1,2}
False
>>> 1,2 == {1,2}
(1, False)


Not-Equals
----------
* ``!=`` - ``ne`` (not-equals)

Comparing ``str``:

>>> 'Monty Python' != 'Python'
True
>>> 'Python' != 'Python'
False
>>> 'python' != 'Python'
True

Comparing ``tuple``:

>>> (1, 2, 3) != (1, 2)
True

Comparing ``list``:

>>> [1, 2, 3] != [1, 2]
True

Comparing ``set``:

>>> {1, 2, 3} != {1, 2}
True


Greater Than
------------
* ``>`` - ``gt`` (greater than)
* Set uses ``>`` for ``set.issuperset()``

>>> 'a' > 'b'
False
>>> 'b' > 'a'
True

>>> 'abc' > 'ab'
True
>>> 'abc' > 'abc'
False
>>> 'abc' > 'abcd'
False

>>> 'def' > 'abc'
True
>>> 'abc' > 'xy'
False
>>> 'abc' > 'self'
False

>>> (3, 12) > (3, 11)
True
>>> (3, 11, 0) > (3, 10, 8)
True
>>> (3, 8) > (3, 9)
False

>>> (2, 7) > (3, 11)
False
>>> (3, 11) > (2, 7)
True

>>> [3, 12] > [3, 11]
True
>>> [3, 11, 0] > [3, 10, 8]
True
>>> [3, 8] > [3, 9]
False

>>> [2, 7] > [3, 11]
False
>>> [3, 11] > [2, 7]
True


Problems
--------
>>> 1, 2 == (1, 2)
(1, False)
>>> 1
1
>>> 2 == (1, 2)
False
>>> 1,     2==(1,2)
(1, False)

>>> (1, 2) == 1, 2
(False, 2)


Examples
--------
>>> import sys
>>>
>>>
>>> print(sys.version_info)  # doctest: +SKIP
sys.version_info(major=3, minor=11, micro=0, releaselevel='final', serial=0)
>>>
>>>
>>> sys.version_info >= (3, 11)
True
>>>
>>> sys.version_info >= (3, 12)
True
>>>
>>> sys.version_info >= (3, 13)
False
>>>
>>> sys.version_info >= (3, 11, 0)
True
>>>
>>> sys.version_info >= (3, 12, 0)
True
>>>
>>> sys.version_info >= (3, 13, 0)
False

>>> '3.8.0' > '3.9.0'
False
>>> '3.9.0' > '3.10.0'
True
>>> '3.09.0' > '3.10.0'
False

>>> myversion = '3.9.0'
>>> required = '3.8.0'
>>>
>>> myversion >= required
True

>>> myversion = '3.10.0'
>>> required = '3.8.0'
>>>
>>> myversion >= required
False

>>> myversion = '3.9.0'.split('.')
>>> required = '3.8.0'.split('.')
>>>
>>> myversion >= required
True


Operator Precedence
-------------------
* Precedence - when an expression contains two different kinds of operators,which should be applied first?
* Associativity - when an expression contains two operators with the same precedence, which should be applied first?

Precedence:

>>> 1 + 2 * 3
7

Associativity:

>>> 1 + 2 - 3
0

.. csv-table:: Operator precedence
    :widths: 25, 75
    :header: "Operator", "Description"

    "``yield x``, ``yield from x``",                                                         "Yield expression"
    "``lambda``",                                                                            "Lambda expression"
    "``if``, ``elif``, ``else``",                                                            "Conditional expression"
    "``or``",                                                                                "Boolean OR"
    "``and``",                                                                               "Boolean AND"
    "``not x``",                                                                             "Boolean NOT"
    "``in``, not in``, ``is``, ``is not``, ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``",    "Comparisons, including membership tests and identity tests"
    "``|``",                                                                                 "Bitwise OR"
    "``^``",                                                                                 "Bitwise XOR"
    "``&``",                                                                                 "Bitwise AND"
    "``<<``, ``>>``",                                                                        "Shifts"
    "``+``, ``-``",                                                                          "Addition and subtraction"
    "``*``, ``@``, ``/``, ``//``, ``%``",                                                    "Multiplication, matrix multiplication, division, remainder"
    "``+x``, ``-x``, ``~x``",                                                                "Positive, negative, bitwise NOT"
    "``**``",                                                                                "Exponentiation"
    "``await x``",                                                                           "Await expression"
    "``x[index]``, ``x[index:index]``, ``x(arguments...)``, ``x.attribute``",                "Subscription, slicing, call, attribute reference"
    "``(expressions...)``, ``[expressions...]``, ``{key: value...}``, ``{expressions...}``", "Binding or tuple display, list display, dictionary display, set display"


To If or not to If
------------------
>>> number = 10
>>>
>>> if number % 2 == 0:
...     is_even = True
... else:
...     is_even = False
>>>
>>> print(is_even)
True

>>> number = 10
>>> is_even = True if number % 2 == 0 else False
>>>
>>> print(is_even)
True

>>> number = 10
>>> is_even = number % 2 == 0
>>>
>>> print(is_even)
True

>>> number = 10
>>> is_even = (number % 2 == 0)
>>>
>>> print(is_even)
True


Assignments
-----------
.. literalinclude:: assignments/conditional_operator_a.py
    :caption: :download:`Solution <assignments/conditional_operator_a.py>`
    :end-before: # Solution
