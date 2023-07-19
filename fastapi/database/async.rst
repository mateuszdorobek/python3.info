User Create
===========
* https://python3.info/database/sqlalchemy/model-define.html
* https://python3.info/database/sqlalchemy/model-column.html


Example
-------
* SQLAlchemy 2.0
* ``AsyncGenerator``
* ``AsyncSession``
* ``create_async_engine``
* ``sqlite+aiosqlite`` - SQLite3 async driver
* ``sqlalchemy.orm``
* ``sqlalchemy.ext.asyncio``
* ``declarative_base`` - SQLAlchemy Declarative Base - ORM Model
* ``Depends`` - FastAPI Dependency Injection

>>> from datetime import datetime, timezone
>>> from typing import AsyncGenerator
>>> from fastapi import APIRouter, Depends
>>> from pydantic import BaseModel as Schema, EmailStr
>>> from sqlalchemy import Boolean, Column, DateTime, Integer, String
>>> from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
>>> from sqlalchemy.orm import declarative_base
>>>
>>>
>>> DATABASE = 'sqlite+aiosqlite:///myfile.db'
>>>
>>> router = APIRouter()
>>> engine = create_async_engine(DATABASE, future=True)
>>> async_session = AsyncSession(engine, expire_on_commit=False)
>>> Model = declarative_base()
>>>
>>>
>>> class UserCreateRequest(Schema):
...     username: str
...     password: str
...     email: EmailStr
...
...     class Config:
...         json_schema_extra = {
...             "example": {
...                 "username": "mwatney",
...                 "password": "myVoiceIsMyPassword",
...                 "email": "mwatney@nasa.gov"}}
>>>
>>>
>>> class UserCreateResponse(Schema):
...     id: int
...     date_created: datetime
...
...     class Config:
...         from_attributes = True
>>>
>>>
>>> def utc_now():
...     return datetime.now(timezone.utc)
>>>
>>>
>>> class User(Model):
...     __tablename__ = 'users'
...
...     # System Field
...     id: int = Column(Integer, primary_key=True, autoincrement=True)
...     is_active = Column(Boolean, nullable=False, default=True)
...     date_created: datetime = Column(DateTime(timezone=True), default=utc_now)
...     date_modified: datetime = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
...
...     # Content Fields
...     username: str = Column(String(length=30), nullable=False, index=True)
...     password: str = Column(String(length=30), nullable=False)
...     email: str = Column(String(length=50), nullable=True, unique=False)
...
...     def __repr__(self):
...         id = self.id
...         username = self.username
...         return f'<User({id=}, {username=})>'
>>>
>>>
>>> @router.on_event('startup')
... async def startup():
...     async with engine.begin() as conn:
...         await conn.run_sync(Model.metadata.create_all)
>>>
>>>
>>> async def get_db() -> AsyncGenerator[AsyncSession, None]:
...     """Dependency function that yields db sessions"""
...     async with async_session as session:
...         yield session
...         await session.commit()
>>>
>>>
>>> @router.post('/user/create', response_model=UserCreateResponse)
... async def user_create(payload: UserCreateRequest, db: AsyncSession = Depends(get_db)):
...     user = User(**payload.dict())
...     db.add(user)
...     await db.commit()
...     return user
