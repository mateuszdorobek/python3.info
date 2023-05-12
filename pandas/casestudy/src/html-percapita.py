"""
>>> result.loc['Polska']
PKB          6.741270e+11
Ludność      3.842069e+07
PerCapita    1.754594e+04
Name: Polska, dtype: float64
"""

import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)


USD = 1

# PKB = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_PKB_nominalnego'
PKB = 'https://python3.info/_static/percapita-pkb.html'

# LUDNOSC = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_liczby_ludno%C5%9Bci'
LUDNOSC = 'https://python3.info/_static/percapita-ludnosc.html'

LUDNOSC_PANSTWA = {
    'Chińska Republika Ludowa': 'Chiny',
    'Korea Północna': pd.NA,
    'Republika Chińska': 'Tajwan',
    'Kuba': pd.NA,
    'Zachodni Brzeg': pd.NA,
    'Strefa Gazy': pd.NA}

LUDNOSC_COLUMNS = {
    'Państwo, obszar lub terytorium zależne': 'Państwo',
    '2018': 'Ludność'}


def clean(column):
    return (column
        .str.replace('\xa0', '')
        .str.replace(' ', ''))

pkb = (pd
    .read_html(PKB)[1]
    .rename(columns={'2021 r.': 'PKB'})
    .loc[:, ['Państwo', 'PKB']]
    .replace('b.d.', pd.NA)
    .dropna(how='any', axis='rows')
    .apply(clean)
    .astype({'PKB': 'int64'})
    .set_index('Państwo')
    .mul(1_000_000*USD))

ludnosc = (pd
    .read_html(LUDNOSC)[0]
    .droplevel(level=0, axis='columns')
    .rename(columns=LUDNOSC_COLUMNS)
    .loc[:, ['Państwo', 'Ludność']]
    .replace(LUDNOSC_PANSTWA)
    .set_index('Państwo')
    .query('index in @pkb.index')
    .apply(clean)
    .astype({'Ludność': 'int64'}))

result = (pkb
    .merge(ludnosc, left_index=True, right_index=True)
    .sort_index(ascending=True)
    .eval('PerCapita = PKB / Ludność'))

plot = (result
    .loc[:, ['PerCapita']]
    .round({'PerCapita': 1})
    .sort_values('PerCapita', ascending=False)
    .head(n=30)
    .plot(kind='bar', legend=True, grid=True, figsize=(16,10)))

# plt.show()
