# Тестирование Stellar Burgers

Проект автоматизированного тестирования веб-приложения Stellar Burgers с использованием Selenium и Python.

## Структура проекта

- `tests/` - директория с тестами
  - `test_login.py` - тесты для функциональности входа
  - `test_registration.py` - тесты для функциональности регистрации
  - `test_logout.py` - тесты для функциональности выхода
  - `test_constructor.py` - тесты для функциональности конструктора бургеров
  - `test_navigation.py` - тесты для функциональности навигации
  - `test_autoregistration.py` - тесты для автоматической регистрации
  - `conftest.py` - фикстуры для тестов

- `locators/` - директория с локаторами элементов
  - `locators.py` - классы с локаторами элементов страницы

- `helpers/` - директория с вспомогательными функциями
  - `data_generators.py` - генераторы тестовых данных (email, пароль)

## Требования

- Python 3.7+
- Selenium WebDriver
- Pytest

## Установка и запуск

1. Клонировать репозиторий
2. Установить зависимости: `pip install -r requirements.txt`
3. Запустить тесты: `pytest tests/`

## Особенности проекта

- Каждый тест автономен (открывает браузер, выполняет действия и закрывает браузер)
- Используется Chrome WebDriver
- Реализованы генераторы тестовых данных для email и паролей 