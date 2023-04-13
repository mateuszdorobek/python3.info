Case Study Auth
===============


Install
-------
.. code-block:: console

    $ pip install 'passlib[bcrypt]'


Example
-------
>>> import uvicorn
>>> from pydantic import BaseModel
>>> from sqlalchemy import create_engine, Column, Integer, String
>>> from sqlalchemy.ext.declarative import declarative_base
>>> from sqlalchemy.orm import sessionmaker, Session
>>> from passlib.context import CryptContext
>>> from fastapi import FastAPI, Depends, HTTPException, status
>>> app = FastAPI()
>>>
>>>
>>> SQLALCHEMY_DATABASE_URL = 'sqlite:///:memory:'
>>>
>>> engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
>>> SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
>>> Base = declarative_base()
>>>
>>>
>>> def get_db():
...     db = SessionLocal()
...     try:
...         yield db
...     finally:
...         db.close()
>>>
>>>
>>> class UserModel(Base):
...     __tablename__ = 'users'
...
...     id = Column(Integer, primary_key=True, index=True)
...     username = Column(String)
...     email = Column(String)
...     password = Column(String)
>>>
>>> Base.metadata.create_all(engine)
>>>
>>>
>>> class UserRequestSchema(BaseModel):
...     username: str
...     email: str
...     password: str
>>>
>>>
>>> class UserResponseSchema(BaseModel):
...     username: str
...     email: str
...
...     class Config:
...         orm_mode = True
>>>
>>>
>>> class Password:
...     context = CryptContext(schemes=['bcrypt'], deprecated='auto')
...
...     @classmethod
...     def encrypt(cls, plaintext_password):
...         return cls.context.hash(plaintext_password)
...
...     @classmethod
...     def verify(cls, plaintext_password, hashed_password):
...         return cls.context.verify(plaintext_password, hashed_password)
>>>
>>>
>>> @app.post('/user', response_model=UserResponseSchema, tags=['User'])
... def create_user(request: UserRequestSchema, db: Session = Depends(get_db)):
...     new_user = UserModel(username=request.username,
...                          password=Password.encrypt(request.password),
...                          email=request.email)
...     db.add(new_user)
...     db.commit()
...     db.refresh(new_user)
...     return new_user
>>>
>>>
>>> @app.get('/user/{id}', response_model=UserResponseSchema, tags=['User'])
... def get_user(id: int, db: Session = Depends(get_db)):
...     if user := db.query(UserModel).filter(UserModel.id == id).first():
...         return user
...     else:
...         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User does not exist')
>>>
>>>
>>> if __name__ == '__main__':
...     uvicorn.run('test:app', host='127.0.0.1', port=8000, reload=True)  # doctest: +SKIP
