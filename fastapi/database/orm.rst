Database ORM
============
* ORM - Object-relational mapping
* ORM has tools to convert (`map`) between objects in code and database tables (`relations`)
* Declarative - First define model, which then maps to the database tables
* If you want to generate


Install
-------
.. code-block:: console

    $ pip install sqlalchemy

>>> import sqlalchemy
>>>
>>>
>>> sqlalchemy.__version__.startswith('2.0')
True


Connection
----------
>>> from sqlalchemy import create_engine
>>> from sqlalchemy.ext.declarative import declarative_base
>>> from sqlalchemy.orm import sessionmaker
>>>
>>>
>>> SQLALCHEMY_DATABASE_URL = 'sqlite:///:memory:'
>>>
>>> engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
>>> SessionLocal = sessionmaker(bind= engine, autocommit=False, autoflush=False)
>>> Base = declarative_base()


Models
------
* Represents database entity

>>> from sqlalchemy import Column, Integer, String
>>>
>>>
>>> class User(Base):
...     __tablename__ = 'users'
...
...     id = Column(Integer, primary_key=True)
...     firstname = Column(String)
...     lastname = Column(String)
...     age = Column(Integer)
...
...     def __repr__(self):
...         firstname = self.name
...         lastname = self.fullname
...         age = self.age
...         return f'<User({firstname=}, {lastname=}, {age=})>'


Schema
------
* Represents JSON request/response data
* ``Config.orm_mode = True`` is required to have model as a ``response_model`` (a decorator parameter).
* Note, that if you set ``orm_mode = True``, then not all fields need to be specified.
* Listed fields will be in response, and not listed will be hidden in response.

>>> from pydantic import BaseModel
>>>
>>>
>>> class AstronautSchema(BaseModel):
...     firstname: str
...     lastname: str
...     active: bool | None = True

``Config.orm_mode = True`` is required to have model as a ``response_model``
(a decorator parameter). Note, that if you set ``orm_mode = True``, then
not all fields need to be specified. Listed fields will be in response,
and not listed will be hidden in response.

>>> from pydantic import BaseModel
>>>
>>>
>>> class AstronautSchema(BaseModel):
...     firstname: str
...     lastname: str
...
...     class Config:
...         orm_mode = True


Example
-------
>>> import uvicorn
>>> from pydantic import BaseModel
>>> from sqlalchemy import create_engine, Column, Integer, String, Boolean
>>> from sqlalchemy.ext.declarative import declarative_base
>>> from sqlalchemy.orm import sessionmaker, Session
>>> from fastapi import FastAPI, HTTPException, status, Depends
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
>>> class AstronautModel(Base):
...     __tablename__ = 'astronauts'
...     id = Column(Integer, primary_key=True, index=True)
...     firstname = Column(String)
...     lastname = Column(String)
...     active = Column(Boolean, nullable=True)
>>>
>>>
>>> class AstronautSchema(BaseModel):
...     firstname: str
...     lastname: str
...     active: bool | None = True
...
...     class Config:
...         orm_mode = True
>>>
>>>
>>> Base.metadata.create_all(engine)
>>>
>>>
>>> @app.post('/astronaut', status_code=status.HTTP_201_CREATED)
... def post(request: AstronautSchema, db: Session = Depends(get_db)):
...     mark = AstronautModel(**request.dict())
...     db.add(astro)
...     db.commit()
...     db.refresh(astro)
...     return astro
>>>
>>>
>>> @app.get('/astronaut', response_model=list[AstronautSchema])
... def list_all(db: Session = Depends(get_db)):
...     return db.query(AstronautModel).all()
>>>
>>>
>>> @app.get('/astronaut/{id}', status_code=status.HTTP_200_OK, response_model=AstronautSchema)
... def get(id: int, db: Session = Depends(get_db)):
...     if result := db.query(AstronautModel).filter(AstronautModel.id == id).first():
...         return result
...     else:
...         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Astronaut does not exist')
>>>
>>>
>>> @app.delete('/astronaut/{id}', status_code=status.HTTP_204_NO_CONTENT)
... def delete(id: int, db: Session = Depends(get_db)):
...     astro = db.query(AstronautModel).filter(AstronautModel.id == id)
...     if not astro.first():
...         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Astronaut does not exist')
...     astro.delete(synchronize_session=False)
...     db.commit()
>>>
>>>
>>> @app.put('/astronaut/{id}', status_code=status.HTTP_202_ACCEPTED)
... def put(id: int, request: AstronautSchema, db: Session = Depends(get_db)):
...     astro = db.query(AstronautModel).filter(AstronautModel.id == id)
...     if not astro.first():
...         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Astronaut does not exist')
...     astro.update(request)
...     db.commit()
...     return request
>>>
>>>
>>> if __name__ == '__main__':
...     uvicorn.run('test:app', host='127.0.0.1', port=8000, reload=True)  # doctest: +SKIP


Further Reading
---------------
* https://fastapi.tiangolo.com/tutorial/sql-databases/
* https://www.sqlalchemy.org
