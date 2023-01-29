Type Annotation TypedDict
=========================
* Since Python 3.8:
* :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys


SetUp
-----
>>> from typing import TypedDict


Definition
----------
>>> class Astronaut(TypedDict):
...     firstname: str
...     lastname: str
...     age: int | float


Example
-------
>>> def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut["firstname"]} {astronaut["lastname"]}'

>>> mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>> hello_astronaut(mark)  # ok
>>>
>>> mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> hello_astronaut(mark)  # error: missing `age`  # doctest: +SKIP
>>>
>>> mark: Astronaut = {'firstname': 'Mark'}
>>> hello_astronaut(mark)  # error: missing `lastname` and `age`  # doctest: +SKIP
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney', age=40)
>>> hello_astronaut(mark)  # ok
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney')
>>> hello_astronaut(mark)  # error: missing `age`  # doctest: +SKIP
>>>
>>> mark = Astronaut(firstname='Mark')
>>> hello_astronaut(mark)  # error: missing `lastname`  # doctest: +SKIP
>>>
>>> iris = {'genus': 'Iris', 'species': 'Setosa'}
>>> hello_astronaut(iris)  # error: not an astronaut  # doctest: +SKIP


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


References
----------
.. [#pyDocTyping] https://docs.python.org/3/library/typing.html#module-contents
