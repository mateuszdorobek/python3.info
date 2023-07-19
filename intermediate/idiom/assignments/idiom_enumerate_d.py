"""
* Assignment: Idiom Zip LabelEncoder
* Complexity: medium
* Lines of code: 3 lines
* Time: 5 min

English:
    1. From `DATA` separate header (first line) from other lines
    2. Split header by comma `,` into:
       a. `nrows` - number of rows
       b. `nfeatures` - number of features
       c. `class_labels` - species names
    3. Generate `result: dict[int,str]` from `class_labels`:
       a. 0: setosa
       b. 1: virginica
       c. 2: versicolor
    4. Use `enumerate()`
    5. Run doctests - all must succeed

Polish:
    1. Z `DATA` odseparuj nagłówek (pierwsza linia) od pozostałych linii
    2. Rozdziel nagłówek po przecinku `,` na:
       a. `nrows` - liczba wierszy
       b. `nfeatures` - liczba cech
       c. `class_labels` - nazwy gatunków
    3. Wygeneruj `result: dict[int,str]` z `class_labels`:
       a. 0: setosa
       b. 1: virginica
       c. 2: versicolor
    4. Użyj `enumerate()`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `dict(enumerate())`
    * `str.splitlines()`
    * `str.split()`
    * `str.strip()`
    * line: "3,4,setosa,virginica,versicolor" is not an error
    * 3 - rows
    * 4 - number of features (values)
    * setosa,virginica,versicolor - if 0 then setosa, if 1 then virginica, etc.

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'
    >>> assert all(type(x) is int for x in result.keys()), \
    'All keys in `result` should be int'
    >>> assert all(type(x) is str for x in result.values()), \
    'All values in `result` should be str'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {0: 'setosa', 1: 'virginica', 2: 'versicolor'}
"""

DATA = """3,4,setosa,virginica,versicolor
5.8,2.7,5.1,1.9,1
5.1,3.5,1.4,0.2,0
5.7,2.8,4.1,1.3,2"""

# values from file (note the list[tuple] format!)
# type: dict[int,str]
result = ...

# Solution
header, *lines = DATA.splitlines()
nrows, ncols, *class_labels = header.strip().split(',')
result = dict(enumerate(class_labels))
