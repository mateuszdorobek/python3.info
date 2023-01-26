"""
* Assignment: Database Model Shop
* Complexity: medium
* Lines of code: 100 lines
* Time: 55 min

English:
    0. Create project `shop` and apps: `customer`, `product`, `order`
    1. In `customer` app, create model `Customer`:
        a. firstname
        b. lastname
        c. born
        d. gender
        e. tax_number
        f. email
        g. phone (including country code)
    2. In `customer` app, create model `Address` with fields:
        a. type - billing or shipping
        b. street - street, house number, apartment
        c. city
        d. postcode
        e. region
        f. country
    3. In `product` app, create model `Product` with fields:
        a. ean13 - EAN-13 Barcode
        b. name - Product name
        c. price - Net price (without tax)
    4. In `order` app, Create model `Orders` with fields:
        a. customer
        b. products
    5. Import data from: `CUSTOMERS`, `ADDRESSES`, `PRODUCTS`, `ORDERS`
    6. Functional requirements:
        a. Customer has only one email address and one phone number
        b. Customer has only one shipping address and one billing address
        c. Address without street, or postcode are possible
        d. Customer can buy many products
        e. Product might not be sold
    7. Non-functional requirements:
        a. You may use any Python standard library module
        b. You can use Django with migrations
        c. Do not install any additional packages
    8. Display data which answer the following questions:
        a. Number of orders and fullname (joined firstname and lastname)
           of a customer who did the most purchases
        b. Total amount, firstname and lastname
           of a customer who summarily paid the most
        c. Total amount of purchases done by women all together
        d. Number of orders and name of a product
           which was purchased the most often
        e. Amount and country name, from which people did the most purchases
        f. Amount and country name, from which people paid the most

Polish:
    0. Stwórz projekt `shop` i apki: `customer`, `product`, `order`
    1. W apce `customer` stwórz model `Customer` z polami:
        a. firstname - imię
        b. lastname - nazwisko
        c. born - data urodzenia
        d. gender - płeć
        e. tax_number - NIP
        f. email - adres email
        g. phone - telefon z numerem kierunkowym kraju
    2. W apce `customer` stwórz model `Address` z polami:
        a. type - rodzaj adresu: rozliczeniowy, dostawy
        b. street - ulica, numer domu, numer mieszkania
        c. city - miasto
        d. postcode - kod pocztowy
        e. region - województwo lub stan
        f. country - kraj
    3. W apce `product` stwórz model `Product`:
        a. ean13 - Kod kreskowy EAN-13
        b. name - Nazwa produktu
        c. price - Cena netto
    4. W apce `order` stwórz model `Orders`:
        a. customer - Klient
        b. products - Produkty
    5. Zaimportuj dane z: `CUSTOMERS`, `ADDRESSES`, `PRODUCTS`, `ORDERS`
    6. Wymagania funkcjonalne:
        a. Klient ma tylko jeden email i jeden telefon
        b. Klient może mieć jeden adres rozliczeniowy i jeden do wysyłki
        c. Adres może nie mieć ulicy lub kodu pocztowego
        d. Klient może zakupić wiele produktów
        e. Produkt mógł nie zostać sprzedany
    7. Wymagania niefunkcjonalne:
        a. Możesz użyć dowolnego modułu z biblioteki standardowej
        b. Możesz użyć Django
        c. Nie instaluj ani nie używaj dodatkowych pakietów
    8. Wyświetl dane odpowiadające na pytania:
        a. Liczbę zamówień i pełną nazwę (połączone imię i nazwisko osoby),
           która dokonała najwięcej zakupów?
        b. Kwotę łączną, imię i nazwisko osoby,
           która sumarycznie zapłaciła najwięcej?
        c. Kwota, za jaką łącznie dokonały zamówień wszystkie kobiety?
        d. Liczbę zamówień i nazwę produktu, który był najczęściej kupowany?
        e. Kwota i nazwa kraju, którego obywatele dokonali najwięcej zakupów?
        f. Kwota i nazwa kraju, którego obywatele dokonali zakupów za
           największą kwotę?

    Tests:
        # doctest: +SKIP_FILE
        >>> import sys; sys.tracebacklimit = 0
        >>> from decimal import Decimal

        >>> assert result_a is not Ellipsis, \
        'Assign your result to variable `result_a`'
        >>> assert result_b is not Ellipsis, \
        'Assign your result to variable `result_b`'
        >>> assert result_c is not Ellipsis, \
        'Assign your result to variable `result_c`'
        >>> assert result_d is not Ellipsis, \
        'Assign your result to variable `result_d`'
        >>> assert result_e is not Ellipsis, \
        'Assign your result to variable `result_e`'
        >>> assert result_f is not Ellipsis, \
        'Assign your result to variable `result_f`'

        >>> assert result_a == {'orders': 11, 'name': 'Beth Johanssen'}
        >>> assert result_b == {'firstname': 'Beth', 'lastname': 'Johanssen',
        ...                     'total': Decimal('9427.79000000000')}
        >>> assert result_c == {'total': Decimal('10645.6800000000')}
        >>> assert result_d == {'product_name': 'Romeo', 'orders': 6}
        >>> assert result_e == {'country': 'USA', 'count': 29}
        >>> assert result_f == {'country': 'USA',
        ...                     'total': Decimal('21324.2300000000')}
"""
from django.db.models import Count, Sum, Value, F
from django.db.models.functions import Concat


CUSTOMERS = [
    {'firstname': 'Mark', 'lastname': 'Watney', 'born': '1994-10-12',
     'gender': 'male', 'tax_number': '94101212345',
     'email': 'mwatney@nasa.gov', 'phone': '+1 (234) 555-0000'},
    {'firstname': 'Melissa', 'lastname': 'Lewis', 'born': '1995-07-15',
     'gender': 'female', 'tax_number': '95071512345',
     'email': 'mlewis@nasa.gov', 'phone': '+1 (234) 555-0001'},
    {'firstname': 'Rick', 'lastname': 'Martinez', 'born': '1996-01-21',
     'gender': 'male', 'tax_number': '96012112345',
     'email': 'rmartinez@nasa.gov', 'phone': '+1 (234) 555-0010'},
    {'firstname': 'Alex', 'lastname': 'Vogel', 'born': '1994-11-15',
     'gender': 'male', 'tax_number': '94111512345',
     'email': 'avogel@esa.int', 'phone': '+49 (234) 555-0011'},
    {'firstname': 'Beth', 'lastname': 'Johanssen', 'born': '2006-05-09',
     'gender': 'female', 'tax_number': '06250912345',
     'email': 'bjohanssen@nasa.gov', 'phone': '+1 (234) 555-0100'},
    {'firstname': 'Chris', 'lastname': 'Beck', 'born': '1999-08-02',
     'gender': 'male', 'tax_number': '99080212345',
     'email': 'cbeck@nasa.gov', 'phone': '+1 (234) 555-0101'}]

ADDRESSES = [
    {'customer': 'mwatney@nasa.gov', 'type': 'billing',
     'street': '2101 E NASA Pkwy', 'city': 'Houston', 'postcode': '77058',
     'region': 'Texas', 'country': 'USA'},
    {'customer': 'mwatney@nasa.gov', 'type': 'shipping', 'street': '',
     'city': 'Kennedy Space Center', 'postcode': '32899', 'region': 'Florida',
     'country': 'USA'},
    {'customer': 'mlewis@nasa.gov', 'type': 'shipping',
     'street': 'Kamienica Pod św. Janem Kapistranem', 'city': 'Kraków',
     'postcode': '31008', 'region': 'Małopolskie', 'country': 'Poland'},
    {'customer': 'rmartinez@nasa.gov', 'type': 'billing', 'street': '',
     'city': 'Звёздный городо́к', 'postcode': '141160',
     'region': 'Московская область', 'country': 'Россия'},
    {'customer': 'rmartinez@nasa.gov', 'type': 'shipping', 'street': '',
     'city': 'Космодро́м Байкону́р', 'postcode': '',
     'region': 'Кызылординская область', 'country': 'Қазақстан'},
    {'customer': 'avogel@esa.int', 'type': 'shipping',
     'street': 'Linder Hoehe', 'city': 'Cologne', 'postcode': '51147',
     'region': 'North Rhine-Westphalia', 'country': 'Germany'},
    {'customer': 'bjohanssen@nasa.gov', 'type': 'shipping',
     'street': '2825 E Ave P', 'city': 'Palmdale', 'postcode': '93550',
     'region': 'California', 'country': 'USA'},
    {'customer': 'cbeck@nasa.gov', 'type': 'shipping',
     'street': '4800 Oak Grove Dr', 'city': 'Pasadena', 'postcode': '91109',
     'region': 'California', 'country': 'USA'}]

PRODUCTS = [
    {'ean13': '5039271113244', 'name': 'Alfa', 'price': '123.00'},
    {'ean13': '5202038482222', 'name': 'Bravo', 'price': '312.22'},
    {'ean13': '5308443764554', 'name': 'Charlie', 'price': '812.00'},
    {'ean13': '5439667086587', 'name': 'Delta', 'price': '332.18'},
    {'ean13': '5527865721147', 'name': 'Echo', 'price': '114.00'},
    {'ean13': '5535686226512', 'name': 'Foxtrot', 'price': '99.12'},
    {'ean13': '5721668602638', 'name': 'Golf', 'price': '123.00'},
    {'ean13': '5776136485596', 'name': 'Hotel', 'price': '444.40'},
    {'ean13': '5863969679442', 'name': 'India', 'price': '674.21'},
    {'ean13': '5908105406923', 'name': 'Juliet', 'price': '324.00'},
    {'ean13': '5957751061635', 'name': 'Kilo', 'price': '932.20'},
    {'ean13': '6190780033092', 'name': 'Lima', 'price': '128.00'},
    {'ean13': '6512625994397', 'name': 'Mike', 'price': '91.00'},
    {'ean13': '6518235371269', 'name': 'November', 'price': '12.00'},
    {'ean13': '6565923118590', 'name': 'Oscar', 'price': '43.10'},
    {'ean13': '6650630136545', 'name': 'Papa', 'price': '112.00'},
    {'ean13': '6692669560199', 'name': 'Quebec', 'price': '997.10'},
    {'ean13': '6711341590108', 'name': 'Romeo', 'price': '1337.00'},
    {'ean13': '6816011714454', 'name': 'Sierra', 'price': '998.10'},
    {'ean13': '7050114819954', 'name': 'Tango', 'price': '123.00'},
    {'ean13': '7251625012784', 'name': 'Uniform', 'price': '564.99'},
    {'ean13': '7251925199277', 'name': 'Victor', 'price': '990.50'},
    {'ean13': '7283004100423', 'name': 'Whisky', 'price': '881.89'},
    {'ean13': '7309682004683', 'name': 'X-Ray', 'price': '123.63'},
    {'ean13': '7324670042560', 'name': 'Zulu', 'price': '311.00'}]

ORDERS = [
    {'customer': 'mwatney@nasa.gov', 'product': 'Sierra'},
    {'customer': 'mwatney@nasa.gov', 'product': 'Victor'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'Delta'},
    {'customer': 'mlewis@nasa.gov', 'product': 'November'},
    {'customer': 'rmartinez@nasa.gov', 'product': 'Mike'},
    {'customer': 'mwatney@nasa.gov', 'product': 'Bravo'},
    {'customer': 'mwatney@nasa.gov', 'product': 'Kilo'},
    {'customer': 'avogel@esa.int', 'product': 'Victor'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'Romeo'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'Whisky'},
    {'customer': 'cbeck@nasa.gov', 'product': 'Zulu'},
    {'customer': 'mwatney@nasa.gov', 'product': 'Romeo'},
    {'customer': 'avogel@esa.int', 'product': 'Romeo'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'Victor'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'Whisky'},
    {'customer': 'mlewis@nasa.gov', 'product': 'Whisky'},
    {'customer': 'rmartinez@nasa.gov', 'product': 'Mike'},
    {'customer': 'mwatney@nasa.gov', 'product': 'November'},
    {'customer': 'mwatney@nasa.gov', 'product': 'Kilo'},
    {'customer': 'avogel@esa.int', 'product': 'Bravo'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'X-Ray'},
    {'customer': 'avogel@esa.int', 'product': 'Romeo'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'Victor'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'India'},
    {'customer': 'mlewis@nasa.gov', 'product': 'Juliet'},
    {'customer': 'rmartinez@nasa.gov', 'product': 'Foxtrot'},
    {'customer': 'avogel@esa.int', 'product': 'Victor'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'Romeo'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'Whisky'},
    {'customer': 'cbeck@nasa.gov', 'product': 'Zulu'},
    {'customer': 'mwatney@nasa.gov', 'product': 'Alfa'},
    {'customer': 'avogel@esa.int', 'product': 'Romeo'},
    {'customer': 'bjohanssen@nasa.gov', 'product': 'Quebec'}]


import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'shop.settings'
django.setup()

from customer.models import *
from orders.models import *
from product.models import *


# Clean environment before inserting data
Product.objects.all().delete()
Customer.objects.all().delete()
Address.objects.all().delete()
Order.objects.all().delete()


# Number of orders and fullname (joined firstname and lastname)
# of a customer who did the most purchases
# expected: {'orders': 11, 'name': 'Beth Johanssen'}
# type: dict[str, str|int]
result_a = ...

# Total amount, firstname and lastname
# of a customer who paid the most
# expected: {'firstname': 'Beth', 'lastname': 'Johanssen',
#            'total': Decimal('9427.79000000000')}
# type: dict[str, str|Decimal]
result_b = ...

# Total amount of purchases done by women all together
# expected: {'total': Decimal('10645.6800000000')}
# type: dict[str, str|Decimal]
result_c = ...

# Number of orders and name of a product which was purchased the most often
# type: dict[str, str|int]
# expected: {'product_name': 'Romeo', 'orders': 6}
result_d = ...

# Amount and country name, from which people did the most purchases
# type: dict[str, str|int]
# expected: {'country': 'USA', 'count': 29}
result_e = ...

# Amount and country name, from which people paid the most
# type: dict[str, str|Decimal]
# expected: {'country': 'USA', 'total': Decimal('21324.2300000000')}
result_f = ...


# Solution
for row in PRODUCTS:
    Product.objects.create(**row)

for row in CUSTOMERS:
    row['tax_number'] = row.pop('tax_number')
    Customer.objects.create(**row)

for row in ADDRESSES:
    customer = Customer.objects.get(email=row.pop('customer'))
    Address.objects.create(customer=customer, **row)

for row in ORDERS:
    customer = Customer.objects.get(email=row.pop('customer'))
    product = Product.objects.get(name=row.pop('product'))
    Order.objects.create(customer=customer, product=product)


# Number of orders and fullname (joined firstname and lastname)
# of a customer who did the most purchases
# type: dict[str, str|int]
# expected: {'orders': 11, 'name': 'Beth Johanssen'}
result_a = (
    Order
    .objects
    .values(
        firstname=F('customer__firstname'),
        lastname=F('customer__lastname'))
    .annotate(
        orders=Count('customer'),
        name=Concat('firstname', Value(' '), 'lastname'))
    .order_by('-orders')
    .values('name', 'orders')
    .first()
)

# Total amount, firstname and lastname
# of a customer who paid the most
# type: dict[str, str|Decimal]
# expected: {'firstname': 'Beth', 'lastname': 'Johanssen',
#            'total': Decimal('9427.79000000000')}
result_b = (
    Order
    .objects
    .values(
        firstname=F('customer__firstname'),
        lastname=F('customer__lastname'))
    .annotate(
        total=Sum('product__price'),
        name=Concat('firstname', Value(' '), 'lastname'))
    .order_by('-total')
    .values('firstname', 'lastname', 'total')
    .first()
)

# Total amount of purchases done by women all together
# type: dict[str, str|Decimal]
# expected: {'total': Decimal('10645.6800000000')}
result_c = (
    Order
    .objects
    .filter(customer__gender='female')
    .aggregate(total=Sum('product__price'))
)

# Number of orders and name of a product which was purchased the most often
# type: dict[str, str|int]
# expected: {'product_name': 'Romeo', 'orders': 6}
result_d = (
    Order
    .objects
    .values(product_name=F('product__name'))
    .annotate(orders=Count('customer'))
    .order_by('-orders')
    .values('product_name', 'orders')
    .first()
)

# Amount and country name, from which people did the most purchases
# type: dict[str, str|int]
# expected: {'country': 'USA', 'count': 29}
result_e = (
    Order
    .objects
    .values(country=F('customer__address__country'))
    .annotate(count=Count('product__price'))
    .order_by('-count')
    .first()
)

# Amount and country name, from which people paid the most
# type: dict[str, str|Decimal]
# expected: {'country': 'USA', 'total': Decimal('21324.2300000000')}
result_f = (
    Order
    .objects
    .values(country=F('customer__address__country'))
    .annotate(total=Sum('product__price'))
    .order_by('-total')
    .first()
)
