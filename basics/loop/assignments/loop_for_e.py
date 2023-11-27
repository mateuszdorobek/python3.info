"""
* Assignment: Loop For Newline
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Define `result: str`
    2. Use `for` to iterate over `DATA`
    3. Join lines of text with newline (`\n`) character
    4. Do not use `str.join()`
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str`
    2. Użyj `for` do iterowania po `DATA`
    3. Połącz linie tekstu znakiem końca linii (`\n`)
    4. Nie używaj `str.join()`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result.count('\\n')
    3

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    'We choose to go to the Moon.\\nWe choose to go to the Moon in this decade
    and do the other things.\\nNot because they are easy, but because they are
    hard.\\n'
"""

DATA = [
    'We choose to go to the Moon.',
    'We choose to go to the Moon in this decade and do the other things.',
    'Not because they are easy, but because they are hard.',
]

# DATA joined with newline - \n
# type: str
result = ...

# Solution
result = ''

for line in DATA:
    result += line + '\n'
