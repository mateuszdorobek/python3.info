import pandas as pd
from matplotlib import pyplot as plt


PKB = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_PKB_(parytet_si%C5%82y_nabywczej)'
LUDNOSC = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_liczby_ludno%C5%9Bci'
USD = 1


COUNTRIES = {
    'Chińska Republika Ludowa': 'Chiny',
    'Republika Chińska': 'Tajwan',
    # 'Strefa Gazy':'Zachodni Brzeg i Strefa Gazy',
    # 'Zachodni Brzeg': 'Zachodni Brzeg i Strefa Gazy',
    # 'Korea Północna': ''
    # 'Syria': ''
    # 'Kuba': ''
    # 'Zachodni Brzeg': ''
    # 'Strefa Gazy': ''
    # 'Polinezja Francuska': ''
    # 'Nowa Kaledonia': ''
    # 'Guam': ''
    # 'Curaçao': ''
    # 'Wyspy Dziewicze': ''
    # 'Jersey': ''
    # 'Wyspa Man': ''
    # 'Andora': ''
    # 'Bermudy': ''
    # 'Guernsey': ''
    # 'Kajmany': ''
    # 'Turks i Caicos': ''
    # 'Grenlandia': ''
    # 'Wyspy Owcze': ''
    # 'Mariany Północne': ''
    # 'Samoa Amerykańskie': ''
    # 'Sint Maarten': ''
    # 'Liechtenstein': ''
    # 'Brytyjskie Wyspy Dziewicze': ''
    # 'Saint-Martin[a]': ''
    # 'Monako': ''
    # 'Gibraltar': ''
    # 'Anguilla': ''
    # 'Wallis i Futuna': ''
    # 'Wyspy Cooka': ''
    # 'Wyspa Świętej Heleny, Wyspa Wniebowstąpienia i ...': ''
    # 'Saint-Barthélemy[a]': ''
    # 'Montserrat': ''
    # 'Saint-Pierre i Miquelon': ''
    # 'Falklandy': ''
    # 'Svalbard': ''
    # 'Niue': ''
    # 'Tokelau': ''
    # 'Watykan': ''
    # 'Pitcairn': ''

}

pkb = (pd
    .read_html(PKB)[0]
    .rename(columns={'Kraj':'kraj', '2019':'pkb'})
    .loc[:, ['kraj', 'pkb']]
    .replace(regex=True, to_replace={
        'pkb': {'b.d': pd.NA, '\s':''},
        'kraj': {'\[2\]': ''}})
    .dropna()
    .set_index('kraj', drop=True)
    .astype('int')
    .convert_dtypes()
    .mul(1_000_000*USD))

ludnosc = (pd
    .read_html(LUDNOSC)[0]
    .droplevel(level=0, axis='columns')
    .rename(columns={'Państwo, obszar lub terytorium zależne':'kraj', '2022':'ludnosc'})
    .loc[:, ['kraj','ludnosc']]
    .replace(regex=True, to_replace={
        'kraj':COUNTRIES,
        'ludnosc':{'–': pd.NA, '\[3\]': '', '\s':''}})
    .set_index('kraj', drop=True)
    .dropna()
    .astype('int')
    .convert_dtypes())

per_capita = (pd
    .merge(left=pkb, right=ludnosc, left_index=True, right_index=True)
    .assign(per_capita=lambda df: df.pkb / df.ludnosc)
    .round(1)
    .convert_dtypes()
    .sort_values(by='per_capita', ascending=False))


plot_percapita = (
    per_capita
    .loc[:, 'per_capita']
    .sort_values(ascending=False)
    .head(n=10)
    .plot(
        kind='bar',
        title='PKB Per Capita',
        xlabel='Państwo',
        ylabel='PKB Per Capita',
        grid=False,
        legend=False,
        figsize=(16,10)))

plt.tight_layout()
plt.show()
