Dragon Sprint 04
================
* Assignment: Dragon Sprint 04
* Complexity: easy
* Time: 8 min


Functional Requirements
-----------------------
1. Użytkownik
   w trakcie gry
   może pobrać obecną pozycję smoka


Use Case
--------
1. Stwórz smoka o nazwie "Wawelski"
2. Ustaw inicjalną pozycję smoka na x=50, y=120
3. Pobierz aktualną pozycję


Tests
-----
.. code-block:: bdd

    Feature: Dragon can return its position

    Scenario: Dragon returns its position
        Given Dragon is created with name "Wawelski" and position x=50 y=120
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
* :download:`Solution <assignments/dragon_sprint_04.py>`
