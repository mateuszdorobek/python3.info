FTP
===


Connect to FTP Server (insecure)
--------------------------------
.. literalinclude:: src/ftp-connect-insecure.py
    :language: python
    :caption: Connect to FTP Server (insecure)


Connect to FTP Server (secure)
------------------------------
.. literalinclude:: src/ftp-connect-secure.py
    :language: python
    :caption: Connect to FTP Server (secure)


Download file
-------------
.. literalinclude:: src/ftp-download.py
    :language: python
    :caption: Download file from FTP Server


Methods
-------
.. csv-table:: FTP Methods
    :header-rows: 1
    :widths: 10, 10, 80
    :file: data/ftp-api.csv


Assignments
-----------
.. todo:: Convert assignments to literalinclude

FTP Download
^^^^^^^^^^^^
* Assignment: FTP Download
* Complexity: easy
* Lines of code: 20 lines
* Time: 21 min

English:
    TODO: English Translation
          Run doctests - all must succeed

Polish:
    1. Stwórz na swoim komputerze plik o nazwie ``imie-nazwisko.txt``, gdzie:

        a. zamiast ``imie`` wpisz swoje imię
        b. zamiast ``nazwisko`` wpisz swoje nazwisko

    2. Do pliku wklej treść tekstu :pep:`20` -- The Zen of Python (wynik polecenia ``import this``)
    3. Połącz się z serwerem podanym przez prowadzącego
    4. Pobierz plik ``README.txt`` z głównego folderu
    5. Do katalogu ``files`` uploaduj plik ``imie-nazwisko.txt``
    6. Skorzystaj z Context Managera do połączenia
    7. Uruchom doctesty - wszystkie muszą się powieść

FTP Upload
^^^^^^^^^^
* Assignment: FTP Upload
* Complexity: easy
* Lines of code: 20 lines
* Time: 21 min

English:
    TODO: English Translation
          Run doctests - all must succeed

Polish:
    1. Pobierz na swój komputer plik :download:`https://python.astrotech.io/_static/favicon.png`
    2. Nazwij plik ``imie-nazwisko.png``, gdzie:

        a. zamiast ``imie`` wpisz swoje imię
        b. zamiast ``nazwisko`` wpisz swoje nazwisko

    3. Połącz się z serwerem podanym przez prowadzącego
    4. Do katalogu ``img`` uploaduj plik pobrany w poprzednim kroku
    5. Skorzystaj z Context Managera do połączenia
    6. Przesyłanie danych ma odbywać się w trybie binarnym
    7. Uruchom doctesty - wszystkie muszą się powieść
