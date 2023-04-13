Matplotlib Scales
=================
* Linear
* Logarithmic
* Symmetrical log (partially linear ``linthreshx: int``)
* Logit - reversed logarithmic

* Subtracting ``x.mean()`` is used to better highlight the function

.. figure:: img/matplotlib-figure-scales.png


Linear Scale
------------
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = x - x.mean()

    plt.yscale('linear')

    plt.plot(x, y)
    plt.show()  # doctest: +SKIP


Logarithmic Scale
-----------------
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = x - x.mean()

    plt.yscale('log')

    plt.plot(x, y)
    plt.show()  # doctest: +SKIP


Symmetrical Logarithmic Scale
-----------------------------
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = x - x.mean()

    plt.yscale('symlog', linthresh=0.01)

    plt.plot(x, y)
    plt.show()  # doctest: +SKIP


Logit Scale
-----------
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = x - x.mean()

    plt.yscale('logit')

    plt.plot(x, y)
    plt.show()  # doctest: +SKIP
