import matplotlib.pyplot as plt


# Функция для визуализации
def plot_volatility(data, volatility_arch, volatility_garch, volatility_garch_optimized):
    plt.figure(figsize=(12, 6))

    # Строим графики для ARCH и GARCH
    plt.plot(data.index, volatility_arch, label='Волатильность ARCH(1)', color='red', linestyle='-')
    plt.plot(data.index, volatility_garch, label='Волатильность GARCH(1, 1)', color='blue', linestyle='-')
    plt.plot(data.index, volatility_garch_optimized, label='Оптимизированная волатильность GARCH(1, 1)', color='green',
             linestyle='-')

    # Оформляем график
    plt.title('Волатильность на основе моделей ARCH и GARCH')
    plt.xlabel('Дата')
    plt.ylabel('Волатильность')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Пример визуализации
#plot_volatility(data, data['Volatility_ARCH'], data['Volatility_GARCH'], data['Volatility_GARCH_Optimized'])
