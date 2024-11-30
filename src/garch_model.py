import numpy as np


def garch_model(returns, omega, alpha, beta):
    """
    Реализация GARCH(1,1)-модели для расчета условной дисперсии.

    :param returns: Массив доходностей.
    :param omega: Параметр omega модели.
    :param alpha: Параметр alpha модели.
    :param beta: Параметр beta модели.
    :return: Массив условной дисперсии.
    """
    n = len(returns)
    sigma2 = np.zeros(n)
    sigma2[0] = np.var(returns)  # Начальная дисперсия

    for t in range(1, n):
        sigma2[t] = omega + alpha * (returns[t - 1] ** 2) + beta * sigma2[t - 1]

    return sigma2
