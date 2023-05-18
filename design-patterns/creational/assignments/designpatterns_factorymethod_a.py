"""
* Assignment: DesignPatterns Creational FactoryMethod
* Complexity: easy
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Create abstract factory `iris` producing instances of `Iris`
    2. Separate `values` from `species` in each row
    3. Create instances of:
        a. class `Setosa` if `species` is "setosa"
        b. class `Versicolor` if `species` is "versicolor"
        c. class `Virginica` if `species` is "virginica"
    4. Initialize instances with `values`
    5. Run doctests - all must succeed

Polish:
    1. Stwórz fabrykę abstrakcyjną `iris` tworzącą instancje klasy `Iris`
    2. Odseparuj `values` od `species` w każdym wierszu
    3. Stwórz instancje:
        a. klasy `Setosa` jeżeli `species` to "setosa"
        b. klasy `Versicolor` jeżeli `species` to "versicolor"
        c. klasy `Virginica` jeżeli `species` to "virginica"
    4. Instancje inicjalizuj danymi z `values`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `globals()[classname]`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result = map(iris, DATA[1:])
    >>> pprint(list(result), width=120)
    [Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
     Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
     Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
     Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
     Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
     Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2)]
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


@dataclass
class Iris:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class Setosa(Iris):
    pass

class Versicolor(Iris):
    pass

class Virginica(Iris):
    pass


# Skip header and separate `values` from `species` in each row
# Create instances of: `Setosa`, `Versicolor`, `Virginica` based on `species`
# Initialize instances with `values`
# type: Callable[[tuple[float,float,float,float,str], Iris]]
def iris(row: tuple[float,float,float,float,str]) -> Iris:
    ...


# Solution
def iris(row: tuple[float,float,float,float,str]) -> Iris:
    *values, species = row
    match species:
        case 'setosa':     return Setosa(*values)
        case 'virginica':  return Virginica(*values)
        case 'versicolor': return Versicolor(*values)


# Solution 2
def iris(row: tuple[float,float,float,float,str]) -> Iris:
    *values, species = row
    if species == 'setosa':
        return Setosa(*values)
    elif species == 'virginica':
        return Virginica(*values)
    elif species == 'versicolor':
        return Versicolor(*values)


# Solution 3
def iris(row: tuple[float,float,float,float,str]) -> Iris:
    *values, species = row
    classname = species.capitalize()
    cls = globals()[classname]
    return cls(*values)
