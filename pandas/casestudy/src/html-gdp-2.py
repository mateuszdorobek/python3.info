import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)

PKB = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_PKB_(parytet_si%C5%82y_nabywczej)'
LUDNOSC = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_liczby_ludno%C5%9Bci'
USD = 1

# %%
pkb = (pd
    .read_html(PKB)[0]
    .rename(columns={'Kraj': 'państwo', '2019':'pkb'})
    .loc[:, ['państwo', 'pkb']]
    .replace(regex=True, to_replace={
        '\xa0': '',
        '\[2\]': '',
        '\[3\]': '',
        'b\.d': pd.NA})
    .dropna()
    .set_index('państwo', drop=True)
    .replace(' ', '', regex=True)
    .astype('int64')
    .convert_dtypes()
    .sort_values(by='pkb', ascending=False)
    .mul(1_000_000*USD)
)

pkb

# %%

ludnosc = (pd
    .read_html(LUDNOSC)[0]
    .droplevel(axis='columns', level=0)
    .rename(columns={
        'Państwo, obszar lub terytorium zależne': 'państwo',
        '2022': 'ludność'})
    .loc[:, ['państwo', 'ludność']]
    .replace(regex=True, to_replace={
        'państwo': {
            'Chińska Republika Ludowa': 'Chiny',
            'Republika Chińska': 'Tajwan',
            'Korea Północna': pd.NA,
            'Kuba': pd.NA,
            'Zachodni Brzeg': pd.NA,
            'Strefa Gazy': pd.NA},
        'ludność': {
            '\xa0': '',
            '\[2\]': '',
            '\[3\]': '',
            ' ': '',
            '–': pd.NA}})
    .dropna()
    .set_index('państwo', drop=True)
    .astype('int64')
    .convert_dtypes()
)

ludnosc

# %%

result = (pd
    .merge(left=pkb, right=ludnosc, left_index=True, right_index=True)
    .assign(per_capita=lambda df: df['pkb'] / df['ludność'])
    .astype('int64')
    .convert_dtypes()
    .sort_values(by='per_capita', ascending=False)
)

#%%
plot = (result
    .loc[:, ['per_capita']]
    .head(n=10)
    .plot(
        kind='bar',
        title='Top 10 countries\nWith highest Global Domestic Product Per Capita',
        ylabel='Population',
        xlabel='Country',
        legend=True,
        grid=True,
        figsize=(16,10))
)

plt.show()
