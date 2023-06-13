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
        f. Method `from_csv()`
    2. Method `from_csv()`:
        a. Parameter `data: str`, example: '5.8,2.7,5.1,1.9,virginica'
        b. Returns instance of a class on which was called
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Iris` z:
        a. Polem `sepal_length: float`
        b. Polem `sepal_width: float`
        c. Polem `petal_length: float`
        d. Polem `petal_width: float`
        e. Polem `species: str`
        f. Metodą `from_csv()`
    2. Metoda `from_csv()`:
        a. Parametr `data: str`, przykład: '5.8,2.7,5.1,1.9,virginica'
        b. Zwraca instancję klasy na której została wykonana
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

    >>> data = '5.8,2.7,5.1,1.9,virginica'
    >>> virginica = Iris.from_csv(data)
    >>> assert type(virginica.sepal_length) is float
    >>> assert type(virginica.sepal_width) is float
    >>> assert type(virginica.petal_length) is float
    >>> assert type(virginica.petal_width) is float
    >>> assert type(virginica.species) is str
    >>> assert virginica.sepal_length == 5.8
    >>> assert virginica.sepal_width == 2.7
    >>> assert virginica.petal_length == 5.1
    >>> assert virginica.petal_width == 1.9
    >>> assert virginica.species == 'virginica'

    >>> data = '5.1,3.5,1.4,0.2,setosa'
    >>> setosa = Iris.from_csv(data)
    >>> assert type(setosa.sepal_length) is float
    >>> assert type(setosa.sepal_width) is float
    >>> assert type(setosa.petal_length) is float
    >>> assert type(setosa.petal_width) is float
    >>> assert type(setosa.species) is str
    >>> assert setosa.sepal_length == 5.1
    >>> assert setosa.sepal_width == 3.5
    >>> assert setosa.petal_length == 1.4
    >>> assert setosa.petal_width == 0.2
    >>> assert setosa.species == 'setosa'

    >>> data = '5.7,2.8,4.1,1.3,versicolor'
    >>> versicolor = Iris.from_csv(data)
    >>> assert type(versicolor.sepal_length) is float
    >>> assert type(versicolor.sepal_width) is float
    >>> assert type(versicolor.petal_length) is float
    >>> assert type(versicolor.petal_width) is float
    >>> assert type(versicolor.species) is str
    >>> assert versicolor.sepal_length == 5.7
    >>> assert versicolor.sepal_width == 2.8
    >>> assert versicolor.petal_length == 4.1
    >>> assert versicolor.petal_width == 1.3
    >>> assert versicolor.species == 'versicolor'
"""

class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species


# Method `from_csv()` with parameter: `data: str`
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
    def from_csv(cls, data):
        *values, species = data.split(',')
        values = map(float, values)
        data = tuple(values) + (species,)
        return cls(*data)


class Setosa(Iris):
    pass


class Virginica(Iris):
    pass


class Versicolor(Iris):
    pass
