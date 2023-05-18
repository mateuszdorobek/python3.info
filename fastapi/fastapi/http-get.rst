FastAPI GET
===========
* Resources
* Query Parameters


SetUp
-----
>>> from fastapi import FastAPI
>>> app = FastAPI()


No Parameters
-------------
* Does define resource (required)
* ``/hello``

>>> @app.get('/hello')
... def hello():
...     return {'data': 'hello'}

.. code-block:: console

    $ curl http://127.0.0.1:8000/hello
    {"data":"hello"}


Single Path - One
-----------------
* Does define resource (required)
* ``/hello/{firstname}``

>>> @app.get('/hello/{firstname}')
... def hello(firstname: str):
...     return {'data': firstname}

.. code-block:: console

    $ curl http://127.0.0.1:8000/hello/Mark
    {"data":"Mark"}


Path Parameter - Many
---------------------
* Does define resource (required)
* ``/hello/{firstname}-{lastname}``

>>> @app.get('/hello/{firstname}-{lastname}')
... def hello(firstname: str, lastname: str):
...     return {'data': f'{firstname} {lastname}'}

.. code-block:: console

    $ curl http://127.0.0.1:8000/hello/Mark-Watney
    {"data":"Mark Watney"}


Query Parameter
---------------
* Does not require a name in URL resource, but requires a parameter
* ``/hello``

>>> @app.get('/hello')
... def hello(firstname: str):
...     return {'data': firstname}

.. code-block:: console

    $ curl http://127.0.0.1:8000/hello?firstname=Mark
    {"data":"Mark"}


Multiple Parameters
-------------------
* Does not require a name in URL resource, but requires a parameter
* ``/hello``

>>> @app.get('/hello')
... def hello(firstname: str, lastname: str):
...     return {'data': f'{firstname} {lastname}'}

.. code-block:: console

    $ curl http://127.0.0.1:8000/hello?firstname=Mark&lastname=Watney
    {"data":"Mark Watney"}


Default Values
--------------
>>> @app.get('/hello')
... def hello(firstname: str, lastname: str, age: int = 42):
...     return {'data': f'{firstname} {lastname} is {age} years old'}

.. code-block:: console

    $ curl http://127.0.0.1:8000/hello/?firstname=Mark&lastname=Watney
    {"data":"Mark Watney is 42 years old"}

.. code-block:: console

    $ curl http://127.0.0.1:8000/hello/?firstname=Mark&lastname=Watney&age=69
    {"data":"Mark Watney is 69 years old"}


Optional
--------
>>> @app.get('/hello/')
... def hello(firstname: str, lastname: str, age: int | None = None):
...     return {'data': f'{firstname} {lastname} is {age} years old'}

.. code-block:: console

    $ curl http://127.0.0.1:8000/hello/?firstname=Mark&lastname=Watney
    {"data":"Mark Watney is None years old"}

.. code-block:: console

    $ curl http://127.0.0.1:8000/hello/?firstname=Mark&lastname=Watney&age=69
    {"data":"Mark Watney is 69 years old"}
