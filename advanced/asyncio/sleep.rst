AsyncIO Sleep
=============
* Coroutine ``asyncio.sleep(delay, result=None)``
* Delay can be int or float
* Block for delay seconds.
* If result is provided, it is returned to the caller when the coroutine completes
* Delay is not guaranteed
* It means that this is at least X number of seconds
* This us due, that after that time of delay, there might still be an other function running
* This does not interrupt or preempt


Example
-------
>>> import asyncio
>>>
>>>
>>> async def main():
...     result = await asyncio.sleep(0.5, 'done')
...     print(result)
>>>
>>>
>>> asyncio.run(main())
done
