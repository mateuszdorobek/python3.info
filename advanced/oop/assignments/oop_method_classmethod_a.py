"""
* Assignment: OOP MethodClassmethod FromTuple
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Define class `Book` with:
        a. Field `title: str`
        b. Field `author: str`
        c. Method `from_tuple()` with parameter: `data: tuple[str,str]`
    2. Method `from_tuple()` returns instance of a class on which was called
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Book` z:
        a. Polem `title: str`
        b. Polem `author: str`
        c. Metodą `from_tuple()` z parametrem `data: tuple[str,str]`
    2. Metoda `from_tuple()` zwraca instancję klasy na której została wykonana
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Book)
    >>> assert isclass(ScienceFiction)
    >>> assert isclass(History)
    >>> assert isclass(Adventure)

    >>> MARTIAN = ('Martian', 'Andy Weir')
    >>> martian = ScienceFiction.from_tuple(MARTIAN)
    >>> assert martian.title == 'Martian'
    >>> assert martian.author == 'Andy Weir'

    >>> DUNE = ('Dune', 'Frank Herbert')
    >>> dune = Adventure.from_tuple(DUNE)
    >>> assert dune.title == 'Dune'
    >>> assert dune.author == 'Frank Herbert'

    >>> RIGHT_STUFF = ('The Right Stuff', 'Tom Wolfe')
    >>> right_stuff = History.from_tuple(RIGHT_STUFF)
    >>> assert right_stuff.title == 'The Right Stuff'
    >>> assert right_stuff.author == 'Tom Wolfe'
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Method `from_tuple()` with parameter: `data: tuple[str,str]`
# Method `from_tuple()` returns instance of a class on which was called
# type: Callable[[type[Self], tuple[str, str]], Self]
    def from_tuple():
        ...


class ScienceFiction(Book):
    pass


class History(Book):
    pass


class Adventure(Book):
    pass


# Solution
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_tuple(cls, data: tuple[str,str]):
        title = data[0]
        author = data[1]
        return cls(title, author)


class ScienceFiction(Book):
    pass

class History(Book):
    pass

class Adventure(Book):
    pass
