TODO
====
* Newsletter, once a month, what changed in the book
* Move webinars (description, scaffolding generation) to the book


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
* Move Interface, ABC, Protocol to Protocols
* Funcprog: Monads, Bridges, Atoms
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
