AsyncIO Shield
==============
* Shielding from Cancellation
* Awaitable ``asyncio.shield(aw)``
* Protect an awaitable object from being cancelled.


Example
-------
>>> import asyncio
>>>
>>>
>>> async def work():
...     return 'done'
>>>
>>>
>>> async def main():
...     try:
...         res = await asyncio.shield(work())
...     except asyncio.CancelledError:
...         res = None
>>>
>>>
>>> asyncio.run(main())
