Database
========


Database schema migration
-------------------------

Makemigrations
--------------
* ``--squash``

.. code-block:: console

    $ python manage.py makemigrations
    Migrations for 'contact':
      addressbook/contact/migrations/0001_initial.py
        - Create model Contact

Migrate
-------
.. code-block:: console

    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, contact, sessions
    Running migrations:
      Applying contact.0001_initial... OK

Management commands
-------------------

dbshell
-------

dumpdata
--------
dumpdata --format json  --exclude=auth --exclude=contenttypes

loaddata
--------

inspectdb
---------

makemigrations
--------------

migrate
-------


Sqlite3
-------
.. code-block:: python

    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'habitatOS.sqlite3'),
        }
    }


PostgreSQL
----------
.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mydatabase',
            'USER': 'mydatabaseuser',
            'PASSWORD': 'mypassword',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

Heroku
------
.. code-block:: python

    if os.environ.get('DATABASE_URL'):
        import dj_database_url
        DATABASES['default'] = dj_database_url.config()


Fixtures
--------
fixtures directory of every installed application


Multiple DB and db routing
--------------------------
