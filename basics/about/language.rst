Python Language
===============
* Turing complete, general purpose language
* Multi platform
* Dynamic typing with automatic memory allocation and GC
* Code readability and simplicity is important
* White space are important
* Everything is an object, but you can write functional code too
* Standard language in Machine Learning and Data Science
* Very good standard system library
* Huge ecosystem of external open source libraries
* Open Source created by non-profit Python Software Foundation

.. figure:: img/python-logo.png

    Python Logo


Which Version?
--------------
* You should use newest official Python version [#pyDevGuideVersions]_
* Source: https://devguide.python.org/#status-of-python-branches
* Source: https://www.python.org/downloads/

.. csv-table:: Python Versions [#pyDevGuideVersions]_
    :header: "Version", "PEP", "Status", "Release", "End-of-life", "Release Manager"
    :widths: 5, 15, 10, 20, 20, 30

    "3.12", "TBA",        "future",      "2023-10",    "2028-10",    "TBA"
    "3.11", ":pep:`664`", "features",    "2022-10-03", "2027-10",    "Pablo Galindo Salgado"
    "3.10", ":pep:`619`", "bugfix",      "2021-10-04", "2026-10",    "Pablo Galindo Salgado"
    "3.9",  ":pep:`596`", "security",      "2020-10-05", "2025-10",    "Łukasz Langa"
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
* Python 2 is no longer developed [`1 <https://www.python.org/psf/press-release/pr20191220/>`_, `2 <https://mail.python.org/archives/list/python-dev@python.org/message/N6JIGTTJCJHS47AYSI76SJPCQS25EBWR/>`_]
* Python 2.7 is the last in 2.x branch, and there won't be Python 2.8
* Python 2.7.18, the last release of Python 2 [`3 <https://pythoninsider.blogspot.com/2020/04/python-2718-last-release-of-python-2.html>`_]


Changes in Python 3
-------------------
* All strings are Unicode
* In Python 3 ``print()`` is a function, not a keyword
* Changes in standard library modules naming and location
* New string formatting


Python Release Cycle
--------------------
* Since Python 3.9: :pep:`602` -- Annual Release Cycle for Python
* 12 months (1 year) release cycle
* 18 months (1.5 year) of bugfix updates
* 42 months (3.5 year) of security updates

.. figure:: img/pep602-release-calendar.png

    Python 12 months release cycle.


Scripts
-------
* Python files use ``.py`` as an extension
* Compiled files are in ``__pycache__`` directory
* Python also uses other extensions

.. csv-table:: Python file types and extensions
    :header-rows: 1
    :widths: 15, 85

    "Extension", "Description"
    "``.pyc``", "Compiled source code (bytecode)"
    "``.pyd``", "Compiled Windows DLL file"
    "``.pyw``", "Compiled Windows file. Executable with ``pythonw.exe``"
    "``.pyx``", "cPythona source for C/C++ conversion"
    "``.pyz``", "`zipapp <https://docs.python.org/3/library/zipapp.html>`_ compressed archive"


Python Console (REPL)
---------------------
* Read–Eval–Print Loop
* Quickly test and evaluate code
* Lines starts with ``>>>``
* Line continuation starts with ``...``
* Result is printed below
* Open REPL with ``python3`` command in terminal

.. code-block:: console

    $ python3.10
    Python 3.10.0 (default, Oct 13 2021, 06:45:00) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    >>> print('Ehlo World!')
    Ehlo World!

In documentation and books you may find ``>>>`` and ``...`` at the beginning of code listing lines

>>> if True:
...     print('yes')
... else:
...     print('no')
yes


Jupyter
-------
* Open Source web application REPL
* Very popular in Machine Learning and Data Science world
* Create and share documents that contain live code, equations, visualizations
  and narrative text
* Uses include: data cleaning and transformation, numerical simulation,
  statistical modeling, data visualization, machine learning, etc


Python Developer Survey
-----------------------
* Annual survey
* https://www.jetbrains.com/lp/python-developers-survey-2020/
* https://www.jetbrains.com/lp/devecosystem-2020/python/
* https://www.jetbrains.com/lp/python-developers-survey-2019/
* https://www.jetbrains.com/research/python-developers-survey-2018/
* https://www.jetbrains.com/research/python-developers-survey-2017/
* https://insights.stackoverflow.com/survey/2020
* https://insights.stackoverflow.com/survey/2019
* https://insights.stackoverflow.com/survey/2018


References
----------
.. [#pyDevGuideVersions] https://devguide.python.org/#status-of-python-branches

Assignments
-----------
.. literalinclude:: assignments/about_language_a.py
    :caption: :download:`Solution <assignments/about_language_a.py>`
    :end-before: # Solution
