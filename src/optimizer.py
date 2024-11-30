from scipy.optimize import minimize
import numpy as np
from src import garch_model

def garch_likelihood(params, returns):
    """
    Вычисляет логарифмическую функцию правдоподобия для GARCH модели.

    :param params: Список параметров [omega, alpha, beta].
    :param returns: Массив доходностей.
    :return: Отрицательное логарифмическое правдоподобие.
    """
    omega, alpha, beta = params
    sigma2 = garch_model(returns, omega, alpha, beta)
    log_likelihood = -np.sum(-0.5 * (np.log(2 * np.pi) + np.log(sigma2) + (returns**2) / sigma2))
    return -log_likelihood

def optimize_garch(returns):
    """
    Оптимизирует параметры GARCH(1,1)-модели.

    :param returns: Массив доходностей.
    :return: Оптимальные параметры [omega, alpha, beta].
    """
    initial_params = [0.1, 0.1, 0.8]
    bounds = [(1e-6, None), (1e-6, 1), (1e-6, 1)]
    result = minimize(garch_likelihood, initial_params, args=(returns,), bounds=bounds)
    if not result.success:
        raise ValueError("Optimization failed.")
    return result.x
