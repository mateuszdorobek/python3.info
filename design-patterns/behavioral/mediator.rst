Mediator
========
* EN: Mediator
* PL: Mediator
* Type: object


Pattern
-------
* Input fields which needs to collaborate
* Cannot submit form if all required fields are not filled
* If you select article in list of articles, editor form with current article content and title gets populated
* Auto slug-field based on title content

.. figure:: img/designpatterns-mediator-pattern.png

.. literalinclude:: uml/designpatterns-mediator-pattern.md
    :language: md


Problem
-------
.. figure:: img/designpatterns-mediator-problem.png

.. literalinclude:: uml/designpatterns-mediator-problem.md
    :language: md

.. literalinclude:: src/designpatterns-mediator-problem.py
    :language: python


Solution
--------
.. figure:: img/designpatterns-mediator-solution-1.png
.. figure:: img/designpatterns-mediator-solution-2.png

.. literalinclude:: uml/designpatterns-mediator-solution.md
    :language: md

.. literalinclude:: src/designpatterns-mediator-solution-1.py
    :language: python

.. literalinclude:: src/designpatterns-mediator-solution-2.py
    :language: python
    :caption: Mediator with Observer Pattern


Assignments
-----------
.. literalinclude:: assignments/designpatterns_mediator_a.py
    :caption: :download:`Solution <assignments/designpatterns_mediator_a.py>`
    :end-before: # Solution
