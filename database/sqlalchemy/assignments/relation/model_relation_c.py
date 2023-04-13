"""
* Assignment: Model Define Product
* Complexity: easy
* Lines of code: 20 lines
* Time: 8 min

TODO: English Translation

Polish:
    1. Użyj SQLAlchemy Core do stworzenia modeli
    2. Wykorzystaj model `User`, `Address`, `Product`, `Orders`

    4. Wymagania niefunkcjonalne:
        a. Dodaj pola systemowe i diagnostyczne (`id`, `created`, `modified`)
           jeżeli uważasz to za stosowne
        b. Stwórz definicje modelu
        c. Stwórz relacje
        b. Użytkownik ma tylko jeden email i jeden telefon
        c. Użytkownik może mieć jeden adres rozliczeniowy i jeden do wysyłki
        d. Adres może nie mieć ulicy lub kodu pocztowego
        e. Użytkownik może zakupić wiele produktów
        f. Produkt mógł nie zostać kupiony
    5. Wymagania systemowe:
        d. Możesz użyć dowolnego modułu z biblioteki standardowej
        e. Nie instaluj ani nie używaj dodatkowych pakietów
        f. Wyjątek: możesz użyć SQLAlchemy do stworzenia modeli
        g. Wyjątek: możesz użyć Alembic do migracji schematu
"""


# Solution
