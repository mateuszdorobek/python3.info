"""
* Assignment: Syntax Comments Inline
* Type: class assignment
* Complexity: easy
* Lines of code: 1 line
* Time: 2 min

English:
    1. Add inline comment to `alone_on_mars` variable definition
       with content: Space Pirate
    2. Run doctests - all must succeed

Polish:
    1. Dodaj komentarz na końcu linii do definicji zmiennej `alone_on_mars`
       treść: Space Pirate
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> result = open(__file__).read()

    >>> assert type(alone_on_mars) is str, \
    'Variable `alone_on_mars` has invalid type, should be str'
    >>> assert "alone_on_mars = 'Mark Watney'  # Space Pirate" in result, \
    'Please write proper inline comment'

    >>> assert alone_on_mars == 'Mark Watney', \
    'Do not change the value of the `alone_on_mars` variable.'
"""

alone_on_mars = 'Mark Watney'

# Solution
alone_on_mars = 'Mark Watney'  # Space Pirate
