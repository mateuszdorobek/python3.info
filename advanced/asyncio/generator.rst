AsyncIO Iterator
================
* Asynchronous Generators https://peps.python.org/pep-0525/


Example
-------
>>> async def myfunc(self):
...     await asyncio.sleep(1)
...     yield 'done'


Type Annotation
---------------
* ``collections.abc.AsyncGenerator``
