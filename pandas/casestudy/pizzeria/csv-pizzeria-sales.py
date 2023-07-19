import matplotlib.pyplot as plt
import pandas as pd


FILE = 'pizzeria-sales.csv'

with open(FILE, encoding='iso-8859-2') as file:
    df = (pd
        .read_csv(
            filepath_or_buffer=file,
            delimiter=';',
            skiprows=13,
            skipfooter=2,
            engine='python')
        .dropna(how='all', axis='rows')
        .dropna(how='all', axis='columns')
        .iloc[15:-1, [2,3,4,5]]
        .set_axis(['ptu', 'netto', 'brutto', 'vat'], axis='columns')
        .set_index(['ptu'], drop=True)
        .replace('\xa0','', regex=True)
        .astype('float32')
        .convert_dtypes()
        .applymap(lambda x: round(x,2))
        .sort_index()
    )
#             netto     brutto       vat
# ptu
# 0 (D)     3960.00    3960.00      0.00
# 23 (A)   23173.21   18839.85   4333.36
# 5 (C)     1755.00    1671.59     83.41
# 8 (B)   164954.00  152736.64  12217.36
# Razem   193842.20  177208.08  16634.13

df.loc[:,'brutto'].plot(
    kind='bar',
    figsize=(16,10),
    title='Podsumowanie stawki VAT',
    xlabel='Stawka PTU [%]',
    ylabel='Kwota [PLN]'
)

plt.tight_layout()
plt.show()
