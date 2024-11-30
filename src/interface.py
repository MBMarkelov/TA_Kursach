import tkinter as tk
from tkinter import messagebox
from src import fetch_stock_data
from src.visualization import plot_results
from src.optimizer import optimize_garch


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

        # Кнопка для выполнения GARCH
        tk.Button(root, text="Run GARCH Model", command=self.run_garch).pack(pady=5)

        # Кнопка для отображения графиков
        tk.Button(root, text="Show Results", command=self.show_results).pack(pady=5)

        # Поле для вывода параметров
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=10)

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

    def run_garch(self):
        if not hasattr(self, 'data'):
            messagebox.showerror("Error", "No data loaded. Please fetch data first.")
            return

        try:
            self.returns = self.data['Close'].pct_change().dropna()
            self.optimized_params = optimize_garch(self.returns)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Optimized Parameters:\n{self.optimized_params}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run GARCH model: {e}")

    def show_results(self):
        if not hasattr(self, 'optimized_params'):
            messagebox.showerror("Error", "No results to show. Please run the GARCH model first.")
            return

        try:
            plot_results(self.returns, self.optimized_params)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show results: {e}")
