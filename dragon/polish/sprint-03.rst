Dragon Sprint 03
================
* Assignment: Dragon Sprint 03
* Complexity: easy
* Time: 13 min


Functional Requirements
-----------------------
1. Smok
   przy tworzeniu
   ma losowe punkty życia z zakresu 50 do 100


Use Case
--------
1. Stwórz smoka
2. Stwórz smoka o nazwie "Wawelski"
3. Stwórz smoka bez nazwy
4. Smok przy tworzeniu ma losowe punkty życia


Tests
-----
.. code-block:: bdd

    Feature: Dragon's health

    Scenario: Create Dragon has random health points
        Given Dragon does not exist
         When Dragon is created with name "Wawelski"
         Then Dragon exists
          and Dragon health is between 50 and 100


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Hints
-----
* ``from random import randint``
* ``randint(a, b)`` - random integer between ``a`` and ``b`` (inclusive!)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_03.py>`
