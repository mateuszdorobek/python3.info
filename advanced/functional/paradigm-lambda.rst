Functional Lambda
=================
* Lambda - Anonymous functions
* When function is used once
* When function is short
* You don't need to name it (therefore anonymous)

.. glossary::

    lambda
        Anonymous function

>>> lambda x: x+1  # doctest: +ELLIPSIS
<function <lambda> at 0x...>

Lambda Expressions:

>>> a = lambda x: x+1
>>> b = lambda x,y: x+y

Equivalent functions:

>>> def a(x):
...     return x+1

>>> def b(x,y):
...     return x+y


Syntax
------
.. code-block:: python

    lambda <arguments>: <expression>


Convention
----------
* Usually parameters are named ``x`` and ``y``
* Use shortest code possible
* Do not assign ``lambda`` to variable
* Lambda is anonymous function and it should stay anonymous. Do not name it
* :pep:`8` -- Style Guide for Python Code: "Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier". Lambda is anonymous function and it should stay anonymous. Do not name it.
* Usually there are no spaces in lambda expressions (to make code shorter)

Bad:

>>> square = lambda x: x**2
>>> square(4)
16

Good:

>>> def square(x):
...     return x**2
...
>>> square(4)
16

:pep:`8` -- Style Guide for Python Code: "Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier":


Note to Programmers of Different Languages
------------------------------------------
.. code-block:: java

    query = 'SELECT * FROM users'

    result = database(query).stream()
                            .filter(user -> user.age > 5)
                            .filter(user -> user.firstname == 'Mark')
                            .filter((x,y) -> x + y)
                            .collect(Collectors.toList());


Noop
----
>>> noop = lambda: ...

>>> def request(on_error = lambda: ...):
...     ...


Lambda with Map
---------------
Increment:

>>> data = [1, 2, 3, 4]
>>>
>>> result = map(lambda x: x+1, data)
>>> list(result)
[2, 3, 4, 5]


Lambda with Filter
------------------
Even numbers:

>>> DATA = [1, 2, 3, 4]
>>>
>>> result = filter(lambda x: x%2==0, DATA)
>>> list(result)
[2, 4]


Performance
-----------
>>> %%timeit -r 1000 -n 10_000  # doctest: +SKIP
... def increment(x):
...     return x + 1
... map(increment, range(0,100))
271 ns ± 30.6 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 10_000  # doctest: +SKIP
... map(lambda x: x+1, range(0,100))
262 ns ± 29 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... def increment(x):
...     return x + 1
... list(map(increment, range(0,100)))
7.48 µs ± 608 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... list(map(lambda x: x+1, range(0,100)))
7.36 µs ± 545 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)


Use Case - 0x01
---------------
>>> data = [1, 2, 3, 4]
>>>
>>> result = map(lambda x: x**2, data)
>>> list(result)
[1, 4, 9, 16]


Use Case - 0x02
---------------
>>> PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
...       'ł': 'l', 'ń': 'n', 'ó': 'o',
...       'ś': 's', 'ż': 'z', 'ź': 'z'}
>>>
>>> text = 'zażółć gęślą jaźń'
>>>
>>>
>>> result = map(lambda x: PL.get(x,x), text)
>>> ''.join(result)
'zazolc gesla jazn'


Use Case - 0x03
---------------
>>> people = [
...     {'age': 21, 'name': 'Mark Watney'},
...     {'age': 25, 'name': 'Melissa Lewis'},
...     {'age': 18, 'name': 'Rick Martinez'}]
>>>
>>>
>>> result = filter(lambda x: x['age'] >= 21, people)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'age': 21, 'name': 'Mark Watney'},
 {'age': 25, 'name': 'Melissa Lewis'}]


Use Case - 0x04
---------------
>>> people = [
...     {'is_staff': True, 'name': 'Mark Watney'},
...     {'is_staff': False, 'name': 'Melissa Lewis'},
...     {'is_staff': True, 'name': 'Rick Martinez'}]
>>>
>>>
>>> can_login = filter(lambda x: x['is_staff'], people)
>>> list(can_login)  # doctest: +NORMALIZE_WHITESPACE
[{'is_staff': True, 'name': 'Mark Watney'},
 {'is_staff': True, 'name': 'Rick Martinez'}]


Use Case - 0x05
---------------
>>> users = [
...     'mwatney',
...     'mlewis',
...     'rmartinez',
...     'avogel',
...     'bjohanssen',
...     'cbeck',
... ]
>>>
>>> staff = [
...     'mwatney',
...     'mlewis',
...     'ptwardowski',
...     'jjimenez',
... ]
>>>
>>>
>>> can_login = filter(staff.__contains__, users)
>>> list(can_login)
['mwatney', 'mlewis']


Use Case - 0x06
---------------
>>> from urllib.request import urlopen
>>>
>>> def fetch(url: str,
...           on_success = lambda result: ...,
...           on_error = lambda error: ...,
...           ) -> None:
...     try:
...         result = urlopen(url).read()
...     except Exception as error:
...         return on_error(error)
...     else:
...         return on_success(result)
>>>
>>> # doctest: +SKIP
... fetch(
...     url = 'https://python3.info',
...     on_success = lambda result: print(result),
...     on_error = lambda error: print(error))


Use Case - 0x07
---------------
>>> class Apply:
...     def __init__(self, values):
...         self.values = values
...
...     def filter(self, fn):
...          self.values = filter(fn, self.values)
...          return self
...
...     def map(self, fn):
...         self.values = map(fn, self.values)
...         return self

>>> DATA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> result = (
...     Apply(DATA)
...     .filter(lambda x: x % 2 == 0)
...     .map(lambda x: x ** 2)
...     .map(lambda x: x + 1)
...     .map(lambda x: x + 10)
... )

>>> list(result.values)
[15, 27, 47, 75]


Further Reading
---------------
* https://youtu.be/eis11j_iGMs


Assignments
-----------
.. literalinclude:: assignments/functional_lambda_a.py
    :caption: :download:`Solution <assignments/functional_lambda_a.py>`
    :end-before: # Solution
