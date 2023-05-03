AsyncIO Iterator
================
* Asynchronous Generators https://peps.python.org/pep-0525/


Example
-------
>>> async def myfunc(self):
...     await asyncio.sleep(1)
...     yield 'done'


Typing
------
* ``collections.abc.AsyncGenerator``
