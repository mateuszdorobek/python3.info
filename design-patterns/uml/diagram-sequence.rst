UML Sequence Diagram
====================
* https://mermaid-js.github.io/mermaid/#/sequenceDiagram


Connections
-----------
* ``->`` - Solid line without arrow
* ``-->`` - Dotted line without arrow
* ``->>`` - Solid line with arrowhead
* ``-->>`` - Dotted line with arrowhead
* ``-x`` - Solid line with a cross at the end (async)
* ``--x`` - Dotted line with a cross at the end (async)


Conversation
------------
.. code-block:: md

    ```mermaid
    sequenceDiagram

        participant Alice
        participant Bob

        Alice ->> Bob: Hello, how are you?
        Bob -->> Alice: Great!
    ```

.. figure:: img/uml-mermaid-sequencediagram-alicebob.png


Nested
------
.. code-block:: md

    ```mermaid
    sequenceDiagram

        participant Client
        participant Server
        participant Database

        activate Client
        Client ->> +Server: HTTP Request
        Server ->> +Database: SQL Query
        Database -->> -Server: Result
        Server -->> -Client: HTTP Response
        deactivate Client
    ```

.. figure:: img/uml-mermaid-sequencediagram-web.png


Async
-----
.. code-block:: md

    ```mermaid
    sequenceDiagram

    participant Client
    participant Server
    participant Database

    activate Client

    Client -x +Server: HTTP Request
    Client -x Server: HTTP Request
    Server ->> +Database: SQL Query
    Client -x Server: HTTP Request
    Client -x Server: HTTP Request
    Client -x Server: HTTP Request

    Database -->> -Server: Result

    Server --x -Client: HTTP Response

    deactivate Client
    ```

.. todo:: generate image from mermaid code


Rationale
---------
.. figure:: img/uml-sequencediagram-1.png
.. figure:: img/uml-sequencediagram-2.jpg
