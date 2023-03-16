Auth JSON Web Token
===================
* https://datatracker.ietf.org/doc/html/rfc7519
* https://jwt.io/
* JWT - JSON Web Token
* ``sub`` - subject - identifies the principal that is the subject of the JWT
* ``iss`` - issuer - claim identifies the principal that issued the JWT
* ``aud`` - Audience - identifies the recipients that the JWT is intended for
* ``exp`` - Expiration Time - identifies the expiration time on or after which the JWT MUST NOT be accepted for processing
* ``nbf`` - Not Before - identifies the time before which the JWT MUST NOT be accepted for processing
* ``iat`` - Issued At - identifies the time at which the JWT was issued
* ``jti`` - JWT ID - provides a unique identifier for the JWT
* ``scopes`` - set of permissions to a JWT token
* ``typ`` - Type - Header Parameter
* ``cty`` - Content Type - Header Parameter

.. code-block:: json

     {"iss":"joe",
      "exp":1300819380,
      "https://example.com/is_root":true}

Base64url encoding the octets of the UTF-8 representation of the JWT
   Claims Set yields this encoded JWS Payload (with line breaks for
   display purposes only):

.. code-block:: text

     eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFt
     cGxlLmNvbS9pc19yb290Ijp0cnVlfQ

   The encoded JWS Signature is the empty string.

   Concatenating these encoded parts in this order with period ('.')
   characters between the parts yields this complete JWT (with line
   breaks for display purposes only):

.. code-block:: text

     eyJhbGciOiJub25lIn0
     .
     eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFt
     cGxlLmNvbS9pc19yb290Ijp0cnVlfQ
     .

.. figure:: img/http-oauth2-jwt-sequence.png

    Source: [#Thiyagarajan2021]_

.. figure:: img/http-oauth2-jwt-components.png

    Source: [#Thiyagarajan2021]_

.. figure:: img/http-oauth2-jwt-signature.png

    Source: [#Thiyagarajan2021]_


Registered Claim Names
----------------------
The following Claim Names are registered in the IANA "JSON Web Token
Claims" registry established by Section 10.1.  None of the claims
defined below are intended to be mandatory to use or implement in all
cases, but rather they provide a starting point for a set of useful,
interoperable claims.  Applications using JWTs should define which
specific claims they use and when they are required or optional.  All
the names are short because a core goal of JWTs is for the
representation to be compact. [#rfc7519]_


"iss" (Issuer) Claim
--------------------
The "iss" (issuer) claim identifies the principal that issued the
JWT.  The processing of this claim is generally application specific.
The "iss" value is a case-sensitive string containing a StringOrURI
value.  Use of this claim is OPTIONAL. [#rfc7519]_


"sub" (Subject) Claim
---------------------
The "sub" (subject) claim identifies the principal that is the
subject of the JWT.  The claims in a JWT are normally statements
about the subject.  The subject value MUST either be scoped to be
locally unique in the context of the issuer or be globally unique.
The processing of this claim is generally application specific.  The
"sub" value is a case-sensitive string containing a StringOrURI
value.  Use of this claim is OPTIONAL. [#rfc7519]_

"aud" (Audience) Claim
----------------------
The "aud" (audience) claim identifies the recipients that the JWT is
intended for.  Each principal intended to process the JWT MUST
identify itself with a value in the audience claim.  If the principal
processing the claim does not identify itself with a value in the
"aud" claim when this claim is present, then the JWT MUST be
rejected.  In the general case, the "aud" value is an array of case-
sensitive strings, each containing a StringOrURI value.  In the
special case when the JWT has one audience, the "aud" value MAY be a
single case-sensitive string containing a StringOrURI value.  The
interpretation of audience values is generally application specific.
Use of this claim is OPTIONAL. [#rfc7519]_


"exp" (Expiration Time) Claim
-----------------------------
The "exp" (expiration time) claim identifies the expiration time on
or after which the JWT MUST NOT be accepted for processing.  The
processing of the "exp" claim requires that the current date/time
MUST be before the expiration date/time listed in the "exp" claim.
Implementers MAY provide for some small leeway, usually no more than
a few minutes, to account for clock skew.  Its value MUST be a number
containing a NumericDate value.  Use of this claim is OPTIONAL. [#rfc7519]_


"nbf" (Not Before) Claim
------------------------
The "nbf" (not before) claim identifies the time before which the JWT
MUST NOT be accepted for processing.  The processing of the "nbf"
claim requires that the current date/time MUST be after or equal to
the not-before date/time listed in the "nbf" claim.  Implementers MAY
provide for some small leeway, usually no more than a few minutes, to
account for clock skew.  Its value MUST be a number containing a
NumericDate value.  Use of this claim is OPTIONAL. [#rfc7519]_


"iat" (Issued At) Claim
------------------------
The "iat" (issued at) claim identifies the time at which the JWT was
issued.  This claim can be used to determine the age of the JWT.  Its
value MUST be a number containing a NumericDate value.  Use of this
claim is OPTIONAL. [#rfc7519]_


"jti" (JWT ID) Claim
--------------------
The "jti" (JWT ID) claim provides a unique identifier for the JWT.
The identifier value MUST be assigned in a manner that ensures that
there is a negligible probability that the same value will be
accidentally assigned to a different data object; if the application
uses multiple issuers, collisions MUST be prevented among values
produced by different issuers as well.  The "jti" claim can be used
to prevent the JWT from being replayed.  The "jti" value is a case-
sensitive string.  Use of this claim is OPTIONAL. [#rfc7519]_


JOSE Header
-----------
For a JWT object, the members of the JSON object represented by the
JOSE Header describe the cryptographic operations applied to the JWT
and optionally, additional properties of the JWT.  Depending upon
whether the JWT is a JWS or JWE, the corresponding rules for the JOSE
Header values apply.

This specification further specifies the use of the following Header
Parameters in both the cases where the JWT is a JWS and where it is a
JWE. [#rfc7519]_


"typ" (Type) Header Parameter
-----------------------------
The "typ" (type) Header Parameter defined by [JWS] and [JWE] is used
by JWT applications to declare the media type [IANA.MediaTypes] of
this complete JWT.  This is intended for use by the JWT application
when values that are not JWTs could also be present in an application
data structure that can contain a JWT object; the application can use
this value to disambiguate among the different kinds of objects that
might be present.  It will typically not be used by applications when
it is already known that the object is a JWT.  This parameter is
ignored by JWT implementations; any processing of this parameter is
performed by the JWT application.  If present, it is RECOMMENDED that
its value be "JWT" to indicate that this object is a JWT.  While
media type names are not case sensitive, it is RECOMMENDED that "JWT"
always be spelled using uppercase characters for compatibility with
legacy implementations.  Use of this Header Parameter is OPTIONAL. [#rfc7519]_


"cty" (Content Type) Header Parameter
-------------------------------------
The "cty" (content type) Header Parameter defined by [JWS] and [JWE]
is used by this specification to convey structural information about
the JWT.

In the normal case in which nested signing or encryption operations
are not employed, the use of this Header Parameter is NOT
RECOMMENDED.  In the case that nested signing or encryption is
employed, this Header Parameter MUST be present; in this case, the
value MUST be "JWT", to indicate that a Nested JWT is carried in this
JWT.  While media type names are not case sensitive, it is
RECOMMENDED that "JWT" always be spelled using uppercase characters
for compatibility with legacy implementations.  See Appendix A.2 for
an example of a Nested JWT. [#rfc7519]_


Install
-------
.. code-block:: console

    $ pip install 'python-jose[cryptography]' python-multipart


Using
-----
.. code-block:: console

    $ openssl rand -hex 32
    8dd0c72c203f1c63bd67d2089b9f3dd069873ef78688cf840c71a2237ec01d1f

Copy the output to the variable ``SECRET_KEY`` (don't use the one in the
example).

>>> SECRET_KEY = '8dd0c72c203f1c63bd67d2089b9f3dd069873ef78688cf840c71a2237ec01d1f'

Create a variable ``ALGORITHM`` with the algorithm used to sign the JWT
token and set it to ``"HS256"``.

>>> ALGORITHM = 'HS256'

Create a variable for the expiration of the token.

>>> ACCESS_TOKEN_EXPIRE_MINUTES = 30


Example
-------
.. code-block:: python

    from datetime import datetime, timedelta

    from fastapi import Depends, FastAPI, HTTPException, status
    from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
    from jose import JWTError, jwt
    from passlib.context import CryptContext
    from pydantic import BaseModel

    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            "disabled": False,
        }
    }


    class Token(BaseModel):
        access_token: str
        token_type: str


    class TokenData(BaseModel):
        username: str | None = None


    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None


    class UserInDB(User):
        hashed_password: str


    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    app = FastAPI()


    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)


    def get_password_hash(password):
        return pwd_context.hash(password)


    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)


    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user


    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt


    async def get_current_user(token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        return user


    async def get_current_active_user(current_user: User = Depends(get_current_user)):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user


    @app.post("/token", response_model=Token)
    async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}


    @app.get("/users/me/", response_model=User)
    async def read_users_me(current_user: User = Depends(get_current_active_user)):
        return current_user


    @app.get("/users/me/items/")
    async def read_own_items(current_user: User = Depends(get_current_active_user)):
        return [{"item_id": "Foo", "owner": current_user.username}]


Verify
------
.. code-block:: console

    $ curl -X GET http://localhost:8000/blog
    {"detail":"Not authenticated"}

    $ curl -X GET http://localhost:8000/login
    {"detail":"Method Not Allowed"}

    $ curl -X POST http://localhost:8000/login -d 'username=admin&password=admin'
    {"detail":"Invalid credentials"}

    $ curl -X POST http://localhost:8000/login -d 'username=mwatney&password=MyVoiceIsMyPassword'
    {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtd2F0bmV5IiwiZXhwIjoxNjE0MTM1MDE4fQ.bbbXexg1lOLENxb-gAoU5xGLrk_VdcB4Aw9_cezEN0w","token_type":"bearer"}

    $ curl -X GET http://localhost:8000/blog
    {"detail":"Not authenticated"}

    $ curl -X GET http://localhost:8000/blog -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtd2F0bmV5IiwiZXhwIjoxNjE0MTM1MDE4fQ.bbbXexg1lOLENxb-gAoU5xGLrk_VdcB4Aw9_cezEN0w'
    [{"title":"My Title","body":"My Content","published":true,"creator":{"username":"mwatney","email":"mwatney@nasa.gov"}}]


References
----------
.. [#Thiyagarajan2021] Thiyagarajan, S. Python API Development - Comprehensive Course for Beginners. Year: 2021. Retrieved: 2022-03-26. URL: https://www.youtube.com/watch?v=0sOvCWFmrtA

.. [#rfc7519] Jones, M. et al. JSON Web Token (JWT). Year: 2015. Retrieved: 2022-03-28. URL: https://datatracker.ietf.org/doc/html/rfc7519
