"""
* Assignment: Comprehension List Translate
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use list comprehension to iterate over `DATA`
    2. If letter is in `PL` then use conversion value as letter
    3. Add letter to `result`
    4. Run doctests - all must succeed

Polish:
    1. Użyj rozwinięcia listowego do iteracji po `DATA`
    2. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera
    3. Dodaj literę do `result`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.join()`
    * `dict.get()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str

    >>> result
    'zazolc gesla jazn'
"""

PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

DATA = 'zażółć gęślą jaźń'

# DATA with substituted PL diacritic chars to ASCII letters
# type: str
result = ...

# Solution
result = ''.join(PL.get(x, x) for x in DATA)
