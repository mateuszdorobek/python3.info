TODO
====
* Newsletter, once a month, what changed in the book
* Move webinars (description, scaffolding generation) to the book


New run.py
----------
* Uruchamianie tylko żądanych plików, a nie wszystkich
* Zapis faili do plików w /tmp, catowanie tych plików na koniec builda
* Pliki z failami maja strukturę katalogów podobną jak pliki książki (czy napewno ?!)


Advanced
--------
* Wywalić atrybuty i metody
* Properties, Refleksja, Deskryptory razem w jednym rozdziale
* ABC dekorator przed Metaklasami
* Wywalić Context Manager i Iterator z Advanced i przenieść do Wzorce Projektowe


Regex
-----
* kropka (.) to nie jest anchor
* przenieść \b do anchorów
* zamienić identifier na character classes
* zadanie identifier_d zrobić przykład z samym \B oraz \b i \B w jednym


Średniozaawansowany
-------------------
* wywalić Smoka z Intermediate
* Smok tylko podczas szkolenia z TDD
* włączyć rozdział "database" do Intermediate
* Dodać formatowanie printa
* Dodać Dataclasses (?!)
* Dodać część OOP: (atrybuty, metody)
* Dodać systemu numeryczne hex, octal, binary
* Dodać locale i encoding
* Rozbić doctest i unittest osobno
* Dodać generatory
* Dodać zadania z TOML


Day 4
-----
* 60 min - Modules: project layout, venv, pip, requirements.txt, pyproject.toml
* 30 min - Logging: debugging messages
* 30 min - Print Formatting
* 45 min - Numbers: bin, hex, oct
* 45 min - Encoding: ascii, cp1250, iso-8859-2, utf-8
* 30 min - Locale: i18n, l10n
* 60 min - Operating system: os, tempfile, sys, platform
* 60 min - Ścieżki: os.path, pathlib, os
* 60 min - Parametry: sys.argv, argparse


Day 5
-----
* 180 min - Database: (SQL, create, index, alter, update, delete, drop, select)
* 60 min - OOP attributes: mutability, instance/class variables, access modifiers
* 15 min - Decimal: float precision problem (IEEE 754)
* 15 min - Random: pseudorandom numbers, random seed
* 60 min - Doctest: using doctests and testing problems
* 90 min - Unittest: introduction to TDD




Bin
---
* New structure for templates

training
    _solution
    Matt
        oop
            _notes.md
            assignment1.py
            assignment2.py
            assignment3.py
            assignment4.py
        functional
            _notes.md
            assignment1.py
            assignment2.py
            assignment3.py
            assignment4.py


Basics
------
* Remove unpack star from (and other examples)
* Cleanup OOP
* Move exception assertions, exit status and custom exceptions to Intermediate
* Move more advanced comprehensions to Intermediate


Intermediate
------------
* Cleanup Match
* Cleanup Operators
* tomllib


Advanced
--------
* ContextMan: Zadanie Buffer, kiepski opis zadania, nie wynika co to jest buffer i jak działa
* ContextMan: Zadanie Buffer, Testy przechodzą nawet jak nie ma bufora (skopiowane z A)
* Move Interface, ABC, Protocol to Protocols
* Functional: Monads, Bridges, Atoms
* Add exception groups (3.11)
* OOP: Add staticmethod assignments
* OOP: improve classmethod assignments
* Add more parallelism, concurrency (async) to Advanced


Case Study
----------
* Dane z Jiry (atlassian-python-api)
* Dane z Github API
* OAuth2
* Dane z Gmail (Google App Script)
* Dane z Facebook (QraphQL)
* Dane z Apki do nurkowania


PyCharm
-------
* Code: Auto-formatowanie kodu, optymalizacja importów
* Code: Indent i unindent wielu linii
* Code: Komentowanie wielu linii
* Code: PEP-8 + SonarLint
* Code: Profiling, concurrency diagram, coverage
* Code: Quick Documentation
* Code: ReST i Markdown + Mermaid
* Code: Refactoring, rename, extract, introduce
* Debugger: breakpoint
* GIT: clone, pull, push, rebase, diff, zmiany branchy, rozwiązywanie konfliktów
* IDE: Diff, różnice, scalanie plików
* IDE: Edit Scopes
* IDE: Konsola iPython
* IDE: Live templates
* IDE: Local history
* IDE: Pionowy podział okna i zamykanie
* IDE: Pliki Scratch
* IDE: Python console automatyczny import i settingsy Pandas
* IDE: Sprawdzanie pisowni i gramatyki
* IDE: Zgłaszanie feedbacku do Jetbrains
* IDE: Rename plików, przenoszenie
* IDE: Kopiowanie ścieżki do pliku
* IDE: tryb Zen, pełny ekran, distraction free mode
* Jupyter: edycja notebook, scientific mode, code cells, dataframe debugger
* Project: Setup interpretera
* Share: Code with Me
* Sortowanie linii, odwracanie kolejności linii
* Testy: TDD, doctest, unittest
* Text: Edit as Table
* Text: Toggle Case tekstu i liter
* Text: Zaznaczanie pionowe i wielozaznaczanie, karetka na końcu linii
* Alt+Enter: dodawanie annotation
* Alt+Enter: dodawanie pól do klasy + annotation
* Alt+Enter: klasy abstrakcyjne i interfejsy


Numerical Analysis
------------------
* Introduction to Python
* Dask
* Numba
* Scipy


Numpy
-----
* Poprawić przykłady z argmin i argmax oraz ``unravel_index()``
* Zrobić rozpiskę, które funkcje zwracają ``np.array`` a które robią ``inplace``
* Poprawić array-concatenate


Pandas
------
* ``pd.Series.dt.assign()`` - przydatne przy chaining
* ``pd.Series.dt.assign(column_name = lambda x: ...)``
* ``pd.Series.dt.tc_convert('Europe/Warsaw')``
* ``pd.Series.str.contains('text')``
* ``pd.pipe()`` - create intermediate variable from chain
* ``pd.pipe(lambda df: display(df) or df)`` - use display from IPython
* ``.memory_usage(deep=True)``
* poprawić przykłady z ``pd.DataFrame.fill()``, ``bfill`` oraz ``ffill``
* ``df.read_csv('filename.csv', chunksize=5)`` # five rows at a time, przydatne gdy czytasz plik np. 20GB
* ``for df in df.read_csv('filename.csv', chunksize=5): print(df)``
* ``df.loc[df['col'].str.contains('a|b', regex=True, flags=re.I)]``
* ``pd.to_datetime(df['Timestamp Column'], unit='s')``
* ``df.resample('d')`` # d - day; m - minute; to taki groupby dla indeksów dat
* ``df['column'].shift(-1)`` # previous column
* ``pd.explode()``
* ``series.describe()`` - inaczej się zachowuje dla indeksów numerycznych a inaczej dla timeseries; describe ignores NaN values
* ``series.describe(percentiles)``
* grouping by multiple series
* ``series.isnull()``
* ``series.isnull().any()``
* ``series.dropna()``
* ``series.groupby([])`` and ``Series.unstack()``
* ``new_series = series / series``
* ``series.describe()``
* ``pd.to_datetime()``
* ``df.index = pd.to_datetime(df['timestamp'])``
* ``ax = df.plot()``
* ``ax.axhline(df['temperature'].median(), color='r', linestyle="-")``
* ``df.index.viewDf.groupby(df.index.date).count()``
* ``df.groupby(df.index.week).count()``
* ``series.isin()``
* ``df[(df.index.hour > 12) & (df.index.hour <= 12)]["temperature"].plot()``
* data report by day "D" or "5T" - 5 minute intervals;
* ``df.resample("D").max().head()dr["temperature"].resample("D").agg(["min", "max"]).plot()``


Machine Learning
----------------
* Complete rewrite
* ROC Curve - stosunek True Positive do False Positive


Python PEP
----------
* array.array('int64'), array.array('uint32'), array.array('bool')
* async def http.fetch(method='GET', url='...', data={}, headers={}, json=True, decode_response=True, encoding='utf-8')
* https://developer.mozilla.org/en-US/docs/Web/API/fetch
* https://fetch.spec.whatwg.org/#fetch-method
* pyproject.toml run configuration: run, test, deploy, other: migrate, makemigrations, makemessages, compilemessages etc.
* Standard way of running your project with pyproject.toml: python run, or python migrate
* vars() should handle slots
* Simple interface for HTTP requests (similar to requests)
* http.get() http.post(), http.put(), http.delete()
* słowo kluczowe interface Cache
* dekorator interface
* metaklasa interface
* dataclass interface
* classlib interface
* classlib abstract
* monthlen
* input(default=..., type=int)
* dict.get(default=...)
* str.isfloat()
* str.isint()
* str.isnumeric() -> is int or float
* Path.rmtree() # skasowanie katalogu z podkatalogami
* datetime.time.now()
* datetime.parse()
* datetime.format()
* from datetime import parse(str, format)
* dataclass(strict=True) - walidacja typów
* type_check decorator, sprawdzający ``function.__annotations__``
* dict(keys=[...], values=[...])
* from pprint import pprint, print(pretty=True) (albo podawanie formatter)
* JSON datetime encoder, decoder to isoformat (UTC)
* json.to_string(), json.to_file(), json.from_file(), json.from_string()
* json.to_file(filename='...') (może przyjmować ścieżkę, a nie tylko uchwyt)
* pickle.to_string(), pickle.to_file(), pickle.from_file(), pickle.from_string()
* CTypes argtypes, restype from TypeAnnotation
* Context manager ``with logging.DEBUG:``
* print('cośtam', level='warning')
* log('cośtam', level='warning')
* NamedTuple oraz TypedDict scalić z tuple i dict
* cykliczny timer (scheduler) zamiast Trampoline


Pydantic
--------
* Contribute dataclass metadata validation methods to Pydantic validator
* Create "contracts" module with TypeAlias validators and Descriptors
