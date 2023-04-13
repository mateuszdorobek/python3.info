Theory UML ERD
==============
* UML - Unified Modeling Language
* ERD - Entity Relationship Diagram

.. figure:: img/uml-erd-1.png
.. figure:: img/uml-erd-2.png


Entities vs Attributes
----------------------
* Entities - rows in database
* Attributes - columns in database

.. figure:: img/uml-erd-entities,attributes.png


Cardinality
-----------
.. figure:: img/uml-erd-cardinality.png

Cardinality:

.. csv-table:: Cardinality
    :header: left, right, description
    :widths: 10, 10, 80

    ``|o``, ``o|``, zero or one
    ``||``, ``||``, exactly one
    ``}o``, ``o{``, zero or more (no upper limit)
    ``}|``, ``|{``, one or more (no upper limit)

Relationship:

.. csv-table:: Cardinality
    :header: cardinality, relationship
    :widths: 10, 90

    ``||..||``, one to one
    ``||..|{``, one to many
    ``}|..||``, many to one
    ``}|..|{``, many to many


Entity Relationship Diagram
---------------------------
* ERD - Entity Relationship Diagram [#mermaidERD]_
* By drawing a line between tables we show, that there is a connection between them in some way
* English: "crows foot notation"
* Polish: "notacja kurzych stóp"

.. figure:: img/uml-erd-astronaut,assignment,mission,role.png

Right:

* ``ASSIGNMENT`` relates to ``one MISSION``
* ``ASSIGNMENT`` assigns ``one ASTRONAUT``
* ``ASSIGNMENT`` defines ``one ROLE``

Left:

* ``MISSION`` is related to ``zero or many ASSIGNMENT``
* ``ASTRONAUT`` is assigned to ``zero or many ASSIGNMENT``
* ``ROLE`` is defined in ``one ASSIGNMENT``

.. code-block:: md

    ```mermaid
    erDiagram

    ASSIGNMENT }o..|| MISSION : "relates to"
    ASSIGNMENT }o..|| ASTRONAUT : "assigns"
    ASSIGNMENT ||..|| ROLE : "defines"

    ASSIGNMENT {
        primary_key id
        foreign_key mission_id
        foreign_key astronaut_id
        str role
    }

    ROLE {
        primary_key id
        str name
    }

    ASTRONAUT {
        primary_key id
        str firstName
        str lastName
        int age
    }

    MISSION {
        primary_key id
        int year
        int name
    }
    ```

.. figure:: img/uml-erd-export.png


Mermaid
-------
* ``mermaid`` - Markdown extension [#mermaidAbout]_

Theming [#mermaidTheme]_:

.. code-block:: md

    %%{init: { 'theme': 'dark' } }%%
    %%{init: { 'theme': 'forest' } }%%

Config [#mermaidConfig]_:

.. code-block:: md

    %%{init: { 'logLevel': 'debug' } }%%
    %%{config: { 'fontFamily': 'Menlo', 'fontSize': 18, 'fontWeight': 400} }%%

.. csv-table:: CSS classes
    :header: "Selector", "Description"
    :widths: 33, 67

    ".er.attributeBoxEven",      "The box containing attributes on even-numbered rows"
    ".er.attributeBoxOdd",       "The box containing attributes on odd-numbered rows"
    ".er.entityBox",             "The box representing an entity"
    ".er.entityLabel",           "The label for an entity"
    ".er.relationshipLabel",     "The label for a relationship"
    ".er.relationshipLabelBox",  "The box surrounding a relationship label"
    ".er.relationshipLine",      "The line representing a relationship between entities"


Use Case - 0x01
---------------
.. code-block:: md

    ```mermaid
    erDiagram

    CUSTOMER }|..|{ DELIVERY-ADDRESS : has
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER ||--o{ INVOICE : "liable for"
    DELIVERY-ADDRESS ||--o{ ORDER : receives
    INVOICE ||--|{ ORDER : covers
    ORDER ||--|{ ORDER-ITEM : includes
    PRODUCT-CATEGORY ||--|{ PRODUCT : contains
    PRODUCT ||--o{ ORDER-ITEM : "ordered in"
    ```

.. figure:: img/uml-erd-mermaid-usecase1.png


Use Case - 0x02
---------------
.. figure:: img/uml-erd-3.png
.. figure:: img/uml-erd-4.jpg
.. figure:: img/uml-erd-5.png
.. figure:: img/uml-erd-6.jpg


References
----------
.. [#mermaidAbout] Sveidqvist, Knut et al. Mermaid Documentation: About. Year: 2022. Retrieved: 2022-01-26. URL: https://mermaid-js.github.io/mermaid/#/README
.. [#mermaidTheme] Sveidqvist, Knut et al. Mermaid Documentation: Theming. Year: 2022. Retrieved: 2022-01-26. URL: https://mermaid-js.github.io/mermaid/#/theming
.. [#mermaidConfig] Sveidqvist, Knut et al. Mermaid Documentation: SyntaxReference. Year: 2022. Retrieved: 2022-01-26. URL: https://mermaid-js.github.io/mermaid/#/n00b-syntaxReference
.. [#mermaidERD] Sveidqvist, Knut et al. Mermaid Documentation: Entity Relationship Diagrams. Year: 2022. Retrieved: 2022-01-26. URL: https://mermaid-js.github.io/mermaid/#/entityRelationshipDiagram
