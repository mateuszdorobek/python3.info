Idiom Next
==========


Range
-----
>>> result = range(0,5)
>>>
>>> next(result)
Traceback (most recent call last):
TypeError: 'range' object is not an iterator


Enumerate
---------
>>> months = ['January', 'February', 'March']
>>> result = enumerate(months)
>>>
>>> next(result)
(0, 'January')
>>>
>>> next(result)
(1, 'February')
>>>
>>> next(result)
(2, 'March')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration


Zip
---
>>> firstnames = ['Mark', 'Melissa', 'Rick']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> result = zip(firstnames, lastnames)
>>>
>>>
>>> next(result)
('Mark', 'Watney')
>>>
>>> next(result)
('Melissa', 'Lewis')
>>>
>>> next(result)
('Rick', 'Martinez')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration


Map
---
>>> def square(x):
...     return x ** 2
>>>
>>> data = [1, 2, 3]
>>> result = map(square, data)
>>>
>>>
>>> next(result)
1
>>>
>>> next(result)
4
>>>
>>> next(result)
9
>>> next(result)
Traceback (most recent call last):
StopIteration


Filter
------
>>> def even(x):
...     return x % 2 == 0
>>>
>>> data = [0, 1, 2, 3, 4]
>>> result = filter(even, data)
>>>
>>>
>>> next(result)
0
>>>
>>> next(result)
2
>>>
>>> next(result)
4
>>> next(result)
Traceback (most recent call last):
StopIteration
