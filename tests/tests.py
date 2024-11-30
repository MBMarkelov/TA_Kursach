import pytest
import numpy as np
from src.fetch_data import fetch_stock_data
from src.garch_model import garch_model
from src.optimizer import optimize_garch
from src.visualization import plot_results
import pandas as pd


# Фиктивные данные для тестов
@pytest.fixture
def mock_returns():
    np.random.seed(42)
    prices = 100 + np.cumsum(np.random.normal(0, 1, 100))
    returns = pd.Series(prices).pct_change().dropna()
    return returns


# 1. Тест функции fetch_stock_data
def test_fetch_stock_data():
    """
    Тест проверяет, что функция fetch_stock_data корректно загружает данные.
    """
    try:
        data = fetch_stock_data("AAPL")
        assert not data.empty, "Data is empty for valid ticker."
    except Exception as e:
        pytest.fail(f"fetch_stock_data failed with error: {e}")


# 2. Тест функции garch_model
def test_garch_model(mock_returns):
    """
    Проверяет правильность расчета GARCH-дисперсии.
    """
    omega, alpha, beta = 0.1, 0.1, 0.8
    sigma2 = garch_model(mock_returns, omega, alpha, beta)
    assert len(sigma2) == len(mock_returns), "Output length mismatch."
    assert np.all(sigma2 > 0), "Variance values should be positive."


# 3. Тест функции optimize_garch
def test_optimize_garch(mock_returns):
    """
    Проверяет корректность оптимизации параметров GARCH.
    """
    try:
        params = optimize_garch(mock_returns)
        assert len(params) == 3, "Optimization should return three parameters."
        omega, alpha, beta = params
        assert omega > 0, "Omega should be positive."
        assert 0 <= alpha <= 1, "Alpha should be between 0 and 1."
        assert 0 <= beta <= 1, "Beta should be between 0 and 1."
    except Exception as e:
        pytest.fail(f"optimize_garch failed with error: {e}")


# 4. Тест функции plot_results
def test_plot_results(mock_returns):
    """
    Проверяет, что функция plot_results работает без ошибок.
    """
    try:
        params = [0.1, 0.1, 0.8]
        plot_results(mock_returns, params)
    except Exception as e:
        pytest.fail(f"plot_results failed with error: {e}")
