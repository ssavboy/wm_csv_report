# wm-csv-report

CLI‑инструмент для отчета о медианных тратах на кофе студентами.

## Формат данных

CSV‑файлы с заголовком:

```text
student,date,coffee_spent,sleep_hours,study_hours,mood,exam
```

## Запуск через Poetry

```bash
poetry install
poetry run coffee-report --files math.csv physics.csv programming.csv --report median-coffee
```

## Запуск через локальное виртуальное окружение (.venv)

```bash
python3 -m venv .venv        # Windows: python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m app.cli --files math.csv physics.csv programming.csv --report median-coffee
```

## Тесты

```bash
poetry run pytest           # (.venv): pytest
```

## Стиль кода и pre-commit

Для единообразного стиля кода используются Black и isort, подключенные через pre-commit.

Конфигурация хуков в `.pre-commit-config.yaml`:

Установка хуков:

```bash
poetry pre-commit install
```

После этого Black и isort автоматически запускаются при каждом `git commit`, форматируя код и упорядочивая импорты.
