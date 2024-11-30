import yfinance as yf

def fetch_stock_data(ticker):
    """Загружает данные по тикеру акции"""
    data = yf.download(ticker, start='2020-01-01', end='2023-01-01')
    if data.empty:
        raise ValueError("No data found for this ticker.")
    return data
