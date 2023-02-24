Dragon (version alpha)
======================
* Assignment: Dragon (version alpha)
* Complexity: medium
* Lines of code: 100 lines
* Time: 89 min, then 144 min live coding with instructor
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


English
-------
1. In your directory create file ``dragon_alpha.py`` with class representing Dragon

2. Dragon has:

    a. name
    b. position on the screen
    c. texture file name, default ``img/dragon/alive.png``
    d. health points, default random ``int`` in range from 50 to 100

3. Dragon can:

    a. have position set to any place on the screen
    b. move in any direction by specified value
    c. make damage in range from 5 to 20
    d. take damage

4. When health points drop to, or below zero:

    a. Dragon has status ``dead``
    b. Change texture file name to  ``img/dragon/dead.png``
    c. Print ``NAME is dead``, where ``NAME`` is the dragon's name
    d. Print how much gold dragon dropped (random integer from 1 to 100)
    e. Print position where dragon died

5. Assume left-top screen corner as an initial coordinates position:

    a. going right add to ``x``
    b. going left subtract from ``x``
    c. going up subtract from ``y``
    d. going down add to ``y``

6. Run the game:

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

Non-functional requirements:

    a. Assignment is simulation of a software development process.
    b. Assignment is a business requirements specification.
    c. Solution must fulfill all the acceptance criteria.
    d. How to implement those criteria is up to you.
    e. You - programmer, Instructor - Product Owner.
    f. Product Owner will not help you in architectural decisions.
    g. Do not check neither solution nor future versions (beta and rc).

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
    i. This is `alpha` version, so no new functionality like
       negative position checking etc
    j. You can create tests, i.e.: unittest, doctest
    k. Do not read solution or any future iterations of this exercise;
       if you read future tasks, you will spoil fun and learning


Polish
------
1. W swoim katalogu stwórz plik ``dragon_alpha.py`` a w nim klasę reprezentującą Smoka

2. Smok ma:

    a. nazwę
    b. pozycję na ekranie
    c. nazwę pliku tekstury, domyślnie ``img/dragon/alive.png``
    d. punkty życia, domyślnie losowy ``int`` z zakresu od 50 do 100

3. Smok może:

    a. być ustawiony w dowolne miejsce ekranu
    b. być przesuwany w którymś z kierunków o zadaną wartość
    c. zadawać komuś losowe obrażenia z przedziału od 5 do 20
    d. otrzymywać obrażenia

4. Kiedy punkty życia Smoka spadną do lub poniżej zera:

    a. Smok ma status ``dead``
    b. Zmień nazwę pliku tekstury na ``img/dragon/dead.png``
    c. Wypisz ``NAME is dead``, gdzie ``NAME`` to nazwa smoka
    d. Wypisz ile złota smok wyrzucił (losowa liczba od 1 do 100)
    e. Wypisz pozycję gdzie smok zginął

5. Przyjmij górny lewy róg ekranu za punkt początkowy:

    a. idąc w prawo dodajesz ``x``
    b. idąc w lewo odejmujesz ``x``
    c. idąc w górę odejmujesz ``y``
    d. idąc w dół dodajesz ``y``

6. Przeprowadź grę:

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

Wymagania niefunkcjonalne:

    a. **Zadanie jest symulacją procesu wytwarzania oprogramowania.**

       Posłuży do demonstracji obiektowego paradygmatu programowania,
       i dobrych praktyk programistycznych. Nie piszemy gry i nie będziemy
       omawiali specyfiki game-dev. Siłą rzeczy poruszymy kilka kwestii
       z tym związanych, ale całość dyskusji znajdzie zastosowanie do
       dowolnego rodzaju projektów informatycznych i problemów inżynierii
       oprogramowania w dowolnej domenie biznesowej.

    b. **Zadanie jest specyfikacją wymagań biznesowych.**

       Nie jest to dokumentacja techniczna. Zadanie opisuje "co Smok ma
       robić", a nie "jak to ma robić". To ważna różnica i zwróć na to uwagę.
       Z tego powodu nie musisz trzymać się kolejności punktów i podpunktów
       w zadaniu, a także rozwiązać problemy inaczej niż jest napisane.

    c. **Rozwiązanie musi spełniać kryteria akceptacyjne.**

       Pamiętaj, że jest to wersja `alpha` więc nie wprowadzaj dodatkowych
       niezamówionych funkcjonalności (np. dodatkowych postaci, sprawdzania
       wychodzenia poza planszę itp.)

    d. **Sposób implementacji jest dowolny.**

       Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stałe,
       klasy, obiekty, unittest lub doctest, type annotation - co tylko
       chcesz, ale `nie korzystaj z modułów spoza biblioteki standardowej`.
       Wyjątkiem może być framework do testów.

    e. **Ty - programista, Prowadzący - Product Owner.**

       Przy tym zadaniu wcielisz się w rolę inżyniera oprogramowania
       (programisty), a Prowadzący będzie zachowywał się jak Product Owner
       z niewielką wiedzą techniczną - 10 lat temu był programistą, a teraz
       większość czasu spędza w Excelu i na spotkaniach. Pamiętaj, że
       doświadczenie Product Ownera rzutuje na sposób w jaki pisze kryteria
       akceptacyjne. Jego kariera programisty może powodować,
       że w specyfikacji wymagań pojawią się kwestie techniczne i sugestie
       jak dany problem rozwiązać. Musisz to odfiltrować z treści zadania.
       Niestety to bardzo częsty scenariusz w branży IT.

    f. **Product Owner nie doradzi Ci w sprawie decyzji architektonicznych.**

       Nie podpowie Ci czy lepiej będzie zrobić to w jakiś konkretny sposób,
       albo czy jak zastosujesz to pewne rozwiązanie to jaki będzie wpływ na
       przyszłość. Zadanie polega na tym, że to Ty musisz podejmować decyzje
       i ponosić ich konsekwencje, tj. łatwa możliwość wprowadzania zmian w
       przyszłych wersjach. Musisz znaleźć balans, między wdrożeniem szybkim
       funkcjonalności, łatwością zrozumienia i utrzymywania kodu i nie
       zablokowaniem sobie drogi na wprowadzanie zmian w przyszłości.
       Pamiętaj o TDD, YAGNI, DRY, KISS, SOLID, emerging architecture
       i over-engineering.

    g. **Nie przeglądaj rozwiązań ani treści kolejnych części zadania.**

       Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i naukę. To
       zadanie ma niesamowity potencjał edukacyjny. Nie niszcz go.

Powodzenia i miłej zabawy!


Hints
-----
* Shortest possible solution could have 24 lines of code
* ``from random import randint``
* ``randint(a, b)`` - random integer between ``a`` and ``b`` (inclusive!)


Solution
--------
* EN: Note, that this will spoil your fun and learning
* PL: Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Basic <assignments/dragon_alpha_basic.py>`
* :download:`Intermediate <assignments/dragon_alpha_intermediate3.py>`
* :download:`Advanced <assignments/dragon_alpha_advanced.py>`
