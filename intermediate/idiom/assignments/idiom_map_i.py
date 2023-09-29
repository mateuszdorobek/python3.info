"""
* Assignment: Idiom Map ReadTypeCast
* Complexity: easy
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Define `class_labels: list[str]` from header (species names)
    2. Define `label_encoder: dict[int,str]` converting `class_labels`
       (species name index is the last digit in the line)
    3. Define function `parse(str) -> list[tuple]`
    4. Define `result: map` with function `parse()` applied to `DATA`
    5. Convert numeric values to `float`
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `class_labels: list[str]` z nagłówka (nazwy gatunków)
    2. Zdefiniuj `label_encoder: dict[int,str]` przekształcając `class_labels`
       (indeks nazwy gatunku to ostatnia cyfra w linii)
    3. Zdefiniuj funckję `parse(str) -> list[tuple]`
    4. Zdefiniuj `result: map` z funkcją `parse()` zaaplikowaną do `DATA`
    5. Przekonwertuj wartości numeryczne do `float`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.splitlines()`
    * `str.strip()`
    * `str.split()`
    * `result, *others = 1, 2, 3, 4`
    * `dict()`
    * `enumerate()`
    * `map()`
    * `float()`
    * `('hello',)` - one element tuple
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

DATA = """3,4,setosa,virginica,versicolor
5.8,2.7,5.1,1.9,1
5.1,3.5,1.4,0.2,0
5.7,2.8,4.1,1.3,2"""

header, *lines = DATA.splitlines()
nrows, nfeatures, *class_labels = header.strip().split(',')
label_encoder = dict(enumerate(class_labels))

def parse(line):
    ...

result = ...

# Solution
def parse(line: str) -> tuple[float,float,float,float,str]:
    *values, species = line.split(',')
    values = map(float, values)
    species = label_encoder[int(species)]
    return tuple(values) + (species,)

result = map(parse, lines)
