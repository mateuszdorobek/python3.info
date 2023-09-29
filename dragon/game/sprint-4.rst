Dragon Sprint 4
===============
* Assignment: Dragon Sprint 4
* Complexity: medium
* Lines of code: 20 lines
* Time: 21 min
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


English
-------
.. todo:: English Translation


Polish
------
Wymagania niefunkcjonalne:

    1. Zapisz (commit) i wypchnij (push) aktualny stan repozytorium
    2. Zmodyfikuj kod gry z poprzedniej wersji zadania
    3. Zapisz kod do rozwiązania zadania w katalogu ``dragon``
    4. Po zakończeniu dodaj wszystkie pliki z ``dragon`` do repozytorium
    5. Zapisz i wypchnij zmiany do centralnego repozytorium (Github)

Wymagania funkcjonalne:

    1. Dodaj możliwość poruszania w 3 wymiarach

        a. Idąc wewnątrz (przed monitorem) dodajesz ``z``
        b. Idąc wgłąb (za monitorem) odejmujesz ``z``

    2. Nie można wyjść poza obszar ekranu:

        a. oś ``x`` od 0 do 1920
        b. oś ``y`` od 0 do 1080
        c. oś ``z`` od -100 do +100

    3. Jeżeli postać dojdzie do granicy ekranu, to przesuwając dalej,
       pozycja będzie ustawiona na brzegową wartość w danej osi.
       Przykładowo, smok jest na pozycji ``x=1, y=2`` i idzie w lewo o 10
       to po ruchu zakończy się na pozycji ``x=0, y=2``.

    4. Scenariusz gry:

        a. Stwórz smoka o nazwie "Wawelski"
        b. Ustaw inicjalną pozycję smoka na x=1, y=2
        c. Ustaw nową pozycję na x=10, y=20
        d. Przesuń smoka w lewo o 10 i w dół o 20
        e. Przesuń smoka w lewo o 10 i w prawo o 15
        f. Przesuń smoka w prawo o 15 i w górę o 5
        g. Przesuń smoka w dół o 5
        h. Przesuń smoka wgłąb o 10
        i. Wyświetl pozycję (powinna być: x=20, y=40)
        j. Smok zadaje obrażenia (5-20)
        k. Zadaj 10 obrażeń smokowi
        l. Zadaj 20 obrażeń smokowi
        m. Zadaj 30 obrażeń smokowi
        n. Zadaj 40 obrażeń smokowi
        o. Zadaj 50 obrażeń smokowi
        p. Wyświetl ostatnią pozycję (powinna być: x=20, y=40, x=-10)

    5. Gdy smok zginie:

        a. Wyświetl ``Dragon NAME is dead``, gdzie NAME to nazwa smoka
        b. Wyświetl ile złota wypadło (losowa liczba od 1 do 100)


Solution
--------
* EN: Note, that this will spoil your fun and learning
* PL: Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_4.py>`
