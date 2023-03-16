Jupyter
=======

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

* https://jupyter.org/
* https://jupyter.readthedocs.io/en/latest/install.html
* https://github.com/jupyter/notebook


Install
-------
.. code-block:: console

    $ pip install jupyter


Run
---
.. code-block:: console

    $ jupyter-notebook
    [I 08:58:24.417 NotebookApp] Serving notebooks from local directory: /Users/catherine
    [I 08:58:24.417 NotebookApp] 0 active kernels
    [I 08:58:24.417 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
    [I 08:58:24.417 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

.. code-block:: console

    $ jupyter-notebook filename.ipynb


Using
-----
* Add code
* Run code
* Modify code and run
* Autocomplete
* Cell type (Markdown, LaTeX, Code)


Shortcut keys
-------------
Indent:

    * ``Tab``
    * ``Shift + Tab``

Comment Code:

    * ``Ctrl + /``

Run:

    * ``Shift`` + ``Enter``


Cells
-----
* Insert Below/Above Cells
* Add, Delete Cells
* Cut, Copy, Paste Cells
* Move Up/Down Cells
* Merge, Split Cells


Run
---
* Run Cell ``Shift-Enter``
* Run All (above/below)
* Restart Kernel
* Restart Kernel and Clear Output
* Clear Output


Magic commands
--------------
* ``%magic``
* ``%`` - Line Magics
* ``%%`` - Cell magic
* ``%run`` - Run the named file inside IPython as a program.
* ``!pip freeze``
* Full list https://ipython.readthedocs.io/en/stable/interactive/magics.html#

Kernels
-------
* Python 3
* https://github.com/jupyter/jupyter/wiki/Jupyter-kernels


Functions
---------
* Checkpoints
* Download
* Trust Notebook
* Close and Halt


Performance and profiling
-------------------------
* ``%%timeit``
* ``%%timeit -n 1000 -r 7``


Markdown
--------
Unorganized lists:

.. code-block:: md

    * first element
    * second element
    * third element

.. code-block:: md

    - first element
    - second element
    - third element

Organized lists:

.. code-block:: md

    1. first element
    1. second element
    1. third element

Headers:

.. code-block:: md

    # Header level 1
    ## Header level 2
    ### Header level 3
    #### Header level 4
    ##### Header level 5
    ###### Header level 6

Formatting:

.. code-block:: md

    *italic*
    **bold**

Code inline:

.. code-block:: md

    `class`

Code blocks:

.. code-block:: md

    ```python
    name = 'José Jiménez'
    print(f'My name... {name}')
    ```

Tables
------
* https://www.tablesgenerator.com/markdown_tables

.. code-block:: md

    | id | firstname | lastname |    agency |
    |----|:-----------|:---------:|----------:|
    | 1  | José       |  Jiménez  |      NASA |
    | 2  | Иван       |  Иванович | Roscosmos |
    | 3  | Mark       |   Watney  |      NASA |
    | 4  | Alex       |   Vogel   |      NASA |


LaTeX
-----
* ``%%latex``

.. code-block:: text

    %%latex

    $$c = \sqrt{a^2 + b^2}$$

.. code-block:: text

    %%latex

    $$\int_{x=0}^{x=\infty} x^\pi dx$$

.. code-block:: text

    %%latex

    \begin{equation}
    H← ​​​60 ​+​ \frac{​​30(B-R)​​}{Vmax-Vmin}  ​​, if V​max​​ = G
    \end{equation}

.. code-block:: python

    from IPython.display import Latex

    Latex(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx')
    Latex(r'$\lim_{x \to 0} (1+x)^{1/x} = e$')


Matplotlib charts
-----------------
.. code-block:: python

    x = np.linspace(-5, 5, 100)  # vector z 100 równo odległymi wartościami od -5 do 5
    y = np.sin(X)                # sinus wszystkich wartości x
    plt.plot(x, y)               # wykres liniowy

.. code-block:: text

    %matplotlib inline

.. code-block:: python

    import math
    import random
    from matplotlib import pyplot as plt

    x1 = [x*0.01 for x in range(0,628)]
    y1 = [math.sin(x*0.01)+random.gauss(0, 0.1) for x in range(0,628)]
    plt.plot(x1, y1)

    x2 = [x*0.5 for x in range(0,round(63/5))]
    y2 = [math.cos(x*0.5) for x in range(0,round(63/5))]
    plt.plot(x2, y2, 'o-')

    plt.show()  # doctest: +SKIP


HTML
----
.. code-block:: python

    from IPython.display import HTML

    HTML("We can <i>generate</i> <code>html</code> code <b>directly</b>!")


JavaScript
----------
.. code-block:: python

    from IPython.display import Javascript

    Javascript("alert('It is JavaScript!')")


Image
-----
.. code-block:: python

    from IPython.display import Image

    Image(url="https://python.astrotech.io/_static/favicon.png")


YouTube
-------
.. code-block:: python

    from IPython.display import YouTubeVideo

    YouTubeVideo("h8mDUc5L0XM")


Execute terminal commands
-------------------------
* ``!``
* ``!pwd``
* ``!ls``

.. code-block:: python
    :force:

    dirs = !ls

    for file in dirs:
        if file.find("1_") >= 0:
            print(file)


Output to different formats
---------------------------
* File -> Download as
* Notebook (.ipynb)
* Python (.py)
* HTML (.html)
* Reveal.js Slides (.html)
* Markdown (.md)
* reST (.rst)
* LaTeX (.lex)
* PDF via LaTeX (.pdf)

Generate HTML
-------------
#. File -> Save and Checkpoint
#. File -> Download as -> HTML (.html)


Slides
------
#. View -> Cell Toolbar -> Slideshow
#. Select slides, sub-slides and speaker notes
#. File -> Save and Checkpoint
#. File -> Download as -> Reveal.js slides (.slides.html)


Github pages with Jupyter Slides
--------------------------------
.. code-block:: console

    $ git submodule add https://github.com/hakimel/reveal.js.git reveal.js

    $ jupyter nbconvert --to slides index.ipynb --reveal-prefix=reveal.js

    $ jupyter nbconvert --to slides index.ipynb --reveal-prefix=reveal.js \
        --SlidesExporter.reveal_theme=serif \
        --SlidesExporter.reveal_scroll=True \
        --SlidesExporter.reveal_transition=none


Assignments
-----------
.. literalinclude:: assignments/jupyter_a.py
    :caption: :download:`Solution <assignments/jupyter_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/jupyter_b.py
    :caption: :download:`Solution <assignments/jupyter_b.py>`
    :end-before: # Solution
