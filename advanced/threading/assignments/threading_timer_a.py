"""
* Assignment: Concurrency Threading Timer
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Define function `ping()`, with optional parameter
       `n: int`, which defaults to 1
    2. Function `ping()` should append value of `n` to `result`
    3. Function should be called every `INTERVAL`
    4. Function should be called maximum `MAX` times
    5. Use `Timer` from `threading` module
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `ping(n: int)` z opcjonalnym parametrem
       `n: int`, który domyślnie jest 1
    2. Funkcja `ping()` powinna dopisywać wartość `n` do `result`
    3. Funkcja powinna być wywoływana co `INTERVAL`
    4. Funkcja powinna być wywołana maksymalnie `MAX` razy
    5. Użyj `Timer` z modułu `threading`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> def check(result):
    ...     assert result == [1, 2, 3], f'Result is {result}'

    >>> Timer(INTERVAL, ping).start()
    >>> Timer(INTERVAL*MAX+1, check, [result]).start()
"""
from threading import Timer


INTERVAL = 0.1
MAX = 3
result = []


# type: Callable[[int], None]
def ping():
    ...


# Solution
def ping(n: int = 1):
    result.append(n)
    if n < MAX:
        Timer(INTERVAL, ping, [n + 1]).start()
