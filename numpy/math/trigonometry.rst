Trigonometry
============



SetUp
-----
>>> import numpy as np


Important
---------
.. glossary::

    Universal Functions
    ufunc
        Mathematical operations optimized to work on ``np.array()``:

        >>> a = np.array([1, 2, 3])
        >>>
        >>> np.sin(a)
        array([0.84147098, 0.90929743, 0.14112001])


Unit conversion
---------------

Degrees:

* ``np.deg2rad()``
* ``np.degrees()``

Radians:

* ``np.rad2deg()``
* ``np.radians()``


Trigonometric functions
-----------------------

Basic functions:

* ``np.sin()``
* ``np.cos()``
* ``np.tan()``

Arcus functions:

* ``np.arcsin()``
* ``np.arccos()``
* ``np.arctan()``

Hyperbolic functions:

* ``np.sinh()``
* ``np.cosh()``
* ``np.tanh()``

Arcus hyperbolic functions:

* ``np.arcsinh()``
* ``np.arccosh()``
* ``np.arctanh()``


Assignments
-----------
.. literalinclude:: assignments/numpy_trigonometry_a.py
    :caption: :download:`Solution <assignments/numpy_trigonometry_a.py>`
    :end-before: # Solution
