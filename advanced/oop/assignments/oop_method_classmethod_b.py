"""
* Assignment: OOP MethodClassmethod FromCsv
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define class `Iris` with:
        a. Field `sepal_length: float`
        b. Field `sepal_width: float`
        c. Field `petal_length: float`
        d. Field `petal_width: float`
        e. Field `species: str`
        f. Method `from_csv()` with parameter: `line: datetime`
    2. Method `from_csv()` returns instance of a class on which was called
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Iris` z:
        a. Polem `sepal_length: float`
        b. Polem `sepal_width: float`
        c. Polem `petal_length: float`
        d. Polem `petal_width: float`
        e. Polem `species: str`
        f. Metodą `from_csv()` z parametrem `line: str`
    2. Metoda `from_csv()` zwraca instancję klasy na której została wykonana
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * str.split()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Iris)
    >>> assert isclass(Setosa)
    >>> assert isclass(Versicolor)
    >>> assert isclass(Virginica)
"""

class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species


# Method `from_csv()` with parameter: `line: datetime`
# Method `from_csv()` returns instance of a class on which was called
# type: Callable[[type[Self], str], Self]
    def from_csv():
        ...


class Setosa(Iris):
    pass


class Virginica(Iris):
    pass


class Versicolor(Iris):
    pass


# Solution
class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    @classmethod
    def from_csv(cls, line):
        values = line.split(',')
        return cls(*values)


class Setosa(Iris):
    pass


class Virginica(Iris):
    pass


class Versicolor(Iris):
    pass
