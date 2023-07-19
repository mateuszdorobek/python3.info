import plotly.offline as py
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('https://python3.info/_static/school-earnings.csv')

table = ff.create_table(df)
py.iplot(table, filename='jupyter-table1')
