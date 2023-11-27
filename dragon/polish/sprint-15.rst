Dragon Sprint 15
================
* Assignment: Dragon Sprint 15
* Complexity: medium
* Time: 21 min


Functional Requirements
-----------------------
1. Smok
   gdy żyje
   ma teksturę ``img/dragon/alive.png``

2. Smok
   gdy zginie
   ma teksturę ``img/dragon/dead.png``


Use Case
--------
1. Stwórz smoka
2. Stwórz smoka o nazwie "Wawelski"
3. Stwórz smoka bez nazwy
4. Smok przy tworzeniu ma losowe punkty życia
5. Ustaw inicjalną pozycję smoka na x=50, y=100
6. Pobierz aktualną pozycję
7. Ustaw nową pozycję na x=10, y=20
8. Przesuń smoka w lewo o 10 i w dół o 20
9. Przesuń smoka w lewo o 10 i w prawo o 15
10. Przesuń smoka w prawo o 15 i w górę o 5
11. Przesuń smoka w dół o 5
12. Smok zadaje obrażenia (losowo 5-20)
13. Zadaj 10 obrażeń smokowi
14. Zadaj 20 obrażeń smokowi
15. Zadaj 30 obrażeń smokowi
16. Zadaj 40 obrażeń smokowi
17. Zadaj 50 obrażeń smokowi


Tests
-----
.. code-block:: bdd

    Feature: Dragon sets texture based on health

    Scenario: Dragon texture when alive
        Given Dragon is created with name "Wawelski"
         When Dragon health is 1
         Then Dragon texture is "img/dragon/alive.png"

    Scenario: Dragon texture when dead
        Given Dragon is created with name "Wawelski"
         When Dragon health is 0
         Then Dragon texture is "img/dragon/dead.png"


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_15.py>`
