from typing import Self


class Database:
    connection: Self | None = None

    @classmethod
    def connect(cls):
        if not cls.connection:
            cls.connection = ...  # connect to database
        return cls.connection


db1 = Database.connect()
db2 = Database.connect()

db1 is db2
# True
