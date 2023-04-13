.. testsetup::

    # doctest: +SKIP_FILE


HTTP Method
===========
* ``GET`` - Read
* ``POST`` - Create
* ``PUT`` - Update/Replace
* ``PATCH`` - Partial Update/Modify
* ``DELETE`` - Delete
* ``HEAD`` - Show Headers
* ``CONNECT`` - Connect
* ``OPTIONS`` - Show HTTP Methods
* ``TRACE`` - Show Trace

.. code-block:: console

    $ nc localhost 8000
    GET / HTTP/1.1
    Host: localhost:8000


GET
---
* ``GET`` - Read
* Retrieve data
* No other effect

Requests using GET should only retrieve data and should have no other effect.

.. code-block:: console

    $ curl -X GET http://localhost:8000/


POST
----
* ``POST`` - Create
* Stores information on the server
* Requires whole object
* Assigns a new URI

The POST method requests that the server accept the entity enclosed in the
request as a new subordinate of the web resource identified by the URI.

.. code-block:: console

    $ curl -X POST http://localhost:8000/


PUT
---
* ``PUT`` - Update/Replace
* Stores information on the server
* Requires whole object
* Reuse URI

The PUT method requests that the enclosed entity be stored under the
supplied URI.

.. code-block:: console

    $ curl -X PUT http://localhost:8000/


PATCH
-----
* ``PATCH`` - Partial Update/Modify
* Stores information on the server
* Requires part of object
* Reuse URI

The PATCH method applies partial modifications to a resource.

.. code-block:: console

    $ curl -X PATCH http://localhost:8000/


DELETE
------
* ``DELETE`` - Delete
* Removes information from the server
* Requires URI
* Discards URI

The DELETE method deletes the specified resource.

.. code-block:: console

    $ curl -X DELETE http://localhost:8000/


HEAD
----
* ``HEAD`` - Show Headers
* Identical to ``GET`` request without the response body

The HEAD method asks for a response identical to that of a GET request,
but without the response body.

.. code-block:: console

    $ curl -X HEAD http://localhost:8000/


CONNECT
-------
* ``CONNECT`` - Connect
* Request connection to a transparent TCP/IP tunnel
* Used for SSL-encryption (HTTPS) through an unencrypted HTTP proxy

The CONNECT method converts the request connection to a transparent TCP/IP
tunnel, usually to facilitate SSL-encrypted communication (HTTPS) through
an unencrypted HTTP proxy.

.. code-block:: console

    $ curl -X CONNECT http://localhost:8000/


OPTIONS
-------
* ``OPTIONS`` - Show HTTP Methods
* Returns HTTP methods for the specified URL

The OPTIONS method returns HTTP methods that the server supports for
the specified URL.

.. code-block:: console

    $ curl -X OPTIONS http://localhost:8000/


TRACE
-----
* ``TRACE`` - Show Trace
* Echoes the received request
* Debug what changes have been made by intermediate servers

The TRACE method echoes the received request so that a client can see
what (if any) changes or additions have been made by intermediate servers.

.. code-block:: console

    $ curl -X TRACE http://localhost:8000/


Match Block
-----------
* HTTP Request
* Match Block
* ``'GET /index.html HTTP/2.0'``

>>> request = 'GET /index.html HTTP/2.0'
>>>
>>> match request.split():
...     case ['GET', uri, version]:     handle_get(uri)
...     case ['POST', uri, version]:    handle_post(uri)
...     case ['PUT', uri, version]:     handle_put(uri)
...     case ['DELETE', uri, version]:  handle_delete(uri)


Use Case - 0x01
---------------
.. code-block:: console

    $ curl -X GET http://localhost:8000/
    $ curl -X POST http://localhost:8000/
    $ curl -X PUT http://localhost:8000/
    $ curl -X PATCH http://localhost:8000/
    $ curl -X DELETE http://localhost:8000/
    $ curl -X HEAD http://localhost:8000/
    $ curl -X OPTIONS http://localhost:8000/
    $ curl -X TRACE http://localhost:8000/
