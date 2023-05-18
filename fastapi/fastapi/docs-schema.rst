FastAPI Schema
==============
* Schema - also known as Model
* Represents data in your system
* Pydantic class
* ``schema_extra`` is used by Swagger to show examples
* Ellipsis (``...``) in Pydantic indicates that a Field is required


Example
-------
>>> from pydantic import BaseModel
>>>
>>>
>>> class Astronaut(BaseModel):
...     firstname: str
...     lastname: str
...     active: bool | None = True


Validation
----------
* Validators are "class methods", so the first argument value they receive is the Astronaut class, not an instance of Astronaut.
* The second argument is always the field value to validate; it can be named as you please
* Validators should either return the parsed value or raise a ValueError, TypeError, or AssertionError (assert statements may be used).
* Validation is done in the order fields are defined

>>> from string import ascii_uppercase
>>> from pydantic import BaseModel, root_validator, validator
>>>
>>>
>>> class Astronaut(BaseModel):
...     firstname: str
...     lastname: str
...     age: float | None = None
...
...     @validator('firstname', 'lastname', allow_reuse=True)
...     def is_capitalize(cls, value: str):
...         uppercase = tuple(ascii_uppercase)
...         if not value.startswith(uppercase):
...             raise ValueError('Must starts with uppercase letter')
...         return value
...
...     @validator('age', allow_reuse=True)
...     def age_in_range(cls, value: float):
...         if 0 < value < 130:
...             return value
...         else:
...             raise ValueError('Age must be in range from 0 to 130')
...
...     @validator('*', allow_reuse=True)
...     def not_empty(cls, value: str | float | None):
...         if type(value) is str and value == '':
...             raise ValueError('Invalid field value')
...         return value
...
...     @root_validator(pre=True, allow_reuse=True)
...     def check_names_differs(cls, values: dict):
...         firstname = values.get('firstname')
...         lastname = values.get('lastname')
...
...         if firstname is None or lastname is None:
...             raise ValueError('fields firstname and lastname are not optional')
...         if firstname == lastname:
...             raise ValueError('firstname and lastname cannot be the same')
...         else:
...             return values
>>>
>>>
>>> Astronaut(firstname='Mark', lastname='Watney')
Astronaut(firstname='Mark', lastname='Watney', age=None)
>>>
>>> Astronaut(firstname='Mark', lastname='Watney', age=42)
Astronaut(firstname='Mark', lastname='Watney', age=42.0)
>>>
>>> Astronaut(firstname='Mark', lastname='Watney', age=-1)
Traceback (most recent call last):
pydantic.error_wrappers.ValidationError: 1 validation error for Astronaut
age
  Age must be in range from 0 to 130 (type=value_error)
>>>
>>> Astronaut(firstname='Mark', lastname='Mark', age=1)
Traceback (most recent call last):
pydantic.error_wrappers.ValidationError: 1 validation error for Astronaut
__root__
  firstname and lastname cannot be the same (type=value_error)
>>>
>>> Astronaut(firstname='mark', lastname='watney', age=-1)
Traceback (most recent call last):
pydantic.error_wrappers.ValidationError: 3 validation errors for Astronaut
firstname
  Must starts with uppercase letter (type=value_error)
lastname
  Must starts with uppercase letter (type=value_error)
age
  Age must be in range from 0 to 130 (type=value_error)

>>> from datetime import datetime
>>> from pydantic import BaseModel, validator
>>>
>>>
>>> class PastDate(BaseModel):
...     dt: datetime = None
...
...     @validator('dt', pre=True, always=True, allow_reuse=True)
...     def past_timestamp(cls, value):
...         if datetime.fromisoformat(value) >= datetime.now():
...             raise ValueError('Timestamp is not in the past')
...         return value
>>>
>>> print(PastDate(dt='1969-07-21T02:56:15'))
dt=datetime.datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> print(PastDate(dt='2969-07-21T02:56:15'))
Traceback (most recent call last):
pydantic.error_wrappers.ValidationError: 1 validation error for PastDate
dt
  Timestamp is not in the past (type=value_error)


Use Case - 0x01
---------------
* ``schema_extra`` is used by Swagger to show examples
* Ellipsis (``...``) in Pydantic indicates that a Field is required

.. code-block:: console

    $ pip install 'pydantic[email]'

>>> from pydantic import BaseModel, EmailStr, Field
>>>
>>>
>>> class StudentSchema(BaseModel):
...     fullname: str = Field(...)
...     email: EmailStr = Field(...)
...     course_of_study: str = Field(...)
...     year: int = Field(..., gt=0, lt=9)
...     gpa: float = Field(..., le=4.0)
...
...     class Config:
...         schema_extra = {
...             "example": {
...                 "fullname": "Mark Watney",
...                 "email": "mark.watney@nasa.gov",
...                 "course_of_study": "Botanics",
...                 "year": 2,
...                 "gpa": "3.0",
...             }
...         }
>>>
>>>
>>> class UpdateStudentModel(BaseModel):
...     fullname: str | None
...     email: EmailStr | None
...     course_of_study: str | None
...     year: int | None
...     gpa: float | None
...
...     class Config:
...         schema_extra = {
...             "example": {
...                 "fullname": "Mark Watney",
...                 "email": "mark.watney@nasa.gov",
...                 "course_of_study": "Botanics",
...                 "year": 4,
...                 "gpa": "4.0",
...             }
...         }


Use Case - 0x01
---------------
>>> from fastapi import FastAPI
>>> from fastapi.responses import JSONResponse
>>> from pydantic import BaseModel as Schema
>>> app = FastAPI()
>>>
>>>
>>> SQL_SELECT_LOGIN = """
...     SELECT id, firstname, lastname
...     FROM users
...     WHERE username = :username
...     AND password = :password; """
>>>
>>>
>>> class LoginIn(Schema):
...     username: str
...     password: str
...
...     class Config:
...         schema_extra = {
...             'example': {
...                 'username': 'mwatney',
...                 'password': 'nasa'}}
>>>
>>>
>>> class LoginOut(Schema):
...     id: int
...     firstname: str
...     lastname: str
...
...     class Config:
...         schema_extra = {
...             'example': {
...                 'uid': 1,
...                 'firstname': 'Mark',
...                 'lastname': 'Watney'}}
>>>
>>>
>>> class NotFound(Schema):
...     status: int = 404
...     reason: str = 'Not Found'
...     details: str | None = None
>>>
>>>
>>> @app.post(
...     path='/login',
...     response_model=LoginOut,
...     responses={
...         200: {'model': LoginOut},
...         404: {'model': NotFound}},
...     tags=['auth'])
... def login(user: LoginIn):
...     from database import DATABASE, SQL_SELECT_LOGIN
...     with sqlite3.connect(DATABASE) as db:
...         db.row_factory = sqlite3.Row
...         if result := db.execute(SQL_SELECT_LOGIN, user.dict()).fetchone():
...             return dict(result)
...         else:
...             return JSONResponse(status_code=404, content={'details': 'invalid login/password'})


Assignments
-----------
.. literalinclude:: assignments/fastapi_schema_a.py
    :caption: :download:`Solution <assignments/fastapi_schema_a.py>`
    :end-before: # Solution
