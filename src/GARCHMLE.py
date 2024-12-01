import numpy as np
import scipy.optimize as opt
from src.GARCH_model import GARCH

# Реализуем метод максимального правдоподобия (MLE) для модели GARCH(1, 1)
class GARCHMLE(GARCH):
    def __init__(self, alpha_0, alpha_1, beta_1):
        super().__init__(alpha_0, alpha_1, beta_1)

    # Функция логарифмической правдоподобия
    def log_likelihood(self, params, returns):
        alpha_0, alpha_1, beta_1 = params
        n = len(returns)
        volatility = np.zeros(n)
        volatility[0] = returns.var()  # Начальная волатильность

        for t in range(1, n):
            epsilon_t_1 = returns[t-1]
            volatility[t] = alpha_0 + alpha_1 * epsilon_t_1**2 + beta_1 * volatility[t-1]**2

        # Логарифмическая вероятность ошибки
        likelihood = -0.5 * np.sum(np.log(2 * np.pi * volatility) + returns**2 / volatility)
        return -likelihood  # Мы минимизируем отрицательную правдоподобие

    # Функция оптимизации
    def fit(self, returns):
        # Ограничения для параметров (0 <= alpha_0, alpha_1, beta_1 <= 1 и alpha_1 + beta_1 < 1)
        bounds = [(1e-6, 1), (1e-6, 1), (1e-6, 1)]
        constraints = {'type': 'ineq', 'fun': lambda x: 1 - x[1] - x[2]}  # alpha_1 + beta_1 < 1

        # Оптимизация параметров
        initial_params = [self.alpha_0, self.alpha_1, self.beta_1]
        result = opt.minimize(self.log_likelihood, initial_params, args=(returns,), bounds=bounds, constraints=constraints)

        # Обновляем параметры модели
        self.alpha_0, self.alpha_1, self.beta_1 = result.x
        print(f"Оптимизированные параметры: α0 = {self.alpha_0:.6f}, α1 = {self.alpha_1:.6f}, β1 = {self.beta_1:.6f}")
        return self.alpha_0, self.alpha_1, self.beta_1

    # Функция подсчета волатильности
    def calculate_volatility(self, returns):
        n = len(returns)
        volatility = np.zeros(n)
        volatility[0] = returns.var()  # Инициализация начальной волатильности

        # Расчет волатильности на основе оптимизированных параметров
        for t in range(1, n):
            volatility[t] = (
                self.alpha_0 + self.alpha_1 * returns[t - 1]**2 + self.beta_1 * volatility[t - 1]
            )
        return volatility
