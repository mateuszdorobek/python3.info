import sqlite3
import pandas as pd


pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)


DATA = 'https://python3.info/_static/apollo11.html'
DATABASE = 'apollo11.sqlite3'


df = pd.read_html(DATA, skiprows=1)[0]
df.columns = ['event', 'met', 'time', 'date']

df['time'] = df['time'].fillna('00:00:00')
df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
df['date'] = df['date'].map(pd.to_datetime).dt.date
df['time'] = df['time'].map(pd.to_datetime).dt.time
df['met'] = df['met'].str.replace(r'\.\d+', '', regex=True)
df['met'] = df['met'].fillna('')

invalid = df['met'].str.count(':') == 1
df.loc[invalid, 'met'] = df.loc[invalid, 'met'].str.replace(r'(\d+):(\d+)', r'\1:\2:00', regex=True)
df['met'] = pd.to_timedelta(df['met'])

df = df.convert_dtypes()
df = df.sort_values('datetime')
df = df.set_index('datetime', drop=True)

df['category'] = 'INFO'
df.loc[:'1969-07-16 13:32:00', 'category'] = 'DEBUG'
df.loc['1969-07-16 13:32:00':'1969-07-20 17:44:00', 'category'] = 'INFO'
df.loc['1969-07-20 17:44:00':'1969-07-21 21:35:00', 'category'] = 'WARNING'
df.loc['1969-07-24 16:50:35':, 'category'] = 'DEBUG'
df.loc['1969-07-20 20:10:22', 'category'] = 'ERROR'
df.loc['1969-07-20 20:11:02', 'category'] = 'ERROR'
df.loc['1969-07-20 20:14:18', 'category'] = 'ERROR'
df.loc['1969-07-20 20:14:43 ', 'category'] = 'ERROR'
df.loc['1969-07-20 20:14:58', 'category'] = 'ERROR'
df.loc['1969-07-16 13:32:00', 'category'] = 'CRITICAL'
df.loc['1969-07-16 13:33:23', 'category'] = 'CRITICAL'
df.loc['1969-07-16 13:34:44', 'category'] = 'CRITICAL'
df.loc['1969-07-16 13:39:40', 'category'] = 'CRITICAL'
df.loc['1969-07-16 13:43:49', 'category'] = 'CRITICAL'
df.loc['1969-07-16 16:22:13', 'category'] = 'CRITICAL'
df.loc['1969-07-16 16:56:03', 'category'] = 'CRITICAL'
df.loc['1969-07-19 17:21:50', 'category'] = 'CRITICAL'
df.loc['1969-07-19 21:43:36', 'category'] = 'CRITICAL'
df.loc['1969-07-20 17:44:00', 'category'] = 'CRITICAL'
df.loc['1969-07-20 20:05:05', 'category'] = 'CRITICAL'
df.loc['1969-07-20 20:17:39', 'category'] = 'CRITICAL'
df.loc['1969-07-20 22:12:00', 'category'] = 'CRITICAL'
df.loc['1969-07-21 02:39:33', 'category'] = 'CRITICAL'
df.loc['1969-07-21 02:56:15', 'category'] = 'CRITICAL'
df.loc['1969-07-21 03:09:08', 'category'] = 'CRITICAL'
df.loc['1969-07-21 03:15:16', 'category'] = 'CRITICAL'
df.loc['1969-07-21 03:24:19', 'category'] = 'CRITICAL'
df.loc['1969-07-21 03:41:43', 'category'] = 'CRITICAL'
df.loc['1969-07-21 03:48:30', 'category'] = 'CRITICAL'
df.loc['1969-07-21 05:01:39', 'category'] = 'CRITICAL'
df.loc['1969-07-21 05:09:32', 'category'] = 'CRITICAL'
df.loc['1969-07-21 05:11:13', 'category'] = 'CRITICAL'
df.loc['1969-07-21 17:54:00', 'category'] = 'CRITICAL'
df.loc['1969-07-21 18:01:15', 'category'] = 'CRITICAL'
df.loc['1969-07-21 21:35:00', 'category'] = 'CRITICAL'
df.loc['1969-07-22 04:55:42', 'category'] = 'CRITICAL'
df.loc['1969-07-22 04:58:13', 'category'] = 'CRITICAL'
df.loc['1969-07-24 16:21:12', 'category'] = 'CRITICAL'
df.loc['1969-07-24 16:35:05', 'category'] = 'CRITICAL'
df.loc['1969-07-24 16:50:35', 'category'] = 'CRITICAL'
df.loc['1969-07-24 17:29:00', 'category'] = 'CRITICAL'

tv = df['event'].str.contains('TV')
df.loc[tv, 'category'] = 'DEBUG'

df = df[['date', 'time', 'met', 'category', 'event']]

with sqlite3.connect(DATABASE) as db:
    df.to_sql('apollo11', db)
