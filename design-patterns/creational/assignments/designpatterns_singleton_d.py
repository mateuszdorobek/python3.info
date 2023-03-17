"""
* Assignment: DesignPatterns Creational SingletonLogger
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Create singleton class ``Singleton``
    2. Use `Metaclass`
    3. Run doctests - all must succeed

Polish:
    TODO: Polish translation

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> class Logger(metaclass=Singleton):
    ...     pass

    >>> result_a = Logger()
    >>> result_b = Logger()

    >>> result_a is result_b
    True
"""
from typing import Self


class Singleton(type):
    pass


# Solution
class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]
