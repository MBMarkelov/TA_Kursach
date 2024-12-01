import numpy as np
from src.ARCH_model import ARCH

class GARCH(ARCH):
    def __init__(self, alpha_0, alpha_1, beta_1):
        super().__init__(alpha_0, alpha_1)
        self.beta_1 = beta_1

    def fit(self, returns):
        volatility = np.zeros(len(returns))
        volatility[0] = returns.var()  # Начальная волатильность (стандартное отклонение)

        for t in range(1, len(returns)):
            epsilon_t_1 = returns[t-1]  # Ошибка на предыдущем шаге
            volatility[t] = self.alpha_0 + self.alpha_1 * epsilon_t_1**2 + self.beta_1 * volatility[t-1]**2  # Расчет волатильности

        return volatility
