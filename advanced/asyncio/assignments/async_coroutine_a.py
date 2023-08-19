"""
* Assignment: OOP Async Coroutine
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define:
        a. coroutine function `a()`
    2. After running coroutine should:
        b. return 'a'
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj:
        a. coroutine function `a()`
    2. Po uruchomieniu coroutine powinna:
        a. zwracać 'a'
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import iscoroutine, iscoroutinefunction
    >>> import asyncio

    >>> assert iscoroutinefunction(a)
    >>> assert iscoroutine(a())

    >>> asyncio.run(a())
    'a'
"""


# Coroutine function `a()`
# Function should return 'a'
# type: Coroutine
def a():
    ...

# Solution
async def a():
    return 'a'
