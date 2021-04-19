"""
* Assignment: About Syntax Newline
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result` with text 'Hello World'
    2. 'Hello' must be in a first line
    3. 'World' must be in a second line

Polish:
    1. Zdefiniuj zmienną `result` z tekstem 'Hello World'
    2. 'Hello' ma być w pierwszej linii
    3. 'World' ma być w drugiej linii

Hint:
    * Either quotes (") or apostrophes (') will work

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> 'Hello' in result
    True
    >>> '\\n' in result
    True
    >>> 'World' in result
    True
"""

result = ...  # str: with Hello and World in separate lines

# Solution
result = 'Hello\nWorld'
