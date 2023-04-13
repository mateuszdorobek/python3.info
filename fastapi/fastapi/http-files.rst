FastAPI Files
=============
* MIME Type ``multipart/form-data``
* ``File`` vs ``UploadFile`` -> use ``UploadFile``
* Single File
* Multiple Files
* ``pip install python-multipart``
* The files will be uploaded as "form data"


SetUp
-----
>>> from pathlib import Path
>>> from fastapi import FastAPI, File, UploadFile
>>> app = FastAPI()


MIME Type
---------
* ``application/x-www-form-urlencoded`` - encoding for html forms without files
* ``multipart/form-data`` - encoding for html forms with files

Data from forms is normally encoded using the "media type"
``application/x-www-form-urlencoded`` when it doesn't include files.
When the form includes files, it is encoded as ``multipart/form-data``
If you use ``File``, FastAPI will know it has to get the files from
the correct part of the body.


File
----
* ``File`` - receive content as bytes (stores in memory)

To declare File bodies, you need to use File, because otherwise the
parameters would be interpreted as query parameters or body (JSON)
parameters.

If you declare the type of your path operation function parameter as
``bytes``, FastAPI will read the file for you and you will receive the
contents as ``bytes``. Have in mind that this means that the whole
contents will be stored in memory. This will work well for small files.

One file:

>>> @app.post('/upload/file')
... async def upload_file(file: bytes = File(...)):
...     filename = '/tmp/myfile.bin'
...     Path(filename).write_bytes(file)
...     return {'file': filename, 'size': len(file)}

Optional:

>>> @app.post('/upload/file')
... async def upload_file(file: bytes | None = File(None)):
...     if not file:
...         return {'message': 'No file sent'}
...     else:
...         filename = '/tmp/myfile.bin'
...         Path(filename).write_bytes(file)
...         return {'file': filename, 'bytes': len(file)}

Many files:

>>> @app.post('/upload/files')
... async def upload_files(files: list[bytes] = File(...)):
...     result = []
...     for i, file in enumerate(files):
...         filename = f'/tmp/myfile-{i}.bin'
...         Path(filename).write_bytes(file)
...         result.append({'file': filename, 'bytes': len(file)})
...     return result

Form:

>>> from fastapi.responses import HTMLResponse
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/upload/form')
... async def upload_form_file():
...     return HTMLResponse(content="""
...         <form method="post" action="/upload/files" enctype="multipart/form-data">
...             <input name="files" type="file" multiple>
...             <input type="submit">
...         </form>""")


UploadFile
----------
* ``UploadFile`` - receives content as file (stores on disk)
* ``UploadFile.filename`` - original file name that was uploaded e.g. ``myimage.jpg``
* ``UploadFile.content_type`` - MIME type e.g. ``image/jpeg``
* ``UploadFile.file`` - file-like object which can be written to file
* ``UploadFile.write(data)`` - writes data (str or bytes) to the file
* ``UploadFile.read(size)`` - reads size (int) bytes/characters of the file
* ``UploadFile.seek(offset)`` - goes to the byte position offset (int) in the file
* ``UploadFile.close()`` - closes the file
* All methods are ``async`` and needs ``await``

There are several cases in which you might benefit from using
``UploadFile``:

* You don't have to use ``File()`` in the default value of the parameter.
* It uses a "spooled" file. A file stored in memory up to a maximum size
  limit, and after passing this limit it will be stored in disk. This means
  that it will work well for large files like images, videos, large binaries,
  etc. without consuming all the memory.
* You can get metadata from the uploaded file.
* It has a file-like async interface.
* It exposes an actual Python ``SpooledTemporaryFile`` object that you can
  pass directly to other libraries that expect a file-like object.

``UploadFile`` attributes:

* ``filename`` -  A str with the original file name that was uploaded
  (e.g. ``myimage.jpg``).

* ``content_type`` - A str with the content type (MIME type / media type)
  (e.g. ``image/jpeg``).

* ``file`` - A ``SpooledTemporaryFile`` (a file-like object). This is the
  actual Python file that you can pass directly to other functions or
  libraries that expect a "file-like" object.

``UploadFile`` has the following async methods. They all call the
corresponding file methods underneath (using the internal
``SpooledTemporaryFile``).

* ``write(data)`` - Writes data (str or bytes) to the file.
* ``read(size)`` - Reads size (int) bytes/characters of the file.
* ``seek(offset)`` - Goes to the byte position offset (int) in the file.
  E.g., ``await myfile.seek(0)`` would go to the start of the file.
  This is especially useful if you run ``await myfile.read()`` once
  and then need to read the contents again.
* ``close()`` - Closes the file.

As all these methods are ``async`` methods, you need to ``await`` them.

One file:

>>> @app.post('/upload/file')
... async def upload_file(file: UploadFile):
...     path = Path('/tmp') / file.filename
...     size = path.write_bytes(await file.read())
...     return {'file': path, 'bytes': size}

Optional:

>>> @app.post('/upload/file')
... async def upload_file(file: UploadFile | None = None):
...     if not file:
...         return {'message': 'No upload file sent'}
...     else:
...         path = Path('/tmp') / file.filename
...         size = path.write_bytes(await file.read())
...         return {'file': path, 'bytes': size}

Many files:

>>> @app.post('/upload/files')
... async def upload_files(files: list[UploadFile]):
...     result = []
...     for file in files:
...         path = Path('/tmp') / file.filename
...         size = path.write_bytes(await file.read())
...         result.append({'file': path, 'bytes': size})
...     return result

.. code-block:: console

    $ curl -X POST 'http://localhost:8000/upload/files' \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F 'files=@myfile.txt;type=text/plain' \
        -F 'files=@myfile.png;type=image/png'
    [
      {
        "file": "/tmp/myfile.txt",
        "bytes": 28
      },
      {
        "file": "/tmp/myfile.png",
        "bytes": 12650
      }
    ]

Form:

>>> from fastapi.responses import HTMLResponse
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/upload/form')
... async def upload_form_file():
...     return HTMLResponse(content="""
...         <form method="post" action="/upload/files" enctype="multipart/form-data">
...             <input name="files" type="file" multiple>
...             <input type="submit">
...         </form>""")
