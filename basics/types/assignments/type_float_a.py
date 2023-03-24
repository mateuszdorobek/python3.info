"""
* Assignment: Type Float Tax
* Required: yes
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Cost of the service is 100.00 PLN net
    2. Service has value added tax (VAT) rate of 23%
    3. Calculate tax and gross values
    4. To calculate tax, multiply net times VAT
    5. To calculate gross multiply net times VAT plus 1
    6. Result must be in PLN
    7. Mind the operator precedence
    8. Run doctests - all must succeed

Polish:
    1. Cena usługi wynosi 100.00 PLN netto
    2. Usługa objęta jest 23% stawką VAT
    3. Oblicz wartości podatku oraz cenę brutto
    4. Aby obliczyć podatek, pomnóż cenę netto razy stawkę VAT
    5. Aby obliczyć cenę brutto pomnóż cenę netto razy stawka VAT plus 1
    6. Wynik musi być w PLN
    7. Zwróć uwagę na kolejność wykonywania działań
    8. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert net is not Ellipsis, \
    'Assign your result to variable `net`'
    >>> assert tax is not Ellipsis, \
    'Assign your result to variable `tax`'
    >>> assert gross is not Ellipsis, \
    'Assign your result to variable `gross`'
    >>> assert type(net) is float, \
    'Variable `net` has invalid type, should be float'
    >>> assert type(tax) is float, \
    'Variable `tax` has invalid type, should be float'
    >>> assert type(gross) is float, \
    'Variable `gross` has invalid type, should be float'

    >>> net / PLN
    100.0
    >>> tax / PLN
    23.0
    >>> gross / PLN
    123.0
"""

PLN = 1.00
VAT_23 = 23 / 100

# 100.0 PLN, without tax
# type: float
net = ...

# 23% of net
# type: float
tax = ...

# Gross is net plus tax in PLN
# type: float
gross = ...


# Solution
net = 100.0 * PLN
tax = net * VAT_23
gross = net + tax / PLN
