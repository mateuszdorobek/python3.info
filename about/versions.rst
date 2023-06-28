Python Versions
===============
* Since Python 3.9: :pep:`602` -- Annual Release Cycle for Python
* New Python release every 12 months (1 year)
* 12 months (1 year) release cycle
* 18 months (1.5 year) of bugfix updates
* 42 months (3.5 year) of security updates


Python Release Cycle
--------------------
* Since Python 3.9: :pep:`602` -- Annual Release Cycle for Python
* 12 months (1 year) release cycle
* 18 months (1.5 year) of bugfix updates
* 42 months (3.5 year) of security updates

.. figure:: img/pep602-release-calendar.png

    Python 12 months release cycle.


Which Version?
--------------
* You should use newest official Python version [#pyDevVersions]_
* Source: https://devguide.python.org/versions/
* Source: https://www.python.org/downloads/

.. csv-table:: Python Versions [#pyDevGuideVersions]_
    :header: "Version", "PEP", "Status", "Release", "End-of-life", "Release Manager"
    :widths: 5, 15, 10, 20, 20, 30

    "3.13", ":pep:`719`", "future",      "2024-10-01", "2029-10",    "Thomas Wouters"
    "3.12", ":pep:`693`", "features",    "2023-10-03", "2028-10",    "Thomas Wouters"
    "3.11", ":pep:`664`", "bugfix",      "2022-10-24", "2027-10",    "Pablo Galindo Salgado"
    "3.10", ":pep:`619`", "bugfix",      "2021-10-04", "2026-10",    "Pablo Galindo Salgado"
    "3.9",  ":pep:`596`", "security",    "2020-10-05", "2025-10",    "Łukasz Langa"
    "3.8",  ":pep:`569`", "security",    "2019-10-20", "2024-10",    "Łukasz Langa"
    "3.7",  ":pep:`537`", "security",    "2018-06-27", "2023-06-27", "Ned Deily"
    "3.6",  ":pep:`494`", "end-of-life", "2016-12-23", "2021-12-23", "Ned Deily"
    "3.5",  ":pep:`478`", "end-of-life", "2015-09-13", "2020-09-13", "Larry Hastings"
    "3.4",  ":pep:`429`", "end-of-life", "2014-03-16", "2019-03-16", "Larry Hastings"
    "3.3",  ":pep:`398`", "end-of-life", "2012-09-29", "2017-09-29", "Georg Brandl"
    "3.2",  ":pep:`392`", "end-of-life", "2011-02-20", "2016-02-20", "Georg Brandl"
    "3.1",  ":pep:`375`", "end-of-life", "2009-06-27", "2012-04-09", "Benjamin Peterson"
    "3.0",  ":pep:`361`", "end-of-life", "2008-12-03", "2009-01-13", "Barry Warsaw"
    "2.7",  ":pep:`373`", "end-of-life", "2010-07-03", "2020-04-20", "Benjamin Peterson"
    "2.6",  ":pep:`361`", "end-of-life", "2008-10-01", "2013-10-29", "Barry Warsaw"

.. glossary::

    features
        new features, bugfixes, and security fixes are accepted.

    prerelease
        feature fixes, bugfixes, and security fixes are accepted for the
        upcoming feature release.

    bugfix
        bugfixes and security fixes are accepted, new binaries are still
        released. (Also called maintenance mode or stable release)

    security
        only security fixes are accepted and no more binaries are released,
        but new source-only versions can be released

    end-of-life
        release cycle is frozen; no further changes can be pushed to it.


Why not Python 2?
-----------------
* :pep:`373` -- Python 2.7 Release Schedule
* :pep:`404` -- Python 2.8 Un-release Schedule
* 2020-04-20 - end of Life for Python 2.7
* Python 2 is no longer developed [#py2discontinuation1]_, [#py2discontinuation2]_
* Python 2.7 is the last in 2.x branch, and there won't be Python 2.8
* Python 2.7.18, the last release of Python 2 [`3 <https://pythoninsider.blogspot.com/2020/04/python-2718-last-release-of-python-2.html>`_]


References
----------
.. [#py2discontinuation1] https://www.python.org/psf/press-release/pr20191220/
.. [#py2discontinuation2] https://mail.python.org/archives/list/python-dev@python.org/message/N6JIGTTJCJHS47AYSI76SJPCQS25EBWR/
.. [#pyDevVersions] van Rossum, G. et al. How do you specify and enforce an interface spec in Python? Year: 2022. Retrieved: 2022-09-25. URL: https://devguide.python.org/versions/
