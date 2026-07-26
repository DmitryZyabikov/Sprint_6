# Яндекс Самокат — Автоматизированное тестирование

Selenium-тесты для сервиса [qa-scooter.praktikum-services.ru](https://qa-scooter.praktikum-services.ru/)

## Структура проекта

```
Sprint_6/
├── conftest.py              # Фикстуры pytest (driver, accept_cookies)
├── constants.py             # Константы (BASE_URL)
├── requirements.txt         # Зависимости Python
├── pytest.ini               # Конфигурация pytest + Allure
├── .gitignore               # Игнорируемые файлы Git
├── locators/                # Локаторы элементов
│   ├── __init__.py
│   ├── main_page_locators.py    # Локаторы главной страницы
│   └── order_page_locators.py   # Локаторы страницы заказа
├── pages/                   # Page Object Model
│   ├── __init__.py
│   ├── base_page.py             # Базовый класс Page Object
│   ├── main_page.py             # Главная страница
│   └── order_page.py            # Страница оформления заказа
└── tests/                   # Тесты
    ├── __init__.py
    └── test_scooter.py        # Все тесты в одном классе
```

## Установка

```bash
# Создаём виртуальное окружение
python -m venv venv

# Активируем
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux/Mac

# Устанавливаем зависимости
pip install -r requirements.txt
```

## Запуск тестов

```bash
# Запуск всех тестов
pytest

# С отчётом Allure
pytest --alluredir=allure-results

# Генерация отчёта Allure
allure generate allure-results -o allure-report --clean

# Открытие отчёта
allure open allure-report
```

## Тестовые сценарии

| № | Тест | Описание |
|---|------|----------|
| 1 | `test_order_entry_points` | Проверка точек входа в заказ (верхняя и нижняя кнопки «Заказать») |
| 2 | `test_full_order_flow` | Полный цикл оформления заказа (parametrized: 2 набора данных) |
| 3 | `test_accordion` | Проверка работы аккордеона на главной странице (8 вопросов) |
| 4 | `test_logo_scooter_redirect` | Переход по логотипу Самоката |
| 5 | `test_logo_yandex_redirect` | Переход по логотипу Яндекса → Дзен |

**Итого: 14 тестов**

## Архитектура

- **Page Object Model** — каждый экран представлен отдельным классом в `pages/`
- **Локаторы вынесены** в отдельные модули в `locators/`
- **Фикстуры** в `conftest.py` управляют жизненным циклом драйвера
- **Allure** — детальные отчёты с шагами тестов"# PR Trigger Update $(date)" 
