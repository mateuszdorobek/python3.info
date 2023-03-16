Dragon v1.0
===========
* Assignment: Dragon v1.0
* Complexity: medium
* Lines of code: on average 100 lines, shortest solution is 24 lines
* Time: 89 min, then 144 min live coding with instructor
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


Agenda
------
* 09:00 - 09:20 - Assignment introduction (functional and non-functional requirements)
* 09:20 - 10:50 - Students write code
* 10:50 - 11:00 - Git commit and push, break
* 11:00 - 11:40 - Code review (2-3 volunteers)
* 11:40 - 11:45 - Break
* 11:45 - 13:15 - Trainer writes code (TDD)
* 13:15 - 14:00 - Lunch
* 14:00 - 15:30 - Trainer performs refactoring
* 15:30 - 15:45 - Survey, break
* 15:45 - 17:00 - ...


English
-------
* Assignment is simulation of a software development process.
* Assignment is a business requirements specification.
* Solution must fulfill all the acceptance criteria.
* How to implement those criteria is up to you.
* You - programmer, Instructor - Product Owner.
* Product Owner will not help you in architectural decisions.
* Do not check neither solution nor future versions (beta and rc).

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

Post notes:

    a. Trainer acts as Product Owner with little technical knowledge
    b. You are the software engineer who need to decide and live with
       consequences of your choices
    c. Task is a narrative story telling to demonstrate OOP
       and good engineering practices
    d. Calculated last position of the game should be x=20, y=40
    e. You can introduce new fields, methods, functions, variables,
       constants, classes, objects, whatever you want
    f. Don't use modules form outside the Python Standard Library
    g. Task is business requirement specification, not a technical
       documentation, i.e., "what Dragon has to do, not how to do it"
    h. You don't have to keep order of specification while writing code
    i. This is `1.0` version, so no new functionality like
       negative position checking etc
    j. You can create tests, i.e.: unittest, doctest
    k. Do not read solution or any future iterations of this exercise;
       if you read future tasks, you will spoil fun and learning

Good luck, have fun!


Polish
------
**Zadanie jest symulacją procesu wytwarzania oprogramowania.**
Motyw Smoka z zadania jest tylko narracją do demonstracji obiektowego
paradygmatu programowania i dobrych praktyk programistycznych. Nie piszemy
gry i nie będziemy omawiali specyfiki game-dev! Siłą rzeczy poruszymy kilka
kwestii z związanych ze specyfiką gier (np. to że smok zieje ogniem itp),
ale całość dyskusji znajdzie zastosowanie do dowolnego rodzaju projektów
informatycznych i problemów inżynierii oprogramowania w każdej domenie
biznesowej.

**Ty - programista, Prowadzący - Product Owner.**
Przy tym zadaniu wcielisz się w rolę inżyniera oprogramowania (programisty),
a Prowadzący będzie zachowywał się jak Product Owner z niewielką wiedzą
techniczną - 10 lat temu był programistą, a teraz większość czasu spędza
w arkuszu kalkulacyjnym i na spotkaniach. Pamiętaj, że doświadczenie Product
Ownera rzutuje na sposób w jaki pisze kryteria akceptacyjne. Jego kariera
programisty może powodować, że w specyfikacji wymagań pojawią się kwestie
techniczne i sugestie jak dany problem rozwiązać. Musisz to odfiltrować
z treści zadania. Niestety to bardzo częsty scenariusz w branży IT.

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

Informacje dodatkowe:

    a. **Zadanie jest specyfikacją wymagań biznesowych.**
       Nie jest to dokumentacja techniczna. Zadanie opisuje "co ma być",
       a nie "jak to robić". Zwróć na to uwagę, bo to ważna różnica!

    b. **Sposób implementacji jest dowolny.**
       Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stałe,
       klasy, obiekty, unittest lub doctest, type annotation - co tylko
       chcesz, ale `nie korzystaj z modułów spoza biblioteki standardowej`.
       Wyjątkiem są frameworki do testów (``pytest``, ``hypothesis``, itp).

    c. **Rozwiązanie musi spełniać kryteria akceptacyjne.**
       Pamiętaj, że jest to wersja `1.0` więc nie wprowadzaj dodatkowych
       niezamówionych funkcjonalności (np. dodatkowych postaci, sprawdzania
       wychodzenia poza planszę itp.). Z tego powodu nie musisz trzymać się
       kolejności punktów i podpunktów w zadaniu, a także rozwiązać problemy
       inaczej niż jest napisane. Masz pełną dowolność.

    d. **Product Owner nie doradzi Ci w sprawie decyzji architektonicznych.**
       Nie podpowie Ci czy lepiej będzie zrobić to w jakiś konkretny sposób,
       albo czy jak zastosujesz to pewne rozwiązanie to jaki będzie wpływ na
       przyszłość. Zadanie polega na tym, że to Ty musisz podejmować decyzje
       i ponosić ich konsekwencje, tj. łatwa możliwość wprowadzania zmian w
       przyszłych wersjach. Musisz znaleźć balans, między wdrożeniem szybkim
       funkcjonalności, łatwością zrozumienia i utrzymywania kodu i nie
       zablokowaniem sobie drogi na wprowadzanie zmian w przyszłości.
       Pamiętaj o TDD, YAGNI, DRY, KISS, SOLID, emerging architecture
       i over-engineering.

    e. **Nie przeglądaj rozwiązań ani treści kolejnych części zadania.**
       Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i naukę.
       To zadanie ma niesamowity potencjał edukacyjny. Nie niszcz go.

Powodzenia i miłej zabawy!


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
