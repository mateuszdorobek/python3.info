Prototype
=========
* EN: Prototype
* PL: Prototyp
* Type: object


Pattern
-------
* Create new object by copying an existing object

.. figure:: img/designpatterns-prototype-pattern.png

.. literalinclude:: uml/designpatterns-prototype-pattern.md
    :language: md


Problem
-------
* Violates Open/Close Principle

.. figure:: img/designpatterns-prototype-problem.png

.. literalinclude:: uml/designpatterns-prototype-problem.md
    :language: md

.. literalinclude:: src/designpatterns-prototype-problem.py
    :language: python


Solution
--------
.. figure:: img/designpatterns-prototype-solution.png

.. literalinclude:: uml/designpatterns-prototype-solution.md
    :language: md

.. literalinclude:: src/designpatterns-prototype-solution.py
    :language: python


Assignments
-----------
Task 1:

* Create file ``designpatterns_prototype_a.py``
* Create class ``Date`` with method ``.clone()``
* Method ``.clone()`` returns the same date

Task 2:

* Create file ``designpatterns_prototype_a.py``
* Create class ``Time`` with method ``.clone()``
* Method ``.clone()`` returns the same date

.. todo:: Assignments
          You're building a video editor similar to Adobe Premier.
          The editor contains a timeline of various types of components
          such as text, clips, audio, and so on. The user should be able
          to duplicate any component. The duplicated component should be
          added to the timeline. Look at the implementation of the ContextMenu
          class in the prototype package of the Exercises project. What are
          the problems in the current implementation?Refactor the code using
          the prototype pattern. What have you achieved?
