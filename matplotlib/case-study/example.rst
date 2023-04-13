Matplotlib Examples
===================


Examples
--------
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()  # doctest: +SKIP

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--')
    plt.plot(t, t**2, 'bs')
    plt.plot(t, t**3, 'g^')

    plt.show()  # doctest: +SKIP

.. figure:: img/matplotlib-example-multiple.png

    Multiple lines on one chart


Gallery
-------
* https://matplotlib.org/gallery/index.html


Scales
------
.. literalinclude:: src/matplotlib-scales.py
    :language: python
    :caption: Scales

.. figure:: img/matplotlib-example-scales.png


Grid
----
.. literalinclude:: src/matplotlib-grid-extra.py
    :language: python
    :caption: Grid

.. figure:: img/matplotlib-example-grid.png


Legend using pre-defined labels
-------------------------------
.. literalinclude:: src/matplotlib-legend.py
    :language: python
    :caption: Legend using pre-defined labels

.. figure:: img/matplotlib-example-legend.png


Radar Chart
-----------
.. literalinclude:: src/matplotlib-radar-chart.py
    :language: python
    :caption: Radar Chart

.. figure:: img/matplotlib-example-radar.png
