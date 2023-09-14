Dragon Sprint 2
===============
* Assignment: Dragon Sprint 2
* Complexity: easy
* Lines of code: 20 lines
* Time: 21 min
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


English
-------
Non-functional requirements:

     1. Commit and push the current state of the repository
     2. Modify the game code from the previous version of the task
     3. Save the code to solve the task in the ``dragon`` directory
     4. When finished, add all files from ``dragon`` to the repository
     5. Commit and push changes to a central repository (Github)

Functional requirements:

    1. Create Dragon with:

        a. Name
        b. Health points, default random ``int`` in range from 50 to 100

    2. Dragon can:

        a. Make damage in range from 5 to 20
        b. Take damage

    3. Run the game:

        a. Create dragon named "Wawelski"
        b. Dragon makes damage
        c. Make 10 points damage to the dragon
        d. Make 5 points damage to the dragon
        e. Make 3 points damage to the dragon
        f. Make 2 points damage to the dragon
        g. Make 15 points damage to the dragon
        h. Make 25 points damage to the dragon
        i. Make 75 points damage to the dragon

    4. When dragon is dead:

        a. Display ``Dragon NAME is dead``, where NAME is dragon's name
        b. Display how much gold dropped (random int from 1 to 100)
        c. Display last position (should be: x=20, y=40)


Polish
------
Wymagania niefunkcjonalne:

    1. Zapisz (commit) i wypchnij (push) aktualny stan repozytorium
    2. Zmodyfikuj kod gry z poprzedniej wersji zadania
    3. Zapisz kod do rozwiązania zadania w katalogu ``dragon``
    4. Po zakończeniu dodaj wszystkie pliki z ``dragon`` do repozytorium
    5. Zapisz i wypchnij zmiany do centralnego repozytorium (Github)

Wymagania funkcjonalne:

    1. Wykorzystaj kod z poprzedniego zadania i dopisz nową funkcjonalność
    2. Smok ma losowe punkty życia z zakresu od 50 do 120
    3. Smok może zadawać komuś losowe obrażenia z przedziału od 5 do 20
    4. Smok może otrzymywać obrażenia
    5. Scenariusz gry:

        a. Stwórz smoka o nazwie "Wawelski"
        b. Ustaw inicjalną pozycję smoka na x=1, y=2
        c. Ustaw nową pozycję na x=10, y=20
        d. Przesuń smoka w lewo o 10 i w dół o 20
        e. Przesuń smoka w lewo o 10 i w prawo o 15
        f. Przesuń smoka w prawo o 15 i w górę o 5
        g. Przesuń smoka w dół o 5
        i. Smok zadaje obrażenia (5-20)
        j. Zadaj 10 obrażeń smokowi
        k. Zadaj 20 obrażeń smokowi
        l. Zadaj 30 obrażeń smokowi
        m. Zadaj 40 obrażeń smokowi
        n. Zadaj 50 obrażeń smokowi

    6. Gdy smok zginie:

        a. Wyświetl ``Dragon NAME is dead``, gdzie NAME to nazwa smoka
        b. Wyświetl ile złota wypadło (losowa liczba od 1 do 100)
        c. Wyświetl ostatnią pozycję (powinna być: x=20, y=40)


Hints
-----
* Shortest solution has 24 lines of code
* There are no errors in the assignment (testes on more than 300 trainings)
* ``from random import randint``
* ``randint(a, b)`` - random integer between ``a`` and ``b`` (inclusive!)


Solution
--------
* EN: Note, that this will spoil your fun and learning
* PL: Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_2.py>`
