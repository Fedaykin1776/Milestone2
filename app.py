from flask import Flask, render_template, request, redirect
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  if request.method == 'POST':
    print("Hellos")
    print(request.form)
    return render_template('about.html')

@app.route('/', methods=['GET', 'POST'])
def no_route():
  return index()

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
