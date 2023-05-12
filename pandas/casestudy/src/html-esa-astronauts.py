"""
>>> result
{'years': 9, 'months': 9, 'days': 21, 'hours': 15, 'minutes': 27, 'seconds': 0}
"""

import pandas as pd

pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30.4375 * DAY
YEAR = 365.25 * DAY

# DATA = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'
DATA = 'https://python3.info/_static/european-astronaut-corps.html'


def duration(between):
    if between is pd.NaT:
        return between
    years, seconds = divmod(between.total_seconds(), YEAR)
    months, seconds = divmod(seconds, MONTH)
    days, seconds = divmod(seconds, DAY)
    hours, seconds = divmod(between.seconds, HOUR)
    minutes, seconds = divmod(seconds, MINUTE)
    return {
        'years': int(years),
        'months': int(months),
        'days': int(days),
        'hours': int(hours),
        'minutes': int(minutes),
        'seconds': int(seconds),
    }


tables = pd.read_html(DATA)
current = tables[0]
former = tables[2]

c = pd.to_timedelta(current['Time in space'], errors='coerce').sum()
f = pd.to_timedelta(former['Time in space'], errors='coerce').sum()
result = duration(c+f)
