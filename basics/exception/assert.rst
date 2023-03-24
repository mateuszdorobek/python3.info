Exception Assertion
===================
* Raises ``AssertionError`` if argument is ``False``
* Can have optional message
* Running Python with the ``-O`` optimization flag disables assert statements

>>> admins = ['mwatney', 'mlewis', 'rmartinez']
>>>
>>> assert 'avogel' in admins, 'You must be an admin to edit this page'
Traceback (most recent call last):
AssertionError: You must be an admin to edit this page


Assert Keyword
--------------
Note the output of the following statements:

>>> data = [1, 2, 3]
>>>
>>> 1 in data
True
>>> 4 in data
False

In both examples from above, the output is visible. We can intercept it to the
variable, but we need to define it and store those values.

In the next example ``assert`` keywords allows to proceed with execution,
if only the assertion is ``True``.

>>> data = [1, 2, 3]
>>>
>>> assert 1 in data
>>>
>>> assert 4 in data
Traceback (most recent call last):
AssertionError

If the assertion is ``True`` (value ``1`` in a member of ``data``) nothing
will happen. However if there is an error (value ``4`` is not a member of
``data``), then the exception (``AssertionError``) is raised.

Assertions can have additional information, which can help with debugging:

>>> data = [1, 2, 3]
>>>
>>> assert 4 in data, '4 must be in data'
Traceback (most recent call last):
AssertionError: 4 must be in data


Sequence Assertion
------------------
>>> data = [1, 2, 3]
>>>
>>> assert type(data) is list
>>> assert all(type(x) is int for x in data)


Use Case - 0x01
---------------
You can use assertions to check Python version.

>>> import sys
>>>
>>> assert sys.version_info >= (3, 11)
>>> assert sys.version_info >= (3, 11), 'Python 3.11+ required'


Assignments
-----------
.. literalinclude:: assignments/exception_assert_a.py
    :caption: :download:`Solution <assignments/exception_assert_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/exception_assert_b.py
    :caption: :download:`Solution <assignments/exception_assert_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/exception_assert_c.py
    :caption: :download:`Solution <assignments/exception_assert_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/exception_assert_d.py
    :caption: :download:`Solution <assignments/exception_assert_d.py>`
    :end-before: # Solution
