Chain
=====

>>> def square(x):
...     return x ** 2
>>>
>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> result = range(0,10)
>>> result = map(square, result)
>>> result = filter(even, result)
>>>
>>> for value in result:
...     print(value)
...     if value > 3:
...         break
0
4
>>>
>>> next(result)
16
>>>
>>> list(result)
[36, 64]
