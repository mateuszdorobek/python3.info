HTTP API Versioning
===================
* Always version API
* Have stable API!
* Do not use plural in resources
* Use HTTP Statuses
* Use HTTP Methods

.. epigraph:: Latest is the greatest! -- Old programmers joke


Version names
-------------
* Semantic versioning
* Django versioning
* alpha
* beta
* rc (release candidate)
* gm (golden master)


Semantic Versioning
-------------------
* https://semver.org/
* 2.0.0
* MAJOR.MINOR.PATCH
* MAJOR version when you make incompatible API changes,
* MINOR version when you add functionality in a backwards compatible manner, and
* PATCH version when you make backwards compatible bug fixes.
* Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.


Django Versioning
-----------------
* 2.0 (experimental)
* 2.1 (stabilization
* 2.2 (long term support)
* 3.0 (experimental)
* 3.1 (stabilization
* 3.2 (long term support)
* 4.0 (experimental)
* 4.1 (stabilization
* 4.2 (long term support)


API Policy
----------
* Deprecation Policy
* Phasing (sunset date)
* Darkening
* PendingDeprecation
* Deprecated

>>> import warnings
>>>
>>> def add(a,b):
...     a + b
>>>
>>> def sumuj(a,b):
...     warnings.warn('Użyj funkcji add()', PendingDeprecationWarning)
...     return add(1,2)
>>>
>>>
>>> sumuj(1, 2)
>>> add(1,2)


Controlling
-----------
* OAuth apps
* Basic Auth
* JWT (bearer)
* Rate limiting (throttling)
* https://api.github.com/users/astromatt/repos


How to version API?
-------------------
.. csv-table:: How to version API?
    :header: "Example", "Description"
    :widths: 50,50

    "``https://example.com/api/v2/user/10``", "API version as a part of URL"
    "``https://example.com/user/10?api=v2``", "Version as a parameter to URL"
    "``https://api-v2.example.com``", "Subdomain"
    "``https://api.example.com/v2/``", "Subdomain+URL"
    "``X-API-VERSION: 2``", "Version as a custom header with ``X-...`` prefix"
    "``Accept: application/vnd.api.v2``", "API version as a custom vendor prefix for ``Accept`` header"
    "``Accept: application/vnd.api.v2;q=0.9,application/vnd.api.v1;q=0.8``", "API version negotiation with weights using ``Accept`` header"


Use Case - 0x01
---------------
.. code-block:: console

    $ curl http://localhost:8000/user/1 -H 'X-API-VERSION: 1.0'
    {"name": "Mark Watney"}

.. code-block:: console

    $ curl http://localhost:8000/user/1 -H 'X-API-VERSION: 2.0'
    {"firstname": "Mark", "lastname": "Watney"}


Use Case - 0x02
---------------
.. code-block:: text

    https://jira.atlassian.com/rest/api/1/issue/JRA-9
    https://jira.atlassian.com/rest/api/2/issue/JRA-9
    https://jira.atlassian.com/rest/api/latest/issue/JRA-9
