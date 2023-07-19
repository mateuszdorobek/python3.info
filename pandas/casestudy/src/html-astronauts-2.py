import pandas as pd


pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)

#%%
DATA = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'
YEAR = 365.25

#%%
dfs = pd.read_html(DATA)
active = dfs[0]
former = dfs[2]

#%%
a = active['Time in space'].map(pd.to_timedelta).sum()
f = former['Time in space'].map(pd.to_timedelta).sum()

years = (a+f).days / YEAR
# 9.806981519507186
