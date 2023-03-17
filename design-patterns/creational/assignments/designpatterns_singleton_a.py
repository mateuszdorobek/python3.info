"""
* Assignment: DesignPatterns Creational SingletonSettings
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Create singleton class `Settings`
    2. Use `get_instance()` classmethod
    3. Run doctests - all must succeed

Polish:
    TODO: Polish translation

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result_a = Settings.get_instance()
    >>> result_b = Settings.get_instance()

    >>> result_a is result_b
    True
"""
from typing import Self


class Settings:
    pass


# Solution

class Settings:
    instance: Self

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls)
        return cls.instance
