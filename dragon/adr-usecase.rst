ADR Template
============

Summary
-------
* Decision: Python backend web framework
* Status: accepted
* Decision Date: 2023-01-01
* Release Date: 2023-01-05
* Deciders: Mark Watney, Melissa Lewis, Rick Martinez


Context and Problem Statement
-----------------------------
* Python backend web framework is needed


Decision Drivers
----------------
* Codebase become unmaintainable
* ORM is needed for refactoring
* Need documentation
* Need REST/JSON API
* Need for tests
* Need for database migrations
* Need for async code
* Need more time-effective way for on-boarding


Considered Options
------------------
* Django
* Django + Ninja
* Django + RESTFramework
* FastAPI
* Flask


Decision Outcome
----------------
* Django + Ninja

Django framework is a first class citizen and well known framework in
Python community. Ninja adds Fast-API style views to Django and automatically
generates documentation in OpenAPI format. Django has ORM, database schema
migration and admin panel. Django supports asynchronous code.


Pros and Cons of the Options
----------------------------
Django:

    * Async
    * ORM
    * DB schema migration
    * Admin
    * No documentation generation

Django + Ninja:

    * Async
    * ORM
    * DB schema migration
    * Admin
    * Documentation generation

Django + RESTFramework:

    * No Async
    * ORM
    * DB schema migration
    * Admin
    * Own documentation generation

FastAPI:

    * Async
    * No ORM
    * No DB schema migration
    * No Admin
    * Documentation generation

Flask:

    * No Async
    * ORM
    * No DB schema migration
    * No Admin
    * No documentation generation


References
----------
* https://www.djangoproject.com/
* https://django-ninja.rest-framework.com/
* https://www.django-rest-framework.org/
* https://fastapi.tiangolo.com/
* https://flask.palletsprojects.com/en/2.2.x/
