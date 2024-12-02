import numpy as np

class ARCH:
    """
    Класс для реализации модели ARCH (Autoregressive Conditional Heteroskedasticity),
    которая используется для моделирования временной зависимости волатильности.

    :param alpha_0 (float): Константа в уравнении для волатильности.
    :param alpha_1 (float): Коэффициент, задающий влияние квадрата ошибки предыдущего периода на текущую волатильность.
    """
    def __init__(self, alpha_0, alpha_1):
        self.alpha_0 = alpha_0
        self.alpha_1 = alpha_1

    def fit(self, returns):
        volatility = np.zeros(len(returns))
        volatility[0] = returns.var()

        for t in range(1, len(returns)):
            epsilon_t_1 = returns[t-1]
            volatility[t] = self.alpha_0 + self.alpha_1 * epsilon_t_1**2

        return volatility