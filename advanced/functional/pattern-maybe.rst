Functional Pattern Maybe
========================
* Maybe monad
* Continues execution, even, if there is an error
* Final state will be none
* But no intermediate error handling is needed

The concept of monad is a functional programming concept that provides a way
to encapsulate and sequence computations. In Python, the concept of monad
can be implemented using classes and methods.

One example of a monad in Python is the ``Maybe`` monad, which is used to
represent computations that may or may not return a value. The ``Maybe`` monad
is implemented as a class with two subclasses: ``Just` and ``Nothing``. The
``Just`` subclass represents a computation that returns a value, while the
``Nothing`` subclass represents a computation that does not return a value.

Here is an example implementation of the ``Maybe`` monad in Python:

>>> class Maybe:
...     def __init__(self, value):
...         self.value = value
...
...     def bind(self, func):
...         if self.value is None:
...             return Nothing()
...         else:
...             return func(self.value)
>>>
>>> class Just(Maybe):
...     pass
>>>
>>> class Nothing(Maybe):
...     def bind(self, func):
...         return self
>>>
>>> def add_one(x):
...     return Just(x + 1)
>>>
>>> def divide_by_zero(x):
...     return Just(x / 0)
>>>
>>> result = Just(2).bind(add_one).bind(divide_by_zero)  # doctest: +SKIP
>>> print(result)  # doctest: +SKIP
None

In this example, the ``Maybe`` class is used to represent computations that
may or may not return a value. The ``bind`` method is used to sequence
computations by applying a function to the result of a previous computation.
The ``Just`` and ``Nothing`` subclasses are used to represent computations
that return a value and computations that do not return a value, respectively.

The ``add_one`` function is used to add one to a value, while the
``divide_by_zero`` function is used to divide a value by zero. The ``result``
variable is used to sequence these computations by first adding one to the
value 2, and then attempting to divide the result by zero. Since dividing by
zero is not possible, the result is a ``Nothing`` object.


Pattern
-------
>>> class Maybe:
...     def __init__(self, value):
...         self.value = value
...
...     def __repr__(self):
...         return f"Maybe({self.value})"
...
...     def unwrap(self):
...         return self.value
...
...     def bind(self, func):
...         if self.value is None:
...             return Maybe(None)
...         return Maybe(func(self.value))


With Value
----------
>>> DATA = 4
>>>
>>> result = (
...     Maybe(DATA)
...     .bind(lambda x: 2*x)
...     .bind(lambda y: y+1)
... )
>>>
>>> print(result)
Maybe(9)
>>>
>>> print(result.unwrap())
9


With Errors
-----------
>>> DATA = 4
>>>
>>> result = (
...     Maybe(DATA)
...     .bind(lambda x: None if x < 10 else x)  # this could fail
...     .bind(lambda x: 2*x)
...     .bind(lambda y: y+1)
... )
>>>
>>> result
Maybe(None)
>>>
>>> result.unwrap()
