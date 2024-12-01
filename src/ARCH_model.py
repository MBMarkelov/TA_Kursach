import numpy as np

class ARCH:
    def __init__(self, alpha_0, alpha_1):
        self.alpha_0 = alpha_0
        self.alpha_1 = alpha_1

    def fit(self, returns):
        volatility = np.zeros(len(returns))
        volatility[0] = returns.var()  # Начальная волатильность (стандартное отклонение)

        for t in range(1, len(returns)):
            epsilon_t_1 = returns[t-1]  # Ошибка на предыдущем шаге
            volatility[t] = self.alpha_0 + self.alpha_1 * epsilon_t_1**2  # Расчет волатильности

        return volatility