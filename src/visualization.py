import matplotlib.pyplot as plt

def plot_volatility(data, volatility_arch, volatility_garch, volatility_garch_optimized, prices):
    """
    Функция визуализации, которая в отдельном окне отображает графики цены и волатильности
    :param volatility_arch: Волатильность по модели ARCH.
    :param volatility_garch: Волатильность по модели GARCH.
    :param prices: Цены тикера.
    """

    fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    axs[0].plot(data.index, volatility_arch, label='Волатильность ARCH(1)', color='red', linestyle='-')
    axs[0].plot(data.index, volatility_garch, label='Волатильность GARCH(1, 1)', color='blue', linestyle='-')
    axs[0].plot(data.index, volatility_garch_optimized, label='Оптимизированная волатильность GARCH(1, 1)', color='green', linestyle='-')

    min_threshold = max(volatility_garch_optimized) - max(volatility_garch_optimized) * 0.5
    high_vol_periods = [i for i, vol in enumerate(volatility_garch_optimized) if vol > min_threshold]
    high_vol_dates = [data.index[i] for i in high_vol_periods]  # data.index должен содержать даты

    axs[0].set_title('Волатильность на основе моделей ARCH и GARCH')
    axs[0].set_xlabel('Дата')
    axs[0].set_ylabel('Волатильность')
    axs[0].legend()
    axs[0].grid(True)

    # Нахождение высокой волатильности по датам
    for start, end in zip(high_vol_dates[:-1], high_vol_dates[1:]):
        if (end - start).days <= 1:
            axs[0].axvspan(start, end, color='red', alpha=0.2, label='High Volatility Period')
            axs[1].axvspan(start, end, color='red', alpha=0.2)

    axs[1].plot(prices, label="Ticker Price", color="green")
    axs[1].set_title("Price of the Ticker")
    axs[1].set_ylabel("Price")
    axs[1].set_xlabel("Time")
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()