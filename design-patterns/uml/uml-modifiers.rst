Access Modifiers
================

Public
------
.. code-block:: md

    ```plantuml
    class User {
        + firstname
        + lastname
    }
    ```


Protected
---------
.. code-block:: md

    ```plantuml
    class User {
        # email
        # phone
    }
    ```


Private
-------
.. code-block:: md

    ```plantuml
    class User {
        - username
        - password
    }
    ```


Package Private
---------------
.. code-block:: md

    ```plantuml
    class User {
        ~ author
        ~ version
    }
    ```
