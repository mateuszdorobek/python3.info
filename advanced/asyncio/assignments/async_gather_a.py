"""
* Assignment: OOP Async GatherMany
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define:
        a. coroutine function `main()`
    2. After running coroutine should:
        a. execute coroutines a(), b() and c()
        b. gather their returned values
        c. return results
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj:
        a. coroutine function `main()`
    2. Po uruchomieniu coroutine powinna:
        a. wykonać korutyny a(), b() i c()
        b. zebrać ich zwracane wartości
        c. zwrócić wyniki
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import iscoroutine, iscoroutinefunction
    >>> import asyncio

    >>> assert iscoroutinefunction(a)
    >>> assert iscoroutinefunction(b)
    >>> assert iscoroutinefunction(c)
    >>> assert iscoroutine(a())
    >>> assert iscoroutine(b())
    >>> assert iscoroutine(c())

    >>> assert iscoroutinefunction(main)
    >>> assert iscoroutine(main())

    >>> asyncio.run(main())
    a: before
    b: before
    c: before
    b: after
    a: after
    c: after
    ['a', 'b', 'c']
"""

import asyncio


async def a():
    print('a: before')
    await asyncio.sleep(1.0)
    print('a: after')
    return 'a'

async def b():
    print('b: before')
    await asyncio.sleep(0.5)
    print('b: after')
    return 'b'

async def c():
    print('c: before')
    await asyncio.sleep(1.5)
    print('c: after')
    return 'c'


# coroutine function `main()`
# execute coroutines a(), b() and c(); return gathered results
# type: Coroutine
def main():
    ...


# Solution
async def main():
    return await asyncio.gather(a(), b(), c())
