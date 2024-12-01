import tkinter as tk
from tkinter import messagebox

import pandas as pd
from src.ARCH_model  import ARCH
from src.GARCH_model import GARCH
from src import fetch_stock_data
from src.visualization import plot_volatility
from src.GARCHMLE import GARCHMLE


class GarchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GARCH Model Analysis")

        # Заголовок
        tk.Label(root, text="GARCH Model", font=("Arial", 16)).pack(pady=10)

        # Поле для тикера
        tk.Label(root, text="Enter Stock Ticker:").pack()
        self.ticker_entry = tk.Entry(root, width=20)
        self.ticker_entry.pack()

        # Кнопка для загрузки данных
        tk.Button(root, text="Fetch Data", command=self.fetch_data).pack(pady=5)
        # Кнопки для выполнения GARCH/ARCH
        tk.Button(root, text="Run ARCH Model", command=self.run_arch).pack(pady=5)
        tk.Button(root, text="Run GARCH Model", command=self.run_garch).pack(pady=5)
        tk.Button(root, text="Run GARCH optimizer Model", command=self.run_garchOpti).pack(pady=5)

        # Кнопка для отображения графиков
        tk.Button(root, text="Show Results", command=self.show_results).pack(pady=5)

        # Поле для вывода параметров
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=10)

    def run_garchOpti(self):
        alpha_0, alpha_1, beta_1 = 0.0001, 0.1, 0.8
        garch_model = GARCHMLE(alpha_0, alpha_1, beta_1)

        # Оптимизируем параметры модели GARCH
        garch_model.fit(self.data['Returns'])

        # Обучаем модель с оптимизированными параметрами
        volatility_garch_optimized = garch_model.calculate_volatility(self.data['Returns'])

        # Добавляем волатильность в данные
        self.data['Volatility_GARCH_Optimized'] = volatility_garch_optimized


    def fetch_data(self):
        ticker = self.ticker_entry.get()
        if not ticker:
            messagebox.showerror("Error", "Please enter a stock ticker.")
            return

        try:
            self.data = fetch_stock_data(ticker)
            messagebox.showinfo("Success", f"Data for {ticker} loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {e}")

    def run_arch(self):
        alpha_0 = 0.0001  # Константа
        alpha_1 = 0.1  # Коэффициент для прошлых ошибок

        if not hasattr(self, 'data'):
            messagebox.showerror("Error", "No data loaded. Please fetch data first.")
            return
        try:
            # Создаем объект модели ARCH и обучаем на данных
            arch_model = ARCH(alpha_0, alpha_1)
            volatility_arch = arch_model.fit(self.data['Returns'])

            # Добавляем волатильность в данные
            self.data['Volatility_ARCH'] = volatility_arch
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run GARCH model: {e}")

    def run_garch(self):
        if not hasattr(self, 'data'):
            messagebox.showerror("Error", "No data loaded. Please fetch data first.")
            return

        try:
            # Пример использования модели GARCH(1, 1)
            alpha_0 = 0.0001  # Константа
            alpha_1 = 0.1  # Коэффициент для прошлых ошибок
            beta_1 = 0.8  # Коэффициент для прошлой волатильности

            # Создаем объект модели GARCH и обучаем на данных
            garch_model = GARCH(alpha_0, alpha_1, beta_1)
            volatility_garch = garch_model.fit(self.data['Returns'])

            # Добавляем волатильность GARCH в данные
            self.data['Volatility_GARCH'] = volatility_garch
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run GARCH model: {e}")

    def show_results(self):
        try:
            plot_volatility(self.data,self.data['Volatility_ARCH'],self.data['Volatility_GARCH'],self.data['Volatility_GARCH_Optimized'])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show results: {e}")