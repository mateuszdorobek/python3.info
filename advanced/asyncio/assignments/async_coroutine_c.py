"""
* Assignment: OOP Async Concurrent
* Complexity: easy
* Lines of code: 15 lines
* Time: 5 min

English:
    1. Define:
        a. coroutine function `a()`
        b. coroutine function `b()`
        c. coroutine function `c()`
    2. After running coroutine should:
        a. print 'NAME: before'
        b. wait for X seconds
        c. print 'NAME: after'
        d. return NAME, where
    3. Definition of NAME:
        a. for coroutine `a()`, NAME is 'a'
        a. for coroutine `b()`, NAME is 'b'
        a. for coroutine `c()`, NAME is 'c'
    4. Definition of X:
        a. for coroutine `a()`, X is 1.0
        a. for coroutine `b()`, X is 0.5
        a. for coroutine `c()`, X is 1.5
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj:
        a. coroutine function `a()`
        b. coroutine function `b()`
        c. coroutine function `c()`
    2. Po uruchomieniu coroutine powinna:
        a. wyświetlić 'NAME: before'
        b. czekać X sekund
        c. wyświetlić 'NAME: after'
        d. zwrócić NAME
    3. Definicja NAME:
        a. dla coroutine `a()`, NAME to 'a'
        a. dla coroutine `b()`, NAME to 'b'
        a. dla coroutine `c()`, NAME to 'c'
    3. Definicja X:
        a. dla coroutine `a()`, X to 1.0
        a. dla coroutine `b()`, X to 0.5
        a. dla coroutine `c()`, X to 1.5
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

    >>> async def main():
    ...     return await asyncio.gather(a(), b(), c())
    >>>
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

# coroutine function `a()`
# print 'a: before', wait 1.0 second, print 'a: after', return 'a'
# type: Coroutine
def a():
    ...

# coroutine function `b()`
# print 'b: before', wait 0.5 second, print 'b: after', return 'b'
# type: Coroutine
def b():
    ...

# coroutine function `c()`
# print 'c: before', wait 1.5 second, print 'c: after', return 'c'
# type: Coroutine
def c():
    ...


# Solution
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
