from pydantic import BaseModel as Schema


class UserCreate(Schema):
    username: str
    email: str
    password: str


class UserOut(Schema):
    username: str
    email: str

    class Config:
        from_attributes = True


class LoginRequest(Schema):
    username: str
    password: str


class Token(Schema):
    access_token: str
    token_type: str


class TokenData(Schema):
    username: str | None = None
