import matplotlib.pyplot as plt


# Функция для визуализации
def plot_volatility(data, volatility_arch, volatility_garch, volatility_garch_optimized, prices):
    fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Строим графики для ARCH и GARCH
    axs[0].plot(data.index, volatility_arch, label='Волатильность ARCH(1)', color='red', linestyle='-')
    axs[0].plot(data.index, volatility_garch, label='Волатильность GARCH(1, 1)', color='blue', linestyle='-')
    axs[0].plot(data.index, volatility_garch_optimized, label='Оптимизированная волатильность GARCH(1, 1)', color='green',
             linestyle='-')

    # Оформляем график
    axs[0].set_title('Волатильность на основе моделей ARCH и GARCH')
    axs[0].set_xlabel('Дата')
    axs[0].set_ylabel('Волатильность')
    axs[0].legend()
    axs[0].grid(True)

    axs[1].plot(prices, label="Ticker Price", color="green")
    axs[1].set_title("Price of the Ticker")
    axs[1].set_ylabel("Price")
    axs[1].set_xlabel("Time")
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()

def plot_with_price(returns, volatility_arch, volatility_garch, prices):
    """
    Построение графиков ARCH, GARCH и цен тикера.
    :param returns: Возвраты актива.
    :param volatility_arch: Волатильность по модели ARCH.
    :param volatility_garch: Волатильность по модели GARCH.
    :param prices: Цены тикера.
    """
    # Создаем два графика: верхний для волатильности, нижний для цен.
    fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Верхний график: волатильность
    axs[0].plot(volatility_arch, label="ARCH Volatility", color="blue")
    axs[0].plot(volatility_garch, label="GARCH Volatility", color="red")
    axs[0].set_title("ARCH vs GARCH Volatility")
    axs[0].set_ylabel("Volatility")
    axs[0].legend()
    axs[0].grid(True)

    # Нижний график: цены
    axs[1].plot(prices, label="Ticker Price", color="green")
    axs[1].set_title("Price of the Ticker")
    axs[1].set_ylabel("Price")
    axs[1].set_xlabel("Time")
    axs[1].legend()
    axs[1].grid(True)

    # Показываем графики
    plt.tight_layout()
    plt.show()
# Пример визуализации
#plot_volatility(data, data['Volatility_ARCH'], data['Volatility_GARCH'], data['Volatility_GARCH_Optimized'])
