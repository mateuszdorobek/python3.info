from typing import Self


class Singleton:
    instance: Self | None = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            cls.instance.__init__(*args, **kwargs)
        return cls.instance


class Database(Singleton):
    pass



db1 = Database()
db2 = Database()

db1 is db2
# True
