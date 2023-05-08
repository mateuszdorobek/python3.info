Functional Pure Functions
=========================
* Pure functions have no side effects (i.e. memory, state, I/O)
* Calling the pure function again with the same arguments returns the same result (this can enable caching optimizations such as memoization)
* If the result of a pure expression is not used, it can be removed without affecting other expressions
* If there is no data dependency between two pure expressions, their order can be reversed, or they can be performed in parallel and they cannot interfere with one another (the evaluation of any pure expression is thread-safe) [#WikipediaFunc]_

Pure functions have two important properties [#Inouye2022]_:

* They always produce the same output with the same arguments irrespective of other factors. This property is also known as immutability.
* They are deterministic. Pure functions either give some output or modify any argument or global variables i.e. they have no side effects.

Because pure functions have no side effects or hidden I/O, programs built using functional paradigms are easy to debug. Moreover, pure functions make writing concurrent applications easier.

When the code is written using the functional programming style, a capable compiler is able to:

* Memorize the results
* Parallelize the instructions
* Wait for evaluating results


>>> def add(a, b):
...     return a + b


Pure Function
-------------
>>> def add(a, b):
...     return a + b
>>>
>>>
>>> add(1, 2)
3
>>> add(1, 2)
3
>>> add(1, 2)
3


Impure Function
---------------
>>> def add(a, b):
...     return a + b + c
>>>
>>>
>>> c = 0
>>>
>>> add(1, 2)
3
>>> add(1, 2)
3
>>> add(1, 2)
3
>>>
>>>
>>> c = 1
>>>
>>> add(1, 2)
4
>>> add(1, 2)
4
>>> add(1, 2)
4


Impure to Pure Function
-----------------------
>>> def add(a, b, c):
...     return a + b + c
>>>
>>>
>>> c = 0
>>>
>>> add(1, 2, c)
3
>>> add(1, 2, c)
3
>>> add(1, 2, c)
3
>>>
>>>
>>> c = 1
>>>
>>> add(1, 2, c)
4
>>> add(1, 2, c)
4
>>> add(1, 2, c)
4


Side Effects
------------
* I/O - Input Output
* Looks like a pure function
* File content can change by other process

>>> def read(filename):
...     with open(filename) as file:
...         return file.read()

Each of those variables can have different value as of the ``read()`` function
depends on file content, which can be modified by other process in the
meantime between reading ``a`` and reading ``b``.

>>> a = read('myfile.txt')  # doctest: +SKIP
>>> b = read('myfile.txt')  # doctest: +SKIP



Use Case - 0x01
---------------
* Math Functions
* Mathematical functions are pure in general

>>> def add(a, b):
...     return a + b

>>> def odd(x):
...     return x % 2

>>> def cube(x):
...     return x ** 3


Use Case - 0x01
---------------
* Select

Pure:

>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> def function(data, species):
...     result = []
...     for *features, label in data:
...         if label == species:
...             result.append(features)
...     return result

Impure:

>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> def function(species):
...     result = []
...     for *features, label in DATA:
...         if label == species:
...             result.append(features)
...     return result


References
----------
.. [#WikipediaFunc] Functional programming. Retrieved: 2020-10-09. URL: https://en.wikipedia.org/wiki/Functional_programming

.. [#Inouye2022] Inouye, Jenna. "Functional Programming Languages: Concepts & Advantages". Year: 2022. Retrieved: 2022-07-28, URL: https://hackr.io/blog/functional-programming
