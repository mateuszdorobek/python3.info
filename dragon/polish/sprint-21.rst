Dragon Sprint 21
================
* Assignment: Dragon Sprint 21
* Complexity: hard
* Time: 34 min


Functional Requirements
-----------------------
1. W grze występuje ekwipunek:

    a. zbroja i tarcza chroni przed uderzeniami obniżając ilość
       obrażeń o wartość obrony,
    b. miecz zwiększa ilość zadawanych obrażeń,

2. Każdy z przedmiotów ma swoją nazwę, typ oraz modyfikator:

    a. zbroję (dodatkowe punkty obrony, np. +10%)
    b. tarczę (dodatkowe punkty obrony, np. +5%)
    c. miecz (dodatkowe punkty ataku, np. +5%)

3. Bohater może założyć ekwipunek:

    a. można mieć tylko jedną zbroję i jeden hełm na raz
    b. bohater dowolnej klasy może używać tylko jednego miecza i tarczy
    c. wojownicy mogą używać dwóch mieczy, ale wtedy tarczy już nie


Use Case
--------
Smok:

1. Stwórz smoka o nazwie "Wawelski"
2. Smok przy tworzeniu ma losowe punkty życia
3. Ustaw inicjalną pozycję smoka na x=50, y=100
4. Pobierz aktualną pozycję
5. Ustaw nową pozycję na x=10, y=20
6. Przesuń smoka w lewo o 10 i w dół o 20
7. Przesuń smoka w lewo o 10 i w prawo o 15
8. Przesuń smoka w prawo o 15 i w górę o 5
9. Przesuń smoka w dół o 5

Bohater:

1. Stwórz bohatera o nazwie "Twardowski"
2. Smok przy tworzeniu ma losowe punkty życia
3. Ustaw inicjalną pozycję bohatera na x=0, y=0
4. Ustaw nową pozycję na x=10, y=20
5. Wypisz aktualną pozycję bohatera
6. Przesuń bohatera w lewo o 10 i w dół o 20
7. Przesuń bohatera w lewo o 10 i w prawo o 15
8. Przesuń bohatera w prawo o 15 i w górę o 5
9. Przesuń bohatera w dół o 5

Gra:

1. Walka podzielona jest na tury
1. Walka toczy się aż któraś ze stron pierwsza nie zginie
3. W każdej turze smok zadaje obrażenia jako pierwszy
4. W każdej turze bohater zadaje obrażenia jako drugi


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_21.py>`
