Dragon Sprint 6
===============
* Assignment: Dragon Sprint 6
* Complexity: medium
* Time: 34 min
* Warning: Don't delete code, assignment will be continued


Functional Requirements
-----------------------
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


Use Case
--------
1. Stwórz smoka o nazwie "Wawelski"
2. Ustaw inicjalną pozycję smoka na x=50, y=120
3. Ustaw nową pozycję na x=10, y=20
4. Wypisz aktualną pozycję
5. Przesuń smoka w lewo o 10 i w dół o 20
6. Przesuń smoka w lewo o 10 i w prawo o 15
7. Przesuń smoka w prawo o 15 i w górę o 5
8. Przesuń smoka w dół o 5
9. Smok zadaje obrażenia (losowo 5-20)
10. Zadaj 10 obrażeń smokowi
11. Zadaj 20 obrażeń smokowi
12. Zadaj 30 obrażeń smokowi
13. Zadaj 40 obrażeń smokowi
14. Zadaj 50 obrażeń smokowi


Non-Functional Requirements
---------------------------
1. Zapisz (commit) i wypchnij (push) aktualny stan repozytorium
2. Zmodyfikuj kod gry z poprzedniej wersji zadania
3. Zapisz kod do rozwiązania zadania w katalogu ``dragon``
4. Po zakończeniu dodaj wszystkie pliki z ``dragon`` do repozytorium
5. Zapisz i wypchnij zmiany do centralnego repozytorium (Github)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_6.py>`
