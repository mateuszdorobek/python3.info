from datetime import date

import pandas as pd
from doctest import testmod as run_tests
from matplotlib import pyplot as plt
import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
from pandas.tseries.offsets import Day

PROCENT = 1


#%%

# CONFIRMED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
# RECOVERED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
# DEATHS = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

CONFIRMED = 'https://python.astrotech.io/_static/covid19-confirmed.csv'
RECOVERED = 'https://python.astrotech.io/_static/covid19-recovered.csv'
DEATHS = 'https://python.astrotech.io/_static/covid19-deaths.csv'


confirmed = pd.read_csv(CONFIRMED).convert_dtypes()
recovered = pd.read_csv(RECOVERED).convert_dtypes()
deaths = pd.read_csv(DEATHS).convert_dtypes()


class PLHolidayCalendar(AbstractHolidayCalendar):
    """
    Custom Holiday calendar for Poland based on
    https://en.wikipedia.org/wiki/Public_holidays_in_Poland

    >>> PLHolidayCalendar().holidays(start='2000-01-01', end='2000-12-31')
    DatetimeIndex(['2000-01-01', '2000-01-06', '2000-04-23', '2000-04-24',
                   '2000-05-01', '2000-05-03', '2000-06-11', '2000-06-22',
                   '2000-08-15', '2000-11-01', '2000-11-11', '2000-12-25',
                   '2000-12-26'],
                  dtype='datetime64[ns]', freq=None)
    """
    rules = [
        Holiday('New Years Day', month=1, day=1),
        Holiday('Epiphany', month=1, day=6),
        Holiday('Easter', month=1, day=1, offset=[Easter()]),
        EasterMonday,
        Holiday('May Day', month=5, day=1),
        Holiday('Constitution Day', month=5, day=3),
        Holiday('Pentecost Sunday', month=1, day=1, offset=[Easter(), Day(49)]),
        Holiday('Corpus Christi', month=1, day=1, offset=[Easter(), Day(60)]),
        Holiday('Assumption of the Blessed Virgin Mary', month=8, day=15),
        Holiday('All Saints Day', month=11, day=1),
        Holiday('Independence Day', month=11, day=11),
        Holiday('Christmas Day', month=12, day=25),
        Holiday('Second Day of Christmastide', month=12, day=26),
    ]


#%%

def _parse(data, country, name):
    """
    >>> _parse(confirmed, 'Poland', name='confirmed').loc['2021-08-04']
    confirmed    2883448
    Name: 2021-08-04 00:00:00, dtype: int64

    >>> _parse(confirmed, 'Poland', name='confirmed').loc['2021-08-05']
    confirmed    2883624
    Name: 2021-08-05 00:00:00, dtype: int64

    >>> _parse(recovered, 'Poland', name='recovered').loc['2021-08-04']
    recovered    2653981
    Name: 2021-08-04 00:00:00, dtype: int64

    >>> _parse(recovered, 'Poland', name='recovered').loc['2021-08-05']
    recovered    0
    Name: 2021-08-05 00:00:00, dtype: int64

    >>> _parse(deaths, 'Poland', name='deaths').loc['2021-08-04']
    deaths    75269
    Name: 2021-08-04 00:00:00, dtype: int64

    >>> _parse(deaths, 'Poland', name='deaths').loc['2021-08-05']
    deaths    75275
    Name: 2021-08-05 00:00:00, dtype: int64
    """
    if country is not None:
        query = data['Country/Region'] == country
        data = data.loc[query]

    return (
        data
        .transpose()
        .iloc[4:]
        .sum(axis='columns')
        .astype('int')
        .to_frame()
        .rename(lambda x: name, axis='columns')
        .rename(pd.to_datetime, axis='index'))

run_tests()

#%%
def get(country=None):
    """
    >>> get('Poland').loc['2021-08-04']
    confirmed    2883448
    recovered    2653981
    deaths         75269
    Name: 2021-08-04 00:00:00, dtype: int64

    >>> get('Poland').loc['2021-08-05']
    confirmed    2883624
    recovered          0
    deaths         75275
    Name: 2021-08-05 00:00:00, dtype: int64

    >>> get('United Kingdom').loc['2021-08-04']
    confirmed    5980830
    recovered      24693
    deaths        157209
    Name: 2021-08-04 00:00:00, dtype: int64

    >>> get('United Kingdom').loc['2021-08-05']
    confirmed    6010860
    recovered          0
    deaths        157314
    Name: 2021-08-05 00:00:00, dtype: int64

    >>> get().loc['2021-08-04']
    confirmed    200758580
    recovered    130899061
    deaths         4283131
    Name: 2021-08-04 00:00:00, dtype: int64

    >>> get().loc['2021-08-05']
    confirmed    201444202
    recovered            0
    deaths         4294122
    Name: 2021-08-05 00:00:00, dtype: int64
    """
    return pd.concat((
       _parse(confirmed, country, name='confirmed'),
       _parse(recovered, country, name='recovered'),
       _parse(deaths, country, name='deaths'),
    ), axis='columns')

run_tests()

#%%

poland = get('Poland')
germany = get('Germany')
india = get('India')

uk = get('United Kingdom')
france = get('France')
china = get('China')

world = get()


#%%

def liczba_potwierdzonych_oraz_smierci_w_tygodniowych_okresach():
    return world.loc[:, ['confirmed', 'deaths']].resample('W').sum()

def liczba_zachorowan_na_jeden_przypadek_smiertelny():
    return world['confirmed'] / world['deaths']

def procent_smiertelnosci():
    return world['deaths'] / world['confirmed'] * 100*PROCENT

def get_holidays(year: int, calendar: AbstractHolidayCalendar) -> pd.DatetimeIndex:
    return calendar.holidays(start=date(year, 1, 1), end=date(year, 12, 31))

def liczba_zachorowan_po_swietach(year, calendar=PLHolidayCalendar()):
    """
    >>> data = liczba_zachorowan_po_swietach(year=2022)
    >>> plot = data.plot(
    ...    kind='line',
    ...    subplots=True,
    ...    sharey=True,
    ...    sharex=True,
    ...    grid=True,
    ...    figsize=(10,20))
    >>> # plt.show()
    """
    today = pd.Timestamp('today')
    holidays = get_holidays(year, calendar)
    holidays_until_today = holidays[holidays < today]

    def days_after_holiday(holiday, days=10):
        return (poland
                .loc[holiday:, 'confirmed']
                .iloc[:days]
                .diff()
                .reset_index(drop=True)
                .iloc[1:]
                .astype('int'))

    return pd.DataFrame({
        column_name: days_after_holiday(swieto)
        for i, swieto in enumerate(holidays_until_today)
        if (column_name := format(swieto, '%Y-%m-%d'))
    })
