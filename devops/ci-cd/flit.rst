Flit
====

Config
------
* ``pyproject.toml``
* Source: https://github.com/tiangolo/fastapi/blob/master/pyproject.toml

.. code-block:: toml

    [build-system]
    requires = ["flit"]
    build-backend = "flit.buildapi"

    [tool.flit.metadata]
    module = "fastapi"
    author = "Sebastián Ramírez"
    author-email = "tiangolo@gmail.com"
    home-page = "https://github.com/tiangolo/fastapi"
    classifiers = [
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: AsyncIO",
        "Framework :: FastAPI",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP",
    ]
    requires = [
        "starlette==0.19.1",
        "pydantic >=1.6.2,!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0",
    ]
    description-file = "README.md"
    requires-python = ">=3.6.1"

    [tool.flit.metadata.urls]
    Documentation = "https://fastapi.tiangolo.com/"

    [tool.flit.metadata.requires-extra]
    test = [
        "pytest >=6.2.4,<7.0.0",
        "pytest-cov >=2.12.0,<4.0.0",
        "mypy ==0.910",
        "flake8 >=3.8.3,<4.0.0",
        "black == 22.3.0",
        "isort >=5.0.6,<6.0.0",
        "requests >=2.24.0,<3.0.0",
        "httpx >=0.14.0,<0.19.0",
        "email_validator >=1.1.1,<2.0.0",
        "sqlalchemy >=1.3.18,<1.5.0",
        "peewee >=3.13.3,<4.0.0",
        "databases[sqlite] >=0.3.2,<0.6.0",
        "orjson >=3.2.1,<4.0.0",
        "ujson >=4.0.1,!=4.0.2,!=4.1.0,!=4.2.0,!=4.3.0,!=5.0.0,!=5.1.0,<6.0.0",
        "python-multipart >=0.0.5,<0.0.6",
        "flask >=1.1.2,<3.0.0",
        "anyio[trio] >=3.2.1,<4.0.0",

        # types
        "types-ujson ==4.2.1",
        "types-orjson ==3.6.2",
        "types-dataclasses ==0.6.5; python_version<'3.7'",
    ]
    doc = [
        "mkdocs >=1.1.2,<2.0.0",
        "mkdocs-material >=8.1.4,<9.0.0",
        "mdx-include >=1.4.1,<2.0.0",
        "mkdocs-markdownextradata-plugin >=0.1.7,<0.3.0",
        # TODO: upgrade and enable typer-cli once it supports Click 8.x.x
        # "typer-cli >=0.0.12,<0.0.13",
        "typer >=0.4.1,<0.5.0",
        "pyyaml >=5.3.1,<7.0.0",
    ]
    dev = [
        "python-jose[cryptography] >=3.3.0,<4.0.0",
        "passlib[bcrypt] >=1.7.2,<2.0.0",
        "autoflake >=1.4.0,<2.0.0",
        "flake8 >=3.8.3,<4.0.0",
        "uvicorn[standard] >=0.12.0,<0.18.0",
        "pre-commit >=2.17.0,<3.0.0",
    ]
    all = [
        "requests >=2.24.0,<3.0.0",
        "jinja2 >=2.11.2,<4.0.0",
        "python-multipart >=0.0.5,<0.0.6",
        "itsdangerous >=1.1.0,<3.0.0",
        "pyyaml >=5.3.1,<7.0.0",
        "ujson >=4.0.1,!=4.0.2,!=4.1.0,!=4.2.0,!=4.3.0,!=5.0.0,!=5.1.0,<6.0.0",
        "orjson >=3.2.1,<4.0.0",
        "email_validator >=1.1.1,<2.0.0",
        "uvicorn[standard] >=0.12.0,<0.18.0",
    ]
