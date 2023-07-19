Case Study Relationship
=======================
* Foreign Key
* One to One
* Many to Many
* Many to One


Example
-------
>>> from typing import Optional
>>> import uvicorn
>>> from passlib.context import CryptContext
>>> from pydantic import BaseModel as Schema
>>> from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Boolean
>>> from sqlalchemy.orm import sessionmaker, Session, relationship, declarative_base
>>> from fastapi import FastAPI, HTTPException, status, Depends
>>> app = FastAPI()
>>>
>>>
>>> SQLALCHEMY_DATABASE_URL = 'sqlite:///:memory:'
>>>
>>> engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
>>> SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
>>> Model = declarative_base()
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
>>> class Astronaut(Model):
...     __tablename__ = 'astronauts'
...     id = Column(Integer, primary_key=True, index=True)
...     firstname = Column(String)
...     lastname = Column(String)
...     active = Column(Boolean, nullable=True)
...     creator_id = Column(Integer, ForeignKey('users.id'))
...     creator = relationship('User', back_populates='created')
>>>
>>>
>>> class User(Model):
...     __tablename__ = 'users'
...     id = Column(Integer, primary_key=True, index=True)
...     username = Column(String)
...     email = Column(String)
...     password = Column(String)
...     created = relationship('Astronaut', back_populates='creator')
>>>
>>> Model.metadata.create_all(engine)
>>>
>>>
>>> class UserIn(Schema):
...     username: str
...     email: str
...     password: str
>>>
>>>
>>> class AstronautIn(Schema):
...     firstname: str
...     lastname: str
...     active: Optional[bool] = True
...
...     class Config:
...         from_attributes = True
>>>
>>>
>>> class UserOut(Schema):
...     username: str
...     email: str
...     created: list[AstronautIn] = []
...
...     class Config:
...         from_attributes = True
>>>
>>>
>>> class AstronautOut(Schema):
...     firstname: str
...     lastname: str
...     active: Optional[bool] = True
...     creator: UserOut
...
...     class Config:
...         from_attributes = True
>>>
>>>
>>> @app.post('/astronaut', status_code=status.HTTP_201_CREATED, response_model=AstronautOut, tags=['Astronaut'])
... def post(request: AstronautIn, db: Session = Depends(get_db)):
...     mark = Astronaut(creator_id=1, **request.dict())
...     db.add(astro)
...     db.commit()
...     db.refresh(astro)
...     return astro
>>>
>>>
>>> @app.get('/astronaut', response_model=list[AstronautOut], tags=['Astronaut'])
... def list_all(db: Session = Depends(get_db)):
...     return db.query(Astronaut).all()
>>>
>>>
>>> @app.get('/astronaut/{id}', status_code=status.HTTP_200_OK, response_model=AstronautOut, tags=['Astronaut'])
... def get(id: int, db: Session = Depends(get_db)):
...     if result := db.query(Astronaut).filter(Astronaut.id == id).first():
...         return result
...     else:
...         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Astronaut does not exist')
>>>
>>>
>>> @app.delete('/astronaut/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Astronaut'])
... def delete(id: int, db: Session = Depends(get_db)):
...     astro = db.query(Astronaut).filter(Astronaut.id == id)
...     if not astro.first():
...         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Astronaut does not exist')
...     astro.delete(synchronize_session=False)
...     db.commit()
>>>
>>>
>>> @app.put('/astronaut/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Astronaut'])
... def put(id: int, request: AstronautOut, db: Session = Depends(get_db)):
...     astro = db.query(Astronaut).filter(Astronaut.id == id)
...     if not astro.first():
...         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Astronaut does not exist')
...     astro.update(request)
...     db.commit()
...     return request
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
>>> @app.post('/user', response_model=UserOut, tags=['User'])
... def create_user(request: UserIn, db: Session = Depends(get_db)):
...     new_user = User(username=request.username,
...                     password=Password.encrypt(request.password),
...                     email=request.email)
...     db.add(new_user)
...     db.commit()
...     db.refresh(new_user)
...     return new_user
>>>
>>>
>>> @app.get('/user/{id}', response_model=UserOut, tags=['User'])
... def get_user(id: int, db: Session = Depends(get_db)):
...     if user := db.query(User).filter(User.id == id).first():
...         return user
...     else:
...         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User does not exist')
>>>
>>>
>>> if __name__ == '__main__':
...     uvicorn.run('test:app', host='127.0.0.1', port=8000, reload=True)  # doctest: +SKIP
