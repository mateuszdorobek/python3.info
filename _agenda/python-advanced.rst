Python: Advanced
================
* https://www.sages.pl/szkolenia/python-zaawansowany

.. todo:: fix inconsistency between Polish and English version


Polish
------
1. Wprowadzenie:

    * Zadania określające poziom grupy
    * Zmiany w najnowszych wydaniach Python

2. Paradygmat funkcyjny:

    * Czyste funkcje (pure functions)
    * Rekurencja
    * Mutowalne i niemutowalne struktury danych
    * Wyrażenia Lambda
    * Funkcje wyższego poziomu i przejrzystość referencyjna
    * Callable, przestrzenie nazewnicze i atrybuty funkcji
    * Funkcyjne wzorce: callback, closure, maybe, some, map-reduce
    * Moduł Functools

3. Dekoratory:

    * Rodzaje dekoratorów i przykłady zastosowania
    * Dekoratory funkcji, klas, metod
    * Dekoratory funkcje, dekoratory klasy, dekoratory metody
    * Dekoratory z wrapperami funkcyjnymi i klasowymi
    * Dekoratory z argumentami i bez argumentów
    * Dekoratory w bibliotece standardowej

4. Paradygmat obiektowy:

    * Zasady S.O.L.I.D.
    * Dziedziczenie, kompozycja i klasy domieszkowe (mixin)
    * Kolejność rozwiązywania metod (MRO) i super()
    * Polimorfizm, enkapsulacja, abstrakcja
    * Mapowanie Obiektowo Relacyjne
    * Interfejsy i klasy abstrakcyjne
    * Metody statyczne i klasowe
    * Slots
    * Konstruktor i fabryki obiektów - __new__ vs. __init__
    * Metaklasy

5. Przeciążanie operatorów:

    * Operatory lewe, prawe i inkrementacji
    * Operatory numeryczne, porównania i binarne
    * Operatory dostępu (akcesory)

6. Protokoły:

    * Context Manager
    * Iterator
    * Property
    * Refleksja (setattr, getattr, hasattr, delattr)
    * Deskryptory

7. CI/CD w projektach Python:

    * Zależności dev, cicd, prod (frozen)
    * Statyczna analiza kodu źródłowego - pylint, pylama, sonarlint, pyflakes
    * Standardy programowania PEP8, PEP20 i dobre praktyki - pycodestyle, pydocstyle
    * Wyszukiwanie podatności bezpieczeństwa - bandit
    * Statyczna analiza typów - mypy

8. Zagadnienia wydajnościowe i optymalizacja:

    * Microbenchmarking: wydajność wbudowanych typów danych - timeit
    * Profiling: wyszukiwanie wąskich gardeł w programie - cProfile
    * Kompilacja kodu Pythona do bibliotek współdzielonych - mypyc

9. Współbieżność:

    * Modele współbieżności
    * Kolejki
    * Komunikacja międzyprocesowa i międzywątkowa
    * Mechanizmy blokujące
    * Wprowadzenie do programowania wielowątkowego
    * Wprowadzenie do programowania wieloprocesowego
    * Wprowadzenie do programowania asynchronicznego

10. Projekt praktyczny:

    * Zastosowanie technologii ze szkolenia
    * Dobre praktyki
    * Wykorzystanie debuggera w IDE
    * Techniki refactoringu
    * Praca z legacy code


English
-------
1. Generators:

    * Built-in generators and generator-like objects
    * Generator expressions
    * Generator functions
    * Introspection
    * Yield and yield-from
    * Itertools module

2. Functional Paradigm:

    * Lambda expressions
    * Function scopes
    * Pure-functions
    * Recurrence
    * Mutable and immutable data structures
    * Higher order functions and referential transparency
    * Function objects and attributes
    * Callable
    * Closures
    * Functools module

3. Decorators:

    * Decorator types and use cases
    * Decorating functions, classes and methods
    * Decorator with functional and class wrappers
    * Decorator with arguments
    * Built-in and standard library decorators

4. Object-Oriented Programming:

    * Mutable and immutable method arguments
    * Static and dynamic attributes
    * Access modifiers
    * Inheritance, composition, and mixin classes
    * Method Resolution Order (MRO) and super()
    * Polymorphism
    * Object-Relational Mapping
    * Interfaces and abstract classes
    * Static and class methods
    * Object identity and equity
    * Slots
    * Object constructor and factories - `__new__` vs `__init__`
    * Metaclasses

5. Performance and optimization:

    * Optimization, profiling and microbenchmarking
    * Alternative compilers, interpreters and performance modules
    * Computational complexity of built-in types and data structures

6. Parallelism:

    * Parallelism Models - threading, multiprocessing
    * queues
    * Inter-Process Communication (IPC)
    * Locking mechanisms
    * Introduction to multiprocessing
    * Introduction to multithreading

7. Concurrency:

    * Introduction to asynchronous programming
    * Event loop and task scheduling
    * Results and exception handling

8. Good practices and code quality:

    * Working with debugger tools in IDE
    * Legacy code refactoring with IDE functions
