Boolean Identity
================
* ``=`` assignment
* ``==`` checks for object equality
* ``is`` checks for object identity
* ``is`` compares ``id()`` output for both objects
* CPython: compares the memory address a object resides in
* Testing strings with ``is`` only works when the strings are interned

Since Python 3.8 - Compiler produces a ``SyntaxWarning`` when identity checks
(``is`` and ``is not``) are used with certain types of literals (e.g. ``str``,
``int``). These can often work by accident in *CPython*, but are not guaranteed
by the language spec. The warning advises users to use equality tests
(``==`` and ``!=``) instead.


Has Value
---------
Has value:

>>> x = 1
>>>
>>> if x:
...     print('Has value')
Has value
>>>
>>> if x is not None:
...     print('Has value')
Has value


Is Empty
--------
>>> x = None
>>>
>>> x is None
True
>>>
>>> x == None
True

Example:

>>> data = None
>>>
>>> if not data:
...     print('Empty')
Empty
>>>
>>> if data is None:
...     print('Empty')
Empty


Is True of False
----------------
* `True` and `False` are singletons
* Comparing identity is faster
* Comparing values will yield the same result

>>> x = False
>>>
>>> x == False
True
>>>
>>> x is False
True

>>> x = True
>>>
>>> x == True
True
>>>
>>> x is True
True

Example:

>>> adult = True
>>>
>>> if adult:
...     print('Yes')
Yes
>>>
>>> if adult is True:
...     print('Yes')
Yes
>>>
>>> if adult == True:
...     print('Yes')
Yes

>>> x = True
>>>
>>> id(x)  # doctest: +SKIP
4385159736
>>>
>>> id(True)  # doctest: +SKIP
4385159736


Is Numeric
----------
* Type ``int`` caches value from -5 to 256
* For those values identity check is ``True``
* For values lower than -5 or greater than 256 identity check is ``False``

>>> x = 256
>>>
>>> x == 256
True
>>>
>>> x is 256  # doctest: +SKIP
<...>: SyntaxWarning: "is" with a literal. Did you mean "=="?
True

>>> x = 257
>>>
>>> x == 257
True
>>>
>>> x is 257  # doctest: +SKIP
<...>: SyntaxWarning: "is" with a literal. Did you mean "=="?
False


Is String
---------
* String instances differs
* You cannot compare their identity
* There is a caching mechanism in Python, which sometimes yield the same result
* In order to compare strings, you should compare their values, not identities

>>> name = 'Mark Watney'
>>>
>>> name == 'Mark Watney'
True
>>> name is 'Mark Watney'  # doctest: +SKIP
<...>: SyntaxWarning: "is" with a literal. Did you mean "=="?
True


Is Type or Instance
-------------------
* ``type()``
* ``isinstance()``

Int:

>>> x = 1
>>>
>>> type(x) is int
True
>>>
>>> isinstance(x, int)
True

Float:

>>> x = 1.0
>>>
>>> type(x) is float
True
>>>
>>> isinstance(x, float)
True

Numeric:

>>> x = 1.0
>>>
>>> type(x) in (int, float)
True
>>>
>>> isinstance(x, int | float)
True

Bool:

>>> x = True
>>>
>>> type(x) is bool
True
>>>
>>> isinstance(x, bool)
True

>>> x = True
>>>
>>> type(x) is int
False
>>>
>>> isinstance(x, int)
True
>>>
>>> bool.mro()  # bool inherits from int
[<class 'bool'>, <class 'int'>, <class 'object'>]

String:

>>> x = 'Mark Watney'
>>>
>>> type(x) is str
True
>>>
>>> isinstance(x, str)
True

List:

>>> x = [1, 2, 3]
>>>
>>> type(x) is list
True
>>>
>>> isinstance(x, list)
True

Iterable:

>>> x = [1, 2, 3]
>>>
>>> type(x) in (list, tuple, set)
True
>>>
>>> isinstance(x, list | tuple | set)
True

Dict:

>>> x = {'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> type(x) is dict
True
>>>
>>> isinstance(x, dict)
True


Performance
-----------
* Tested on Python 3.11.2

SetUp:

>>> x = True

Value comparison:

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x == True
...
52 ns ± 23.8 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Identity check:

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x is True
...
39.5 ns ± 18.7 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)




.. todo:: Assignments
