import yfinance as yf

def fetch_stock_data(ticker, start_date="2020-01-01", end_date="2022-01-01", save_to_csv=True):
    """
    Загружает исторические данные по акции с помощью yfinance.

    :param ticker: Строка. Тикер акции (например, 'AAPL').
    :param start_date: Строка. Дата начала в формате 'YYYY-MM-DD'.
    :param end_date: Строка. Дата окончания в формате 'YYYY-MM-DD'.
    :param save_to_csv: Логическое. Сохранять ли данные в CSV.
    :return: DataFrame с историческими данными.
    """
    try:
        # Загрузка данных
        data = yf.download(ticker, start=start_date, end=end_date)

        # Проверяем, получили ли мы данные
        if data.empty:
            raise ValueError(f"No data found for ticker {ticker}")

        # Рассчитываем доходности
        data['Returns'] = data['Adj Close'].pct_change()
        data.dropna(inplace=True)

        # Сохранение данных в CSV, если нужно
        if save_to_csv:
            data.to_csv("C:/Users\mark2\Documents\GitHub\TA_Kursach\data/raw_data.csv")
            print(f"Данные сохранены в 'raw_data.csv'")

        return data
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
        return None
