Dragon Sprint 06
===============
* Assignment: Dragon Sprint 06
* Complexity: easy
* Time: 8 min


Functional Requirements
-----------------------
1. Smok
   w trakcie gry
   może być przesuwany w prawo o zadaną wartość

2. Smok
   w trakcie gry
   może być przesuwany w lewo o zadaną wartość

3. Smok
   w trakcie gry
   może być przesuwany w dół o zadaną wartość

4. Smok
   w trakcie gry
   może być przesuwany do góry o zadaną wartość

5. Smok
   w trakcie gry
   może być jednocześnie przesuwany w lewo, w prawo, w górę i w dół


Non-Functional Requirements
---------------------------
1. Przyjmij górny lewy róg ekranu za punkt początkowy
2. Idąc w prawo dodajesz ``x``
3. Idąc w lewo odejmujesz ``x``
4. Idąc w górę odejmujesz ``y``
5. Idąc w dół dodajesz ``y``


Use Case
--------
1. Stwórz smoka o nazwie "Wawelski"
2. Ustaw inicjalną pozycję smoka na x=50, y=120
3. Pobierz aktualną pozycję
4. Ustaw nową pozycję na x=10, y=20
5. Przesuń smoka w lewo o 10 i w dół o 20
6. Przesuń smoka w lewo o 10 i w prawo o 15
7. Przesuń smoka w prawo o 15 i w górę o 5
8. Przesuń smoka w dół o 5


Tests
-----
.. code-block:: bdd

    Title: Dragon can be set at any position.

    Scenario 1: Dragon can be set at any position.
    Given Dragon is created with name "Wawelski",
    When Dragon is set at position x=1 y=2,
    Then Dragon position is x=1 y=2.


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Hints
-----
* To nie błąd: "lewo o 10 i w prawo o 15"
* Pozycja końcowa powinna być: x=20, y=40


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_06.py>`
