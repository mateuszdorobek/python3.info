"""
* Assignment: Functional About CSV
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Convert `DATA` to `result: map`
    2. Convert numeric values to `float`
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` to `result: map`
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
    >>> assert type(result) is map, \
    'Variable `result` has invalid type, must be a map'

    >>> result = list(result)  # expand map object
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is tuple for x in result), \
    'All rows in `result` should be tuple'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor')]
"""

DATA = """5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

# values from file (note the list[tuple] format!)
# type: map
result = ...

# Solution
def parse(line: str) -> tuple[float,float,float,float,str]:
    *values, species = line.strip().split(',')
    values = map(float, values)
    return tuple(values) + (species,)


result = map(parse, DATA.splitlines())
