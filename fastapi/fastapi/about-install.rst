FastAPI Install
===============
* ``pip install fastapi``
* ``pip install uvicorn`` - minimal (pure Python) dependencies
* ``pip install uvicorn[standard]`` - "Cython-based" dependencies and other "extras"


Install
-------
To install ``FastAPI`` execute:

.. code-block:: console

    $ pip install fastapi

To install ``uvicorn`` there are two options: ``uvicorn``
or ``uvicorn[standard]``.

``uvicorn``:

    * Install uvicorn with minimal (pure Python) dependencies

``uvicorn[standard]``:

    * Install uvicorn with "Cython-based" dependencies (where possible) and other "optional extras"
    * The event loop ``uvloop`` will be installed and used if possible
    * The `HTTP` protocol will be handled by ``httptools`` if possible
    * The `Websocket` protocol will be handled by ``websockets`` if possible
    * If you want to use ``wsproto`` you'd need to install it manually
    * The ``--reloader`` flag in development mode will use ``watchgod``
    * Windows users will have ``colorama`` installed for the colored logs
    * ``python-dotenv`` will be installed should you want to use the ``--env-file`` option
    * ``PyYAML`` will be installed to allow you to provide a ``.yaml`` file to ``--log-config``, if desired

.. code-block:: console

    # Install uvicorn with minimal (pure Python) dependencies
    $ pip install uvicorn

.. code-block:: console

    # Install uvicorn with "Cython-based" dependencies (where possible) and other "optional extras"
    $ pip install 'uvicorn[standard]'


App
---
Create file ``main.py`` with content:

>>> from fastapi import FastAPI
>>>
>>>
>>> app = FastAPI()
>>>
>>> @app.get('/')
... def index():
...     return {'message': 'hello world'}


Run
---
* ``uvicorn`` - lightning-fast ASGI server implementation, using ``uvloop`` and ``httptools``
* ``main`` - name of the module to run (filename without ``.py`` extension)
* ``app`` - name of the ``FastAPI`` class instance (inside of the ``main.py`` file)
* ``--reload`` - reload webserver each time when ``main.py`` changes (flag is optional)

.. code-block:: console

    $ uvicorn main:app --reload
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [63402] using statreload
    INFO:     Started server process [63404]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

Optional configuration arguments:

.. code-block:: console

    $ uvicorn main:app --workers 2
    $ uvicorn main:app --reload --port 8000
    $ uvicorn main:app --reload --host 0.0.0.0 --port 8000

Open browser at ``http://127.0.0.1:8000/``


Run Configuration
-----------------
.. todo:: Describe how to create "Run Configuration" in PyCharm


Debug
-----
* PyCharm Run Configuration
* Set breakpoint
* Run Debugger
* Step Over

Create file ``main.py``:

>>> import uvicorn
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/')
... def index():
...     return {'data': 'hello world'}
>>>
>>>
>>> if __name__ == '__main__':
...     uvicorn.run('main:app', host='127.0.0.1', port=8000)  # doctest: +SKIP

.. code-block:: console

    $ python main.py
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [68005] using watchgod
    INFO:     Started server process [68007]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
