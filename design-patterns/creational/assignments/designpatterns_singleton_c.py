"""
* Assignment: DesignPatterns Creational SingletonQueue
* Complexity: medium
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Create singleton class ``Singleton``
    2. Use `__new__()` object constructor
    3. Run doctests - all must succeed

Polish:
    TODO: Polish translation

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> class Queue(Singleton):
    ...     pass

    >>> result_a = Queue()
    >>> result_b = Queue()

    >>> result_a is result_b
    True
"""
from typing import Self


class Singleton:
    pass


# Solution
class Singleton:
    instance: Self

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls)
        obj = cls.instance
        obj.__init__(*args, **kwargs)
        return obj
