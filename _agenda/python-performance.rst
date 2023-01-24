Python: performance optimization
================================
* https://www.sages.pl/szkolenia/python-optymalizacja


Polish
------
1. Wprowadzenie:

    * Python 3.11 i projekt Faster CPython
    * Alternatywne wersje kompilatora/interpretera
    * Type Annotation
    * Kompilacja kodu Python do C shared objects (mypyc, cython, cmodules)

2. Rodzaje testów na przykładach:

    * Analiza statyczna
    * Obciążeniowe

3. Refactoring:

    * Środowisko IDE (PyCharm) i jego możliwości
    * Podstawowe opcje refactoringowe
    * Zaawansowane opcje refactoringowe
    * Refactoring w środowisku bez testów
    * Praca z legacy code
    * Refactoring cudzego kodu
    * Dobre praktyki
    * Proces Code Review

4. Optymalizacja:

    * Pojęcia złożoności kodu (pamięciowa, obliczeniowa, cyklomatyczna, kognitywna)
    * Definicja długu technicznego
    * Ręczna identyfikacja złożonego kodu
    * Automatyczna identyfikacja złożonego kodu
    * Silosy kompetencyjne vs. Collective code ownership
    * Pojęcie emerging architecture

5. Tuning wydajnościowy:

    * Techniki pomiaru wydajności kodu
    * Microbenchmarking i jego pułapki
    * Profiling kodu i wizualizacja wyników
    * Identyfikacja wąskich gardeł
    * Testy obciążeniowe
    * Automatyzacja testów wydajnościowych w procesie CI/CD

6. Wprowadzenie do współbieżności:

    * GIL - Global Interpreter Lock
    * Programowanie wieloprocesowe
    * Programowanie wielowątkowe
    * Programowanie asynchroniczne
