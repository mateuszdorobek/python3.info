Scatter Plot
============
* Used to show correlation

.. figure:: img/matplotlib-chart-scatter.png

Syntax
------
.. code-block:: python

    import matplotlib.pyplot as plt


    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]

    plt.scatter(x, y)
    plt.show()  # doctest: +SKIP


Simple Points
-------------
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 50)
    y = np.sin(x)

    plt.scatter(x, y)
    plt.show()  # doctest: +SKIP

Markers
-------
* ``marker``
* ``s`` - size

.. figure:: img/matplotlib-chart-scatter-markers-filled.png

.. figure:: img/matplotlib-chart-scatter-markers-unfilled.png

.. code-block:: python

    import matplotlib.pyplot as plt


    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [5, 2, 4, 2, 1, 4, 5, 2]

    plt.scatter(x, y, marker='*', s=100)
    plt.show()  # doctest: +SKIP

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [5, 2, 4, 2, 1, 4, 5, 2]

    plt.scatter(x, y, marker='x', s=100)
    plt.show()  # doctest: +SKIP

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [4, 7, 6, 2, 7, 4, 5, 2]

    plt.scatter(x, y, marker='*', s=500)
    plt.scatter(y, x, marker='o', s=500)

    plt.show()  # doctest: +SKIP
