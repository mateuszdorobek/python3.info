"""
* Assignment: OOP Async GatherParams
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Define:
        a. coroutine function `run()`
        a. coroutine function `main()`
    2. Coroutine `main()` should schedule `run()` 3 times with parameters:
        a. First: name=a, sleep=1.0
        b. Second: name=b, sleep=0.5
        c. Third: name=c, sleep=1.5
    3. Coroutine `main()` should return gathered results
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj:
        a. coroutine function `run()`
        a. coroutine function `main()`
    2. Korutyna `main()` powinna zaschedulować `run()` 3 razy z parametrami:
        a. Pierwsze: name=a, sleep=1.0
        b. Drugie: name=b, sleep=0.5
        c. Trzecie: name=c, sleep=1.5
    3. Uruchom doctesty - wszystkie muszą się powieść

    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import iscoroutine, iscoroutinefunction
    >>> import asyncio

    >>> assert iscoroutinefunction(run)
    >>> assert iscoroutine(run(None,0))

    >>> assert iscoroutinefunction(main)
    >>> assert iscoroutine(main())

    >>> asyncio.run(main())
    ['a', 'b', 'c']
"""

import asyncio


# type: Coroutine
def run():
    ...


# coroutine function `main()`
# type: Coroutine
def main():
    ...


# Solution
async def run(name, sleep):
    await asyncio.sleep(sleep)
    return f'{name}'

async def main():
    return await asyncio.gather(
        run(name='a', sleep=1.0),
        run(name='b', sleep=0.5),
        run(name='c', sleep=1.5),
    )
