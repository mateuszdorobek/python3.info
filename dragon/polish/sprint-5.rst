Dragon Sprint 5
===============
* Assignment: Dragon Sprint 5
* Complexity: medium
* Time: 34 min
* Warning: Don't delete code, assignment will be continued


Functional Requirements
-----------------------
1. Dodaj możliwość poruszania w 3 wymiarach

    a. Idąc wyżej dodajesz ``z`` (latanie)
    b. Idąc głębiej odejmujesz ``z`` (nurkowanie)

2. Nie można wyjść poza obszar ekranu:

    a. oś ``x`` od 0 do 1920
    b. oś ``y`` od 0 do 1080
    c. oś ``z`` od -100 do +100

3. Jeżeli postać dojdzie do granicy ekranu, to przesuwając dalej,
   pozycja będzie ustawiona na brzegową wartość w danej osi.
   Przykładowo, smok jest na pozycji ``x=1, y=2`` i idzie w lewo o 10
   to po ruchu zakończy się na pozycji ``x=0, y=2``.


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
* :download:`Solution <assignments/dragon_sprint_5.py>`
