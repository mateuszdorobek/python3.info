Gateway Interface
=================
* You want your *WSGI* server to respond to incoming requests as quickly as possible.
* Each request ties up a worker process until the response is finished.
* Moving work off those workers by spinning up asynchronous jobs as tasks in a queue is a straightforward way to improve *WSGI* server response times.


.. glossary::

    ASGI
    Asynchronous Server Gateway Interface
        Is a spiritual successor to WSGI, intended to provide a standard
        interface between async-capable Python web servers, frameworks,
        and applications.


ASGI
----
* https://asgi.readthedocs.io/en/latest/

ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to
WSGI, intended to provide a standard interface between async-capable Python
web servers, frameworks, and applications.

Where WSGI provided a standard for synchronous Python apps, ASGI provides
one for both asynchronous and synchronous apps, with a WSGI
backwards-compatibility implementation and multiple servers
and application frameworks.
