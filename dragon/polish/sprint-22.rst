Dragon Sprint 22
================
* Assignment: Dragon Sprint 22
* Complexity: hard
* Time: 34 min


Functional Requirements
-----------------------
1. Bohater może należeć do drużyny składającej się maksymalnie z 6 postaci

    a. Mag: punkty życia: 10-20, złoto: 20-40, obrażenia: 1-4
    b. Kapłan: punkty życia: 30-40, złoto: 30-40, obrażenia: 1-6
    c. Łowca: punkty życia: 40-50, złoto: 10-40, obrażenia: 1-8
    d. Wojownik: punkty życia: 10-50, złoto: 10-20, obrażenia: 1-12
    e. Łotrzyk: punkty życia: 20-30, złoto: 0-50, obrażenia: 1-6
    f. Druid: punkty życia: 30-40, złoto: 0, obrażenia: 1-6


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
* :download:`Solution <assignments/dragon_sprint_22.py>`
