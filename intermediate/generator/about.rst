Generator About
===============
* Processes one element at a time
* Does not remember previous element
* Does not know next element
* Can be used only once
* Save memory (does not require more memory for processing large data)
* Uses around 10% more CPU than regular processing
* Typical usage: streams, processing larger than memory files or data
* Cannot use ``len()`` as of generators don't have length
* Previous element is overridden by current on ``next()``
* Functions (list, dict, tuple, frozenset, set, sum, all, any, etc)
  will evaluate generator instantly


Example
-------
Generator Expression:

>>> result = (x for x in range(0,5))

Generator Function:

>>> def mygenerator():
...    yield 'something'


Inspect
-------
>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> result = (x for x in range(0,5))
>>>
>>> isgenerator(result)
True
>>> isgeneratorfunction(result)
False

>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> def mygenerator():
...    yield 'something'
>>>
>>>
>>> isgenerator(mygenerator)
False
>>> isgeneratorfunction(mygenerator)
True
>>>
>>> result = mygenerator()
>>>
>>> isgenerator(result)
True
>>> isgeneratorfunction(result)
False
