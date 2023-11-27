"""
* Assignment: Star Assignment Nested
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Separate values from species name
    2. Use star expression
    3. Run doctests - all must succeed

Polish:
    1. Odseparuj wartości od nazwy gatunku
    2. Użyj wyrażenia z gwiazdką
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert values is not Ellipsis, \
    'Assign result to variable: `values`'
    >>> assert species is not Ellipsis, \
    'Assign result to variable: `species`'
    >>> assert len(values) > 0, \
    'Variable `values` cannot be empty'
    >>> assert len(species) > 0, \
    'Variable `species` cannot be empty'
    >>> assert type(values) is list, \
    'Variable `values` has invalid type, should be list'
    >>> assert type(species) is str, \
    'Variable `species` has invalid type, should be str'
    >>> assert all(type(x) is float for x in values), \
    'All rows in `values` should be float'

    >>> values
    [5.1, 3.5, 1.4, 0.2]

    >>> species
    'setosa'
"""

DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

# All numeric values from DATA
# type: list[float]
values = ...

# species name from DATA (last element)
# type: str
species = ...

# Solution
*values, species = DATA
