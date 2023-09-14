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

    1. Dodaj statusy, które są aktualizowane na podstawie życia:

        a. "Full Health" - gdy punkty życia 100%
        b. "Injured" - gdy punkty życia 99% - 75%
        c. "Badly Wounded" - gdy punkty życia 74% - 25%
        d. "Near Death" - gdy punkty życia 24% - 1%
        e. "Dead" - gdy punkty życia poniżej lub równe 0%

    2. Dodaj tekstury, które są aktualizowane na podstawie życia:

        a. tekstura żyjącego: ``img/dragon/alive.png``
        b. tekstura martwego: ``img/dragon/dead.png``

    3. Kiedy punkty życia spadną do lub poniżej zera:

        a. istocie nie można zadawać więcej obrażeń
        b. istota nie może zadawać obrażeń
        c. istota nie może się poruszać


Solution
--------
* EN: Note, that this will spoil your fun and learning
* PL: Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_4.py>`
