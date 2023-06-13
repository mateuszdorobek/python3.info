"""
* Assignment: OOP MethodClassmethod FromJson
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define class `Movie` with:
        a. Field `title: str`
        b. Field `director: str`
        c. Method `from_json()`
    2. Method `from_json()`:
        a. Parameter `data: str`, example: '{"title":"Martian","director":"Ridley Scott"}'
        b. Returns instance of a class on which was called
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Movie` z:
        a. Polem `title: str`
        b. Polem `director: str`
        c. Metodą `from_json()`
    2. Metoda `from_json()`:
        a. Parametr `data: str`, przykład: '{"title":"Martian","director":"Ridley Scott"}'
        b. Zwraca instancję klasy na której została wykonana
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * json.loads()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Movie)
    >>> assert isclass(ScienceFiction)
    >>> assert isclass(History)
    >>> assert isclass(Adventure)

    >>> MARTIAN = '{"title":"Martian","director":"Ridley Scott"}'
    >>> martian = ScienceFiction.from_json(MARTIAN)
    >>> assert type(martian.title) is str
    >>> assert type(martian.director) is str
    >>> assert martian.title == 'Martian'
    >>> assert martian.director == 'Ridley Scott'

    >>> DUNE = '{"title":"Dune","director":"Denis Villeneuve"}'
    >>> dune = Adventure.from_json(DUNE)
    >>> assert type(dune.title) is str
    >>> assert type(dune.director) is str
    >>> assert dune.title == 'Dune'
    >>> assert dune.director == 'Denis Villeneuve'

    >>> RIGHT_STUFF = '{"title":"The Right Stuff","director":"Philip Kaufman"}'
    >>> right_stuff = History.from_json(RIGHT_STUFF)
    >>> assert type(right_stuff.title) is str
    >>> assert type(right_stuff.director) is str
    >>> assert right_stuff.title == 'The Right Stuff'
    >>> assert right_stuff.director == 'Philip Kaufman'
"""
import json


class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

# Method `from_json()` with parameter: `data: str`
# Method `from_json()` returns instance of a class on which was called
# type: Callable[[type[Self]], Self]
    def from_json(self):
        ...


class ScienceFiction(Movie):
    pass


class History(Movie):
    pass


class Adventure(Movie):
    pass


# Solution
class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    @classmethod
    def from_json(cls, data: str):
        values = json.loads(data)
        return cls(**values)


class ScienceFiction(Movie):
    pass

class History(Movie):
    pass

class Adventure(Movie):
    pass
