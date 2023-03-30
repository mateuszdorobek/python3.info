ADR About
=========
* Decision: Python backend web framework
* Status: accepted
* Decision Date: 2000-01-01
* Release Date: 2000-01-05
* Deciders: Mark Watney, Melissa Lewis, Rick Martinez


Problem
-------
* Python backend web framework is needed
* Need documentation
* Need REST/JSON API
* Need authorization and authentication
* Need admin panel
* Need for tests
* Need for ORM
* Need for database migrations
* Need for async code
* Need more time-effective way for on-boarding


Motivation
----------
* Codebase become unmaintainable
* Current documentation in old
* Onboarding takes too much time
* ORM makes refactoring easier
* ORM standardizes model


Considerations
--------------
* Django
* Django + Ninja
* Django + RESTFramework
* FastAPI
* Flask


Option 1 - Django
-----------------
* Async
* ORM
* DB schema migration
* Admin
* No documentation generation


Option 2 - Django + Ninja
-------------------------
* Async
* ORM
* DB schema migration
* Admin
* Documentation generation


Option 3 - Django + RESTFramework
---------------------------------
* No Async
* ORM
* DB schema migration
* Admin
* Own documentation generation


Option 4 - FastAPI
------------------
* Async
* No ORM
* No DB schema migration
* No Admin
* Documentation generation


Option 5 - Flask
----------------
* No Async
* ORM
* No DB schema migration
* No Admin
* No documentation generation


Decision
--------
* Django + Ninja

Django framework is a first class citizen and well known framework in
Python community. Ninja adds Fast-API style views to Django and automatically
generates documentation in OpenAPI format. Django has ORM, database schema
migration and admin panel. Django supports asynchronous code.


References
----------
* https://www.djangoproject.com/
* https://django-ninja.rest-framework.com/
* https://www.django-rest-framework.org/
* https://fastapi.tiangolo.com/
* https://flask.palletsprojects.com/en/2.2.x/
