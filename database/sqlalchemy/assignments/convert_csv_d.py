"""
* Assignment: Database Convert ReadTypeCast
* Complexity: easy
* Lines of code: 9 lines
* Time: 8 min

English:
    1. Convert `DATA` to `result: list[tuple[str]]`
    2. Convert numeric values to `float`
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` to `result: list[tuple[str]]`
    2. Przekonwertuj wartości numeryczne do `float`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.strip()`
    * `str.split()`
    * `map()`
    * `list() + list()`
    * `list.append()`
    * `tuple()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is tuple for x in result), \
    'All rows in `result` should be tuple'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
     (5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor')]
"""

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

# data from file (note the list[tuple] format!)
# type: list[tuple]
result = ...

# Solution
result = []
header, *lines = DATA.splitlines()
header = header.strip().split(',')
result.append(tuple(header))

for line in lines:
    *values, species = line.strip().split(',')
    values = map(float, values)
    row = list(values) + [species]
    result.append(tuple(row))
