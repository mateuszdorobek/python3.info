ADR Example
===========
* Decision: Python backend web framework
* Status: accepted
* Decision Date: 2000-01-01
* Release Date: 2000-01-05
* Deciders: Mark Watney, Melissa Lewis, Rick Martinez


Problem
-------
* Python backend web framework is needed


Motivation
----------
* Codebase become unmaintainable
* Current documentation in old
* Need API documentation auto-generation
* Need REST/JSON API
* Need authorization and authentication
* Need admin panel
* Need for tests
* Need for ORM
* Need for database migrations
* Need for async code
* Need more time-effective way for on-boarding of new employees
* Onboarding takes too much time
* ORM makes refactoring easier
* ORM standardizes data model


Considerations
--------------
* FastAPI
* Flask
* Django (+Ninja)

Source: https://lp.jetbrains.com/python-developers-survey-2022/#FrameworksLibraries


Option 1 - FastAPI
------------------
* Good: Easy
* Good: Fast onboarding
* Good: Async
* Good: API documentation auto-generation
* Good: Worldwide adoption (on hype)
* Bad: New project
* Bad: No ORM
* Bad: No DB schema migration
* Bad: No Admin
* Bad: Single-person driven project (single point of failure)
* Bad: No steering committee
* Decision: rejected, no ORM


Option 2 - Flask
----------------
* Good: Easy
* Good: Fast onboarding
* Good: ORM (as separate package)
* Good: Mature project
* Good: Async since 2.0
* Bad: FastAPI took his hype
* Bad: No DB schema migration
* Bad: No Admin
* Bad: No API documentation auto-generation
* Decision: rejected, no schema migration


Option 3 - Django + Ninja
-------------------------
* Good: Async
* Good: ORM
* Good: DB schema migration
* Good: Admin
* Good: API documentation auto-generation (Ninja)
* Good: FastAPI style REST/JSON views (Ninja)
* Good: Steering committee (no single point of failure)
* Bad: Intermediate
* Bad: More complex than FastAPI and Flask
* Decision: candidate


Decision
--------
* Django + Ninja

Django framework is a first class citizen and well known framework in
Python community. Ninja adds FastAPI style views to Django and automatically
generates documentation in OpenAPI format. Django has ORM, database schema
migration and admin panel. Django supports asynchronous code. Good community
support big players included (Instagram, Youtube).


References
----------
* https://lp.jetbrains.com/python-developers-survey-2022/#FrameworksLibraries
* https://www.djangoproject.com/
* https://django-ninja.rest-framework.com/
* https://www.django-rest-framework.org/
* https://fastapi.tiangolo.com/
* https://flask.palletsprojects.com/en/2.2.x/
