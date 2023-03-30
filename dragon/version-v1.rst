Dragon v1.0
===========
* Assignment: Dragon v1.0
* Complexity: medium
* Lines of code: on average 100 lines, shortest solution is 24 lines
* Time: 89 min, then 144 min live coding with instructor
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


English
-------
Non-functional requirements:

    1. In your directory create an empty file ``dragon_v1.py``
    2. Add file to the version control system (should be automatic)
    3. Commit with message: "Dragon: NAME", where ``NAME`` is your first name
    4. Push changes to the repository
    5. In this file write a solution to the assignment
    6. Upon completing assignment commit and push changes to the repository

Functional requirements:

    1. Create Dragon with:

        a. name
        b. position on the screen
        c. health points, default random ``int`` in range from 50 to 100
        d. path to the texture file, default ``img/dragon/alive.png``

    2. Dragon can:

        a. have position set to any place on the screen
        b. move in any direction by specified value
        c. make damage in range from 5 to 20
        d. take damage

    3. Assume left-top screen corner as an initial coordinates position:

        a. going right add to ``x``
        b. going left subtract from ``x``
        c. going up subtract from ``y``
        d. going down add to ``y``

    4. When health points drop to, or below zero:

        a. Dragon has status ``dead``
        b. Change texture file name to  ``img/dragon/dead.png``
        c. Display ``NAME is dead``, where ``NAME`` is the dragon's name
        d. Display how much gold dragon dropped (random integer from 1 to 100)
        e. Display position where dragon died

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
        p. Dragon should die at the position x=20, y=40 and drop gold (1-100)


Polish
------
Wymagania niefunkcjonalne:

    1. W swoim katalogu stwórz pusty plik ``dragon_v1.py``
    2. Dodaj plik do systemu kontroli wersji
    3. Zapisz (commit) zmiany jako "Dragon: NAME", gdzie ``NAME`` to Twoje imię
    4. Wypchnij (push) zmiany do repozytorium
    5. W pliku zapisz kod do rozwiązania zadania
    6. Po skończeniu zadania zapisz i wypchnij zmiany do repozytorium

Wymagania funkcjonalne:

    1. Stwórz Smoka z:

        a. nazwą
        b. pozycją na ekranie
        c. punktami życia, domyślnie losowy ``int`` z zakresu od 50 do 100
        d. ścieżką do pliku tekstury, domyślnie ``img/dragon/alive.png``

    2. Smok może:

        a. być ustawiony w dowolne miejsce ekranu
        b. być przesuwany w którymś z kierunków o zadaną wartość
        c. zadawać komuś losowe obrażenia z przedziału od 5 do 20
        d. otrzymywać obrażenia

    3. Przyjmij górny lewy róg ekranu za punkt początkowy:

        a. idąc w prawo dodajesz ``x``
        b. idąc w lewo odejmujesz ``x``
        c. idąc w górę odejmujesz ``y``
        d. idąc w dół dodajesz ``y``

    4. Kiedy punkty życia Smoka spadną do lub poniżej zera:

        a. smok ma status ``dead``
        b. zmień nazwę pliku tekstury na ``img/dragon/dead.png``
        c. wyświetl ``NAME is dead``, gdzie ``NAME`` to nazwa smoka
        d. wyświetl ile złota smok wyrzucił (losowa liczba od 1 do 100)
        e. wyświetl pozycję gdzie smok zginął

    5. Przeprowadź grę:

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
        p. Smok powinien zginąć na pozycji: x=20, y=40 i zostawić złoto (1-100)


Hints
-----
* Shortest solution has 24 lines of code
* ``from random import randint``
* ``randint(a, b)`` - random integer between ``a`` and ``b`` (inclusive!)


Solution
--------
* EN: Note, that this will spoil your fun and learning
* PL: Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Basic <assignments/dragon_v1_basic.py>`
* :download:`Intermediate <assignments/dragon_v1_intermediate.py>`
* :download:`Advanced <assignments/dragon_v1_advanced.py>`
