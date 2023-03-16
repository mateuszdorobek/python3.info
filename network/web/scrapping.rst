HTML Scrapping
==============


* Requests HTML https://github.com/psf/requests-html
* BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
* Scrapy https://scrapy.org/

``BeautifulSoup``
-----------------

Example usage
-------------
* https://github.com/AstroMatt/thesis-masters-aerospace/blob/master/src/worldspaceflight-astronaut-bios.py

Install
-------
.. code-block:: console

    $ pip install BeautifulSoup4

Parser
------
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| Parser               | Typical usage                              | Advantages                     | Disadvantages            |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| Python's html.parser | ``BeautifulSoup(markup, "html.parser")``   | * Batteries included           | * Not very tolerant      |
|                      |                                            | * Decent speed                 |   (before Python 2.7.3   |
|                      |                                            | * tolerant (as of Python 2.7.3 |   or 3.2.2)              |
|                      |                                            |   and 3.2.)                    |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| lxml's HTML parser   | ``BeautifulSoup(markup, "lxml")``          | * Very fast                    | * External C dependency  |
|                      |                                            | * Tolerant                     |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| lxml's XML parser    | ``BeautifulSoup(markup, "lxml-xml")``      | * Very fast                    | * External C dependency  |
|                      | ``BeautifulSoup(markup, "xml")``           | * The only currently supported |                          |
|                      |                                            |   XML parser                   |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| html5lib             | ``BeautifulSoup(markup, "html5lib")``      | * Extremely tolerant           | * Very slow              |
|                      |                                            | * Parses pages the same way a  | * External Python        |
|                      |                                            |   web browser does             |   dependency             |
|                      |                                            | * Creates valid HTML5          |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+

Open
----
.. code-block:: python

    from bs4 import BeautifulSoup

    with open("index.html") as file:
        html = BeautifulSoup(file, 'html.parser')

    html.find(id='menubox').decompose()

Basic Usage
-----------
.. code-block:: python

    from bs4 import BeautifulSoup


    html_doc = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>

        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="https://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="https://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="https://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>

        <p class="story">...</p>
    """

    html = BeautifulSoup(html_doc, 'html.parser')

    print(html.prettify())
    # <html>
    #  <head>
    #   <title>
    #    The Dormouse's story
    #   </title>
    #  </head>
    #  <body>
    #   <p class="title">
    #    <b>
    #     The Dormouse's story
    #    </b>
    #   </p>
    #   <p class="story">
    #    Once upon a time there were three little sisters; and their names were
    #    <a class="sister" href="https://example.com/elsie" id="link1">
    #     Elsie
    #    </a>
    #    ,
    #    <a class="sister" href="https://example.com/lacie" id="link2">
    #     Lacie
    #    </a>
    #    and
    #    <a class="sister" href="https://example.com/tillie" id="link2">
    #     Tillie
    #    </a>
    #    ; and they lived at the bottom of a well.
    #   </p>
    #   <p class="story">
    #     ...
    #   </p>
    #  </body>
    # </html>

.. code-block:: python

    html.title              # <title>The Dormouse's story</title>
    html.title.name         # 'title'
    html.title.string       # 'The Dormouse's story'
    html.title.parent.name  # 'head'
    html.p                  # <p class="title"><b>The Dormouse's story</b></p>
    html.p['class']         # 'title'
    html.a                  # <a class="sister" href="https://example.com/elsie" id="link1">Elsie</a>

    html.find_all('a')
    # [<a class="sister" href="https://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="https://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="https://example.com/tillie" id="link3">Tillie</a>]

    html.find(id="link3")
    # <a class="sister" href="https://example.com/tillie" id="link3">Tillie</a>

Iterating over items
--------------------
.. code-block:: python

    for link in html.find_all('a'):
        print(link.get('href'))

    # https://example.com/elsie
    # https://example.com/lacie
    # https://example.com/tillie

Getting Page Text
-----------------
.. code-block:: python

    html.get_text()
    # The Dormouse's story
    #
    # The Dormouse's story
    #
    # Once upon a time there were three little sisters; and their names were
    # Elsie,
    # Lacie and
    # Tillie;
    # and they lived at the bottom of a well.
    #
    # ...


Assignments
-----------
.. todo:: Convert assignments to literalinclude

Scrapping Iris
^^^^^^^^^^^^^^
* Assignment: Scrapping Iris
* Complexity: medium
* Lines of code: 20 lines
* Time: 21 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Za pomocą BeautifulSoup4 ze strony https://github.com/AstroMatt/book-python/blob/master/numerical-analysis/data/iris-dirty.csv pobierz dane zbioru Irysów.
    2. Parsując kod HTML oczyść dane.
    3. Skasuj pierwszy wiersz nagłówkowy.
    4. Kolumny nazwij: ``Sepal length``, ``Sepal width``, ``Petal length``, ``Petal width``, ``Species``
    5. Wyświetl dane w formacie listy dictów, kluczami mają być nazwy kolumn.
    6. Uruchom doctesty - wszystkie muszą się powieść

Scrapping EVA
^^^^^^^^^^^^^
* Assignment: Scrapping EVA
* Complexity: medium
* Lines of code: 100 lines
* Time: 21 min

English:
    TODO: English Translation
          Run doctests - all must succeed

Polish:
    1. Na podstawie podanych URL:

        a. https://www.worldspaceflight.com/bios/eva/eva.php
        b. https://www.worldspaceflight.com/bios/eva/eva2.php
        c. https://www.worldspaceflight.com/bios/eva/eva3.php
        d. https://www.worldspaceflight.com/bios/eva/eva4.php

    2. Skrapuj stronę wykorzystując ``BeautifulSoup4``
    3. Przygotuj plik CSV z danymi dotyczącymi spacerów kosmicznych
    4. Spróbuj to samo zrobić za pomocą ``pandas.read_html()``:

        a. Podając jako parametr czwarty URL
        b. Dla częściowo sparsowanej strony, np. wyciągniętej tabelki

    5. Uruchom doctesty - wszystkie muszą się powieść
