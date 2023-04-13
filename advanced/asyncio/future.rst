AsyncIO Future
==============
* Low-level awaitable object
* Represents an eventual result of an asynchronous operation
* Normally there is *no need* to create Future objects at the application level code
* When a ``Future`` object is awaited it means that the coroutine will wait until the ``Future`` is resolved in some other place
* Future objects in asyncio are needed to allow callback-based code to be used with ``async``/``await``


Example
-------
>>> import asyncio
>>> import concurrent.futures
>>>
>>>
>>> def blocking_io():
...     # File operations (such as logging) can block the
...     # event loop: run them in a thread pool.
...     with open('/dev/urandom', 'rb') as f:
...         return f.read(100)
>>>
>>> def cpu_bound():
...     # CPU-bound operations will block the event loop:
...     # in general it is preferable to run them in a
...     # process pool.
...     return sum(i * i for i in range(10 ** 7))
>>>
>>>
>>> async def main():
...     loop = asyncio.get_running_loop()
...
...     ## Options:
...
...     # 1. Run in the default loop's executor:
...     result = await loop.run_in_executor(None, blocking_io)
...     print('default thread pool', result)
...
...     # 2. Run in a custom thread pool:
...     with concurrent.futures.ThreadPoolExecutor() as pool:
...         result = await loop.run_in_executor(pool, blocking_io)
...         print('custom thread pool', result)
...
...     # 3. Run in a custom process pool:
...     with concurrent.futures.ProcessPoolExecutor() as pool:
...         result = await loop.run_in_executor(pool, cpu_bound)
...         print('custom process pool', result)
>>>
>>>
>>> asyncio.run(main())  # doctest: +SKIP
default thread pool b'\x11l\xdf\xd5\x95\xddm\x1a\x0e\xbfj\x06\xf3\x8a\xe2\x88\xbf\x970\xd8\x93W\x1e\x13E\xde\xf2\xdc\x02\xcae\x97f\xee\x04\xd5\xab\x9fd(Z\t\x17\xf8]X\x1cn\xfc\xa1\xa6\xb0\x9eMx8\rt\xbc~\x06g+8\xa5b4p,\xe5\x91H\x99\x98\x0b\xbd?}h\x7f\xacGH9\t\xe3\xd2\xe5R\x82o5k.Wd\xd27`-'
custom thread pool b'\x99\xc5K%n\xb5\x06\x99\x80\xa1\xa0\x84E\x0ed\xc4x\xa5\xc8C\x19-\x97\xe8\xc0\x8f\xdf\xd3\x1c\xc3\xe2\xc1\xe8\x85.\x19L\x97{\xce\xf7u\xeap\x89@F}\xa1,\x06:\x9bU\xdc\xf1\xc7\x12\xed\xdf\xae\x9e\x88#\xd4K\xfat\xcd\x8f[\xe9\x80d&\xb8H\x1ed\x8e\x97\x8b\xce\x00_\x85\xbd4\xd6\xf4\x88\xa7\x12\xa0\xcaSI\x1b\xb1\xcf'
