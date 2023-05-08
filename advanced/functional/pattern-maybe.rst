Functional Pattern Maybe
========================
* Maybe monad
* Continues execution, even, if there is an error
* Final state will be none
* But no intermediate error handling is needed


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
