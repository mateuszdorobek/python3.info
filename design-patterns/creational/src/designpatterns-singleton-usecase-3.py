class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class Database(metaclass=Singleton):
    pass

class Settings(metaclass=Singleton):
    pass


db1 = Database()
db2 = Database()

db1 is db2
# True
