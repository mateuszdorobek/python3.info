Attributes
==========


.. code-block:: md

    ```plantuml
    class User {
        username: str
        password: str
        login() -> None
        logout() -> None
    }
    ```


Instance Variables
------------------

.. code-block:: md

    ```plantuml
    class User {
        {field} firstname: str
        {field} lastname: str
    }
    ```


Class Variables
---------------
.. code-block:: md

    ```plantuml
    class User {
        {static} AGE_MAX: int
        {static} AGE_MIN: int
    }
    ```


Abstract Properties
-------------------
.. code-block:: md

    ```plantuml
    class User {
        {abstract} role
        {abstract} group
    }
    ```

Methods
-------
.. code-block:: md

    ```plantuml
    class User {
        {method} login()
        {method} logout()
    }
    ```


Grouping
--------
.. code-block:: md

    ```plantuml
    class User {
        .. Personal Info ..
        firstname: str
        lastname: str
        email: str
        .. Account Info ..
        username: str
        password: str
      ==
      .. Setters ..
      + set_firstname()
      + set_lastname()
      + set_email()
      + set_username()
      + set_password()
      .. Getters ..
      + get_firstname()
      + get_lastname()
      + get_email()
      + get_username()
      + get_password()
      __ Methods __
      + login()
      + logout()
    }
    ```
