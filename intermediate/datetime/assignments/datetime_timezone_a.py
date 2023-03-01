"""
* Assignment: Datetime Timezone ZoneInfo
* Complexity: easy
* Lines of code: 13 lines
* Time: 13 min

English:
    0. If you're on Windows then install module `tzdata` (`pip install tzdata`)
    1. Create `zoneinfo.ZoneInfo` object of:
        a. UTC
        b. London, United Kingdom
        c. Buenos Aires, Argentina
        d. Warsaw, Poland
        e. Tokyo, Japan
        f. Sydney, Australia
        g. Auckland, New Zealand
        h. New York, USA
    2. Use `List of tz database time zones` [1]
    3. Run doctests - all must succeed

Polish:
    0. Jeżeli masz Windows to zainstaluj moduł `tzdata` (`pip install tzdata`)
    1. Stwórz obiekt `zoneinfo.ZoneInfo` z:
        a. UTC
        b. London, Wielka Brytania
        c. Buenos Aires, Argentyna
        d. Warsaw, Polska
        e. Tokyo, Japan
        f. Sydney, Australia
        g. Auckland, Nowa Zelandia
        h. New York, USA
    2. Użyj `List of tz database time zones` [1]
    3. Uruchom doctesty - wszystkie muszą się powieść

Extra Task:
    1. Cape Canaveral, FL, USA
    2. Houston, TX, USA
    3. Bajkonur Cosmodrome, Kazachstan
    4. North Pole
    5. South Pole (Henryk Arctowski Polish Antarctic Station)

References:
    [1] Wikipedia. List of tz database time zones.
        Retrieved: 2022-12-01
        Year: 2022
        URL: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    [2] IANA. Time Zone Database.
        Retrieved: 2022-12-01
        Year: 2022
        URL: https://data.iana.org/time-zones/releases/

Hints:
    * https://en.wikipedia.org/wiki/Time_in_Antarctica

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from datetime import datetime

    >>> assert utc is not Ellipsis, \
    'Assign value to variable `utc` has instead of Ellipsis (...)'
    >>> assert london is not Ellipsis, \
    'Assign value to variable `london` instead of Ellipsis (...)'
    >>> assert buenos_aires is not Ellipsis, \
    'Assign value to variable `buenos_aires` instead of Ellipsis (...)'
    >>> assert warsaw is not Ellipsis, \
    'Assign value to variable `warsaw` instead of Ellipsis (...)'
    >>> assert tokyo is not Ellipsis, \
    'Assign value to variable `tokyo` instead of Ellipsis (...)'
    >>> assert sydney is not Ellipsis, \
    'Assign value to variable `sydney` instead of Ellipsis (...)'
    >>> assert auckland is not Ellipsis, \
    'Assign value to variable `auckland` instead of Ellipsis (...)'
    >>> assert new_york is not Ellipsis, \
    'Assign value to variable `new_york` instead of Ellipsis (...)'
    >>> assert cape_canaveral is not Ellipsis, \
    'Assign value to variable `cape_canaveral` instead of Ellipsis (...)'
    >>> assert houston is not Ellipsis, \
    'Assign value to variable `houston` instead of Ellipsis (...)'
    >>> assert bajkonur is not Ellipsis, \
    'Assign value to variable `bajkonur` instead of Ellipsis (...)'
    >>> assert north_pole is not Ellipsis, \
    'Assign value to variable `north_pole` instead of Ellipsis (...)'
    >>> assert south_pole is not Ellipsis, \
    'Assign value to variable `south_pole` instead of Ellipsis (...)'

    >>> assert isinstance(utc, ZoneInfo), \
    'Variable `utc` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(london, ZoneInfo), \
    'Variable `london` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(buenos_aires, ZoneInfo), \
    'Variable `buenos_aires` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(warsaw, ZoneInfo), \
    'Variable `warsaw` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(tokyo, ZoneInfo), \
    'Variable `tokyo` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(sydney, ZoneInfo), \
    'Variable `sydney` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(auckland, ZoneInfo), \
    'Variable `auckland` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(new_york, ZoneInfo), \
    'Variable `new_york` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(cape_canaveral, ZoneInfo), \
    'Variable `cape_canaveral` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(houston, ZoneInfo), \
    'Variable `houston` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(bajkonur, ZoneInfo), \
    'Variable `bajkonur` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(north_pole, ZoneInfo), \
    'Variable `north_pole` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(south_pole, ZoneInfo), \
    'Variable `south_pole` has invalid type, must be a ZoneInfo'

    >>> def utcoffset(tz: ZoneInfo):
    ...     dt = datetime(2023, 1, 1)
    ...     return tz.utcoffset(dt).total_seconds()
    >>>
    >>> assert utcoffset(utc) == 0, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(london) == 0, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(buenos_aires) == -10800.0, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(warsaw) == 3600, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(tokyo) == 32400, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(sydney) == 39600, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(auckland) == 46800, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(new_york) == -18000.0, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(cape_canaveral) == -18000.0, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(houston) == -21600.0, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(bajkonur) == 21600, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(north_pole) == 3600, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(south_pole) == 3600, \
    'Invalid time zone, check IANA Time Zone Database'
"""

from zoneinfo import ZoneInfo


# Timezone in UTC
# type: ZoneInfo
utc = ...

# Timezone in London, United Kingdom
# type: ZoneInfo
london = ...

# Timezone in Buenos Aires, Argentina
# type: ZoneInfo
buenos_aires = ...

# Timezone in Warsaw, Poland
# type: ZoneInfo
warsaw = ...

# Timezone in Tokyo, Japan
# type: ZoneInfo
tokyo = ...

# Timezone in Sydney, Australia
# type: ZoneInfo
sydney = ...

# Timezone in Auckland, New Zealand
# type: ZoneInfo
auckland = ...

# Timezone in New York, USA
# type: ZoneInfo
new_york = ...

# Timezone in Cape Canaveral, FL, USA
# type: ZoneInfo
cape_canaveral = ...

# Timezone in Houston, TX, USA= ...
# type: ZoneInfo
houston = ...

# Timezone in Bajkonur Cosmodrome, Kazachstan
# type: ZoneInfo
bajkonur = ...

# Timezone in North Pole
# type: ZoneInfo
north_pole = ...

# Timezone in South Pole
# type: ZoneInfo
south_pole = ...

# Solution
utc = ZoneInfo('UTC')
london = ZoneInfo('Europe/London')
buenos_aires = ZoneInfo('America/Argentina/Buenos_Aires')
warsaw = ZoneInfo('Europe/Warsaw')
tokyo = ZoneInfo('Asia/Tokyo')
sydney = ZoneInfo('Australia/Sydney')
auckland = ZoneInfo('Pacific/Auckland')
new_york = ZoneInfo('America/New_York')

cape_canaveral = ZoneInfo('America/New_York')
houston = ZoneInfo('America/Chicago')
bajkonur = ZoneInfo('Asia/Almaty')
north_pole = ZoneInfo('Arctic/Longyearbyen')
south_pole = ZoneInfo('Europe/Warsaw')
