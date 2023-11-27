"""
* Assignment: Syntax Comments Line
* Type: class assignment
* Complexity: easy
* Lines of code: 1 line
* Time: 2 min

English:
    1. Add line comment: This is my first Python script
    2. Run doctests - all must succeed

Polish:
    1. Dodaj komentarz liniowy: This is my first Python script
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> result = open(__file__).read()

    >>> assert '# This is my first Python script' in result, \
    'Please write proper line comment'
"""

# Solution

# This is my first Python script
