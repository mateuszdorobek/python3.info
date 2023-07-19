ReST and Sphinx documentation
=============================


reStructuredText vs. Markdown
-----------------------------


Format reStructuredText
-----------------------
* https://devguide.python.org/documenting/#rst-primer
* https://devguide.python.org/documenting/#sections


Po co?
------


Paragrafy
---------
* newline


Nagłówki
--------
* Tytuł
* Nagłówek pierwszego poziomu
* Nagłówek drugiego poziomu
* Nagłówek trzeciego poziomu
* Nagłówek czwartego poziomu (czy stosować?)

* https://devguide.python.org/documenting/#sections


Odnośniki
---------
* Wewnątrz dokumentu
* numref
* na zewnątrz dokumentu


Obrazki i media
---------------
* figure (scale, name, align, podpisy pod obrazkami)


Specjalne wstawki
-----------------
* ``.. todo::``


Listingi kodu
-------------
* Osadzone
* Z plików zewnętrznych


TODO
----


Listy
-----
* listy nieuporządkowane
* listy numerowane
* jednopoziomowe i zagnieżdżone
* listy mieszane


Tabele
------
* Table
* List Table
* CSV Table


Cytowanie
---------
* ``cite``
* bibtex


Sphinx
------


Zależności
----------
* ``requirements.txt``

    .. code-block:: text

        # Minimalne wymaganie
        sphinx==7.0.*

        # Theme Read the Docs
        sphinx_rtd_theme

        # System cytowania i parsowanie bibtex
        sphinxcontrib-bibtex

        # Jeżeli chcemy generować slajdy RevealJS
        sphinxjp.themes.revealjs


Config
------
* Wersja na podstawie hasha git


Dobre praktyki
--------------
* podział na rozdziały
* rozkład katalogów
* listingi kodu
* zdjęcia
* dane w tabelkach CSV
* konwencja nazewnicza plików
* konwencja nazewnicza figure, csv-table, literalinclude


Generowanie dokumentacji
------------------------
* Table of Contents


toctree
-------


Automatyczne odpalanie doctestów do listingów kodu
--------------------------------------------------


Osadzanie LaTeX
---------------


Budowanie
---------
* make html
* make singlehtml
* make pdf

* generowanie Word (docx) -> pandoc


Read the docs
-------------
* http://readthedocs.org


Assignments
-----------
.. literalinclude:: ../_assignments/devops_gep_sphinx.py
    :caption: :download:`Solution <../_assignments/devops_gep_sphinx.py>`
    :end-before: # Solution
