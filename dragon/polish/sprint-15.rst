Dragon Sprint 15
================
* Assignment: Dragon Sprint 15
* Complexity: medium
* Time: 13 min


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


Testy
-----
.. code-block:: bdd

    Title: Ustaw status Smoka na podstawie życia.

    Scenario 1: Smok ze statusem "Full Health"
         Given: Jako Smok
          When: Punkty życia są 100%
          Then: Mam status "Full Health"

    Scenario 2: Smok ze statusem "Injured"
         Given: Jako Smok
          When: Punkty życia są 99%-75%
          Then: Mam status "Injured"

    Scenario 3: Smok ze statusem "Badly Wounded"
         Given: Jako Smok
          When: Punkty życia są 74%-25%
          Then: Mam status "Badly Wounded"

    Scenario 4: Smok ze statusem "Near Death"
         Given: Jako Smok
          When: Punkty życia są 24%-1%
          Then: Mam status "Near Death"

    Scenario 5: Smok ze statusem "Dead"
         Given: Jako Smok
          When: Punkty życia są 0% i mniej
          Then: Mam status "Dead"


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
