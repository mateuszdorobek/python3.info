Dragon Sprint 05
================
* Assignment: Dragon Sprint 05
* Complexity: easy
* Time: 13 min


Functional Requirements
-----------------------
1. Smok
   w trakcie gry
   może zwrócić pozycję którą zajmuje


Use Case
--------
1. Stwórz smoka
2. Stwórz smoka o nazwie "Wawelski"
3. Stwórz smoka bez nazwy
4. Smok przy tworzeniu ma losowe punkty życia
5. Ustaw inicjalną pozycję smoka na x=50, y=100
6. Pobierz aktualną pozycję


Tests
-----
.. code-block:: bdd

    Feature: Dragon's position

    Scenario: Dragon returns its position
        Given Dragon is created with name "Wawelski" and position x=1 y=2
         When Dragon gets position
         Then value is x=1 y=2


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_05.py>`
