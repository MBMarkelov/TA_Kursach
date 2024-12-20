# GARCH Model Analysis

## Описание проекта

Данный проект реализует приложение для анализа волатильности ценных бумаг с использованием моделей ARCH, GARCH и оптимизированной GARCH. Основная цель проекта — показать, как модели временных рядов могут быть использованы для оценки волатильности рынка на основе исторических данных.

Приложение предоставляет графический интерфейс для загрузки данных, выполнения расчетов и визуализации результатов.

---

## Возможности приложения

- Загрузка данных о ценах акций с использованием заданного тикера.
- Расчет волатильности с использованием моделей:
  - **ARCH**
  - **GARCH**
  - **Оптимизированная GARCH**
- Визуализация результатов в виде графиков, включая периоды высокой волатильности.
- Отображение графика цен актива под графиками волатильности для более полного анализа.

---

## Установка

### Требования

Для работы приложения необходимы следующие библиотеки Python:

- `numpy`
- `pandas`
- `matplotlib`
- `yfinance`
- `tkinter`
- `scipy`

### Шаги установки

1. Склонируйте репозиторий или загрузите архив с кодом проекта.
2. Убедитесь, что Python версии 3.8 или выше установлен на вашем компьютере.
3. Запустите файл с приложением: app.py

## Использование приложения

1. Запустите программу, выполнив скрипт `app.py`.
2. Введите тикер актива (например, `AAPL` для акций Apple) в текстовое поле и нажмите **Fetch Data** для загрузки данных.
3. Используйте кнопки для выполнения моделей:
    - **Run ARCH Model** — запускает расчет волатильности с использованием модели ARCH.
    - **Run GARCH Model** — запускает расчет волатильности с использованием базовой модели GARCH.
    - **Run GARCH optimizer Model** — запускает расчет с использованием модели GARCH с оптимизацией параметров.
4. Нажмите **Show Results**, чтобы увидеть графики волатильности, включая периоды высокой волатильности, и график цен актива.
