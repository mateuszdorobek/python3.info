from doctest import testmod as run_tests
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)

#%%

CONFIRMED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
DEATHS = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
RECOVERED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

COLUMNS = {
    'Province/State': 'region',
    'Country/Region': 'country',
}

confirmed = pd.read_csv(CONFIRMED).rename(columns=COLUMNS)
deaths = pd.read_csv(DEATHS).rename(columns=COLUMNS)
recovered = pd.read_csv(RECOVERED).rename(columns=COLUMNS)

#%%
def _get(df: pd.DataFrame, country: str, name: str) -> pd.Series:
    """
    >>> _get(confirmed, 'Poland', 'confirmed').loc['2021-01-01']
    1305774
    >>> _get(deaths, 'Poland', 'deaths').loc['2021-01-01']
    28956
    >>> _get(recovered, 'Poland', 'recovered').loc['2021-01-01']
    1046281
    """
    if country is not None:
        df = df.query('country == @country')
    return (df
        .transpose()
        .iloc[4:]
        .sum(axis='columns')
        .rename(name)
        .rename(index=pd.to_datetime)
        .astype('int64')
        .convert_dtypes())

def covid19(country: str = None) -> pd.DataFrame:
    """
    >>> covid19('Poland').loc['2021-01-01']
    confirmed    1305774
    deaths         28956
    recovered    1046281
    Name: 2021-01-01 00:00:00, dtype: Int64

    >>> covid19('US').loc['2021-01-01']
    confirmed    20397398
    deaths         352844
    recovered           0
    Name: 2021-01-01 00:00:00, dtype: Int64

    >>> covid19('China').loc['2021-01-01']
    confirmed    102649
    deaths         4884
    recovered     90031
    Name: 2021-01-01 00:00:00, dtype: Int64
    """
    return pd.concat((
        _get(confirmed, country, name='confirmed'),
        _get(deaths, country, name='deaths'),
        _get(recovered, country, name='recovered')
    ), axis='columns')

run_tests()

#%%
pl = covid19('Poland')
us = covid19('US')
india = covid19('India')
china = covid19('China')
france = covid19('France')
world = covid19()


#%%

data = pl['confirmed']
plot_confirmed_total = data.plot(
    kind='line',
    label='Confirmed',
    title='Total confirmed cases in Poland',
    xlabel='Date',
    ylabel='Total confirmed cases',)

plt.tight_layout()
# plt.show()
#%%

data = pl['confirmed'].diff()
plot_confirmed_daily = data.plot(
    kind='line',
    label='Confirmed',
    title='Daily confirmed cases in Poland',
    xlabel='Date',
    ylabel='Daily confirmed cases',)

plt.tight_layout()
# plt.show()

# %%

def mortality(df: pd.DataFrame, since='2020-04-01', until=None) -> pd.Series:
    return (df.deaths / df.confirmed).loc[slice(since,until)].mul(100).dropna()

data = mortality(pl)
plot_mortality = data.plot(
    kind='line',
    title='Mortality in Poland',
    ylabel='mortality [%]',
    label='Mortality',
    xlabel='date')
plt.hlines(data.mean(), xmin=data.index.min(), xmax=data.index.max(), color='red', label='Mean')
plt.legend()
plt.tight_layout()
# plt.show()
