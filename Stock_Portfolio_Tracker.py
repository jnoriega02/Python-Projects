import requests

API_KEY = 'LIH4PAZF01LEO67U'
BASE_URL = 'https://www.alphavantage.co/query'

portfolio = [
    {'symbol': 'AAPL', 'shares': 10, 'purchase_price': 150.0},
    {'symbol': 'MSFT', 'shares': 5, 'purchase_price': 200.0},
    {'symbol': 'GOOGL', 'shares': 3, 'purchase_price': 2500.0}
]

def fetch_stock_data(symbol):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data['Global Quote']

def calculate_stock_value(stock, current_price):
    return stock['shares'] * current_price

def main():
    total_portfolio_value = 0.0
    print("Stock Portfolio:")
    for stock in portfolio:
        symbol = stock['symbol']
        stock_data = fetch_stock_data(symbol)
        current_price = float(stock_data['05. price'])
        stock_value = calculate_stock_value(stock, current_price)
        total_portfolio_value += stock_value
        print(f"{symbol}: {stock['shares']} shares | Current Price: ${current_price:.2f} | Total Value: ${stock_value:.2f}")

    print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")

if __name__ == "__main__":
    main()