Dragon Sprint 16
================
* Assignment: Dragon Sprint 16
* Complexity: medium
* Time: 21 min


Functional Requirements
-----------------------
1. Smok
   w trakcie gry ma punkty życia 100%
   ma status "Full Health"

2. Smok
   w trakcie gry ma punkty życia 99% - 75%
   ma status "Injured"

3. Smok
   w trakcie gry ma punkty życia 74% - 25%
   ma status "Badly Wounded"

4. Smok
   w trakcie gry ma punkty życia 24% - 1%
   ma status "Near Death"

5. Smok
   w trakcie gry ma punkty życia 0% i mniej
   ma status "Dead"


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


Testy
-----
.. code-block:: bdd

    Feature: Set Dragon status based on health

    Scenario: Dragon with status "Full Health"
        Given Dragon is created with name "Wawelski"
         When Dragon health is 100%
         Then Dragon status is "Full Health"

    Scenario: Dragon with status "Injured"
        Given Dragon is created with name "Wawelski"
         When Dragon health is between 75% and 99%
         Then Dragon status is "Injured"

    Scenario: Dragon with status "Badly Wounded"
        Given Dragon is created with name "Wawelski"
         When Dragon health is between 25% and 74%
         Then Dragon status is "Badly Wounded"

    Scenario: Dragon with status "Near Death"
        Given Dragon is created with name "Wawelski"
         When Dragon health is between 1% and 24%
         Then Dragon status is "Near Death"

    Scenario: Dragon with status "Dead"
        Given Dragon is created with name "Wawelski"
         When Dragon health is 0%
         Then Dragon status is "Dead"


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_16.py>`
