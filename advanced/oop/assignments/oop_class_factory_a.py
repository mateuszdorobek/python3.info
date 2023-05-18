"""
* Assignment: OOP ClassFactory Iris
* Complexity: medium
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Create `result: list[Iris]`
    2. Iterate over `DATA` skipping header
    3. Separate `features` from `species` in each row
    4. Append to `result`:
        a. if `species` is "setosa" append instance of a class `Setosa`
        b. if `species` is "versicolor" append instance of a class `Versicolor`
        c. if `species` is "virginica" append instance of a class `Virginica`
    5. Initialize instances with `features` using `*args` notation
    6. Run doctests - all must succeed

Polish:
    1. Stwórz `result: list[Iris]`
    2. Iterując po `DATA` pomijając header
    3. Odseparuj `features` od `species` w każdym wierszu
    4. Dodaj do `result`:
        a. jeżeli `species` jest "setosa" to dodaj instancję klasy `Setosa`
        b. jeżeli `species` jest "versicolor" to dodaj instancję klasy `Versicolor`
        c. jeżeli `species` jest "virginica" to dodaj instancję klasy `Virginica`
    5. Instancje inicjalizuj danymi z `features` używając notacji `*args`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `globals()[classname]`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> list(result)  # doctest: +NORMALIZE_WHITESPACE
    [Virginica(5.8, 2.7, 5.1, 1.9),
     Setosa(5.1, 3.5, 1.4, 0.2),
     Versicolor(5.7, 2.8, 4.1, 1.3),
     Virginica(6.3, 2.9, 5.6, 1.8),
     Versicolor(6.4, 3.2, 4.5, 1.5),
     Setosa(4.7, 3.2, 1.3, 0.2)]
"""

from dataclasses import dataclass


DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


@dataclass(repr=False)
class Iris:
    _sepal_length: float
    _sepal_width: float
    _petal_length: float
    _petal_width: float

    def __repr__(self):
        name = self.__class__.__name__
        args = tuple(self.__dict__.values())
        return f'{name}{args}'


# Append to `result`:
# Use type() to create classes dynamically
# a. if `species` is "setosa" append instance of a class `Setosa`
# b. if `species` is "versicolor" append instance of a class  `Versicolor`
# c. if `species` is "virginica" append instance of a class `Virginica`
# type: list[Iris]
result = ...


# Solution
def factory(row):
    *features, species = row
    clsname = species.capitalize()
    cls = type(clsname, (Iris,), {})
    return cls(*features)

result = map(factory, DATA[1:])


# Alternative Solution
result = [cls(*values)
          for *values,species in DATA[1:]
          if (clsname := species.capitalize())
          and (cls := type(clsname, (Iris,), {}))]
