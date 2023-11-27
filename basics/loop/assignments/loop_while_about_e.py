"""
* Assignment: Loop While Translate
* Type: class assignment
* Complexity: medium
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Use `while` to iterate over `DATA`
    2. If letter is in `PL` then use conversion value as letter
    3. Add letter to `result`
    4. Run doctests - all must succeed

Polish:
    1. Użyj `while` do iteracji po `DATA`
    2. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera
    3. Dodaj literę do `result`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'str'>
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
result = ''
i = 0

while i < len(DATA):
    letter = DATA[i]
    result += PL.get(letter, letter)
    i += 1
