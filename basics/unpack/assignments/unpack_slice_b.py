"""
* Assignment: Iterable Slice Substr
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use `str.find()` and slicing
    2. Print `TEXT` without fragment from `REMOVE`
    3. Output should be: 'We choose the Moon!'
    4. Do not use `str.replace()`
    5. Run doctests - all must succeed

Polish:
    1. Użyj `str.find()` oraz wycinania
    2. Wypisz `TEXT` bez fragmentu znajdującego się w `REMOVE`
    3. Wynik powinien być: 'We choose the Moon!'
    4. Nie używaj `str.replace()`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result
    'We choose the Moon!'
"""

TEXT = 'We choose to go to the Moon!'
REMOVE = 'to go to '

# String with TEXT without REMOVE part
# type: str
result = ...

# Solution
a = TEXT.find(REMOVE)  # 10
b = a + len(REMOVE)  # 19
result = TEXT[:a] + TEXT[b:]
