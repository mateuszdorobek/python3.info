Test Doctest
============
* Tests are always the most up-to-date code documentation
* Tests cannot get out of sync from code
* Checks if function output is exactly as expected
* Useful for regex modifications
* Can add text (i.e. explanations) between tests

Use Cases:

    * https://github.com/scikit-learn/scikit-learn/blob/3bca0412c10b89bb474bcf2f38442e2b1f36e6f4/sklearn/linear_model/_base.py#L465
    * https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L434


Docstring
---------
* Docstring is a first multiline comment in: File/Module, Class, Method/Function
* Used for generating ``help()`` documentation
* It is accessible in ``__doc__`` property of an object
* Used for ``doctest``
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters
* More information in `Function Doctest`

Docstring used for documentation:

>>> def say_hello():
...     """This is the say_hello function"""
...     print('Hello')
>>>
>>>
>>> # doctest: +SKIP
... help(say_hello)
Help on function say_hello in module __main__:
<BLANKLINE>
say_hello()
    This is the say_hello function
>>>
>>> print(say_hello.__doc__)
This is the say_hello function

Docstring used for documentation:

>>> def say_hello():
...     """
...     This is the say_hello function
...     And the description is longer then one line
...     """
...     print('Hello')
>>>
>>>
>>> help(say_hello)  # doctest: +SKIP
Help on function say_hello in module __main__:
<BLANKLINE>
say_hello()
    This is the say_hello function
    And the description is longer then one line
>>>
>>> print(say_hello.__doc__)
<BLANKLINE>
    This is the say_hello function
    And the description is longer then one line
<BLANKLINE>


Syntax
------
* Docstring is a first multiline comment in: File/Module, Class, Method/Function
* Used for generating ``help()`` documentation
* It is accessible in ``__doc__`` property of an object
* Used for ``doctest``
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters

>>> def add(a, b):
...     """
...     >>> add(1, 2)
...     3
...     >>> add(-1, 1)
...     0
...     >>> add(0, 0)
...     0
...     """
...     return a + b

>>> # doctest: +SKIP
... """
... >>> add(1, 2)
... 3
... >>> add(-1, 1)
... 0
... >>> add(0, 0)
... 0
... """
>>>
>>> def add(a, b):
...     return a + b


Running Tests
-------------
Running tests in Pycharm IDE (either option):

    * Right click on source code with doctests -> Run 'Doctest for ...'
    * View menu -> Run... -> Doctest in ``myfunction``
    * Note, that doctests are not discovered in scratch files in PyCharm

Running Tests from Python Code:

>>> if __name__ == "__main__":
...     from doctest import testmod
...     testmod()  # doctest: +SKIP

Running tests from command line (displays errors only):

.. code-block:: console

    $ python -m doctest myfile.py

Add ``-v`` to display more verbose output.

.. code-block:: console

    $ python -m doctest -v myfile.py


Test Int, Float
---------------
``int`` values:

    >>> # doctest: +SKIP
    ... """
    ... >>> add(1, 2)
    ... 3
    ... >>> add(-1, 1)
    ... 0
    ... >>> add(0, 0)
    ... 0
    ... """
    >>>
    >>> def add(a, b):
    ...     return a + b

``float`` values:

    >>> # doctest: +SKIP
    ... """
    ... >>> add(1.0, 2.0)
    ... 3.0
    ...
    ... >>> add(0.1, 0.2)
    ... 0.30000000000000004
    ...
    ... >>> add(0.1, 0.2)   # doctest: +ELLIPSIS
    ... 0.3000...
    ... """
    >>>
    >>> def add(a, b):
    ...     return a + b

This is due to the floating point arithmetic in IEEE 754 standard:

    >>> 0.1 + 0.2
    0.30000000000000004

    >>> 0.1 + 0.2  # doctest: +ELLIPSIS
    0.3000...

    >>> round(0.1+0.2, 16)
    0.3

    >>> round(0.1+0.2, 17)
    0.30000000000000004

More information in `Math Precision`


Test Bool
---------
    >>> # doctest: +SKIP
    ... """
    ... Function checks if person is adult.
    ... Adult person is over 18 years old.
    ...
    ... >>> is_adult(18)
    ... True
    ...
    ... >>> is_adult(17.9)
    ... False
    ... """
    >>>
    >>> AGE_ADULT = 18
    >>>
    >>> def is_adult(age):
    ...     if age >= AGE_ADULT:
    ...         return True
    ...     else:
    ...         return False


Test Str
--------
* Python will change to single quotes in most cases
* Python will change to double quotes to avoid escapes
* ``print()`` function output, don't have quotes

Returning ``str``. Python will change to single quotes in most cases:

    >>> # doctest: +SKIP
    ... """
    ... >>> echo('hello')
    ... 'hello'
    ...
    ... # Python will change to single quotes in most cases
    ... >>> echo("hello")
    ... 'hello'
    ...
    ... Following test will fail
    ... >>> echo('hello')
    ... "hello"
    ...
    ... Python will change to double quotes to avoid escapes
    ... >>> echo('It\\'s Twardowski\\'s Moon')
    ... "It's Twardowski's Moon"
    ... """
    >>>
    >>> def echo(data):
    ...     return data

There are no quotes in ``print()`` function output:

    >>> # doctest: +SKIP
    ... """
    ... >>> echo('hello')
    ... hello
    ... """
    >>>
    >>> def echo(data):
    ...     print(data)

Testing ``print(str)`` with newlines:

    >>> # doctest: +SKIP
    ... """
    ... >>> echo('hello')
    ... hello
    ... hello
    ... hello
    ... <BLANKLINE>
    ... """
    >>>
    >>> def echo(data):
    ...     print(f'{data}\n' * 3)


Test Ordered Sequence
---------------------
    >>> # doctest: +SKIP
    ... """
    ... >>> echo([1,2,3])
    ... [1, 2, 3]
    ...
    ... >>> echo((1,2,3))
    ... (1, 2, 3)
    ... """
    >>>
    >>> def echo(data):
    ...     return data

    >>> # doctest: +SKIP
    ... """
    ... >>> echo([1,2,3])
    ... [1, 2, 3]
    ...
    ... >>> echo((1,2,3))
    ... [1, 2, 3]
    ... """
    >>>
    >>> def echo(data):
    ...     return [x for x in data]

    >>> # doctest: +SKIP
    ... """
    ... >>> echo([1,2,3])
    ... [274.15, 275.15, 276.15]
    ...
    ... >>> echo((1,2,3))
    ... (274.15, 275.15, 276.15)
    ... """
    >>>
    >>> def echo(data):
    ...     cls = type(data)
    ...     return cls(x+273.15 for x in data)


Test Unordered Sequence
-----------------------
Hash from numbers are constant:

    >>> # doctest: +SKIP
    ... """
    ... >>> echo({1})
    ... {1}
    ... >>> echo({1,2})
    ... {1, 2}
    ... """
    >>>
    >>> def echo(data):
    ...     return data

However hash from `str` elements changes at every run:

    >>> # doctest: +SKIP
    ... """
    ... >>> echo({'a', 'b'})
    ... {'b', 'a'}
    ... """
    >>>
    >>> def echo(data):
    ...     return data

Therefore you should test if element is in the result, rather than comparing output:

    >>> # doctest: +SKIP
    ... """
    ... >>> result = echo({'a', 'b'})
    ... >>> 'a' in result
    ... True
    ... >>> 'b' in result
    ... True
    ... """
    >>>
    >>> def echo(data):
    ...     return data


Test Mapping
------------
    >>> # doctest: +SKIP
    ... """
    ... >>> result = echo({'a': 1, 'b': 2})
    ... >>> result
    ... {'a': 1, 'b': 2}
    ... >>> 'a' in result.keys()
    ... True
    ... >>> 1 in result.values()
    ... True
    ... >>> ('a', 1) in result.items()
    ... True
    ... >>> result['a']
    ... 1
    ... """
    >>>
    >>> def echo(data):
    ...     return data


Test Nested
-----------
    >>> # doctest: +SKIP
    ... """
    ... >>> DATA = [
    ... ...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    ... ...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
    ... ...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
    ... ...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ... ...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ... ...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    ... ...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
    ...
    ... >>> echo(DATA)
    ... [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'), (5.8, 2.7, 5.1, 1.9, 'virginica'), (5.1, 3.5, 1.4, 0.2, 'setosa'), (5.7, 2.8, 4.1, 1.3, 'versicolor'), (6.3, 2.9, 5.6, 1.8, 'virginica'), (6.4, 3.2, 4.5, 1.5, 'versicolor'), (4.7, 3.2, 1.3, 0.2, 'setosa')]
    ...
    ... >>> echo(DATA)  # doctest: +NORMALIZE_WHITESPACE
    ... [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    ...  (5.8, 2.7, 5.1, 1.9, 'virginica'),
    ...  (5.1, 3.5, 1.4, 0.2, 'setosa'),
    ...  (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ...  (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ...  (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    ...  (4.7, 3.2, 1.3, 0.2, 'setosa')]
    ... """
    >>>
    >>> def echo(data):
    ...     return data


Test Exceptions
---------------
    >>> # doctest: +SKIP
    ... """
    ... >>> echo()
    ... Traceback (most recent call last):
    ... NotImplementedError
    ... """
    >>>
    >>> def echo():
    ...     raise NotImplementedError

    >>> # doctest: +SKIP
    ... """
    ... >>> echo()
    ... Traceback (most recent call last):
    ... NotImplementedError: This will work in future
    ... """
    >>>
    >>> def echo():
    ...     raise NotImplementedError('This will work in future')


Test Type
---------
    >>> # doctest: +SKIP
    ... """
    ... >>> result = echo(1)
    ... >>> type(result)
    ... <class 'int'>
    ...
    ... >>> result = echo(1.1)
    ... >>> type(result)
    ... <class 'float'>
    ...
    ... >>> result = echo(True)
    ... >>> type(result)
    ... <class 'bool'>
    ...
    ... >>> result = echo([1, 2])
    ... >>> type(result)
    ... <class 'list'>
    ...
    ... >>> result = echo([1, 2])
    ... >>> any(type(x) is int
    ... ...     for x in result)
    ... True
    ... """
    >>>
    >>> def echo(data):
    ...     return data


The following doctest will fail:

    >>> # doctest: +SKIP
    ... """
    ... >>> add_numbers('one', 'two')
    ... Traceback (most recent call last):
    ... TypeError: not a number
    ...
    ... >>> add_numbers(True, 1)
    ... Traceback (most recent call last):
    ... ValueError: not a number
    ... """
    >>>
    >>> def add_numbers(a, b):
    ...     if not isinstance(a, (int, float)):
    ...         raise ValueError('c')
    ...     if not isinstance(b, (int, float)):
    ...         raise ValueError('not a number')
    ...     return a + b

Expected exception, got 2.0:

    Expected:
        Traceback (most recent call last):
        ValueError: not a number
    Got:
        2.0

This test will pass:

    >>> # doctest: +SKIP
    ... """
    ... >>> add_numbers('one', 'two')
    ... Traceback (most recent call last):
    ... TypeError: not a number
    ...
    ... >>> add_numbers(True, 1)
    ... Traceback (most recent call last):
    ... ValueError: not a number
    ... """
    >>>
    >>> def add_numbers(a, b):
    ...     if type(a) not in (int, float):
    ...         raise ValueError('not a number')
    ...     if type(b) not in (int, float):
    ...         raise ValueError('not a number')
    ...     return a + b


Test Python Expressions
-----------------------
Using python statements in ``doctest``:

    >>> def echo(text):
    ...     """
    ...     >>> name = 'Mark Watney'
    ...     >>> print(name)
    ...     Mark Watney
    ...     """
    ...     return text

    >>> def when(date):
    ...     """
    ...     >>> from datetime import datetime, timezone
    ...     >>> moon = datetime(1969, 7, 21, 17, 54, tzinfo=timezone.utc)
    ...     >>> when(moon)
    ...     1969-07-21 17:54 UTC
    ...     """
    ...     print(f'{date:%Y-%m-%d %H:%M %Z}')

Flags
-----
* ``DONT_ACCEPT_TRUE_FOR_1``
* ``DONT_ACCEPT_BLANKLINE``
* ``NORMALIZE_WHITESPACE``
* ``ELLIPSIS``
* ``IGNORE_EXCEPTION_DETAIL``
* ``SKIP``
* ``COMPARISON_FLAGS``
* ``REPORT_UDIFF``
* ``REPORT_CDIFF``
* ``REPORT_NDIFF``
* ``REPORT_ONLY_FIRST_FAILURE``
* ``FAIL_FAST``
* ``REPORTING_FLAGS``


Case Studies
------------
Docstring used for doctest:

    >>> def apollo_dsky(noun, verb):
    ...     """
    ...     This is the Apollo Display Keyboard
    ...     It takes noun and verb
    ...
    ...     >>> apollo_dsky(6, 61)
    ...     Program selected. Noun: 06, verb: 61
    ...
    ...     >>> apollo_dsky(16, 68)
    ...     Program selected. Noun: 16, verb: 68
    ...     """
    ...     print(f'Program selected. Noun: {noun:02}, verb: {verb:02}')

Celsius to Kelvin conversion:

    >>> def celsius_to_kelvin(data):
    ...     """
    ...     >>> celsius_to_kelvin([1,2,3])
    ...     [274.15, 275.15, 276.15]
    ...
    ...     >>> celsius_to_kelvin((1,2,3))
    ...     [274.15, 275.15, 276.15]
    ...     """
    ...     return [x+273.15 for x in data]

    >>> def celsius_to_kelvin(data):
    ...     """
    ...     >>> celsius_to_kelvin([1,2,3])
    ...     [274.15, 275.15, 276.15]
    ...
    ...     >>> celsius_to_kelvin((1,2,3))
    ...     (274.15, 275.15, 276.15)
    ...     """
    ...     cls = type(data)
    ...     return cls(x+273.15 for x in data)


Adding two numbers:

    >>> def add_numbers(a, b):
    ...     """
    ...     >>> add_numbers(1, 2)
    ...     3.0
    ...     >>> add_numbers(-1, 1)
    ...     0.0
    ...     >>> add_numbers(0.1, 0.2)  # doctest: +ELLIPSIS
    ...     0.3000...
    ...     >>> add_numbers(1.5, 2.5)
    ...     4.0
    ...     >>> add_numbers(1, 1.5)
    ...     2.5
    ...     >>> add_numbers([1, 2], 3)
    ...     Traceback (most recent call last):
    ...     ValueError: not a number
    ...
    ...     >>> add_numbers(0, [1, 2])
    ...     Traceback (most recent call last):
    ...     ValueError: not a number
    ...
    ...     >>> add_numbers('one', 'two')
    ...     Traceback (most recent call last):
    ...     ValueError: not a number
    ...
    ...     >>> add_numbers(True, 1)
    ...     Traceback (most recent call last):
    ...     ValueError: not a number
    ...     """
    ...     if type(a) not in (int, float):
    ...         raise ValueError('not a number')
    ...
    ...     if type(b) not in (int, float):
    ...         raise ValueError('not a number')
    ...
    ...     return float(a + b)

Celsius to Kelvin temperature conversion:

    >>> def celsius_to_kelvin(celsius):
    ...     """
    ...     >>> celsius_to_kelvin(0)
    ...     273.15
    ...
    ...     >>> celsius_to_kelvin(1)
    ...     274.15
    ...
    ...     >>> celsius_to_kelvin(-1)
    ...     272.15
    ...
    ...     >>> celsius_to_kelvin(-273.15)
    ...     0.0
    ...
    ...     >>> celsius_to_kelvin(-273.16)
    ...     Traceback (most recent call last):
    ...     ValueError: Negative Kelvin
    ...
    ...     >>> celsius_to_kelvin(-300)
    ...     Traceback (most recent call last):
    ...     ValueError: Negative Kelvin
    ...
    ...     >>> celsius_to_kelvin(True)
    ...     Traceback (most recent call last):
    ...     TypeError: Argument must be: int, float or Sequence[int, float]
    ...
    ...     >>> celsius_to_kelvin([0, 1, 2, 3])
    ...     [273.15, 274.15, 275.15, 276.15]
    ...
    ...     >>> celsius_to_kelvin({0, 1, 2, 3})
    ...     {273.15, 274.15, 275.15, 276.15}
    ...
    ...     >>> celsius_to_kelvin([0, 1, 2, -300])
    ...     Traceback (most recent call last):
    ...     ValueError: Negative Kelvin
    ...
    ...     >>> celsius_to_kelvin([0, 1, [2, 3], 3])
    ...     [273.15, 274.15, [275.15, 276.15], 276.15]
    ...     """
    ...     datatype = type(celsius)
    ...
    ...     if type(celsius) in {list, tuple, set, frozenset}:
    ...         return datatype(celsius_to_kelvin(x) for x in celsius)
    ...
    ...     if datatype not in {int, float}:
    ...         raise TypeError('Argument must be: int, float or Sequence[int, float]')
    ...
    ...     kelvin = celsius + 273.15
    ...
    ...     if kelvin < 0.0:
    ...         raise ValueError('Negative Kelvin')
    ...
    ...     return float(kelvin)


Assignments
-----------
.. literalinclude:: assignments/test_doctest_a.py
    :caption: :download:`Solution <assignments/test_doctest_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/test_doctest_b.py
    :caption: :download:`Solution <assignments/test_doctest_b.py>`
    :end-before: # Solution
