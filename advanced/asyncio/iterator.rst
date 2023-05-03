AsyncIO Iterator
================
* Asynchronous Generators https://peps.python.org/pep-0525/
* Asynchronous Comprehensions https://peps.python.org/pep-0530/
* ``__aiter__``
* ``__anext__``


Example
-------
>>> class Reader:
...     async def readline(self):
...         ...
...
...     def __aiter__(self):
...         return self
...
...     async def __anext__(self):
...         line = await self.readline()
...         if line == b'':
...             raise StopAsyncIteration
...         return line


Typing
------
* ``collections.abc.AsyncGenerator``
