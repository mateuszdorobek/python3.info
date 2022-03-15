"""
* Assignment: Decorator Function Memoization
* Complexity: easy
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Create decorator `@cache`
    2. Decorator must check before running function, if for given argument
       the computation was already done:
       a. if yes, return from `_cache`
       b. if not, calculate new result, update cache and return value
    3. Using `timeit` compare execution time (it might take around 30 seconds)
    4. Last three tests (prints) are only infomation about execution time
    5. Run doctests - all must succeed (beside three prints)

Polish:
    1. Stwórz dekorator `@cache`
    2. Decorator ma sprawdzać przed uruchomieniem funkcji, czy dla danego
       argumentu wynik został już wcześniej obliczony:
       a. jeżeli tak, zwróć dane z `_cache`
       b. jeżeli nie, oblicz, zaktualizuj `_cache` i zwróć wartość
    3. Używając `timeit` porównaj czas wykonywania (może trwać około 30 sekund)
    4. Ostatnie trzy testy (printy) to tylko informacja o czasie wykonywania
    5. Uruchom doctesty - wszystkie muszą się powieść (poza trzema printami)

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from timeit import timeit
    >>> from inspect import isfunction
    >>> sys.setrecursionlimit(5000)

    >>> assert type(_cache) is dict, \
    'Cache storage should be a dict'

    >>> assert len(_cache) == 0, \
    'Cache storage should be empty'

    >>> assert isfunction(cache), \
    'Create cache() function'

    >>> assert isfunction(cache(lambda: ...)), \
    'cache() should take function as an argument'

    >>> @cache
    ... def fn1(n):
    ...     if n == 0:
    ...         return 1
    ...     else:
    ...         return n * fn1(n - 1)

    >>> def fn2(n):
    ...     if n == 0:
    ...         return 1
    ...     else:
    ...         return n * fn2(n - 1)

    >>> duration_cache = timeit('fn1(500); fn1(400); fn1(450); fn1(350)',
    ...                         globals=globals(), number=10_000)

    >>> duration_nocache = timeit('fn2(500); fn2(400); fn2(450); fn2(350)',
    ...                           globals=globals(), number=10_000)

    >>> duration_ratio = duration_nocache / duration_cache
    >>> print(f'With Cache time: {duration_cache:.4f} seconds')  # this will fail (see point 4)
    >>> print(f'Without Cache time: {duration_nocache:.3f} seconds')  # this will fail (see point 4)
    >>> print(f'Cached solution is {duration_ratio:.1f} times faster')  # this will fail (see point 4)

    TODO: Make tests faster
"""

_cache = {}


def cache(func):
    def wrapper(n):
        return func(n)

    return wrapper


# Solution
def cache(func):
    def wrapper(n):
        if n not in _cache:
            _cache[n] = func(n)
        return _cache[n]

    return wrapper
