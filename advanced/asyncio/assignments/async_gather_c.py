"""
* Assignment: OOP Async Fetch
* Complexity: easy
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Define:
        a. coroutine function `check()`
        a. coroutine function `main()`
    2. Coroutine `check()` should use coroutine `fetch()` to download html
    3. Coroutine `check()` should check if string 'CC-BY-SA' is in html
    4. Coroutine `main()` should schedule `check()` for each URL in DATA
    5. Coroutine `main()` should return gathered results as list[dict]:
       [{'url': 'https://python3.info', 'license': True},
        {'url': 'https://python3.info/index.html', 'license': True},
        {'url': 'https://python3.info/about.html', 'license': False},
        {'url': 'https://python3.info/LICENSE.html', 'license': True}]
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj:
        a. coroutine function `check()`
        a. coroutine function `main()`
    2. Korutyna `check` powinna użyć korutyny `fetch()` aby ściągnąć html
    3. Korutyna `check()` powinna sprawdzać czy string 'CC-BY-SA' jest w htmlu
    4. Korutyna `main()` powinna zaschedulować `check()` dla każdego URL w DATA
    5. Korutyna `main()` powinna zwrócić zebrane wyniki jako list[dict]:
       [{'url': 'https://python3.info', 'license': True},
        {'url': 'https://python3.info/index.html', 'license': True},
        {'url': 'https://python3.info/about.html', 'license': False},
        {'url': 'https://python3.info/LICENSE.html', 'license': True}]

    6. Uruchom doctesty - wszystkie muszą się powieść

    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import iscoroutine, iscoroutinefunction
    >>> import asyncio

    >>> assert iscoroutinefunction(fetch)
    >>> assert iscoroutine(fetch(''))

    >>> assert iscoroutinefunction(check)
    >>> assert iscoroutine(check(''))

    >>> assert iscoroutinefunction(main)
    >>> assert iscoroutine(main())

    >>> asyncio.run(main())  # doctest: +NORMALIZE_WHITESPACE
    [{'url': 'https://python3.info', 'license': True},
     {'url': 'https://python3.info/index.html', 'license': True},
     {'url': 'https://python3.info/about.html', 'license': False},
     {'url': 'https://python3.info/LICENSE.html', 'license': True}]
"""

import asyncio
from httpx import AsyncClient


DATA = [
    'https://python3.info',
    'https://python3.info/index.html',
    'https://python3.info/about.html',
    'https://python3.info/LICENSE.html',
]


async def fetch(url):
    return await AsyncClient().get(url)



# Solution
async def check(url):
    resp = await fetch(url)
    license = 'CC-BY-SA' in resp.text
    return {'url': url, 'license': license}


async def main():
    todo = [check(url) for url in DATA]
    return await asyncio.gather(*todo)
