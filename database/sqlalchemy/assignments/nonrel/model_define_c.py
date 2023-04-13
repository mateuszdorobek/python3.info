"""
* Assignment: Model Define Product
* Complexity: easy
* Lines of code: 20 lines
* Time: 8 min

TODO: English Translation

Polish:
    1. Użyj SQLAlchemy Core do stworzenia modeli
    2. Stwórz model `Product`:
        a. Kod kreskowy EAN-13
        b. Nazwa produktu
        c. Cena netto
        d. Stawka VAT
    3. Wymagania funkcjonalne:
        a. Kod EAN13, nazwa produktu oraz cena nie mogą być puste
        b. Kod EAN13 i nazwa muszą być indeksowane
        c. Kod EAN13 musi być unikalny
    4. Wymagania niefunkcjonalne:
        a. Dodaj pola systemowe i diagnostyczne (`id`, `created`, `modified`)
           jeżeli uważasz to za stosowne
        b. Stwórz definicje modelu
        c. Nie twórz żadnych relacji
    5. Wymagania systemowe:
        d. Możesz użyć dowolnego modułu z biblioteki standardowej
        e. Nie instaluj ani nie używaj dodatkowych pakietów
        f. Wyjątek: możesz użyć SQLAlchemy do stworzenia modeli
        g. Wyjątek: możesz użyć Alembic do migracji schematu
"""


# Solution
