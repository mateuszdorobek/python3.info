Dragon Sprint 2
===============
* Assignment: Dragon Sprint 2
* Complexity: easy
* Lines of code: 11 lines
* Time: 34 min
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

    1. Dragon has position on the screen
    2. Dragon can have position set to any place on the screen
    3. Dragon can move in any direction by specified value
    4. Assume left-top screen corner as an initial coordinates position:

        a. Going right add to ``x``
        b. Going left subtract from ``x``
        c. Going up subtract from ``y``
        d. Going down add to ``y``

    5. Run the game:

        a. Create dragon named "Wawelski"
        b. Set Dragon's initial position to x=50, y=120
        c. Set new position to x=10, y=20
        d. Move dragon left by 10 and down by 20
        e. Move dragon left by 10 and right by 15
        f. Move dragon right by 15 and up by 5
        g. Move dragon down by 5

    6. End position should be: x=20, y=40


Polish
------
Wymagania niefunkcjonalne:

    1. Zapisz (commit) i wypchnij (push) aktualny stan repozytorium
    2. Zmodyfikuj kod gry z poprzedniej wersji zadania
    3. Zapisz kod do rozwiązania zadania w katalogu ``dragon``
    4. Po zakończeniu dodaj wszystkie pliki z ``dragon`` do repozytorium
    5. Zapisz i wypchnij zmiany do centralnego repozytorium (Github)

Wymagania funkcjonalne:

    1. Smok ma pozycję na ekranie
    2. Smok może być ustawiony w dowolne miejsce ekranu
    3. Smok może być przesuwany w którymś z kierunków o zadaną wartość
    4. Przyjmij górny lewy róg ekranu za punkt początkowy:

        a. Idąc w prawo dodajesz ``x``
        b. Idąc w lewo odejmujesz ``x``
        c. Idąc w górę odejmujesz ``y``
        d. Idąc w dół dodajesz ``y``

    5. Scenariusz gry:

        a. Stwórz smoka o nazwie "Wawelski"
        b. Ustaw inicjalną pozycję smoka na x=1, y=2
        c. Ustaw nową pozycję na x=10, y=20
        d. Przesuń smoka w lewo o 10 i w dół o 20
        e. Przesuń smoka w lewo o 10 i w prawo o 15
        f. Przesuń smoka w prawo o 15 i w górę o 5
        g. Przesuń smoka w dół o 5
        h. Wyświetl pozycję (powinna być: x=20, y=40)


Hints
-----
* It is not a mistake: 'left by 10 and right by 15'


Solution
--------
* EN: Note, that this will spoil your fun and learning
* PL: Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_2.py>`
