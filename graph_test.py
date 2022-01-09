from bokeh.plotting import figure, show
import requests
import pandas as pd

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()
data = data['Time Series (Daily)']
price = [data[x]['1. open'] for x in list(data.keys())]
df = pd.DataFrame()
df['date'] = list(data.keys())
df['date'] = pd.to_datetime(df['date'])
df['price']=price
# prepare some data
x = df['date']
y = df['price']


# create a new plot with a title and axis labels
p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Temp.", line_width=2)

# show the results
show(p)