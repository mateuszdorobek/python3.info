Dragon (version release candidate)
==================================
* Assignment: Dragon (version release candidate)
* Complexity: hard
* Lines of code: 50 lines
* Time: 21 min

.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


English
-------
.. todo:: English Translation


Polish
------
1. Dodaj możliwość poruszania się smoka i bohatera w 3 wymiarach
2. Bohater może należeć do drużyny, który może składać się maks z 6 postaci
   (różnych klas)
3. Żadna z istot na planszy nie może wyjść poza zakres ekranu
4. Bohater może dodatkowo założyć ekwipunek i może być to wiele obiektów na
   raz
5. Każdy z przedmiotów ma swoją nazwę, typ oraz modyfikator

    a. zbroję (dodatkowe punkty obrony, np. +10%)
    b. tarczę (dodatkowe punkty obrony, np. +5%)
    c. miecz (dodatkowe punkty ataku, np. +5%)

6. Zbroja i tarcza chroni przed uderzeniami obniżając ilość obrażeń
   o wartość obrony
7. Miecz zwiększa ilość zadawanych obrażeń
8. Obrażenia smoka maleją z sześcianem odległości (zianie ogniem)
9. Bohater nie może zadawać obrażeń jak jest dalej niż 50 punktów od
   przeciwnika
10. Wszystkie istoty mogą levelować a bazowe punty życia i obrażeń się
    zmieniają z poziomem
11. Przeprowadź symulację walki. Kto zginie pierwszy?
12. Wymagania niefunkcjonalne:

    a. Zadanie jest symulacją procesu developmentu
    b. Trener zachowuje się jak Product Owner z niewielką techniczną wiedzą
    c. Ty jesteś inżynierem oprogramowania, który musi podejmować decyzje i
       ponosić ich konsekwencje
    d. Zadanie jest tylko narracją do demonstracji OOP i dobrych
       praktyk programowania
    e. Wyliczona pozycja Smoka na końcu gry powinna być x=20, y=40
    f. Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stałe,
       klasy, obiekty, co tylko chcesz
    g. Nie korzystaj z modułów spoza standardowej biblioteki Pythona
    h. Zadanie jest specyfikacją wymagań biznesowych, a nie dokumentacją
       techniczną, tj. "co Smok ma robić, a nie jak to ma robić"
    i. Nie musisz trzymać się kolejności punktów i podpunktów w zadaniu
    j. Jest to wersja `alpha` więc bez dodatkowych funkcjonalności
       (np. sprawdzanie koordynatów, wychodzenia poza planszę itp.)
    k. Możesz stworzyć testy, np. unittest lub doctest
    l. Nie przeglądaj rozwiązań ani treści kolejnych części zadania;
       jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i naukę


Solution
--------
* EN: Note, that this will spoil your fun and learning
* PL: Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_rc.py>`
