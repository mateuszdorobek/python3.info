"""
* Assignment: OOP AttributeAccessModifiers Members
* Complexity: easy
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Extract from class `User` attribute names and their values:
        a. Define `protected: dict` with protected attributes
        b. Define `private: dict` with private attributes
        c. Define `public: dict` with public attributes
    2. Run doctests - all must succeed

Polish:
    1. Wydobądź z klasy `User` nazwy atrybutów i ich wartości:
        a. Zdefiniuj `protected: dict` z atrybutami chronionymi (protected)
        b. Zdefiniuj `private: dict` z atrybutami prywatnymi (private)
        c. Zdefiniuj `public: dict` z atrybutami publicznymi (public)
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(public) is dict
    >>> assert all(type(k) is str for k,v in public.items())
    >>> assert all(type(v) is str for k,v in public.items())

    >>> assert type(protected) is dict
    >>> assert all(type(k) is str for k,v in protected.items())
    >>> assert all(type(v) is str for k,v in protected.items())

    >>> assert type(private) is dict
    >>> assert all(type(k) is str for k,v in private.items())
    >>> assert all(type(v) is str for k,v in private.items())

    >>> assert len(public) > 0, \
    'public: list[dict] must not be empty'

    >>> assert len(protected) > 0, \
    'protected: list[dict] must not be empty'

    >>> assert len(private) > 0, \
    'private: list[dict] must not be empty'

    >>> public
    {'firstname': 'Mark', 'lastname': 'Watney'}

    >>> protected
    {'_email': 'mwatney@nasa.gov', '_phone': '+1 (234) 555 1337'}

    >>> private
    {'_User__username': 'mwatney', '_User__password': 'Ares3'}

"""
from dataclasses import dataclass


@dataclass
class User:
    def __init__(self, firstname, lastname, email, phone, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self._email = email
        self._phone = phone
        self.__username = username
        self.__password = password


DATA = User(
    firstname='Mark',
    lastname='Watney',
    email='mwatney@nasa.gov',
    phone='+1 (234) 555 1337',
    username='mwatney',
    password='Ares3',
)

# All public attributes and their values
# type: dict[str,float|str]
public = ...

# All protected attributes and their values
# type: dict[str,float|str]
protected = ...

# All private attributes and their values
# type: dict[str,str]
private = ...

# Solution
public = {attrname: attrvalue
          for attrname, attrvalue in vars(DATA).items()
          if not attrname.startswith('_')}

protected = {attrname: attrvalue
             for attrname, attrvalue in vars(DATA).items()
             if attrname.startswith('_')
             and not attrname.startswith(f'_User__')}

private = {attrname: attrvalue
           for attrname, attrvalue in vars(DATA).items()
           if attrname.startswith(f'_User__')}
