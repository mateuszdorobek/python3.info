"""
* Assignment: String Methods Join
* Required: no
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Join lines of text with newline (`\n`) character
    2. Run doctests - all must succeed

Polish:
    1. Połącz linie tekstu znakiem końca linii (`\n`)
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.join()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'
    >>> assert result.count('\\n') == 2, \
    'There should be only two newline characters in result'

    >>> line = 'We choose to go to the Moon'
    >>> assert line in result, f'Line "{line}" is not in the result'

    >>> line = 'in this decade and do the other things.'
    >>> assert line in result, f'Line "{line}" is not in the result'

    >>> line = 'Not because they are easy, but because they are hard.'
    >>> assert line in result, f'Line "{line}" is not in the result'
"""

DATA = [
    'We choose to go to the Moon',
    'in this decade and do the other things.',
    'Not because they are easy, but because they are hard.',
]

# Join DATA with newline (`\n`) character
# type: str
result = ...

# Solution
result = '\n'.join(DATA)
