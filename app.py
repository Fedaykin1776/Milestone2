from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, show
import requests
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def no_route():
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
  p = figure(title="IBM Opening Price", x_axis_label='Date', y_axis_label='Opening Price')

  # add a line renderer with legend and line thickness to the plot
  p.line(x, y, legend_label="IBM", line_width=2)

  # show the results
  return show(p);
  
if __name__ == '__main__':
  app.run(port=33507)
