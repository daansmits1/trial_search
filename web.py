from flask import Flask, render_template, request
app = Flask(__name__)
from googlefinance import getQuotes

def get_stock_price(ticker):
	quotes = getQuotes(ticker)
	price = quotes[0]['LastTradePrice']
	return "The price of {} is {}".format(ticker, price)

@app.route('/')
def index(): #needs to be right under the app line
	name = request.values.get('name', 'Nobody')
	greeting = "Hello {}".format(name)
	return render_template('index.html', greeting=greeting)

@app.route('/about')
def about(): #needs to be right under the app line
	return render_template('about.html')

@app.route('/results')
def results(): #needs to be right under the app line
	stock = request.values.get('stock')
	price = get_stock_price(stock)
	return render_template('results.html', price=price)

app.run(debug=True)