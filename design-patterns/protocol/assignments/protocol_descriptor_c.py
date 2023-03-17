"""
* Assignment: Protocol Descriptor Inheritance
* Complexity: medium
* Lines of code: 47 lines
* Time: 21 min

English:
    1. Define class `GeographicCoordinate`
    2. Use descriptors to check value boundaries
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `GeographicCoordinate`
    2. Użyj deskryptory do sprawdzania wartości brzegowych
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> place1 = GeographicCoordinate(50, 120, 8000)
    >>> place1
    GeographicCoordinate(latitude=50, longitude=120, elevation=8000)

    >>> place2 = GeographicCoordinate(22, 33, 44)
    >>> place2
    GeographicCoordinate(latitude=22, longitude=33, elevation=44)

    >>> place1.latitude = 1
    >>> place1.longitude = 2
    >>> place1
    GeographicCoordinate(latitude=1, longitude=2, elevation=8000)

    >>> place2
    GeographicCoordinate(latitude=22, longitude=33, elevation=44)

    >>> GeographicCoordinate(90, 0, 0)
    GeographicCoordinate(latitude=90, longitude=0, elevation=0)
    >>> GeographicCoordinate(-90, 0, 0)
    GeographicCoordinate(latitude=-90, longitude=0, elevation=0)
    >>> GeographicCoordinate(0, +180, 0)
    GeographicCoordinate(latitude=0, longitude=180, elevation=0)
    >>> GeographicCoordinate(0, -180, 0)
    GeographicCoordinate(latitude=0, longitude=-180, elevation=0)
    >>> GeographicCoordinate(0, 0, +8848)
    GeographicCoordinate(latitude=0, longitude=0, elevation=8848)
    >>> GeographicCoordinate(0, 0, -10994)
    GeographicCoordinate(latitude=0, longitude=0, elevation=-10994)

    >>> GeographicCoordinate(-91, 0, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(+91, 0, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, -181, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, +181, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, 0, -10995)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, 0, +8849)
    Traceback (most recent call last):
    ValueError: Out of bounds
"""
from dataclasses import dataclass


@dataclass
class GeographicCoordinate:
    """
    latitude - min: -90.0, max: 90.0
    longitude - min: -180.0, max: 180.0
    elevation - min: -10994.0, max: 8848.0
    """


# Solution
from abc import ABC, abstractproperty


class GEOProperty(ABC):
    _fieldname: str

    @abstractproperty
    def MIN(self) -> float:
        pass

    @abstractproperty
    def MAX(self) -> float:
        pass

    def __set_name__(self, owner, attrname):
        self._fieldname = f'__{attrname}'

    def __set__(self, instance, newvalue):
        if self.MIN <= newvalue <= self.MAX:
            setattr(instance, self._fieldname, newvalue)
        else:
            raise ValueError('Out of bounds')

    def __get__(self, instance, *args):
        return getattr(instance, self._fieldname)


class Latitude(GEOProperty):
    MIN: float = -90.0
    MAX: float = +90.0


class Longitude(GEOProperty):
    MIN: float = -180.0
    MAX: float = +180.0


class Elevation(GEOProperty):
    MIN: float = -10994.0
    MAX: float = +8848.0


@dataclass
class GeographicCoordinate:
    latitude: float = Latitude()
    longitude: float = Longitude()
    elevation: float = Elevation()
