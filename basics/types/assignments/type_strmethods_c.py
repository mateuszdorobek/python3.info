"""
* Assignment: String Methods Normalize
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Use `str` methods to clean `DATA`
    2. Run doctests - all must succeed

Polish:
    1. Wykorzystaj metody `str` do oczyszczenia `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result
    'Pana Twardowskiego III'
"""

DATA = 'UL. pana \tTWArdoWskIEGO 3'

# Expected result: 'Pana Twardowskiego III'
# type: str
result = ...

# Solution
result = (
    DATA
    .upper()
    .removeprefix('UL.')
    .replace('\t', '')
    .strip()
    .title()
    .replace('3', 'III')
)
