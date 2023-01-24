Python: optymalizacja, refactoring i tuning wydajności
======================================================
* https://www.sages.pl/szkolenia/python-optymalizacja


Polish
------
* Wprowadzenie
	* Python 3.11 i projekt Faster CPython
	* Alternatywne wersje kompilatora/interpretera
	* Type Annotation
	* Kompilacja kodu Python do C shared objects (mypyc, cython, cmodules)
* Rodzaje testów na przykładach
	* Analiza statyczna
	* Obciążeniowe
* Refaktoring
	* Środowisko IDE (PyCharm) i jego możliwości
	* Podstawowe opcje refactoringowe
	* Zaawansowane opcje refactoringowe
	* Refactoring w środowiku bez testów
	* Praca z legacy code
	* Refactoring cudzego kodu
	* Dobre praktyki
	* Proces Code Review
* Optymalizacja
	* Pojęcia złożoności kodu (pamięciowa, obliczeniowa, cyklomatyczna, kognitywna)
	* Definicja długu technicznego
	* Ręczna identyfikacja złożonego kodu
	* Automatyczna identyfikacja złożonego kodu
	* Silosy kompetencyjne vs. Collective code ownership
	* Pojęcie emerging architecture
* Tuning wydajnościowy
	* Techniki pomiaru wydajności kodu
	* Microbenchmarking i jego pułapki
	* Profiling kodu i wizualizacja wyników
	* Identyfikacja wąskich gardeł
	* Testy obciążeniowe
	* Automatyzacja testów wydajnościowych w procesie CI/CD
* Wprowadzenie do współbieżności
	* GIL - Global Interpreter Lock
	* Programowanie wieloprocesowe
	* Programowanie wielowątkowe
	* Programowanie asynchroniczne
