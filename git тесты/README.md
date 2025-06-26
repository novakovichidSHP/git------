# Пример проекта на Python

## 1. Решение задачи

В файле `solution.py` реализована функция сложения двух чисел с логированием в файл `logs.txt`:
```python
from solution import add
print(add(2, 3))  # Выведет 5 и добавит запись в logs.txt
```

## 2. Автотесты

Для запуска автотестов используйте:
```bash
pytest
```
Тесты автоматически очищают лог-файл и проверяют, что записи о вызовах функции появляются в `logs.txt`.

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