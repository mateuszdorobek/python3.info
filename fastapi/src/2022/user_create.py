from datetime import datetime, timezone
from typing import AsyncGenerator

from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from pydantic import BaseModel as Schema, EmailStr
from sqlalchemy import Boolean, Column, DateTime, Integer, String, select
from sqlalchemy.ext.asyncio import (AsyncSession, create_async_engine)
from sqlalchemy.orm import declarative_base


DATABASE = 'sqlite+aiosqlite:///myfile.db'

router = APIRouter()
engine = create_async_engine(DATABASE, future=True)
async_session = AsyncSession(engine, expire_on_commit=False)
Model = declarative_base()

def utc_now():
    return datetime.now(timezone.utc)


class UserCreateRequest(Schema):
    username: str
    password: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "username": "mwatney",
                "password": "myVoiceIsMyPassword",
                "email": "mwatney@nasa.gov"}}


class UserCreateResponse(Schema):
    id: int
    date_created: datetime

    class Config:
        from_attributes = True


class UserDetailResponse(Schema):
    id: int
    is_active: bool
    date_created: datetime
    date_modified: datetime | None
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class Password:
    context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classmethod
    def encrypt(cls, plaintext_password):
        return cls.context.hash(plaintext_password)

    @classmethod
    def verify(cls, plaintext_password, hashed_password):
        return cls.context.verify(plaintext_password, hashed_password)


class User(Model):
    __tablename__ = 'users'

    # System Field
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, nullable=False, default=True)
    date_created: datetime = Column(DateTime(timezone=True), default=utc_now)
    date_modified: datetime = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)

    # Content Fields
    username: str = Column(String(length=30), nullable=False, index=True)
    password: str = Column(String(length=30), nullable=False)
    email: str = Column(String(length=50), nullable=True, unique=False)

    def __repr__(self):
        id = self.id
        username = self.username
        return f'<User({id=}, {username=})>'


@router.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency function that yields db sessions"""
    async with async_session as session:
        yield session
        await session.commit()


@router.post('/user', response_model=UserCreateResponse)
async def user_create(payload: UserCreateRequest, db: AsyncSession = Depends(get_db)):
    user = User(username=payload.username,
                password=Password.encrypt(payload.password),
                email=payload.email)
    db.add(user)
    await db.commit()
    return user

@router.get('/user/{id}', response_model=UserDetailResponse)
async def user_get(id: int, db: AsyncSession = Depends(get_db)):
    query = select(User).where(User.id==id)
    if user := await db.execute(query):
        return user.scalar()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User does not exist')
