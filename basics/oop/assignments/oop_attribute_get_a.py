"""
* Assignment: OOP Attribute Get
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define `result_mark: dict[str,str]`
       with all attributes and values of `mark` object
    2. Define `result_nasa: dict[str,str]`
       with all attributes and values of `nasa` object
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result_mark: dict[str,str]`
       z wszystkimi atrybutami i wartościami obiektu `mark`
    2. Zdefiniuj `result_nasa: dict[str,str]`
       z wszystkimi atrybutami i wartościami obiektu `nasa`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result_mark) is dict
    >>> assert type(result_nasa) is dict

    >>> result_mark
    {'name': 'Mark', 'country': 'USA', 'date': '1969-07-21'}

    >>> result_nasa
    {'name': 'Nasa', 'country': 'USA', 'date': '1969-07-21'}
"""


class Astronaut:
    name: str
    country: str
    date: str


class SpaceAgency:
    name: str
    country: str
    date: str


mark = Astronaut()
nasa = SpaceAgency()

mark.name = 'Mark'
mark.country = 'USA'
mark.date = '1969-07-21'

nasa.name = 'Nasa'
nasa.country = 'USA'
nasa.date = '1969-07-21'


# Dict with all attributes and values of `mark` object
# type: dict[str,str]
result_mark = ...

# Dict with all attributes and values of `nasa` object
# type: dict[str,str]
result_nasa = ...


# Solution
result_mark = vars(mark)
result_nasa = vars(nasa)
