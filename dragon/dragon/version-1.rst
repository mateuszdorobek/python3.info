Dragon v1.0
===========
* Assignment: Dragon v1.0
* Complexity: easy
* Lines of code: on average 100 lines, shortest solution is 24 lines
* Time: 55 min, then 55 min live coding with instructor
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


English
-------
Non-functional requirements:

    1. Commit and push your current state of repository
    2. In your directory create an empty directory ``dragon``
    3. In ``dragon`` directory create an empty file ``README.md``
    4. Add file to the version control system (should be automatic)
    5. Commit with message: "Dragon: NAME", where ``NAME`` is your first name
    6. Push changes to the repository
    7. Write a solution to the assignment in ``dragon`` directory
    8. Upon completing add all files in ``dragon`` to repository
    9. Commit and push changes to the central repository (Github)

Functional requirements:

    1. Create Dragon with:

        a. Name
        b. Position on the screen
        c. Health points, default random ``int`` in range from 50 to 100

    2. Dragon can:

        a. Have position set to any place on the screen
        b. Move in any direction by specified value
        c. Make damage in range from 5 to 20
        d. Take damage

    3. Assume left-top screen corner as an initial coordinates position:

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
        h. Dragon makes damage
        i. Make 10 points damage to the dragon
        j. Make 5 points damage to the dragon
        k. Make 3 points damage to the dragon
        l. Make 2 points damage to the dragon
        m. Make 15 points damage to the dragon
        n. Make 25 points damage to the dragon
        o. Make 75 points damage to the dragon
        p. When dead: display ``Dragon is dead``
        q. When dead: display how much gold dropped (random int from 1 to 100)
        r. When dead: display last position (should be: x=20, y=40)


Polish
------
Wymagania niefunkcjonalne:

    1. Zapisz (commit) i wypchnij (push) aktualny stan repozytorium
    2. W swoim katalogu stwórz pusty katalog ``dragon``
    3. W katalogu ``dragon`` stwórz pusty plik ``README.md``
    4. Dodaj plik ``README.md`` do systemu kontroli wersji
    5. Zapisz (commit) zmiany jako "Dragon: NAME", gdzie ``NAME`` to Twoje imię
    6. Wypchnij (push) zmiany do repozytorium
    7. Zapisz kod do rozwiązania zadania w katalogu ``dragon``
    8. Po zakończeniu dodaj wszystkie pliki z ``dragon`` do repozytorium
    9. Zapisz i wypchnij zmiany do centralnego repozytorium (Github)

Wymagania funkcjonalne:

    1. Stwórz Smoka z:

        a. Nazwą
        b. Pozycją na ekranie
        c. Punktami życia, domyślnie losowy ``int`` z zakresu od 50 do 100

    2. Smok może:

        a. Być ustawiony w dowolne miejsce ekranu
        b. Być przesuwany w którymś z kierunków o zadaną wartość
        c. Zadawać komuś losowe obrażenia z przedziału od 5 do 20
        d. Otrzymywać obrażenia

    3. Przyjmij górny lewy róg ekranu za punkt początkowy:

        a. Idąc w prawo dodajesz ``x``
        b. Idąc w lewo odejmujesz ``x``
        c. Idąc w górę odejmujesz ``y``
        d. Idąc w dół dodajesz ``y``

    4. Przeprowadź grę:

        a. Stwórz smoka o nazwie "Wawelski"
        b. Ustaw inicjalną pozycję smoka na x=50, y=120
        c. Ustaw nową pozycję na x=10, y=20
        d. Przesuń smoka w lewo o 10 i w dół o 20
        e. Przesuń smoka w lewo o 10 i w prawo o 15
        f. Przesuń smoka w prawo o 15 i w górę o 5
        g. Przesuń smoka w dół o 5
        h. Smok zadaje obrażenia (5-20)
        i. Zadaj 10 obrażeń smokowi
        j. Zadaj 5 obrażeń smokowi
        k. Zadaj 3 obrażenia smokowi
        l. Zadaj 2 obrażenia smokowi
        m. Zadaj 15 obrażeń smokowi
        n. Zadaj 25 obrażeń smokowi
        o. Zadaj 75 obrażeń smokowi
        p. Gdy zginie: wyświetl ``Dragon is dead``
        q. Gdy zginie: wyświetl ile złota wypadło (losowa liczba od 1 do 100)
        r. Gdy zginie: wyświetl ostatnią pozycję (powinna być: x=20, y=40)


Hints
-----
* Shortest solution has 24 lines of code
* It is not a mistake: 'left by 10 and right by 15'
* There are no errors in the assignment (testes on more than 300 trainings)
* ``from random import randint``
* ``randint(a, b)`` - random integer between ``a`` and ``b`` (inclusive!)


Solution
--------
* EN: Note, that this will spoil your fun and learning
* PL: Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Basic <assignments/dragon_v1_basic.py>`
* :download:`Intermediate <assignments/dragon_v1_intermediate.py>`
* :download:`Advanced <assignments/dragon_v1_advanced.py>`
