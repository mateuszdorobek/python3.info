import plotly.offline as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://python3.info/_static/finance-charts-apple.csv')

data = [go.Scatter(
    x=df.Date,
    y=df['AAPL.Close'])]

py.iplot(data)
