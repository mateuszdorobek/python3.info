AsyncIO Context Manager
=======================
* ``__aenter__``
* ``__aexit__``


Example
-------
>>> class AsyncContextManager:
...     async def __aenter__(self):
...         await print('entering context')
...
...     async def __aexit__(self, exc_type, exc, tb):
...         await print('exiting context')
