Notes
=====

Oneline
-------
.. code-block:: md

    ```plantuml
    class User
    note right: Comment
    ```


Multiline
---------
.. code-block:: md

    ```plantuml
    class User
    note right
      Comment
      Comment
      Comment
    end note
    ```


Directions
----------
.. code-block:: md

    ```plantuml
    class User
    note left: On last defined class
    ```

.. code-block:: md

    ```plantuml
    class User
    note right: On last defined class
    ```

.. code-block:: md

    ```plantuml
    class User
    note top: On last defined class
    ```

.. code-block:: md

    ```plantuml
    class User
    note bottom: On last defined class
    ```


Attached to One Object
----------------------
Notes attached to the particular object

.. code-block:: md

    ```plantuml
    class User

    note top of User: Comment
    ```

.. code-block:: md

    ```plantuml
    class User

    note top of User
      Comment
      Comment
      Comment
    end note
    ```

Attached to Many Objects
------------------------
.. code-block:: md

    ```plantuml
    class User
    class Admin

    note "Two roles in our system" as Comment

    User .. Comment
    Admin .. Comment
    ```

Attributes
----------
.. code-block:: md

    ```plantuml
    class User {
        username: str
        password: str
    }

    note right of User::password
        Password will be encrypted
    end note
    ```

Methods
-------
.. code-block:: md

    ```plantuml
    class User {
        + login()
        + logout()
    }

    note right of User::login
        Logs user in
    end note

    note right of User::logout
        Logs user out
    end note
    ```

Relations
---------
.. code-block:: md

    ```plantuml
    class User
    User <|-- Admin
    note on link: Admin inherits from User
    ```


Floating
--------
.. code-block:: md

    ```plantuml
    class User
    note "This is a floating note" as N1
    ```


Formatting
----------
.. code-block:: md

    ```plantuml
    class object

    note top of object : "In Python, <b>every</b> class\n<u>inherits</u> from <i>object</i>."
    ```

.. code-block:: md

    ```plantuml
    class User
    User <|-- Admin
    note on link #red: Admin inherits from User
    ```
