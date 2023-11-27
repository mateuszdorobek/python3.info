"""
* Assignment: Iterable Tuple Mean
* Type: homework
* Complexity: medium
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Calculate mean for each numerical values column
    2. To convert table use multiline select with `alt` key in your IDE
    3. Do not use `str.split()`, `slice`, `getitem`, `for`, `while`
       or any other control-flow statement
    4. Run doctests - all must succeed

Polish:
    1. Wylicz średnią arytmetyczną dla każdej z kolumn numerycznych
    2. Do konwersji tabelki wykorzystaj zaznaczanie wielu linijek
       za pomocą klawisza `alt` w Twoim IDE
    3. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while`
       lub jakiejkolwiek innej instrukcji sterującej
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `mean = sum(...) / len(...)`
    * `ALT` + `left mouse button` = multiple select
    * `ALT` + `SHIFT` + `left mouse button drag` = vertical selection
    * `ALT` + `SHIFT` + `right` = select word to the right (macOS)
    * `ALT` + `SHIFT` + `left` = select word to the left (macOS)
    * `CTRL` + `SHIFT` + `right` = select word to the right (Windows)
    * `CTRL` + `SHIFT` + `left` = select word to the left (Windows)
    * `CTRL` + `right` = jump over the word to the right
    * `CTRL` + `left` = jump over the word to the left
    * `CTRL` + `ALT` + L = Reformat Code on Windows
    * `CMD` + `ALT` + L = Reformat Code on macOS

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert sepal_length is not Ellipsis, \
    'Assign your result to variable `sepal_length`'
    >>> assert sepal_width is not Ellipsis, \
    'Assign your result to variable `sepal_width`'
    >>> assert petal_length is not Ellipsis, \
    'Assign your result to variable `petal_length`'
    >>> assert petal_width is not Ellipsis, \
    'Assign your result to variable `petal_width`'

    >>> assert type(sepal_length) is float, \
    'Variable `sepal_length` has invalid type, should be float'
    >>> assert type(sepal_width) is float, \
    'Variable `sepal_width` has invalid type, should be float'
    >>> assert type(petal_length) is float, \
    'Variable `petal_length` has invalid type, should be float'
    >>> assert type(petal_width) is float, \
    'Variable `petal_width` has invalid type, should be float'

    >>> sepal_length
    5.86

    >>> sepal_width
    3.02

    >>> petal_length
    4.14

    >>> petal_width
    1.34
"""

DATA = [
    'sepal_length,sepal_width,petal_length,petal_width,species',
    '5.8,2.7,5.1,1.9,virginica',
    '5.1,3.5,1.4,0.2,setosa',
    '5.7,2.8,4.1,1.3,versicolor',
    '6.3,2.9,5.6,1.8,virginica',
    '6.4,3.2,4.5,1.5,versicolor',
]

# Arithmetic mean from tuple with 5.8, 5.1, 5.7, 6.3, 6.4
# type: float
sepal_length = ...

# Arithmetic mean from tuple with 2.7, 3.5, 2.8, 2.9, 3.2
# type: float
sepal_width = ...

# Arithmetic mean from tuple with 5.1, 1.4, 4.1, 5.6, 4.5
# type: float
petal_length = ...

# Arithmetic mean from tuple with 1.9, 0.2, 1.3, 1.8, 1.5
# type: float
petal_width = ...

# Solution
sepal_length = (5.8, 5.1, 5.7, 6.3, 6.4)
sepal_width = (2.7, 3.5, 2.8, 2.9, 3.2)
petal_length = (5.1, 1.4, 4.1, 5.6, 4.5)
petal_width = (1.9, 0.2, 1.3, 1.8, 1.5)

sepal_length = sum(sepal_length) / len(sepal_length)
sepal_width = sum(sepal_width) / len(sepal_width)
petal_length = sum(petal_length) / len(petal_length)
petal_width = sum(petal_width) / len(petal_width)
