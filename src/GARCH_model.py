import numpy as np
from src.ARCH_model import ARCH

class GARCH(ARCH):
    """
    Класс для моделирования условной волатильности методом GARCH (Generalized Autoregressive Conditional Heteroskedasticity).
    Этот класс наследует от класса ARCH и добавляет параметр бета_1 для учета долгосрочной зависимости волатильности.

    :param alpha_0: Константа модели, которая представляет собой базовую волатильность.
    :param alpha_1: Коэффициент, который учитывает влияние прошлых квадратичных отклонений на текущую волатильность.
    :param beta_1: Коэффициент, который учитывает влияние прошлой волатильности на текущую волатильность.
    """
    def __init__(self, alpha_0, alpha_1, beta_1):
        super().__init__(alpha_0, alpha_1)
        self.beta_1 = beta_1

    def fit(self, returns):
        volatility = np.zeros(len(returns))
        volatility[0] = returns.var()

        for t in range(1, len(returns)):
            volatility[t] = self.alpha_0 + self.alpha_1 * returns[t - 1]**2 + self.beta_1 * volatility[t - 1]
        return volatility
