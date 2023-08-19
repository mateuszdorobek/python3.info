Relations
=========


Cardinality
-----------
* ``0`` - Exactly 0
* ``0..1`` - Zero or one
* ``0..n`` - Zero to `n` (where `n` > 1)
* ``0..*`` - Zero or more

* ``1`` - Only one
* ``1..n`` - One to `n` (where `n` > 1)
* ``1..*`` - One or more

* ``*`` - Many
* ``n..n`` - {where n>1}


Association
-----------
is a broad term that encompasses just about any logical connection or 
relationship between classes. For example, passengers and airline may
be linked as above.

.. code-block:: md

    ```plantuml
    class Passengers
    class Airplane

    Passengers -- Airplane
    ```

Directed Association
--------------------
refers to a directional relationship represented by a line with an arrowhead.
The arrowhead depicts a container-contained directional flow.

.. code-block:: md

    ```plantuml
    class Passengers
    class Airplane

    Passengers <-- Airplane
    ```

Reflexive Association
---------------------
This occurs when a class may have multiple functions or responsibilities.
For example, a staff member working in an airport may be a pilot, aviation
engineer, ticket dispatcher, guard, or maintenance crew member. If the
maintenance crew member is managed by the aviation engineer there could
be a managed by relationship in two instances of the same class.

.. code-block:: md

    ```plantuml
    class Staff

    Staff -- Staff: "0..*"
    ```

Multiplicity
------------
is the active logical association when the cardinality of a class in relation
to another is being depicted. For example, one fleet may include multiple
airplanes, while one commercial airplane may contain zero to many passengers.
The notation ``0..*`` in the diagram means "zero to many".

.. code-block:: md

    ```plantuml
    class Passengers
    class Airplane

    Passengers "0" -- "*" Airplane
    ```

.. code-block:: md

    ```plantuml
    class Passengers
    class Airplane

    Passengers "0..*" -- "1..*" Airplane
    ```

.. code-block:: md

    ```plantuml
    class A
    class B

    A -- B: "0..*"
    ```

Aggregation
-----------
refers to the formation of a particular class as a result of one class being
aggregated or built as a collection. For example, the class "library" is made
up of one or more books, among other materials. In aggregation, the contained
classes are not strongly dependent on the lifecycle of the container. In the
same example, books will remain so even when the library is dissolved. To show
aggregation in a diagram, draw a line from the parent class to the child class
with a diamond shape near the parent class.

To show aggregation in a diagram, draw a line from the parent class to the
child class with a diamond shape near the parent class.

.. code-block:: md

    ```plantuml
    class Library
    class Books

    Library o-- Books
    ```

Composition
-----------
The composition relationship is very similar to the aggregation relationship.
with the only difference being its key purpose of emphasizing the dependence
of the contained class to the life cycle of the container class. That is,
the contained class will be obliterated when the container class is destroyed.
For example, a shoulder bag’s side pocket will also cease to exist once the
shoulder bag is destroyed.

To show a composition relationship in a UML diagram, use a directional line
connecting the two classes, with a filled diamond shape adjacent to the
container class and the directional arrow to the contained class.

.. code-block:: md

    ```plantuml
    class Library
    class Books

    Library *-- Books
    ```

Extension (Inheritance)
-----------------------
refers to a type of relationship wherein one associated class is a child
of another by virtue of assuming the same functionalities of the parent
class. In other words, the child class is a specific type of the parent
class. To show inheritance in a UML diagram, a solid line from the child
class to the parent class is drawn using an unfilled arrowhead.

.. code-block:: md

    ```plantuml
    class Account
    class User

    Account <|-- User
    ```

Realization
-----------
denotes the implementation of the functionality defined in one class
by another class. To show the relationship in UML, a broken line with
an unfilled solid arrowhead is drawn from the class that defines the
functionality of the class that implements the function. In the example,
the printing preferences that are set using the printer setup interface
are being implemented by the printer.

.. code-block:: md

    ```plantuml
    class Printer
    class PrinterSetup

    Printer <|.. PrinterSetup
    ```

Other
-----
.. code-block:: md

    ```plantuml
    Class01 "1" *-- "many" Class02 : contains
    Class03 o-- Class04 : aggregation
    Class05 --> "1" Class06
    Class13 --> Class14
    Class19 <--* Class20
    ```

.. code-block:: md

    ```plantuml
    Class91 ^-- Class92
    Class11 <|-- Class12
    Class21 <-- Class22
    Class41 *-- Class42
    Class31 o-- Class32
    Class51 #-- Class52
    Class61 x-- Class62
    Class71 }-- Class72
    Class81 +-- Class82
    ```
