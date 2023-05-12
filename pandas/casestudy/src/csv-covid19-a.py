#%% Imports
from datetime import date
import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday
from pandas.tseries.holiday import EasterMonday, Easter
from pandas.tseries.offsets import Day
import matplotlib.pyplot as plt
import matplotlib.axes


#%% Settings
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)


#%% Data Sources
#CONFIRMED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
#DEATHS = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
#RECOVERED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

CONFIRMED = 'https://python3.info/_static/covid19-confirmed.csv'
DEATHS = 'https://python3.info/_static/covid19-deaths.csv'
RECOVERED = 'https://python3.info/_static/covid19-recovered.csv'


#%% Data Frames
confirmed = pd.read_csv(CONFIRMED)
deaths = pd.read_csv(DEATHS)
recovered = pd.read_csv(RECOVERED)


#%% Get Country from DataFrame
def covid19(country: str = None) -> pd.DataFrame:
    """
    Get Confirmed, Deaths, Recovered for given country

    >>> covid19('Poland').loc['2022-01-01']
    Confirmed    4120248
    Deaths         97559
    Recovered          0
    Name: 2022-01-01 00:00:00, dtype: int64

    >>> covid19('France').loc['2022-01-01']
    Confirmed    10296909
    Deaths         124839
    Recovered           0
    Name: 2022-01-01 00:00:00, dtype: int64

    >>> covid19().loc['2022-01-01']
    Confirmed    289931319
    Deaths         5473487
    Recovered            0
    Name: 2022-01-01 00:00:00, dtype: int64
    """
    def _get(data: pd.DataFrame, country: str = None) -> pd.Series:
        """
        Get Country from DataFrame

        >>> _get(confirmed, 'Poland').loc['2022-01-01']
        4120248
        >>> _get(deaths, 'Poland').loc['2022-01-01']
        97559
        >>> _get(recovered, 'Poland').loc['2022-01-01']
        0
        """
        if country is not None:
            data = data.query('`Country/Region` == @country')
        return (data
                .transpose()
                .iloc[4:]
                .sum(axis='columns')
                .astype('int64')
                .rename(pd.to_datetime, axis='index'))

    return pd.DataFrame({
        'Confirmed': _get(confirmed, country),
        'Deaths': _get(deaths, country),
        'Recovered': _get(recovered, country)})


#%% Calendars
class PLHolidayCalendar(AbstractHolidayCalendar):
    """
    Custom Holiday calendar for Poland based on
    https://en.wikipedia.org/wiki/Public_holidays_in_Poland
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
        Holiday('Second Day of Christmastide', month=12, day=26)]


#%% Show trendline
def plot_trendline(data: pd.DataFrame) -> matplotlib.axes.Axes:
    return (data
            .loc[:, ['Confirmed','Deaths']]
            .plot(kind='line',
                  subplots=True,
                  layout=(2, 1),
                  figsize=(10, 10)))


#%% Show fatalities
def plot_fatalities(data: pd.DataFrame) -> matplotlib.axes.Axes:
    return ((data['Deaths'] / data['Confirmed'])
            .mul(100)  # convert to percent
            .round(2)
            .plot(kind='line',
                  title='Percent of deaths vs new cases in last two weeks',
                  xlabel='Day',
                  ylabel='Percent',
                  ylim=(0.0, 6.0),
                  figsize=(10, 10),
                  grid=True))


#%% Confirmed cases day-by-day difference
def plot_confirmed_daily(data: pd.DataFrame) -> matplotlib.axes.Axes:
    return data['Confirmed'].diff().plot()


#%% Covid infection waves
def plot_confirmed_waves(data:pd.DataFrame) -> matplotlib.axes.Axes:
    return data['Confirmed'].diff().resample('W').median().plot()


#%% Confirmed cases in last two weeks
def plot_confirmed_last(data: pd.DataFrame, freq='2W') -> matplotlib.axes.Axes:
    return data['Confirmed'].last(freq).diff().plot()


#%% Confirmed cases every month
def plot_confirmed_monthly(data: pd.DataFrame) -> matplotlib.axes.Axes:
    return data['Confirmed'].resample('M').sum().plot()


#%%
def plot_confirmed_after_holidays(
        data: pd.DataFrame,
        since: date | str | None = '2021-01-01',
        until: date | str | None = '2022-02-07',
        days: int = 14,
        calendar: AbstractHolidayCalendar = PLHolidayCalendar(),
    ) -> matplotlib.axes.Axes:
    """
    Confirmed cases in period of 14 days after holidays
    """
    def _get(since, days):
        return (data
                .loc[since:, 'Confirmed']
                .iloc[:days]
                .reset_index(drop=True))

    data = {column: _get(since=holiday, days=days)
            for holiday in calendar.holidays(since, until)
            if (column := holiday.strftime('%Y-%m-%d'))}

    return pd.DataFrame(data).diff().plot(
        kind='line',
        subplots=True,
        layout=(15,1),
        sharex=True,
        figsize=(5, 15),
        grid=True)


#%% Run
if __name__ == '__main__':
    poland = covid19('Poland')
    usa = covid19('US')
    france = covid19('France')
    china = covid19('China')
    world = covid19()


    data = poland.loc['2020-01-01':'2022-02-01']

    plot_trendline(data)
    # plt.show()

    plot_fatalities(data)
    # plt.show()

    plot_confirmed_daily(data)
    # plt.show()

    plot_confirmed_waves(data)
    # plt.show()

    plot_confirmed_last(data)
    # plt.show()

    plot_confirmed_monthly(data)
    # plt.show()

    plot_confirmed_after_holidays(data)
    # plt.show()



"""TODO:

# Resample
poland['Confirmed'].shift(periods=1, freq='D').plot(kind='line')


# Z rozróżnianiem na kwartały (Q)
plot = poland['Confirmed'].resample('Q').plot(kind='line', legend=True)
plot[0].name = '2020-Q1'
plot[1].name = '2020-Q2'
plot[2].name = '2020-Q3'
plot[3].name = '2020-Q4'
plot[4].name = '2021-Q1'
plot[5].name = '2021-Q2'
plot[6].name = '2021-Q3'
plot[7].name = '2021-Q4'
plot[8].name = '2022-Q1'
plt.show()


# Makrotrendy
poland['Confirmed'].diff().rolling(window=14).median().plot()
plt.show()

poland['Confirmed'].diff().rolling(window=14).median().plot()
plt.show()

poland['Confirmed'].diff().resample('W').median().plot()
plt.show()

poland['Confirmed'].diff().resample('M').median().plot()
plt.show()

poland['Confirmed'].diff().resample('Q').median().plot()
plt.show()
"""
