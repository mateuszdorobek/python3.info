Datetime Standards
==================
* Date and time formats varies from country to country [#wikiDateTimeFormats]_


Date
----
Formal date format in USA [#wikiDateFormatUS]_:

.. code-block:: text

    4/12/61
    April 12, 1961

Formal date format in Japan [#wikiDateFormatJapan]_:

.. code-block:: text

    61/04/12
    1961年04月12日

    20/12/31
    平成20年12月31日

Formal date format in Germany:

.. code-block:: text

    12.04.1961

Date format in Poland:

.. code-block:: text

    12 kwietnia 1961
    12 kwiecień 1961

    12 IV 1961
    12.IV.1961

    12.4.1961
    12.04.1961

    12/4/1961
    12/04/1961

    12-04-1961
    1961-04-12

Which format is a formal standard in Poland? [#wikiISO8601]_


Time
----
* 24 and 12 hour clock
* Confusion at noon and midnight

24 and 12 hour clock:

    .. code-block:: text

        5:00 AM
        5:00 PM
        5:00
        17:00


Zero padded
-----------
* Zero padded minutes, seconds and microseconds but not hours
* Variable length microseconds

.. code-block:: text

    06:07       # ok
    6:07        # ok
    6:7         # error

.. code-block:: text

    06:07:00    # ok
    6:07:00     # ok
    6:07:0      # error
    6:07:       # error
    6:07        # ok

.. code-block:: text

    6:07:00.000001
    6:07:00.123456
    6:07:00.123
    6:07:00.1


Noon and Midnight
-----------------
* Which time is a midnight?
* Which time is a noon?

.. code-block:: text

    00:00
    12:00
    24:00


AM vs PM
--------
* What AM stands for?
* What PM stands for?
* Which time is a midnight?
* Which time is a noon?
* Confusion at noon and midnight [#wikiNoonMidnight]_

.. code-block:: text

    12:00 am
    12:00 pm


Roman Numerals
--------------
.. code-block:: text

    IV
    IIII



Leap Second
-----------
* UTC leap second [#wikiLeapSecond]_
* Leap second discontinuation post 2035 [#natureLeapSecond]_
* Issues created by insertion (or removal) of leap seconds
* Calculation of time differences and sequence of events
* Missing leap seconds announcement
* Implementation differences
* Textual representation of the leap second
* Binary representation of the leap second
* Other reported software problems associated with the leap second
* June 30th or December 31st
* Introduced in 1972
* Last leap second in 2016

Normal second:

.. code-block:: text

    23:59:59
    00:00:00

Leap Second:

.. code-block:: text

    23:59:59
    23:59:60
    00:00:00


Times after 24:00
-----------------
* Times after 24:00 [#wikiTimesAfter2400]_

.. code-block:: text

    00:00:00 - 23:59:59.999999...   # almost midnight
    00:00:00 - 24:00:00             # until midnight

.. code-block:: text

    23:00 - 25:30   # 2h 30m
    14:00 - 26:00   # 12h


Decimal Time
------------
* Unix time gives date and time as the number of seconds since January 1, 1970
* Microsoft's FILETIME as multiples of 100ns since January 1, 1601 [#wikiMetricTime]_
* VAX/VMS uses the number of 100ns since November 17, 1858 [#wikiMetricTime]_
* RISC OS the number of centiseconds since January 1, 1900 [#wikiMetricTime]_


Other
-----
* Military time [#wikiMilitaryTime]_
* Military time zones [#wikiMilitaryTimezones]_
* Swatch Internet Time - Beats @300 [#wikiSwatchInternetTime]_
* sidereal day on Earth is approximately 86164.0905 seconds (23 h 56 min 4.0905 s or 23.9344696 h)


Calendars
---------
* Julian Calendar [#wikiJulianCalendar]_
* Gregorian Calendar [#wikiGregorianCalendar]_
* Introduced by Pope Gregory XIII in October 1582
* Last country (Saudi Arabia) adopted Julian calendar in 2016
* List of adoption dates of the Gregorian calendar by country [#wikiGregorianCalendarAdoption]_
* There are only four countries which have not adopted the Gregorian calendar: Ethiopia (Ethiopian calendar), Nepal (Vikram Samvat and Nepal Sambat), Iran and Afghanistan (Solar Hijri calendar)


Astronomy
---------
* Synodic day - the period for a celestial object to rotate once in relation to the star it is orbiting [#wikiSynodicDay]_
* Solar time - calculation of the passage of time based on the position of the Sun in the sky [#wikiSolarTime]_
* Epoch (astronomy) [#wikiEpochAstronomy]_
* Sidereal Time [#wikiSiderealTime]_
* JD - Julian Day [#wikiJulianDay]_


Space Industry
--------------
* UTC - Coordinated Universal Time [#wikiCoordinatedUniversalTime]_
* GMT - Greenwich Mean Time [#wikiGreenwichMeanTime]_
* MET - Mission Elapsed Time
* Relativistic effects
* Time dilatation due to speed approaching speed of light


Planet Mars
-----------
* MSD - Mars Sol Date [#wikiMarsSolDate]_
* MTC - Coordinated Mars Time [#wikiCoordinatedMarsTime]_
* Timekeeping on Mars [#wikiTimekeepingOnMars]_
* Mars Clock [#wikiMarsClock]_
* Martian sidereal day is 24 h 37 m 22.663 s (88,642.663 seconds)
* Martian solar day is 24 h 39 m 35.244 s (88,775.244 seconds)


References
----------
.. [#natureLeapSecond] Gibney, E. The leap second's time is up: world votes to stop pausing clocks. Year: 2022. Retrieved: 2022-11-18. URL: https://www.nature.com/articles/d41586-022-03783-5 DOI: https://doi.org/10.1038/d41586-022-03783-5
.. [#wikiGregorianCalendarAdoption]  Wikipedia. List of adoption dates of the Gregorian calendar by country. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/List_of_adoption_dates_of_the_Gregorian_calendar_by_country
.. [#wikiGregorianCalendar]  Wikipedia. Gregorian Calendar. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Gregorian_calendar
.. [#wikiSiderealTime]  Wikipedia. Sidereal Time. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Sidereal_time
.. [#wikiEpochAstronomy]  Wikipedia. Epoch Astronomy. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Epoch_(astronomy)
.. [#wikiJulianDay]  Wikipedia. Julian Day. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Julian_day
.. [#wikiSwatchInternetTime]  Wikipedia. Swatch Internet Time. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Swatch_Internet_Time
.. [#wikiJulianCalendar]  Wikipedia. Julian Calendar. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Julian_calendar
.. [#wikiSolarTime]  Wikipedia. Solar Time. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Solar_time
.. [#wikiSynodicDay]  Wikipedia. Synodic Day. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Synodic_day
.. [#wikiGreenwichMeanTime]  Wikipedia. Greenwich Mean Time. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Greenwich_Mean_Time
.. [#wikiMarsClock]  Wikipedia. Mars Clock. Year: 2022. Retrieved: 2022-05-10. URL: https://marsclock.com/
.. [#wikiCoordinatedUniversalTime]  Wikipedia. Coordinated Universal Time. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Coordinated_Universal_Time
.. [#wikiTimekeepingOnMars]  Wikipedia. Timekeeping On Mars. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Timekeeping_on_Mars
.. [#wikiMarsSolDate]  Wikipedia. Timekeeping On Mars - Mars Sol Date. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Timekeeping_on_Mars#Mars_Sol_Date
.. [#wikiCoordinatedMarsTime]  Wikipedia. Timekeeping On Mars - Coordinated Mars Time. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Timekeeping_on_Mars#Coordinated_Mars_Time
.. [#wikiMetricTime] Wikipedia. Metric time. Leap Second. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Metric_time
.. [#wikiLeapSecond] Wikipedia. Leap Second. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Leap_second
.. [#wikiDateTimeFormats] Wikipedia. Date Time Formats. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Date_format_by_country
.. [#wikiNoonMidnight] Wikipedia. Noon Midnight. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/12-hour_clock#Confusion_at_noon_and_midnight
.. [#wikiTimesAfter2400] Wikipedia. Times After 2400. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/24-hour_clock#Times_after_24:00
.. [#wikiMilitaryTime] Wikipedia. Military Time. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/24-hour_clock#Military_time
.. [#wikiMilitaryTimezones] Wikipedia. Military Timezones. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/List_of_military_time_zones
.. [#wikiISO8601] Wikipedia. ISO8601. Year: 2022. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/ISO_8601
.. [#wikiDateFormatJapan] Date and time notation in Japan. Wikipedia. Year: 2022. Retrieved: 2019-06-27. URL: https://en.wikipedia.org/wiki/Date_and_time_notation_in_Japan#Date
.. [#wikiDateFormatUS] Date and time notation in the United States. Wikipedia. Year: 2022. Retrieved: 2019-06-27. URL: https://en.wikipedia.org/wiki/Date_and_time_notation_in_the_United_States
