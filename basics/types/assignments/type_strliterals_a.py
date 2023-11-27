"""
* Assignment: String Literals Emoticon
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Print `Hello 😀`
    2. Run doctests - all must succeed

Polish:
    1. Wypisz `Hello 😀`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 😀 unicode codepoint is `\U0001F600`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> '😀' in result
    True
    >>> result
    'Hello 😀'
"""

# Expected result: 'Hello 😀'
# type: str
result = ...

# Solution
result = 'Hello \U0001F600'
