Example
=======

.. code-block:: python

    # pip install fastapi uvicorn pydantic
    # uvicorn web:app --reload

    from pathlib import Path
    from fastapi import FastAPI, UploadFile
    from pydantic import BaseModel as Schema, validator


    UPLOAD_DIR = '/tmp'

    app = FastAPI()


    @app.get('/')
    async def index():
        """
        $ curl -X GET 'http://localhost:8000/'
        """
        return {'msg': 'hello'}


    @app.get('/hello')
    async def hello(firstname: str, lastname: str, age: int | None = None):
        """
        $ curl -X GET 'http://localhost:8000/hello?firstname=Mark&lastname=Watney'
        """
        return {'msg': f'hello {firstname} {lastname} masz {age} lat'}


    @app.get('/file')
    async def file(path: str):
        """
        $ curl -X GET 'http://localhost:8000/dir?path=/tmp/myfile.txt'
        """
        file = Path(path)
        content = file.read_text()
        return {'content': content}


    @app.get('/dir')
    async def dir(path: str):
        """
        $ curl -X GET 'http://localhost:8000/dir?path=/tmp/mydir'
        """
        dir = Path(path)
        content = dir.rglob('*.py')
        return {'content': content}


    @app.post('/upload/file')
    async def upload_file(file: UploadFile):
        """
        $ curl -X POST 'http://localhost:8000/upload/file' \
        -H 'Content-Type: multipart/form-data' \
        -H 'Accept: application/json' \
        -F 'files=@myfile.txt;type=text/plain'
        """
        path = Path(UPLOAD_DIR) / file.filename
        size = path.write_bytes(await file.read())
        return {'file': path, 'bytes': size}


    @app.post('/upload/files')
    async def upload_files(files: list[UploadFile]):
        """
        $ curl -X POST 'http://localhost:8000/upload/files' \
        -H 'Content-Type: multipart/form-data' \
        -H 'Accept: application/json' \
        -F 'files=@myfile.txt;type=text/plain' \
        -F 'files=@myfile.png;type=image/png'
        """
        result = []
        for file in files:
            path = Path(UPLOAD_DIR) / file.filename
            size = path.write_bytes(await file.read())
            result.append({'file': path, 'bytes': size})
        return result


    class UserLoginSchema(Schema):
        username: str
        password: str

        @field_validator('password', pre=True)
        def valid_password(cls, password):
            if '$' in password:
                raise ValueError('Invalid character in password')
            else:
                return password


    @app.post('/login')
    async def login(user: UserLoginSchema):
        """
        $ curl -X POST 'http://localhost:8000/login' \
        -H 'Content-Type: application/json' \
        -d '{"username":"mwatney","password":"Ares3"}'
        """
        return {'msg': f'hello {user.username}'}
