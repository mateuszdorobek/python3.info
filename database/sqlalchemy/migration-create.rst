Migration Create
================


Initialize
----------
.. code-block:: console

    $ alembic init migrations
      Creating directory /tmp/project/migrations/versions ...  done
      Generating /tmp/project/migrations/script.py.mako ...  done
      Generating /tmp/project/migrations/env.py ...  done
      Generating /tmp/project/migrations/README ...  done
      Generating /tmp/project/migrations/alembic.ini ...  done
      Please edit configuration/connection/logging settings in '/tmp/project/migrations/alembic.ini' before proceeding.

Configure
---------
.. code-block:: console

    $ vim alembic.ini +55
    $ grep 'sqlalchemy.url' alembic.ini
    sqlalchemy.url = sqlite:///tmp.db


Initial Revision
----------------
.. code-block:: console

    $ alembic revision -m "Initial revision"
      Generating /tmp/project/migrations/versions/ad4de013e007_initial_revision.py ...  done


Upgrade
-------
.. code-block:: console

    $ alembic upgrade heads
    INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.runtime.migration] Running upgrade  -> ad4de013e007, Initial revision

.. code-block:: console

    # Show alembic where you have your ORM models
    # Set proper value for ``target_metadata``
    $ vim env.py +18


Autogenerate
------------
.. code-block:: console

    $ alembic revision --autogenerate -m "User Model"
    INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.autogenerate.compare] Detected added table 'user'
      Generating /private/tmp/project/versions/21fa69deb961_user_model.py ...  done


Upgrade
-------
.. code-block:: console

    $ alembic upgrade head
    INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.runtime.migration] Running upgrade ad4de013e007 -> 21fa69deb961, User Model

.. code-block:: console

    $ alembic upgrade 21fa69deb961  # you can also use shorter, but still unique hash


Downgrade
---------
.. code-block:: console

    $ alembic downgrade <hash>
    $ alembic downgrade -1  # one revision back
