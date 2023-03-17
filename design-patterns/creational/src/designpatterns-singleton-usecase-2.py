from typing import Self

class Singleton:
    instance: Self | None = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        obj = cls.instance
        obj.__init__(*args, **kwargs)
        return obj


class MyClass(Singleton):
    pass
