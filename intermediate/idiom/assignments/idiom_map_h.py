"""
* Assignment: Idiom Map CSV
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define function `parse(str) -> list[tuple]`
    2. Define `result: map` with function `parse()` applied to `DATA`
    3. Convert numeric values to `float`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `parse(str) -> list[tuple]`
    2. Zdefiniuj `result: map` z funkcją `parse()` zaaplikowaną do `DATA`
    3. Przekonwertuj wartości numeryczne do `float`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.strip()`
    * `str.split()`
    * `str.splitlines()`
    * `map()`
    * `float()`
    * ('hello',) - one element tuple
    * `(1, 2, 3) + ('hello',)` - adding tuples

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is map, \
    'Variable `result` has invalid type, should be map'

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


# values from file (note the tuple format!)
def parse(line):
    ...

# Define `result: map` with function `parse()` applied to `DATA`
# type: map
result = ...


# Solution
def parse(line: str) -> tuple:
    *values, species = line.strip().split(',')
    values = map(float, values)
    return tuple(values) + (species,)

result = map(parse, DATA.splitlines())
