TOML Use Case
=============


Use Case - 0x01
---------------
.. code-block:: toml

    [project]
    name = "myproject"
    version = "1.0.0"
    requires-python = ">=3.11"
    authors = [{name = "Mark Watney", email = "mwatney@nasa.gov"}]
    readme = "README.md"
    license = {file = "LICENSE"}
    keywords = ["ares", "mars", "nasa", "human-spaceflight"]
    urls.homepage = "https://github.com/myusername/myproject"
    urls.repository = "https://github.com/myusername/myproject.git"
    urls.documentation = "https://github.com/myusername/myproject"
    urls.changelog = "https://github.com/myusername/myproject/releases"
    urls.bugtracker = "https://github.com/myusername/myproject/issues"
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
        "Natural Language :: Polish",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"]
    dependencies = [
        "django == 4.2.*",
        "django-ninja == 0.19.*"]
