import string
from pydantic import BaseModel as Schema, validator


class UserLoginIn(Schema):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                'username': 'mwatney',
                'password': 'mypassword'}}


class UserLoginOut(Schema):
    uid: int
    username: str

    class Config:
        schema_extra = {
            "example": {
                'uid': 1,
                'username': 'mwatney'}}


class UserCreate(Schema):
    firstname: str
    lastname: str
    username: str
    password: str

    @validator('firstname', 'lastname', pre=True)
    def capitalized(cls, value):
        uppercase_letters = tuple(string.ascii_uppercase)
        if not value.startswith(uppercase_letters):
            raise ValueError('Firsname and lastname must be capitalized')
        else:
            return value

    class Config:
        schema_extra = {
            "example": {
                'firstname': 'Mark',
                'lastname': 'Watney',
                'username': 'mwatney',
                'password': 'ares3'}}
