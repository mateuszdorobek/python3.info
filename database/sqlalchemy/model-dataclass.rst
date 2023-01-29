.. testsetup::

    # doctest: +SKIP_FILE


Model Dataclass
===============
* https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#whatsnew-20-dataclasses
* https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#native-support-for-dataclasses-mapped-as-orm-models


Use Case - 0x01
---------------
>>> from __future__ import annotations
>>> from dataclasses import dataclass, field
>>> from sqlalchemy import Column, ForeignKey, Integer, String
>>> from sqlalchemy.orm import registry, relationship
>>>
>>> mapper_registry = registry()
>>>
>>>
>>> @mapper_registry.mapped
... @dataclass
... class User:
...     __tablename__ = "user"
...     __sa_dataclass_metadata_key__ = "sa"
...
...     id: int = field(init=False, metadata={"sa": Column(Integer, primary_key=True)})
...     name: str = field(default=None, metadata={"sa": Column(String(50))})
...     fullname: str = field(default=None, metadata={"sa": Column(String(50))})
...     nickname: str = field(default=None, metadata={"sa": Column(String(12))})
...     addresses: list[Address] = field(default_factory=list, metadata={"sa": relationship("Address")})
>>>
>>>
>>> @mapper_registry.mapped
... @dataclass
... class Address:
...     __tablename__ = "address"
...     __sa_dataclass_metadata_key__ = "sa"
...
...     id: int = field(init=False, metadata={"sa": Column(Integer, primary_key=True)})
...     user_id: int = field(init=False, metadata={"sa": Column(ForeignKey("user.id"))})
...     email_address: str = field(default=None, metadata={"sa": Column(String(50))})
