# Пример проекта на Python

## 1. Решение задачи

В файле `solution.py` реализована функция сложения двух чисел:
```python
from solution import add
print(add(2, 3))  # Выведет 5
```

## 2. Автотесты

Для запуска автотестов используйте:
```bash
pytest
```

## 3. GitHub Actions

Автотесты автоматически запускаются при каждом push или pull request в ветку `main` с помощью GitHub Actions (`.github/workflows/python-app.yml`).

## 4. Требования
- Python 3.11+
- pytest

## Быстрый старт
1. Установите зависимости:
   ```bash
   pip install pytest
   ```
2. Запустите тесты:
   ```bash
   pytest
   ``` 