Multiprocessing About
=====================
* IPC - Inter-Process Communication
* Aby ``pickle`` mógł odtworzyć obiekt, musi posiadać jego definicję - klasę

.. glossary::

    IPC
        Inter Process Communication

    Process
    Daemon
    Dead Lock
    Race Condition
    Starvation


FAQ
---
#. Co to jest proces?
#. Ile czasu trwa tworzenie procesów?
#. Kto zarządza procesami?
#. Ile może być równoległych procesów?
#. Co to jest ``nice``
#. Jak komunikować się między procesami?

#. Procesy są w pełni niezależne między sobą.
#. Nie trzeba stawiać locków, bo nie wchodzą sobie w grę
#. Działanie jednego nie wpływa na drugi
#. Pamięć jest odseparowana
#. Wadą procesów jest brak komunikacji (dlatego potrzebne są metody IPC, np. pickle)
#. Bardzo duży koszt związany z komunikacją i serializacją


Problems
--------
* Deadlock (Zakleszczania)
* Race Condition
* Starvation (Głodzenie)
* Problem 5 filozofów:

    * 5 filozofów (albo rozmyśla, albo je)
    * 5 misek ze spaghetti,
    * 5 widelców,
    * 2 widelce potrzebne aby zjeść,
    * problem zakleszczania

* Problem producenta i konsumenta
* Problem czytelników i pisarzy


Process Lifecycle
-------------------
* Tworzenie procesów
* Zamykanie procesów
* Multiprocesowość
* Komunikacja między procesami
