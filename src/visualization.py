import matplotlib.pyplot as plt
from src.garch_model import garch_model


def plot_results(returns, params):
    """
    Строит графики квадратов доходностей и волатильности GARCH.

    :param returns: Массив доходностей.
    :param params: Параметры модели [omega, alpha, beta].
    """
    omega, alpha, beta = params
    sigma2 = garch_model(returns, omega, alpha, beta)

    plt.figure(figsize=(10, 6))
    plt.plot(returns.index, returns ** 2, label='Squared Returns')
    plt.plot(returns.index, sigma2, label='GARCH Volatility', color='red')
    plt.legend()
    plt.title("GARCH Model Volatility")
    plt.show()
